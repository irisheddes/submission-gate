# The system

What this folder is, as a machine: one input slot, one body of machinery, one output.

## The unit of work

**One audit: one package, against one standard, producing one ledger.**

Not a review, not a critique, not a score. A ledger — every requirement in the standard
accounted for, whether it passed or failed.

## The three layers

| Layer | Files | Changes when |
| --- | --- | --- |
| **Input — resident** | `reference/` — the rulebook, as provision-numbered sections | You point the auditor at a different standard |
| **Input — transient** | `package/` — the artifact under audit. Never committed | Every run |
| **Machinery** | `identity.md`, `rules.md`, `examples.md` | The auditing method itself changes — rarely |
| **Output** | `runs/` | Every run |

**The two inputs are not alike.** The standard is loaded once, sectioned, and read
selectively; the package arrives for one run, is read in full, and leaves. Keeping them in
separate folders is what lets `.gitignore` protect one and commit the other.

`fixtures/` sits beside these: synthetic packages that test the machinery against the loaded
standard. They belong to the standard, not to the machinery — retarget the input and the
fixtures must be rebuilt.

**The split is the point.** The machinery knows how to audit; it does not know what it is
auditing against. That is what makes this folder portable between funders, and what makes it
portable into a studio where every call folder is a different standard.

## The flow

```
reference/            the standard, loaded
    │
    ├── rules.md § 3  extract every obligation → the requirement list
    │
    ▼
package/              supplied by the applicant, gitignored, read in full
    │
    ├── rules.md § 1  for each requirement: re-read its provision, quote it
    ├── rules.md § 2  record the location it was checked in
    ├── rules.md § 5  assign a verdict
    ├── rules.md § 6  assign severity, on FAIL and PARTIAL only
    │
    ▼
runs/<date>.md        the ledger + totals + the blind-spot declaration
    │
    ▼
a person reads it and decides whether to submit
```

## Where each part states its own rules

Every folder here carries its own contract. This page says how they fit together; each of those
says what its folder holds, who reads it, and what a human checks before it is trusted.

| Folder | Its contract | Also holds |
| --- | --- | --- |
| `reference/` | `CONTEXT.md` — verbatim only, one standard at a time | `LOADING.md` (how to point this at a new rulebook), `SOURCES.md`, `INDEX.md`, `PROVISIONS.md`, `REQUIREMENTS.md` |
| `package/` | `CONTEXT.md` — any format, never committed | — |
| `fixtures/` | `CONTEXT.md` — synthetic only, one violation each | `EXPECTED.md` (the answer key), `_build.py` |
| `runs/` | `CONTEXT.md` — never edited after the fact | every ledger this auditor has produced |

`_tools/` holds six scripts, each answering one question: is this ready (`status.py`), is the
standard separable (`unload.py`), what does a blind run see (`stage.py`), does each quote
resolve under the provision it is cited to (`check-citations.py`), does that check actually
fail what it should (`test-citations.py`), and does the stored text match the PDF by two
extractors (`check-extraction.py`).

## Inputs

- **Every run:** `identity.md`, `rules.md`, `reference/INDEX.md` plus the sections cited
- **This run:** `package/` — files, not descriptions of files. Or `fixtures/<name>/` when testing
- **Re-audit only:** the previous ledger in `runs/`, for prior-ID scoring (`rules.md` § 10)

## Output

One ledger in `runs/`, named by date. It carries every requirement as a row, totals by
verdict, the `BLOCKING` count on its own line, and what was not checked.

## The human check

**The applicant reads the ledger and decides whether to submit.** The auditor has no view on
that and never states one. A `BLOCKING` row says the funder would be entitled to set the
package aside — it does not say do not submit.

## What this system is not

An editor, a reviewer, a scorer, or an advisor. It has no opinion about the quality of what
it reads. `identity.md` holds the full refusal list, and those refusals are load-bearing: an
auditor that starts giving advice has stopped being checkable.
