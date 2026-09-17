# Fixture: broken-04-sector

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A copy of `../clean/` with **one** planted change. Regenerate with `python3 ../_build.py`.

| | |
| --- | --- |
| **Requirement touched** | `R-05` |
| **Expected verdict** | `FAIL · NON-CONFORMANT` |
| **What was changed** | Operates outside the priority sectors: freight logistics, declared on the form and described throughout the Executive Summary. Art. 3(5) says the company *should* belong to one, and Art. 4 admits applicants outside them at the Organizer's discretion. Marking this BLOCKING is severity inflation, forbidden by rules.md § 8. (Until 2026-09-17 only the form and one sentence changed, and the rest of the summary still described public administration - a second fault, found by blind case 11.) |

Every other requirement must come back exactly as it does for `../clean/`. A second finding in
this fixture is a false positive, and is as much a failure as missing the planted one.
