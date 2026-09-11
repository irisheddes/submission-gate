# Fixture: broken-03-age-justified

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-02` |
| **Expected verdict** | `PASS` |
| **What was changed** | Incorporated 13 years ago — but the package documents a pivot, which Art. 3(2) admits in the same sentence. A finding here is a FALSE POSITIVE: the auditor quoted the age limit without reading 'unless justified'. |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
