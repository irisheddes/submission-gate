# Fixture: clean-04-age-at-limit — conformant

**Cartulary is a fictional company.** Every fact here was invented for this repository.

A **passing** package. The auditor must return no `FAIL` and no `PARTIAL`.

| | |
| --- | --- |
| **Requirement exercised** | `R-02` |
| **Expected** | `R-02` `PASS`; everything else as the control |
| **How it differs from the control** | Incorporated exactly 10 years ago, at the boundary of the 0–10 year range rather than inside it. Tests that the limit is read as inclusive, as the source states it. |

Four of the fifteen fixtures here conform. They are the point as much as the broken ones: a
gate that fires on everything catches every violation and is useless. These test that it stays
quiet on packages that are unusual and still correct.
