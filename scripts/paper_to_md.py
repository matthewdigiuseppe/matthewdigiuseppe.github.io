#!/usr/bin/env python3
"""Turn a paper (a PDF, or an arXiv id) into clean Markdown.

The output is the *body* of a papers/<slug>.md file: everything that goes
below the generated header. Paste it under "## Full text" (see
scripts/build_agent_files.py for the file layout).

    python3 scripts/paper_to_md.py paper.pdf > /tmp/body.md
    python3 scripts/paper_to_md.py arxiv:2602.18092 > /tmp/body.md

PDFs need poppler's `pdftohtml` (brew install poppler). arXiv ids need
`pandoc` and use arXiv's HTML rendering, which keeps math and tables.
The PDF route is tuned for LaTeX manuscripts: one column, footnotes at the
bottom of the page, references with hanging indents.
"""

import collections
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET

LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl", "∗": "*", " ": " "}
REFERENCES_RE = re.compile(r"^(\d+(\.\d+)*\.?\s+)?(references|bibliography|works cited)$", re.I)


def clean(text):
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    return text


class Frag:
    def __init__(self, el, fonts):
        self.top = float(el.get("top"))
        self.left = float(el.get("left"))
        self.width = float(el.get("width"))
        self.height = float(el.get("height"))
        self.size, family = fonts[el.get("font")]
        self.text = clean("".join(el.itertext()))
        bold_chars = sum(len("".join(b.itertext())) for b in el.iter("b"))
        self.bold = bold_chars >= 0.6 * len(self.text.strip()) or bool(
            re.search(r"bold|bx|semibold|black|heavy|-bd", family, re.I))
        self.bottom = self.top + self.height
        self.right = self.left + self.width


class Line:
    def __init__(self, frag):
        self.frags = [frag]

    def overlaps(self, f):
        top = min(g.top for g in self.frags)
        bottom = max(g.bottom for g in self.frags)
        height = min(bottom - top, f.height)
        return min(bottom, f.bottom) - max(top, f.top) >= 0.4 * height

    def finish(self):
        self.frags.sort(key=lambda f: f.left)
        weights = collections.Counter()
        for f in self.frags:
            weights[f.size] += len(f.text.strip())
        self.size = weights.most_common(1)[0][0]
        main = [f for f in self.frags if f.size >= 0.85 * self.size] or self.frags
        self.top = min(f.top for f in main)
        self.bottom = max(f.bottom for f in main)
        self.left = min(f.left for f in self.frags)
        self.right = max(f.right for f in self.frags)
        chars = sum(len(f.text.strip()) for f in self.frags) or 1
        self.bold = sum(len(f.text.strip()) for f in self.frags if f.bold) >= 0.7 * chars
        self.lead_note = None
        self.gaps = 0
        parts, prev = [], None
        for i, f in enumerate(self.frags):
            t = f.text
            raised = f.size < 0.8 * self.size and f.bottom < self.bottom - 1.5
            if raised and re.fullmatch(r"\s*\d{1,3}\s*", t):
                if i == 0:
                    self.lead_note = t.strip()
                    prev = f
                    continue
                t = f"[^{t.strip()}]"
            if prev is not None:
                gap = f.left - prev.right
                if gap > 1.4 * self.size:
                    self.gaps += 1
                    parts.append("  ")
                elif gap > 1.5 and not parts[-1].endswith(" ") and not t.startswith(" "):
                    parts.append(" ")
            parts.append(t)
            prev = f
        self.text = re.sub(r"[ \t]+", " ", "".join(parts)).strip() if self.gaps == 0 else "".join(parts).strip()


def read_pdf(path):
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "doc")
        subprocess.run(["pdftohtml", "-xml", "-i", "-q", "-nodrm", "-enc", "UTF-8", path, out], check=True)
        root = ET.parse(out + ".xml").getroot()
    fonts, pages = {}, []
    for page in root.iter("page"):
        frags = []
        for el in page:
            if el.tag == "fontspec":
                fonts[el.get("id")] = (float(el.get("size")), el.get("family"))
            elif el.tag == "text":
                f = Frag(el, fonts)
                if f.text.strip():
                    frags.append(f)
        frags.sort(key=lambda f: (f.top, f.left))
        lines = []
        for f in frags:
            for ln in reversed(lines[-4:]):
                if ln.overlaps(f):
                    ln.frags.append(f)
                    break
            else:
                lines.append(Line(f))
        for ln in lines:
            ln.finish()
        lines = [ln for ln in lines if ln.text]
        lines.sort(key=lambda ln: (ln.top, ln.left))
        pages.append({"height": float(page.get("height")), "lines": lines})
    return pages


