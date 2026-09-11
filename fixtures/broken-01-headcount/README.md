# Fixture: broken-01-headcount

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-04` |
| **Expected verdict** | `FAIL · BLOCKING` |
| **What was changed** | Company size raised above the limit of 20. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
