# Fixtures — what each one should produce

Twelve synthetic application packages for one fictional company, **Cartulary**. Every fact in
every fixture was invented for this repository. No real organisation, person, tax identifier
or funding application is represented anywhere in this folder.

Run the auditor against a fixture and compare its ledger to the row below. A reader who knows
nothing about EU funding can verify this auditor in a few minutes, because every expected
verdict names the provision it comes from and that provision is in `../reference/`.

Requirement IDs are `../reference/REQUIREMENTS.md`.

> **`R-11` and `broken-10-no-acceptance` were added on 2026-09-11, after a blind run found a
> mandatory requirement this test set did not test and the requirement list did not list.** The
> ACCEPTANCE section obliges every applicant to upload a signed copy of the Rules; the list had
> scoped that section out. Every conformant fixture now carries `signed-acceptance`, because
> without it none of them was actually conformant. The test set was wrong for as long as the
> list was.

---

## Nineteen fixtures, five of which conform

An auditor is not proved by what it catches. A gate that fires on everything catches every
violation and is useless, so a third of this set is packages that are **correct** — including
two that look wrong and are not.

### Conformant — must produce no `FAIL` and no `PARTIAL`

| Fixture | Exercises | Expected |
| --- | --- | --- |
| `clean/` | the control | `R-01`–`R-09` `PASS`; `R-10` `NOT APPLICABLE`. **Eight `CONFIRMED`, `R-08` and `R-09` `TO CHECK`** |
| `clean-02-with-deck` | `R-10` | `R-10` `PASS` — the optional document present, rather than absent |
| `clean-03-minimal` | brevity | Same as the control. A 2-page summary, a 31-second video, 19 employees, on-site exactly at the 3-day minimum |
| `clean-04-age-at-limit` | `R-02` | `R-02` `PASS` — incorporated exactly 10 years ago, on the boundary |
| **`clean-05-as-pdf`** | the format | Same as the control — **but `R-08` becomes `PASS · CONFIRMED`**, because a PDF has real pages and the count can be measured rather than taken on trust |

**`R-09` is `NOT SUPPLIED`, not `PASS`** — corrected 2026-09-11 after a blind run disagreed
with this page and was right. No video is in the package; a file *describing* a video is, and
`rules.md` § 9 says review documents, not descriptions of documents. A described video is not a
video. The earlier expectation of `PASS · TO CHECK` credited the applicant for a document
nobody had.

**Confidence is part of the expected result.** `R-08` (page count) is *declared* by the
markdown fixtures and cannot be measured in them, so `rules.md` § 7 requires `TO CHECK`. An auditor returning `CONFIRMED` on either has overstated what it checked,
and passes only because it was not asked the right question. The readiness half of `R-03` is
`TO CHECK` for a different reason — see `../reference/REQUIREMENTS.md`.

The control is not a soft pass: `R-08` sits **exactly at** the 5-page maximum and `R-09` at
**58 seconds** against a 1-minute cap. `clean-03-minimal` is the false-positive test that
matters most — an auditor that reads *short* as *incomplete* fails it, and most will.

*(`clean-03-minimal` is authored, with its own shorter Executive Summary. The others are
generated from the control by `_build.py`.)*

### One planted violation each

Each is a copy of `clean/` with a single change, enforced by `_build.py` — every edit asserts
its target appears exactly once. **Every other requirement must come back exactly as it does
for the control**; a second finding is a false positive and fails that fixture.

