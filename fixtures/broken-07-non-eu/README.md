# Fixture: broken-07-non-eu

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-01` |
| **Expected verdict** | `FAIL · BLOCKING` |
| **What was changed** | Incorporated outside the European Union, with a US federal tax id rather than an EU one. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
