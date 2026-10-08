#!/usr/bin/env python3
"""Rebuild the files that make this site easy for AI agents to read.

Run this after every change to index.html, papers/ or cv.md:

    python3 scripts/build_agent_files.py          # rewrite everything
    python3 scripts/build_agent_files.py --check  # exit 1 if anything is stale

index.html is the source of truth. Each <li class="publication-item"> is one
listing of a paper. Its data-paper="<slug>" attribute ties listings of the
same paper together and names the paper's text file, papers/<slug>.md. New
listings get the attribute automatically, from the title.

papers/metadata.json adds what the page doesn't show: DOI, full author names,
year, volume and pages. Entries are optional.

papers/<slug>.md: everything above the END OF GENERATED HEADER line is
rewritten on every run. Everything below it (## Abstract, ## Full text) is
hand-kept and never touched. scripts/paper_to_md.py makes the full text from
a PDF or an arXiv id.

Writes: papers/<slug>.md headers, llms.txt, llms-full.txt, publications.bib,
sitemap.xml, robots.txt, and two things inside index.html: the JSON-LD block
and a "Plain text" link on every paper that has full text.
"""

import html
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://www.matthewdigiuseppe.com"
ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
MARKER = "<!-- END OF GENERATED HEADER: edit freely below this line; scripts/build_agent_files.py keeps it -->"
STATUS_CATEGORIES = {"Recently Accepted", "Revise & Resubmit", "Under Review"}
STOPWORDS = {"a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "by", "at", "from", "or", "is"}


def text_of(fragment):
    """Visible text of an HTML fragment, on one line."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def slugify(title):
    title = re.sub(r"[\u2010-\u2015/]", " ", title)
    title = re.sub(r"['\u2019.]", "", title)
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    words = re.findall(r"[a-z0-9]+", ascii_title)
    return "-".join([w for w in words if w not in STOPWORDS][:5])


def absolute(href):
    if re.match(r"https?://", href):
        return href
    return f"{SITE}/{href.lstrip('/')}"


# ---------------------------------------------------------------- index.html

LI_RE = re.compile(r'<li class="publication-item"(?P<attrs>[^>]*)>(?P<body>.*?)</li>', re.S)


def add_slugs(page):
    """Give every publication listing a data-paper attribute."""
    def fix(m):
        if "data-paper=" in m.group("attrs"):
            return m.group(0)
        title = text_of(re.search(r'<p class="publication-title">(.*?)</p>', m.group("body"), re.S).group(1))
        return f'<li class="publication-item"{m.group("attrs")} data-paper="{slugify(title)}">{m.group("body")}</li>'
    return LI_RE.sub(fix, page)


def parse_listings(page):
    """Every publication listing, with the section and category it sits under."""
    marks = [(m.start(), "h3", text_of(m.group(2)), m.group(1))
             for m in re.finditer(r'<h3 id="([^"]+)">(.*?)</h3>', page, re.S)]
    marks += [(m.start(), "h4", text_of(m.group(2)), m.group(1))
              for m in re.finditer(r'<h4 id="([^"]+)">(.*?)</h4>', page, re.S)]
    marks.sort()
    listings = []
    for m in LI_RE.finditer(page):
        section = category = category_id = None
        for pos, tag, label, ident in marks:
            if pos > m.start():
                break
            if tag == "h3":
                section, category, category_id = label, None, None
            else:
                category, category_id = label, ident
        body = m.group("body")

        def field(cls):
            f = re.search(rf'<p class="{cls}">(.*?)</p>', body, re.S)
            return text_of(f.group(1)) if f else ""

        links = [(text_of(a.group(2)), html.unescape(a.group(1)))
                 for a in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>', body, re.S)]
        listings.append({
            "slug": re.search(r'data-paper="([^"]+)"', m.group("attrs")).group(1),
            "title": field("publication-title"),
            "authors": field("publication-authors"),
            "venue": field("publication-journal"),
            "links": links,
            "section": section,
            "category": category,
            "category_id": category_id,
        })
    return listings


def merge_papers(listings, metadata):
    papers = {}
    for item in listings:
        p = papers.setdefault(item["slug"], {
            "slug": item["slug"], "title": item["title"], "authors": item["authors"], "venue": "",
            "links": [], "categories": [], "section": item["section"],
        })
        if len(item["venue"]) > len(p["venue"]):
            p["venue"] = item["venue"]
        for link in item["links"]:
            if link[1] not in [h for _, h in p["links"]] and not link[1].startswith("papers/"):
                p["links"].append(link)
        if item["category"] not in p["categories"]:
            p["categories"].append(item["category"])
    for p in papers.values():
        meta = metadata.get(p["slug"], {})
        p["meta"] = meta
        status = [c for c in p["categories"] if c in STATUS_CATEGORIES]
        p["topics"] = [c for c in p["categories"] if c not in STATUS_CATEGORIES]
        if p["section"] == "Published Articles":
            p["status"] = "Published"
        else:
            p["status"] = "Working paper" + (f" ({status[0].lower()})" if status else "")
        year = re.search(r"\((\d{4})\)", p["authors"])
        p["year"] = int(year.group(1)) if year else meta.get("year")
        p["authors_short"] = re.sub(r"\s*\(\d{4}\)\s*$", "", p["authors"])
        # metadata.json stores "Family, Given" (BibTeX order); everything else wants "Given Family".
        p["authors_full"] = [" ".join(reversed(a.split(", ", 1))) for a in meta.get("authors", [])]
    return papers


def read_body(slug):
    path = PAPERS / f"{slug}.md"
    if path.exists():
        text = path.read_text()
        if MARKER in text:
            return text.split(MARKER, 1)[1].lstrip("\n")
    return ""


def section_of(body, heading):
    m = re.search(rf"^## {heading}\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def citation(p):
    venue = p["venue"]
    year = f" ({p['year']})" if p["year"] and f"({p['year']})" not in p["authors"] else ""
    head = p["authors"] + year
    head += "" if head.endswith(".") else "."
    title = p["title"] if p["title"][-1] in ".?!" else p["title"] + "."
    return f"{head} {title}" + (f" {venue.rstrip('.')}." if venue else "")


def paper_md(p, body):
    url = f"{SITE}/papers/{p['slug']}.md"
    links = {text: absolute(href) for text, href in p["links"]}
    doi = p["meta"].get("doi")
    front = {
        "title": p["title"],
        "authors": p["authors_full"] or p["authors_short"],
        "year": p["year"],
        "status": p["status"],
        "venue": p["venue"] or None,
        "topics": p["topics"],
        "doi": doi,
        "url": url,
        "links": links,
        "full_text": p["has_full_text"],
    }
    lines = ["---"]
    for key, value in front.items():
        if value in (None, [], {}):
            continue
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines += ["---", "", f"# {p['title']}", "", citation(p), ""]
    lines.append(f"- Status: {p['status']}")
    if p["topics"]:
        lines.append(f"- Topics: {', '.join(p['topics'])}")
    if doi:
        lines.append(f"- DOI: https://doi.org/{doi}")
    for text, href in links.items():
        lines.append(f"- {text}: {href}")
    lines.append(f"- Listed on: {SITE}/#research")
    lines += ["", MARKER, ""]
    return "\n".join(lines) + ("\n" + body if body else "")


def sync_text_links(page, papers):
    """Add or remove the "Plain text" link so it matches papers/<slug>.md."""
    def fix(m):
        slug = re.search(r'data-paper="([^"]+)"', m.group("attrs")).group(1)
        body = re.sub(r'\n\s*<a href="papers/[^"]+"[^>]*>Plain text</a>', "", m.group("body"))
        if papers[slug]["has_full_text"]:
            link = (f'<a href="papers/{slug}.md" type="text/markdown" target="_blank" rel="noopener noreferrer"\n'
                    f'                                    class="publication-link">Plain text</a>')
            if '<div class="publication-links">' in body:
                body = re.sub(r'(<div class="publication-links">.*?)(\n\s*</div>)',
                              lambda d: f"{d.group(1)}\n                                {link}{d.group(2)}", body, count=1, flags=re.S)
            else:
                body = body.rstrip() + ('\n                            <div class="publication-links">\n'
                                        f'                                {link}\n                            </div>\n                        ')
        return f'<li class="publication-item"{m.group("attrs")}>{body}</li>'
    return LI_RE.sub(fix, page)


def json_ld(page, papers):
    """Structured data for search engines: who this is, and where the machine-readable files live."""
    desc = re.search(r'<meta name="description"\s+content="([^"]+)"', page).group(1)
    person = {
        "@type": "Person",
        "@id": f"{SITE}/#person",
        "name": "Matthew DiGiuseppe",
        "jobTitle": "Associate Professor of Political Science and International Relations",
        "description": html.unescape(re.sub(r"\s+", " ", desc)),
        "affiliation": {"@type": "CollegeOrUniversity", "name": "Leiden University",
                        "department": {"@type": "Organization", "name": "Institute of Political Science"}},
        "url": f"{SITE}/",
        "image": f"{SITE}/actionshot2.jpeg",
        "sameAs": ["https://scholar.google.com/citations?user=uLty40oAAAAJ",
                   "https://github.com/matthewdigiuseppe"],
        "knowsAbout": ["International political economy", "Comparative political economy", "Sovereign debt",
                       "Public opinion on public debt", "Armed conflict", "Alliance politics",
                       "Politics of artificial intelligence", "Large language models in social science"],
        "subjectOf": {"@type": "DigitalDocument", "name": "Curriculum Vitae", "url": f"{SITE}/CV.pdf"},
    }
    graph = {"@context": "https://schema.org", "@graph": [
        person,
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Matthew DiGiuseppe",
         "author": {"@id": f"{SITE}/#person"}},
        {"@type": "Dataset", "name": "Publications and working papers of Matthew DiGiuseppe",
         "description": f"Citation details, abstracts and (where public) full texts of {len(papers)} papers, as plain text.",
         "creator": {"@id": f"{SITE}/#person"},
         "distribution": [
             {"@type": "DataDownload", "encodingFormat": "text/markdown", "contentUrl": f"{SITE}/llms-full.txt"},
             {"@type": "DataDownload", "encodingFormat": "application/x-bibtex", "contentUrl": f"{SITE}/publications.bib"}]},
    ]}
    block = json.dumps(graph, ensure_ascii=False, indent=2)
    block = "\n".join("    " + line for line in block.splitlines())
    return re.sub(r'<script type="application/ld\+json">.*?</script>',
                  lambda _: f'<script type="application/ld+json">\n{block}\n    </script>', page, count=1, flags=re.S)


# ---------------------------------------------------------------- llms files

class MiniMarkdown(HTMLParser):
    """Just enough HTML-to-Markdown for the page's prose sections."""

    SKIP = {"script", "style", "button", "nav", "i"}

    def __init__(self):
        super().__init__()
        self.out, self.skip, self.li = [], 0, 0
        self.link = None  # (href, aria-label, index in out where the link text starts)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in self.SKIP:
            self.skip += 1
        if self.skip:
            return
        if tag in ("h2", "h3", "h4", "h5"):
            self.out.append("**" if self.li else "\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.out.append(" — " if self.li else "\n\n")
        elif tag == "div" and not self.li:
            self.out.append("\n\n")
        elif tag == "li":
            self.li += 1
            self.out.append("\n- ")
        elif tag == "br":
            self.out.append(", ")
        elif tag == "a":
            self.link = (attrs.get("href", ""), attrs.get("aria-label", ""), len(self.out))

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip -= 1
            return
        if self.skip:
            return
        if tag in ("h2", "h3", "h4", "h5") and self.li:
            self.out.append("**")
        elif tag == "li":
            self.li -= 1
        elif tag == "a" and self.link:
            href, label, start = self.link
            text = "".join(self.out[start:]).strip() or label
            del self.out[start:]
            self.out.append(text if href.startswith("#") else f"[{text}]({absolute(href)})")
            self.link = None

    def handle_data(self, data):
        if not self.skip:
            self.out.append(re.sub(r"\s+", " ", data))

    def markdown(self):
        text = "".join(self.out)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"\*\* +", "** ", re.sub(r"- +\*\*", "- **", text))
        text = re.sub(r"\s+ — ", " — ", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def section_markdown(page, start_pattern, end_pattern):
    m = re.search(start_pattern + r"(.*?)" + end_pattern, page, re.S)
    parser = MiniMarkdown()
    parser.feed(m.group(1))
    return parser.markdown()


def paper_entry(p, with_abstract):
    detail =f"{p['authors_short']}" + (f" ({p['year']})" if p["year"] else "") + (f". {p['venue']}" if p["venue"] else "")
    line = f"- [{p['title']}]({SITE}/papers/{p['slug']}.md): {detail.rstrip('.')}."
    if p["has_full_text"]:
        line += " Full text."
    if not with_abstract:
        return line
    out = [f"### {p['title']}", "", citation(p), "", f"- Status: {p['status']}"]
    if p["topics"]:
        out.append(f"- Topics: {', '.join(p['topics'])}")
    if p["meta"].get("doi"):
        out.append(f"- DOI: https://doi.org/{p['meta']['doi']}")
    for text, href in p["links"]:
        out.append(f"- {text}: {absolute(href)}")
    out.append(f"- Text version{' (with full text)' if p['has_full_text'] else ''}: {SITE}/papers/{p['slug']}.md")
    if p["abstract"]:
        out += ["", p["abstract"]]
    return "\n".join(out)


def ordered(papers, section):
    return [p for p in papers.values() if p["section"] == section]


def llms_txt(page, papers):
    desc = html.unescape(re.sub(r"\s+", " ", re.search(r'<meta name="description"\s+content="([^"]+)"', page).group(1)))
    extra = []
    if (ROOT / "cv.md").exists():
        extra.append(f"- [CV as text]({SITE}/cv.md): the full CV in Markdown")
    lines = [
        "# Matthew DiGiuseppe",
        "",
        f"> {desc}",
        "",
        "This file lists everything on the site in plain text. Each paper has its own Markdown page with "
        "citation details, links and the abstract; working papers with a public preprint include the full text. "
        f"Everything in one file, with abstracts: [llms-full.txt]({SITE}/llms-full.txt).",
        "",
        "## About",
        "",
        f"- [Homepage]({SITE}/): research, teaching and contact details",
        *extra,
        f"- [CV (PDF)]({SITE}/CV.pdf)",
        f"- [MIDEBT project]({SITE}/midebt.html): ERC Starting Grant project on the microfoundations of debt crises",
        f"- [All publications as BibTeX]({SITE}/publications.bib)",
        "",
        "## Working papers",
        "",
        *[paper_entry(p, False) for p in ordered(papers, "Working Papers")],
        "",
        "## Published articles",
        "",
        *[paper_entry(p, False) for p in ordered(papers, "Published Articles")],
        "",
        "## Optional",
        "",
        "- [Google Scholar profile](https://scholar.google.com/citations?user=uLty40oAAAAJ)",
        "- [GitHub](https://github.com/matthewdigiuseppe)",
        "",
    ]
    return "\n".join(lines)


def llms_full(page, papers):
    desc = html.unescape(re.sub(r"\s+", " ", re.search(r'<meta name="description"\s+content="([^"]+)"', page).group(1)))
    home = section_markdown(page, r'<div class="hero-text">', r'<div class="hero-buttons">')
    summary = section_markdown(page, r'<div class="hero-summary">', r"</section>")
    projects = section_markdown(page, r'<div class="research-highlight">', r'<div class="publication-categories">')
    teaching = section_markdown(page, r'<section id="teaching" class="teaching">', r"</section>")
    contact = section_markdown(page, r'<section id="contact" class="contact">', r"</section>")
    parts = [
        "# Matthew DiGiuseppe — the whole site as text",
        "",
        f"> {desc}",
        "",
        f"Generated from {SITE}/ by scripts/build_agent_files.py. Paper titles link to one Markdown file per paper; "
        "those files carry the full text where a public preprint exists.",
        "",
        "## Profile",
        "",
        re.sub(r"^#+ ", "", home, flags=re.M),
        "",
        summary,
        "",
        f"CV: {SITE}/CV.pdf" + (f" (text version: {SITE}/cv.md)" if (ROOT / "cv.md").exists() else ""),
        "",
        projects.replace("### Current Projects", "## Current projects").replace("#### ", "### "),
        "",
        "## Working papers",
        "",
        "\n\n".join(paper_entry(p, True) for p in ordered(papers, "Working Papers")),
        "",
        "## Published articles",
        "",
        "\n\n".join(paper_entry(p, True) for p in ordered(papers, "Published Articles")),
        "",
        teaching,
        "",
        contact,
        "",
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(parts))


# ---------------------------------------------------------------- bib, sitemap, robots

def bib_escape(s):
    return s.replace("&", r"\&").replace("%", r"\%").replace("$", r"\$").replace("#", r"\#")


def publications_bib(papers):
    entries, keys = [], set()
    for p in papers.values():
        meta = p["meta"]
        authors = meta.get("authors") or [a for a in re.split(r",?\s*&\s*|(?<=\.),\s+", p["authors_short"]) if a]
        first = re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", (p["authors_short"].split(",")[0])).encode("ascii", "ignore").decode().lower())
        word = next((w for w in slugify(p["title"]).split("-") if len(w) > 3), "paper")
        key = f"{first}{p['year'] or 'wp'}{word}"
        while key in keys:
            key += "b"
        keys.add(key)
        published = p["section"] == "Published Articles"
        fields = [("title", "{" + bib_escape(p["title"]) + "}"), ("author", " and ".join(bib_escape(a) for a in authors))]
        if published:
            fields.append(("journal", bib_escape(meta.get("journal") or p["venue"].split(",")[0])))
            for f in ("volume", "number", "pages"):
                if meta.get(f):
                    fields.append((f, str(meta[f]).replace("-", "--")))
        elif p["venue"]:
            fields.append(("note", bib_escape(p["venue"])))
        else:
            fields.append(("note", "Working paper"))
        if p["year"]:
            fields.append(("year", str(p["year"])))
        if meta.get("doi"):
            fields.append(("doi", meta["doi"]))
        link = next((absolute(h) for _, h in p["links"]), None)
        if link and not meta.get("doi"):
            fields.append(("url", link))
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields)
        entries.append(f"@{'article' if published else 'unpublished'}{{{key},\n{body}\n}}")
    head = f"% Publications and working papers of Matthew DiGiuseppe.\n% Generated from {SITE}/ by scripts/build_agent_files.py.\n\n"
    return head + "\n\n".join(entries) + "\n"


def sitemap(page, papers):
    urls = [f"{SITE}/", f"{SITE}/midebt.html", f"{SITE}/CV.pdf", f"{SITE}/llms.txt", f"{SITE}/llms-full.txt",
            f"{SITE}/publications.bib"]
    if (ROOT / "cv.md").exists():
        urls.append(f"{SITE}/cv.md")
    for href in re.findall(r'href="([^"#:]+\.pdf)"', page):
        if absolute(href) not in urls:
            urls.append(absolute(href))
    urls += [f"{SITE}/papers/{slug}.md" for slug in papers]
    body = "\n".join(f"  <url><loc>{html.escape(u)}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'


ROBOTS = f"""# Everyone is welcome here, AI agents included.
# Plain-text index of this site: {SITE}/llms.txt
User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""


# ---------------------------------------------------------------- main

def build():
    page = (ROOT / "index.html").read_text()
    metadata = json.loads((PAPERS / "metadata.json").read_text()) if (PAPERS / "metadata.json").exists() else {}
    page = add_slugs(page)
    papers = merge_papers(parse_listings(page), metadata)
    for slug in metadata:
        if slug not in papers:
            print(f"warning: papers/metadata.json has '{slug}', which is not on the page", file=sys.stderr)
    files = {}
    for slug, p in papers.items():
        body = read_body(slug)
        p["abstract"] = section_of(body, "Abstract")
        p["has_full_text"] = bool(section_of(body, "Full text"))
        files[f"papers/{slug}.md"] = paper_md(p, body)
    page = sync_text_links(page, papers)
    page = json_ld(page, papers)
    files["index.html"] = page
    files["llms.txt"] = llms_txt(page, papers)
    files["llms-full.txt"] = llms_full(page, papers)
    files["publications.bib"] = publications_bib(papers)
    files["sitemap.xml"] = sitemap(page, papers)
    files["robots.txt"] = ROBOTS
    orphans = sorted(f.name for f in PAPERS.glob("*.md") if f.stem not in papers) if PAPERS.exists() else []
    return files, orphans


def main():
    check = "--check" in sys.argv
    files, orphans = build()
    stale = []
    for name, content in files.items():
        path = ROOT / name
        if not path.exists() or path.read_text() != content:
            stale.append(name)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    for name in orphans:
        print(f"warning: papers/{name} matches no paper on the page (renamed or removed?)", file=sys.stderr)
    if check:
        if stale:
            print("Out of date (run python3 scripts/build_agent_files.py):\n  " + "\n  ".join(stale))
            sys.exit(1)
        print("Agent files are up to date.")
    else:
        print("Updated:\n  " + "\n  ".join(stale) if stale else "Nothing to update.")


if __name__ == "__main__":
    main()
