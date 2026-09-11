#!/usr/bin/env python3
"""Regenerate every planted-violation fixture from clean/.

Each fixture is clean/ plus exactly ONE change. That claim is what makes a missed
finding unambiguous, so it is enforced here rather than asserted in prose: every
edit below asserts its target appears exactly once before replacing it.

    python3 _build.py          # rebuild, then `git diff` to see nothing else moved

The conformant variants (clean-02, clean-03, clean-04) are authored, not generated.
"""
import shutil, pathlib
F = pathlib.Path(__file__).parent
C = F / "clean"

BROKEN = [
 ("broken-01-headcount", "R-04", "FAIL · BLOCKING",
  "Company size raised above the limit of 20.",
  [("registration-form.md", "| Total employees | 7 |", "| Total employees | 22 |"),
   ("registration-form.md", "| Of which technical | 5 |", "| Of which technical | 15 |"),
   ("executive-summary.md", "Seven people. Two founders", "Twenty-two people. Two founders"),
   ("executive-summary.md", "plus three ML engineers, one backend engineer and one\npart-time commercial lead. Five are technical.",
    "plus fifteen ML engineers, three backend engineers and two\ncommercial leads. Fifteen are technical.")]),
 ("broken-02-age-unjustified", "R-02", "FAIL · BLOCKING",
  "Incorporated 13 years ago, with no justification anywhere in the package.",
  [("registration-form.md", "| Date of legal incorporation | 14 March 2023 |", "| Date of legal incorporation | 14 March 2013 |")]),
 ("broken-03-age-justified", "R-02", "PASS",
  "Incorporated 13 years ago — but the package documents a pivot, which Art. 3(2) admits in the "
  "same sentence. A finding here is a FALSE POSITIVE: the auditor quoted the age limit without "
  "reading 'unless justified'.", []),
 ("broken-04-sector", "R-05", "FAIL · NON-CONFORMANT",
  "Operates outside the priority sectors. Art. 3(5) says the company *should* belong to one, and "
  "Art. 4 admits applicants outside them at the Organizer's discretion. Marking this BLOCKING is "
  "severity inflation, forbidden by rules.md § 8.",
  [("registration-form.md", "Primary sector: **Policy Making & Public Administration**", "Primary sector: **Logistics & Freight Optimisation**"),
   ("registration-form.md", "Secondary relevance: Communication & Media (municipal records and publication archives).", "Secondary relevance: none."),
   ("executive-summary.md", "The strategic fit with the AI Factory is direct: this is AI applied to public administration,",
    "The strategic fit with the AI Factory is indirect: this is AI applied to freight logistics,")]),
 ("broken-05-summary-length", "R-08", "FAIL · NON-CONFORMANT",
  "Executive Summary declared at 7 pages against a 5-page maximum. Present, so not blocking.",
  [("executive-summary.md", "*Length as submitted: **5 pages** (PDF, A4).", "*Length as submitted: **7 pages** (PDF, A4)."),
   ("registration-form.md", "| Executive Summary | Yes | `executive-summary.md` — 5 pages |", "| Executive Summary | Yes | `executive-summary.md` — 7 pages |")]),
 ("broken-06-video-missing", "R-09", "FAIL · BLOCKING",
  "No Presentation Video submitted. Art. 6.1 conditions assessment on it.",
  [("registration-form.md", "| Presentation Video | Yes | `presentation-video.md` — 58 seconds |", "| Presentation Video | No | Not submitted |")]),
 ("broken-07-non-eu", "R-01", "FAIL · BLOCKING",
  "Incorporated outside the European Union, with a US federal tax id rather than an EU one.",
  [("registration-form.md", "| Legal form | Sociedad Limitada |", "| Legal form | Delaware C Corporation |"),
   ("registration-form.md", "| Country of incorporation | Spain (European Union) |", "| Country of incorporation | United States (Delaware) |"),
   ("registration-form.md", "| Tax identification number | ESB-67451209 |", "| Tax identification number | EIN 88-4013967 |"),
   ("registration-form.md", "| Registered address | Carrer de Pallars 193, 08005 Barcelona, Spain |", "| Registered address | 1209 Orange St, Wilmington, DE 19801, United States |")]),
 ("broken-08-onsite", "R-06", "FAIL · BLOCKING",
  "On-site presence twice weekly, against a stated minimum of three times per week.",
  [("registration-form.md", "Site **four days per week** (Monday, Tuesday, Wednesday, Thursday)", "Site **two days per week** (Tuesday, Wednesday)"),
   ("executive-summary.md", "The CTO and one ML engineer will be on site four days a week.", "The CTO and one ML engineer will be on site two days a week.")]),
]

