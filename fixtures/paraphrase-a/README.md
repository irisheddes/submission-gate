# Fixture: paraphrase-a — plain numeral

**Cartulary is a fictional company.** Every fact here was invented for this repository.

One of three fixtures carrying **the same violation**, worded three ways: 22 employees against
a limit of fewer than 20 (`R-04`, § II Art. 3(4)). The explicit headcount field has been removed
from the registration form, so the prose is the only source.

| | |
| --- | --- |
| **Requirement touched** | `R-04` |
| **Expected verdict** | `FAIL · BLOCKING` — identically in a, b and c |
| **How it is worded here** | Twenty-two, stated as a numeral in running prose. |

## What this set tests

Not whether the gate fires. Whether it fires on the **provision** or on the **phrasing**.

If it fires on one or two of the three, it is matching strings, not applying a rule — and the
ones it missed look exactly like clean passes, which is why this failure normally goes
unnoticed. `-c` is the hard case: the total is never stated and has to be summed.
