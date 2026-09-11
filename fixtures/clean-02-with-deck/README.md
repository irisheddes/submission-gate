# Fixture: clean-02-with-deck — conformant

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A **passing** package. The auditor must return no `FAIL` and no `PARTIAL`.

| | |
| --- | --- |
| **Requirement exercised** | `R-10` |
| **Expected** | `R-10` `PASS` instead of `NOT APPLICABLE`; everything else as the control |
| **How it differs from the control** | The optional Company Deck **is** submitted. Tests the optional requirement in the other direction — present and satisfied, rather than absent and not applicable. |

Four of the fifteen fixtures here conform. They are the point as much as the broken ones: a
gate that fires on everything catches every violation and is useless. These test that it stays
quiet on packages that are unusual and still correct.