PIVOT_NOTE = """## 2b · Note on corporate age

Cartulary was incorporated in 2013 as a document-digitisation bureau. The company pivoted to
sovereign context hosting in 2023, when the current founding team took over, the prior service
line was wound down, and headcount fell from 31 to 4 before rebuilding. The product line
described in this application dates from that pivot.

## 3 · Sector"""

PARAPHRASE = [
 ("a", "plain numeral", "We are a team of 22. Two founders",
  "Twenty-two, stated as a numeral in running prose."),
 ("b", "number written out", "Headcount currently stands at twenty-two FTEs. Two founders",
  "Twenty-two, written out as a word."),
 ("c", "requires summing", "Our staff: 14 engineers, 5 in operations, 3 in commercial. Two founders",
  "Never stated as a total. The auditor must add 14 + 5 + 3 to reach 22."),
]

def edit(path, old, new):
    s = path.read_text()
    assert s.count(old) == 1, f"{path}: expected 1 occurrence, found {s.count(old)}: {old[:50]!r}"
    path.write_text(s.replace(old, new))

def fresh(name):
    d = F / name
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(C, d)
    return d

for name, rid, expect, why, edits in BROKEN:
    d = fresh(name)
    if name == "broken-03-age-justified":
        edit(d/"registration-form.md", "| Date of legal incorporation | 14 March 2023 |",
             "| Date of legal incorporation | 14 March 2013 |")
        edit(d/"registration-form.md", "## 3 · Sector", PIVOT_NOTE)
    for f, old, new in edits:
        edit(d/f, old, new)
    if name == "broken-06-video-missing":
        (d/"presentation-video.md").unlink()
    (d/"README.md").write_text(f"""# Fixture: {name}

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `{rid}` |
| **Expected verdict** | `{expect}` |
| **What was changed** | {why} |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
""")
    print(f"  {name:32s} {rid} -> {expect}")

for k, label, opening, why in PARAPHRASE:
    d = fresh(f"paraphrase-{k}")
    edit(d/"registration-form.md", "| Total employees | 7 |\n| Of which technical | 5 |",
         "| Total employees | *see Executive Summary, page 5* |")
    edit(d/"executive-summary.md", "Seven people. Two founders", opening)
    edit(d/"executive-summary.md",
         "plus three ML engineers, one backend engineer and one\npart-time commercial lead. Five are technical.",
         "plus the engineering and commercial staff above.")
    (d/"README.md").write_text(f"""# Fixture: paraphrase-{k} — {label}

**Cartulary is a fictional company.** Every fact here was invented for this repository.

One of three fixtures carrying **the same violation**, worded three ways: 22 employees against
a limit of fewer than 20 (`R-04`, § II Art. 3(4)). The explicit headcount field has been removed
from the registration form, so the prose is the only source.

| | |
| --- | --- |
| **Requirement touched** | `R-04` |
| **Expected verdict** | `FAIL · BLOCKING` — identically in a, b and c |
| **How it is worded here** | {why} |

## What this set tests

Not whether the gate fires. Whether it fires on the **provision** or on the **phrasing**.

If it fires on one or two of the three, it is matching strings, not applying a rule — and the
ones it missed look exactly like clean passes, which is why this failure normally goes
unnoticed. `-c` is the hard case: the total is never stated and has to be summed.
""")
    print(f"  paraphrase-{k:22s} R-04 -> FAIL · BLOCKING")
print("regenerated from clean/")