def dehyphenate_join(a, b, vocab):
    """Join two wrapped lines, fixing words split across them."""
    if re.search(r"https?://\S*$", a) and not a.endswith("."):
        return a + b
    if re.search(r"https?://\S*\.$", a) and b[:1].islower():
        return a + b
    m = re.search(r"(\w+)-$", a)
    if m and b[:1].islower():
        head, tail = m.group(1), re.match(r"\w+", b).group(0) if re.match(r"\w+", b) else ""
        joined, hyphened = (head + tail).lower(), (head + "-" + tail).lower()
        if vocab[hyphened] > vocab[joined]:
            return a + b
        return a[:-1] + b
    return a + " " + b


def pdf_to_md(path):
    pages = read_pdf(path)
    all_lines = [ln for p in pages for ln in p["lines"]]
    sizes = collections.Counter()
    for ln in all_lines:
        sizes[ln.size] += len(ln.text)
    body = sizes.most_common(1)[0][0]
    vocab = collections.Counter(w.lower() for ln in all_lines for w in re.findall(r"\w+(?:-\w+)*", ln.text))
    for ln in all_lines:
        for w in re.findall(r"\w+(?:-\w+)+", ln.text.lower()):
            vocab[w] += 1

    # Running headers: the same short text at the top of many pages.
    tops = collections.Counter()
    for p in pages:
        for ln in p["lines"]:
            if ln.top < 0.08 * p["height"]:
                tops[re.sub(r"\d+", "#", ln.text)] += 1
    running = {t for t, n in tops.items() if n >= 3}

    body_lines, notes, note_order = [], {}, []
    last_note = None
    for pno, p in enumerate(pages):
        h = p["height"]
        keep = []
        for ln in p["lines"]:
            if re.fullmatch(r"\d{1,3}|[ivxlc]{1,6}", ln.text) and (ln.top > 0.85 * h or ln.top < 0.1 * h):
                continue  # page number
            if ln.top < 0.08 * h and re.sub(r"\d+", "#", ln.text) in running:
                continue
            keep.append(ln)
        # Footnotes: a trailing block of small lines that starts with a note number.
        i = len(keep)
        while i > 0 and keep[i - 1].size <= 0.9 * body:
            i -= 1
        start = None
        for j in range(i, len(keep)):
            ln = keep[j]
            if ln.top < 0.4 * h:
                continue
            if ln.lead_note or re.match(r"\d{1,3}\s+\S", ln.text):
                start = j
                break
        if start is not None:
            # Table rows that sit among the notes go back to the body.
            stray = [ln for ln in keep[start:] if ln.gaps >= 2]
            for ln in keep[start:]:
                if ln.gaps >= 2:
                    continue
                num = ln.lead_note
                text = ln.text
                if not num:
                    m = re.match(r"(\d{1,3})\s+(.*)", text)
                    if m and (last_note is None or int(m.group(1)) == int(last_note) + 1):
                        num, text = m.group(1), m.group(2)
                if num:
                    last_note = num
                    if num not in notes:
                        note_order.append(num)
                    notes[num] = text
                elif last_note:
                    notes[last_note] = dehyphenate_join(notes[last_note], text, vocab)
            keep = keep[:start] + stray
        for ln in keep:
            ln.page = pno
        body_lines.extend(keep)

    caption_re = re.compile(r"^(Figure|Fig\.|Table)\s+[A-Z]?\d+(\.\d+)?[:.]")
    terminal_re = re.compile(r"[.:?!\"”)\]]$")

    # Headings: bigger than body text, or short bold lines that read like titles.
    def is_heading(ln):
        text = ln.text.strip()
        if ln.gaps or len(text) < 3 or len(text) > 140 or caption_re.match(text) or text[0] in "•◦":
            return False
        if not re.match(r"[A-Z0-9]", text) or re.search(r"[a-z]\. [A-Z]", text):
            return False
        if ln.page == 0:
            return bool(re.fullmatch(r"(\d+\.?\s+)?Introduction", text))
        if ln.size >= 1.12 * body:
            return True
        return ln.bold and abs(ln.size - body) < 1 and len(text) < 90 and not re.search(r"[.,;:]$", text)

    head_sizes = sorted({round(ln.size) for ln in body_lines if is_heading(ln)}, reverse=True)

    def level(ln):
        r = round(ln.size)
        idx = head_sizes.index(r) if r in head_sizes else len(head_sizes)
        return min(3 + idx, 6)

    lefts = collections.Counter(round(ln.left) for ln in body_lines if abs(ln.size - body) < 1)
    margin = lefts.most_common(1)[0][0]
    rights = sorted(ln.right for ln in body_lines if abs(ln.size - body) < 1)
    rmax = rights[int(0.9 * (len(rights) - 1))]
    steps = collections.Counter()
    for a, b in zip(body_lines, body_lines[1:]):
        if a.page == b.page and abs(a.size - body) < 1 and abs(b.size - body) < 1:
            steps[round(b.top - a.top)] += 1
    lead = steps.most_common(1)[0][0] if steps else body * 1.2

    out = []
    para, kind, table = None, None, []
    pending = None  # (slot in out, text) of a paragraph cut off by a figure or table
    in_refs = False

    def settle_pending():
        nonlocal pending
        if pending:
            out[pending[0]] = pending[1]
            pending = None

    def end_para(interrupted=False):
        nonlocal para, kind, pending
        if para is not None:
            if interrupted and kind == "text" and not in_refs and not terminal_re.search(para):
                settle_pending()
                out.append(None)
                pending = (len(out) - 1, para)
            elif kind == "title":
                out.append(f"**{para}**")
            else:
                out.append("\\" + para if para.startswith("#") and kind != "heading" else para)
        para, kind = None, None

    def end_table():
        nonlocal table
        if table:
            out.append("```text\n" + "\n".join(table) + "\n```")
            table = []

    def start(text, new_kind):
        nonlocal para, kind, pending
        end_table()
        if new_kind == "text" and pending and text[:1].islower():
            para = dehyphenate_join(pending[1], text, vocab)
            pending = None
        else:
            settle_pending()
            para = text
        kind = new_kind

    prev = pprev = None
    for ln in body_lines:
        text = ln.text.strip()
        if ln.page == 0 and ln.size >= 1.3 * body:
            # Title block on the first page.
            if kind == "title" and prev is not None and prev.size == ln.size:
                para += " " + text
            else:
                end_para()
                start(text, "title")
            pprev, prev = prev, ln
            continue
        if ln.page == 0 and ln.gaps:
            text = re.sub(r"\s{2,}", " · ", text)
        if kind == "heading" and para.endswith("-") and prev is not None and prev.size == ln.size:
            para = dehyphenate_join(para, text, vocab)
            pprev, prev = prev, ln
            continue
        if is_heading(ln):
            text = re.sub(r"\s+", " ", text)
            if kind == "heading" and prev is not None and prev.size == ln.size and prev.page == ln.page \
                    and ln.top - prev.bottom < lead:
                para = dehyphenate_join(para, text, vocab)
            else:
                end_para()
                settle_pending()
                start("#" * level(ln) + " " + text, "heading")
            in_refs = bool(REFERENCES_RE.match(text))
            pprev, prev = prev, ln
            continue
        if caption_re.match(text):
            end_para(interrupted=True)
            start(text, "caption")
            pprev, prev = prev, ln
            continue
        if ln.gaps >= 2 and ln.page > 0:
            end_para(interrupted=True)
            table.append(ln.text)
            pprev, prev = prev, ln
            continue
        if text[0] in "•◦":
            end_para(interrupted=True)
            start("- " + text[1:].strip(), "bullet")
            pprev, prev = prev, ln
            continue
        new = para is None or kind in ("title", "heading") or prev is None
        if not new:
            same_page = ln.page == prev.page
            indented = ln.left > margin + 8
            run_in = ln.frags[0].bold and not ln.bold and terminal_re.search(para) is not None
            if in_refs:
                new = not indented
            elif kind == "bullet":
                new = (same_page and ln.top - prev.top > 1.45 * lead) or (not indented and terminal_re.search(para) is not None)
            else:
                new = (
                    (same_page and ln.top - prev.top > 1.45 * lead)
                    or (indented and prev.left <= margin + 3)
                    or (prev.right < max(ln.right, pprev.right if pprev else rmax) - 40
                        and terminal_re.search(prev.text) is not None)
                    or abs(ln.size - prev.size) > 1.5
                    or run_in
                )
        if new:
            end_para(interrupted=kind == "text" and ln.page != getattr(prev, "page", ln.page))
            start(text, "text")
        else:
            para = dehyphenate_join(para, text, vocab)
        pprev, prev = prev, ln
    end_para()
    end_table()
    settle_pending()
    out = [o for o in out if o]

    md = "\n\n".join(out)
    if note_order:
        md += "\n\n### Notes\n\n" + "\n".join(f"[^{n}]: {notes[n]}" for n in note_order)
    # Drop markers whose note we never found, so they don't render as broken links.
    md = re.sub(r"\[\^(\d+)\](?!:)", lambda m: m.group(0) if m.group(1) in notes else "", md)
    return md.strip() + "\n"


def arxiv_to_md(arxiv_id):
    url = f"https://arxiv.org/html/{arxiv_id}"
    with urllib.request.urlopen(url) as r:
        page = r.read().decode("utf-8")
    m = re.search(r"<article.*?</article>", page, re.S)
    if not m:
        sys.exit(f"No HTML rendering for {arxiv_id}; download the PDF and convert that instead.")
    article = m.group(0)
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=article, capture_output=True, text=True, check=True).stdout
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)  # figures are images; keep their captions only
    md = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", md)  # in-page links (citations, figure refs)
    md = md[md.find("\n#") + 1:] if "\n#" in md else md  # LaTeX preamble debris before the title
    md = re.sub(r"^(#{1,4}) ", lambda m: "#" * min(len(m.group(1)) + 2, 6) + " ", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return clean(md).strip() + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    sys.stdout.write(arxiv_to_md(src[6:]) if src.startswith("arxiv:") else pdf_to_md(src))
