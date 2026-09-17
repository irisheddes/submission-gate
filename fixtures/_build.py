#!/usr/bin/env python3
"""Regenerate every planted-violation fixture from clean/.

Each fixture is clean/ plus exactly ONE change. That claim is what makes a missed
finding unambiguous, so it is enforced here rather than asserted in prose: every
edit below asserts its target appears exactly once before replacing it.

    python3 _build.py          # rebuild, then `git diff` to see nothing else moved

The conformant variants (clean-02, clean-03, clean-04) are authored, not generated.

broken-04-sector is the one planted fixture whose Executive Summary is authored rather than
edited: the control's summary is about public administration from its first line to its last,
so changing only the declared sector planted a second fault, a package contradicting itself.
Blind case 11 found that on 2026-09-17 (runs/blind-case-11-2026-09-17.md). Its summary below
keeps every fact another requirement depends on - seven staff, five pages, the three kinds of
AI evidence, TRL 6, two people on site four days - and changes only the sector the company
works in. The assertions after the rebuild check that.
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
  "Operates outside the priority sectors: freight logistics, declared on the form and described "
  "throughout the Executive Summary. Art. 3(5) says the company *should* belong to one, and Art. 4 "
  "admits applicants outside them at the Organizer's discretion. Marking this BLOCKING is severity "
  "inflation, forbidden by rules.md § 8. (Until 2026-09-17 only the form and one sentence changed, "
  "and the rest of the summary still described public administration - a second fault, found by "
  "blind case 11.)",
  [("registration-form.md", "Primary sector: **Policy Making & Public Administration**", "Primary sector: **Logistics & Freight Optimisation**"),
   ("registration-form.md", "Secondary relevance: Communication & Media (municipal records and publication archives).", "Secondary relevance: none.")]),
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

LOGISTICS_SUMMARY = """# Cartulary — Executive Summary

*BSC AI Factory Incubation Programme, Call 3. Submitted 2026-09-08.*
*Length as submitted: **5 pages** (PDF, A4). FICTIONAL — see README.md.*

---

## Page 1 · The problem

Agentic AI has a working architecture for knowledge work, and European freight operators
cannot trust it with their dispatch floor.

The architecture is interpretable context methodology: instead of hiding a process inside
model weights or framework code, you express it as a folder of plain files a person can read
— what the agent is, what rules it follows, what it may and may not load at each step. One
model walks the structure. A dispatcher can open any folder and see exactly what the system
was told. For freight this is not a nicety; when a load is rerouted, refused or delivered late,
the operator has to explain to the shipper and the carrier why, and a folder can be read in a
way an embedding cannot.

The platforms that host these workspaces are American. That places the workspace — which for
a road-freight operator holds consignment notes, shipper contracts, rate agreements and the
reasoning applied to them — on infrastructure the operator does not control, next to the
commercial data of its competitors' platforms. Shippers write data-location clauses into
their contracts, and the largest of them audit those clauses. The outcome is predictable:
pilots that never leave the sandbox, tenders that stall at the shipper's security review, and
a working methodology adopted everywhere except the operators whose margins most depend on
getting dispatch right.

The methodology is not the gap. The hosting is.

## Page 2 · What we build

Cartulary is European hosting for interpretable context workspaces: the same folder-shaped
architecture, run entirely on European infrastructure, with the guarantees a freight operator
has to be able to write into a shipper contract.

Three things, none of which is a model:

1. **Location with proof.** Every workspace, every document and every inference stays in the
   EU. Not a statement of intent — a per-request log a shipper's security team can audit, naming
   which node served it.
2. **The folder is the record.** Because the workspace is plain files, the archive of what the
   agent was told is the workspace itself, versioned. When a delivery dispute reaches a claim
   months later, the exact context that produced the dispatch decision can be reconstructed and
   read.
3. **Inference on EU compute.** Open-weight models served from European hardware, so the
   location guarantee survives the part where the work actually happens.

### Why this is infrastructure and not a promise

A data-location promise written into a service agreement is a request. A location guarantee
enforced by the fact that no node outside the Union can serve the request is a constraint.
Large shippers have learned to tell the difference, which is why so many pilots die at the
security review: the vendor offers the first and the reviewer needs the second.

The same distinction shapes the product. An interpretable workspace already separates the
part the operator owns — its loads, its documents, its dispatch decisions — from the part the
platform maintains. Hosting that split is the whole job: the operator's half never leaves the
jurisdiction, the platform's half updates underneath it, and neither can silently absorb the
other. We hold the split as a hard boundary rather than a convention, because a convention is
something an upgrade can quietly cross.

And because the workspace is files under version control, it accretes. The record of what the
system was told is not a log written beside the work — it *is* the work, at every past
version. A dispatch decision disputed next season is reconstructed by checking out the
workspace as it stood, not by trusting a description of it.

The methodology is published and open (Van Clief & McDermott, *Folder Structure as Agentic
Architecture*, arXiv:2603.16021, MIT-licensed). We did not invent it and do not claim it. What
does not exist is a European place to run it for freight, and that absence is the whole
company.

