# Loading a standard

The procedure for pointing this auditor at a rulebook. Run once, at setup — **never during an
audit.** A standard that arrives mid-run is not resident, cannot be cited by section, and
cannot carry stable requirement IDs.

This is what makes the auditor general. The machinery in `../identity.md` and `../rules.md`
names no funder and no provision; everything specific to a standard lives in this folder and
arrives through the steps below.

---

## Before anything — the question that gates the rest

**Is the document publicly available, at a URL anyone can open without a login?**

If not, stop. A finding citing a provision the reader cannot open is not checkable, and an
auditor whose standard cannot be opened is an opinion generator. Either obtain a version that
can be published, or accept that this auditor cannot be shared — those are the only two
honest outcomes.

## 1 · Vendor the document

Download it from the publisher's own URL, not from a copy. Record the URL, the date, and the
hash:

```sh
curl -sL -o reference/<slug>.pdf "<publisher URL>"
shasum -a 256 reference/<slug>.pdf
```

The hash goes in `SOURCES.md` with a re-download command, so any reader can prove the vendored
copy is byte-identical to what the publisher serves — and so a later reader can tell whether a
clean report meant compliance or meant the folder was reading a version that no longer exists.

## 2 · Split at the document's own seams

One file per section, `<nn>-<slug>.md`, numbered in the document's own order. Not by topic, not
by what seems useful — by the seams the publisher put there.

**Verbatim.** Its spelling, its numbering, its mistakes. The Call 3 rulebook prints "ELEGIBLE"
and "JURISDICITION"; both are kept. A citation that silently corrects its source is no longer a
citation, and a corrected excerpt is the clearest evidence that nobody checked it against the
original.

**Extract with two tools and reconcile them.** One extractor can invent text the document does
not hold, and everything downstream then enforces the invention. This folder learned that the
hard way: pypdf split `should` into `s hould`, moved two tables into the wrong sections, and
this repository defended the splits as the PDF's own kerning for a week. The citation checker
then rejected any run that quoted the PDF correctly. Judges found it by measuring the glyphs.
See `SOURCES.md`.

So: extract with two tools built differently (here pdfplumber and pdftotext), compare them word
for word on every page, and **where they disagree, look at the page** and keep what it prints.
Never adopt one tool's output because it looks tidy, and never defend an oddity as "the source"
until a second tool and the page agree. `../_tools/check-extraction.py` does the comparison and
prints every disagreement. Write tables out one cell at a time, so a quoted cell stays whole.

Insert page markers (`[pN]`) if the source paginates, and **say in each file's header that you
inserted them.** Start each file with the marker for the page it begins on. Declared insertions
are fine; undeclared ones are tampering.

Each file's header carries: the source title, the edition, what was captured, the extractors
used, and the date.

## 3 · Write `SOURCES.md`

Title, publisher, edition, URL, date read, public-or-not, language, hash, size. This is the
page that answers "which version was this audit made against?" two years later.

**The language of publication, always.** A translation is not the standard and may not be
shipped as one; if a rendering helps, it sits beside the original, labelled, and is never
cited.

## 4 · Write `INDEX.md` and `PROVISIONS.md`

The section list, plus a **topic→section map** — "looking for who may apply → section 02". The
map is what makes narrow loading possible; without it an agent opens files until it finds the
right one, which is the whole cost the split was meant to avoid.

State what is stored and what is not. "The whole document" is a valid answer and a useful one.

**Then write `PROVISIONS.md`: every provision a finding could cite, mapped by hand to the file
and the exact stretch of text that holds it.** `../_tools/check-citations.py` uses it to check
that a quote sits under the provision it is cited to. Without the map it can only check that
the quote is somewhere in the standard, so a row citing the wrong article passes. Write each
row explicitly. Don't derive rows from filenames or page numbers, because documents break
those rules: tables run over pages, clauses repeat numbers, articles get misnumbered. Then run
`python3 ../_tools/test-citations.py`, after rewriting its cases in `../_tools/tests/citations/`
to quote the new standard. It must show a neighbour swap and a non-existent provision failing.

## 5 · Derive `REQUIREMENTS.md`

Extract every obligation the standard places on the party being audited — *shall, must,
required, should* — before looking at any package. One row per obligation, each citing the
section it came from.

**Read the verb.** `must` bars; `should` does not. A requirement stated as a preference that
gets marked `BLOCKING` is severity inflation, and it is the most common way an auditor stops
being trusted.

**Split a requirement whose halves differ.** Art. 3(3) of the Call 3 rulebook says a company
*must* demonstrate AI use and *should* be at a given readiness level — two verbs, two
severities, and the readiness definition sits at an external URL this folder does not hold.
They are `R-03` and `R-03b` for that reason: one verifiable half should not be dragged down by
an unverifiable one.

**Mark what points outward.** Where the standard defines a term by reference to a document you
do not hold, that requirement can be raised but never `CONFIRMED`. Say so in the row.

## 6 · Rebuild the fixtures

**Fixtures do not survive a change of standard.** A planted violation breaks a *specific
provision*; point the folder at a new rulebook and every fixture in `../fixtures/` is testing
something that no longer exists.

Rebuild: one conformant control, several conformant variants that look unusual and are correct,
one planted violation per fixture, and a paraphrase set carrying one violation worded three
ways. `../fixtures/CONTEXT.md` holds the rules; `../fixtures/_build.py` is a worked example of
generating them from a control with exactly one change each.

**Watch for date-relative requirements.** A fixture built to sit at an age limit is correct on
the day it is written and wrong afterwards. One in this repository was wrong the day it was
written — see `../runs/fixtures-2026-09-11.md`.

## 7 · Run the fixtures before trusting anything

An auditor that has not been run against its own test set is a document, not a tool. Record the
run in `../runs/`, including what it got wrong.

## 8 · Rewrite `../examples.md` from that run

Its rows quote provisions, so they belong to the standard that was loaded when they were
written, and they are wrong the moment it changes. Take the new ones from the run you just
recorded — **never invent them.** Between them they must show every verdict and both confidence
levels, because those are what a reader learns the row shape from.

---

## What does not change

`../identity.md`, `../rules.md`, the row shape, the verdicts, the severity scale, the citation
gate. Those are the auditor. Everything above is what it is currently pointed at.
