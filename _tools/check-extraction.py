#!/usr/bin/env python3
"""Check the section files against the PDF, word for word, page by page, with two extractors.

    python3 _tools/check-extraction.py

Exit 0 if every page's words in reference/<nn>-*.md match what at least one extractor reads off
that page of the PDF. Exit 1 if any word matches neither. Exit 3 if an extractor is missing.
Needs pdfplumber (pip install pdfplumber) and pdftotext (poppler).

Why two. One extractor can invent text the PDF does not hold, and a checker that compares
quotes against that extraction will then enforce the invention. That happened here: pypdf split
"should" into "s hould" and moved two tables, SOURCES.md defended the splits as the PDF's own
kerning, and check-citations.py failed any run that quoted the PDF correctly. Two extractors
built differently rarely invent the same thing. Where they disagree, this prints the words, and
a person looks at the page and decides.

What it compares is a multiset of words per page, not their order. Order is a layout decision
(tables especially) and is checked by reading, not by this script. Running headers and footers
(any line that repeats on more than half the pages, digits ignored) are not compared, because
the section files leave them out.

Each section file's page markers say which page its text is on: the first [pN] is the page the
section starts on, and each later one is where that page begins.
"""
import re, sys, shutil, subprocess, pathlib
from collections import Counter

R = pathlib.Path(__file__).resolve().parent.parent
REF = R/"reference"

try:
    import pdfplumber
except ImportError:
    sys.exit(print("pdfplumber is not installed: pip install pdfplumber") or 3)
if not shutil.which("pdftotext"):
    sys.exit(print("pdftotext is not installed (poppler)") or 3)

pdf = next(REF.glob("*.pdf"), None)
sections = sorted(REF.glob("[0-9][0-9]-*.md"))
if not pdf or not sections:
    sys.exit("Nothing to check: reference/ needs the PDF and its section files.")

# the section files, as words per page
held, page = {}, None
for f in sections:
    text = re.sub(r"<!--.*?-->", " ", f.read_text(), flags=re.S)
    for line in text.split("\n"):
        if line.startswith("# "):
            continue
        for part in re.split(r"(\[p\d+\])", line):
            m = re.fullmatch(r"\[p(\d+)\]", part)
            if m:
                page = int(m.group(1)); held.setdefault(page, Counter()); continue
            if part.strip():
                if page is None:
                    sys.exit(f"{f.name} has text before its first [pN] marker - no page to check it against.")
                held.setdefault(page, Counter()).update(part.split())

# the two extractors, as lines per page
with pdfplumber.open(pdf) as doc:
    n = len(doc.pages)
    plumber = {i: (p.extract_text() or "").split("\n") for i, p in enumerate(doc.pages, 1)}
poppler = {i: subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(pdf), "-"],
                             capture_output=True, text=True).stdout.split("\n") for i in range(1, n + 1)}

shape = lambda l: re.sub(r"\d+", "#", l.strip())
seen = Counter(s for pages in (plumber, poppler) for i in pages for s in {shape(l) for l in pages[i] if l.strip()})
furniture = {s for s, c in seen.items() if c > n}          # counted across both extractors
words = lambda lines: Counter(w for l in lines if shape(l) not in furniture for w in l.split())

bad = 0
print(f"\n{pdf.name}: {n} pages · sections cover pages {min(held)}-{max(held)}\n" + "=" * 58)
for i in range(1, n + 1):
    a, b, s = words(plumber[i]), words(poppler[i]), held.get(i, Counter())
    if i < min(held):
        print(f"  p{i:<3} not stored ({sum(a.values())} words)"); continue
    neither = {w: s[w] for w in set(a) | set(b) | set(s) if s[w] != a[w] and s[w] != b[w]}
    disagree = {w: (a[w], b[w], s[w]) for w in set(a) | set(b) if a[w] != b[w]}
    if neither:
        bad += 1
        print(f"  p{i:<3} FAIL  words matching neither extractor (word: sections / pdfplumber / pdftotext):")
        for w in sorted(neither):
            print(f"          {w!r}: {s[w]} / {a[w]} / {b[w]}")
    else:
        print(f"  p{i:<3} ok    {sum(s.values())} words")
    if disagree:
        print(f"        extractors disagree - look at the page (pdfplumber / pdftotext / sections):")
        for w, (x, y, z) in sorted(disagree.items()):
            print(f"          {w!r}: {x} / {y} / {z}")

print("=" * 58)
print(f"{bad} page(s) hold words neither extractor reads" if bad else
      "Every stored word matches the PDF, by at least one extractor.")
sys.exit(1 if bad else 0)