## Page 3 · Technical maturity and why HPC

Technology Readiness Level 6: running with two Catalan road-freight operators under pilot
agreements, 340,000 documents, eleven live workspaces.

- **Trained models:** three fine-tuned encoders for Catalan and Spanish consignment notes and
  delivery records, plus a routing model that decides which part of a workspace a query needs
  — the component that makes narrow context loading work at fleet scale.
- **Annotated datasets:** 41,000 dispatcher-confirmed shipment-record pairs and 12,000
  delivery-exception labels, annotated by working dispatchers over eighteen months. To our
  knowledge the only labelled corpus of its kind for Iberian road-freight documents.
- **Validated algorithms:** routing reaches 0.91 macro-F1 on held-out workspaces; provenance
  reconstruction resolves 0.97 of citations to a specific file and version.

What we cannot do is serve inference at the scale of a national fleet on hardware we can
afford to rent in Europe, which is precisely the constraint the AI Factory exists to remove.
Access to MareNostrum5 would let us do two things we have specified and cannot run: train one
cross-operator routing model instead of one per operator, and benchmark open-weight serving
against the commercial APIs our customers' shippers will not let them call.

## Page 4 · Market and strategic relevance

Road carries most of the Union's inland freight, and the operators behind it are
overwhelmingly small. Every one of them is being sold agentic AI, and every one of them hits the same wall at the same point in a shipper's
tender.

We sell per-workspace hosting with an annual support component, to the operator or to the
logistics group serving several. Two paid pilots to date. The buyer is usually not the
operations director — it is the person answering the shipper's security questionnaire, who
has been saying no for two years and would prefer to say yes.

**We are not proposing to rebuild the American platforms in Europe.** They are good, they are
years ahead, and duplicating them would waste the head start the open methodology gave
everyone. The missing piece is narrower and duller: a European tier those platforms can hand a
workspace to when the customer's shipper requires it — European storage, European inference,
European audit trail, and nothing else different. The platform keeps the customer and the
product; the workspace simply runs on compute inside the jurisdiction.

That is what makes European HPC the right substrate rather than another commercial cloud. A
tier whose guarantee rests on a commercial provider's regional pledge is back to a promise;
one that runs on infrastructure located and operated in the Union is a fact about where the
hardware is.

The strategic fit with the AI Factory is indirect: this is AI applied to freight logistics,
built on European compute, where explainability and data location are contractual demands
rather than preferences. It is also, plainly, an argument for European AI infrastructure
having a commercial customer outside research.

## Page 5 · Team and use of the Programme

Seven people. Two founders — a freight dispatcher of fourteen years and an ML engineer
previously at a Barcelona research group — plus three ML engineers, one backend engineer and one
part-time commercial lead. Five are technical.

What we would use the Programme for, in order:

1. **Compute** — the cross-operator routing model, specified and unrun.
2. **Serving** — benchmarking open-weight inference on EU hardware against the commercial
   APIs our customers cannot use, and publishing the comparison.
3. **Proximity** — the Barcelona site is where the Catalan language-resource groups are, and
   annotation is our bottleneck.

There is a pattern worth naming. The published methodology has produced a large body of
working folder-shaped systems, and only a small fraction of them are wired to anything a
non-author can actually use. The gap between a folder that works on its author's laptop and a
system a freight operator can adopt is not intelligence, and it is not method — it is hosting,
identity, versioning and a guarantee about where the bytes are. Those are unglamorous and they
are the entire adoption barrier for the operators who most need dispatch they can explain.

If the Programme wanted one sentence: the methodology for interpretable AI is already
published and already works. European freight is missing the place to run it, and that is a
hosting problem, not a research problem.

The CTO and one ML engineer will be on site four days a week.
"""

# Facts other requirements are scored on. The authored summary must keep every one of them.
KEPT_FACTS = ["*Length as submitted: **5 pages** (PDF, A4).", "Seven people. Two founders",
              "Five are technical.", "Technology Readiness Level 6", "**Trained models:**",
              "**Annotated datasets:**", "**Validated algorithms:**",
              "The CTO and one ML engineer will be on site four days a week."]
# Words that would put the authored summary back inside a priority sector.
SECTOR_WORDS = ["municipal", "public bod", "public admin", "civil servant", "citizen", "health",
                "agricultur", "climate", "financ", "legal", "polic", "media", "energy"]

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
    if name == "broken-04-sector":
        (d/"executive-summary.md").write_text(LOGISTICS_SUMMARY)
        s = LOGISTICS_SUMMARY.lower()
        missing = [f for f in KEPT_FACTS if f not in LOGISTICS_SUMMARY]
        assert not missing, f"broken-04 summary lost facts other rows depend on: {missing}"
        leaks = [w for w in SECTOR_WORDS if w in s]
        assert not leaks, f"broken-04 summary drifts toward a priority sector: {leaks}"
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
