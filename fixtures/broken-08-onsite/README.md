# Fixture: broken-08-onsite

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-06` |
| **Expected verdict** | `FAIL · BLOCKING` |
| **What was changed** | On-site presence twice weekly, against a stated minimum of three times per week. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
