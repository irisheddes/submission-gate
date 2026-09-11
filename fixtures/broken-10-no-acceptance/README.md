# Fixture: broken-10-no-acceptance

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with the signed acceptance form removed.

| | |
| --- | --- |
| **Requirement touched** | `R-11` |
| **Expected verdict** | `FAIL` · `BLOCKING` |
| **What was changed** | No signed copy of the Rules for Participation uploaded with the application |

## Why this fixture exists

`R-11` was **not in the requirement list** when this test set was first built. A blind run on
2026-09-11 read the ACCEPTANCE section, found an obligation the derived list had scoped out,
and reported it. The list was wrong; the auditor was right.

The provision names its own mechanism — acceptance is *"a mandatory condition to take part in
the selection process"* — which is what earns `BLOCKING` rather than assuming it from the word
*mandatory* in a document list (`../rules.md` § 6).
