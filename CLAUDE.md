# Notes for working on this site

Static site on GitHub Pages, served straight from `main`. `.nojekyll` turns Jekyll off, so `.md` and `.txt` files are served as plain text.

## Keep the agent-readable files in sync

`index.html` is the source of truth for the paper lists. After any change to the publication lists, to `papers/`, or to `cv.md`, run

    python3 scripts/build_agent_files.py

and commit everything it changes. `python3 scripts/build_agent_files.py --check` exits 1 if anything is stale.

The script rewrites the header of each `papers/<slug>.md`, `llms.txt`, `llms-full.txt`, `publications.bib`, `sitemap.xml`, `robots.txt`, the JSON-LD block in `index.html`, and the "Plain text" link on each paper that has full text.

- **New paper:** add the `<li class="publication-item">` as usual, then run the script. It adds `data-paper="<slug>"` to the listing and creates `papers/<slug>.md`. Put the DOI and full author names (as "Family, Given") in `papers/metadata.json`.
- **Abstract:** an `## Abstract` section in `papers/<slug>.md`.
- **Full text:** `python3 scripts/paper_to_md.py <file.pdf | arxiv:ID>` (needs `brew install poppler pandoc`). Paste the output under `## Full text`, after a one-line note naming the source URL. Use only versions that are already public (the site's own PDFs, arXiv, OSF, SSRN), never a publisher's PDF.
- Never edit above the `END OF GENERATED HEADER` line in a paper file; the script overwrites it.
- Never change an existing `data-paper` slug. It is the paper's public URL.
- `cv.md` is a transcription of `CV.pdf` without the phone numbers or postal address. Update it whenever `CV.pdf` changes.