| Fixture | ID | Expected verdict | Provision |
| --- | --- | --- | --- |
| `broken-01-headcount` | `R-04` | `FAIL` · `BLOCKING` | § II Art. 3(4) |
| `broken-02-age-unjustified` | `R-02` | `FAIL` · `BLOCKING` | § II Art. 3(2) |
| **`broken-03-age-justified`** | `R-02` | **`PASS`** | § II Art. 3(2) |
| **`broken-04-sector`** | `R-05` | `FAIL` · **`NON-CONFORMANT`** | § II Art. 3(5), Art. 4 |
| `broken-05-summary-length` | `R-08` | `FAIL` · `NON-CONFORMANT` | § III Art. 6.1 |
| `broken-06-video-missing` | `R-09` | `FAIL` · `BLOCKING` | § III Art. 6.1 |
| `broken-07-non-eu` | `R-01` | `FAIL` · `BLOCKING` | § II Art. 3(1) |
| `broken-08-onsite` | `R-06` | `FAIL` · `BLOCKING` | § II Art. 3(6) |
| **`broken-10-no-acceptance`** | `R-11` | `FAIL` · `BLOCKING` | ACCEPTANCE OF THE RULES, PDF p12 |
| **`broken-11-encrypted`** | `R-01`, `R-02`, `R-04`–`R-07` | **`UNREADABLE`**, no severity | the registration form is password-protected and cannot be opened by any means |
| **`broken-09-scanned`** | all rows | **Same as the control — read by sight, not `UNREADABLE`** | the registration form is an image-only scan, legible but not extractable |

**The two that look alike and are not.** `broken-09-scanned` has no text layer and is perfectly
legible; `broken-11-encrypted` cannot be opened at all. The first must be read and scored; the
second must be `UNREADABLE`. An auditor that treats them the same has either invented findings
from a file it could not open, or reported its own extraction failure as the applicant's defect.

### The two that test the harder half

- **`broken-03`** looks like a violation and is not. The company is 13 years old, past the
  10-year limit — but Art. 3(2) says *"unless justified (e.g. pivot, new AI product line,
  recent scale-down)"* in the same sentence, and the package documents a pivot. An auditor
  that quotes the age limit without reading the rest of its own sentence reports a violation
  that does not exist. It keeps the `broken-` prefix deliberately: the name is bait.
- **`broken-04`** is a violation but not a bar. *(Rebuilt 2026-09-17. Until then only its form
  and one sentence said "logistics" while the rest of its summary described public
  administration, a priority sector. Blind case 11 found the contradiction. It is now logistics
  throughout.)* Art. 3(5) says the company *should* belong to
  a priority sector, and Art. 4 admits applicants outside them at the Organizer's discretion.
  Marking it `BLOCKING` inflates a preference into a rejection, which `../rules.md` § 8
  forbids.

## The paraphrase set — the provision, or the phrasing?

Three fixtures carrying **the same violation**: 22 employees against a limit of fewer than 20.
The explicit headcount field is removed from the registration form, so the prose is the only
source.

| Fixture | How the fact is worded | Expected |
| --- | --- | --- |
| `paraphrase-a` | "We are a team of 22." | `R-04` `FAIL` · `BLOCKING` |
| `paraphrase-b` | "Headcount currently stands at twenty-two FTEs." | `R-04` `FAIL` · `BLOCKING` |
| `paraphrase-c` | "Our staff: 14 engineers, 5 in operations, 3 in commercial." | `R-04` `FAIL` · `BLOCKING` |

**All three, identically, or the auditor is matching strings rather than applying a rule.**

If it fires on one or two, the ones it missed look exactly like clean passes — which is why
this failure normally goes unnoticed, and why a gate tested only against a single broken
fixture has proved almost nothing. `-c` is the hard case: the total is never stated and must
be summed.

*This test is not our idea. It was proposed by a member of the Clief Notes community in the
comment thread for this round; we are using it as given rather than reinventing it.*

## What these fixtures do not test

- **Real file properties.** A repository cannot hold a video, and markdown has no pages. The
  Presentation Video declares its duration and the Executive Summary declares its page count;
  the auditor audits the declaration and cannot measure either. `../rules.md` § 7 requires
  `TO CHECK` where material cannot be verified, and `R-08`/`R-09` are exactly that case.
- **Multiple simultaneous violations.** Every fixture carries one, so a miss is unambiguous.
  A real package with four interacting problems is not represented here.
- **Sections IV, V, VII and Annex 1.** Those bind a participant after admission; nothing in an
  application package can satisfy or breach them. See `../reference/REQUIREMENTS.md`, *Scope*.
