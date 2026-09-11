# Fixture: broken-02-age-unjustified

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-02` |
| **Expected verdict** | `FAIL · BLOCKING` |
| **What was changed** | Incorporated 13 years ago, with no justification anywhere in the package. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
