# Fixture: broken-05-summary-length

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-08` |
| **Expected verdict** | `FAIL · NON-CONFORMANT` |
| **What was changed** | Executive Summary declared at 7 pages against a 5-page maximum. Present, so not blocking. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
