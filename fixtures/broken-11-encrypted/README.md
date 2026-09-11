# Fixture: broken-11-encrypted — a file that genuinely cannot be read

**Cartulary is a fictional company.** Every fact here was invented for this repository.

`registration-form.pdf` is **password-protected**, and the password is not in this repository
and not in the package. It cannot be opened by extraction, by sight, or by any other means
available to an auditor.

| | |
| --- | --- |
| **Requirements touched** | `R-01`, `R-02`, `R-04`, `R-05`, `R-06`, `R-07` — everything the registration form evidences |
| **Expected verdict** | `UNREADABLE`. **Never `NOT SUPPLIED`, never `FAIL`** |
| **Severity** | None. `UNREADABLE` carries no severity (`../rules.md` § 6) |

## Why this fixture exists

`broken-09-scanned` was built to test `UNREADABLE` and does not. A blind run read its
image-only scan by sight and pointed out that § 9 reserves the verdict for material that *could
not* be read — and that one could. The rule was redefined; the fixture now expects the control's
result.

So the verdict had no test at all. This is it: a file that defeats every method, not just the
first one tried.

## What it must not do

- **Not `NOT SUPPLIED`.** The form was supplied. It is in the package. It cannot be opened.
  The applicant needs to re-send it unlocked, not go looking for it.
- **Not `FAIL`.** Nothing is known about whether the company is EU-incorporated or has fewer
  than twenty employees. An auditor that fails a requirement it could not check has invented a
  finding.
- **Not a guess from the other files.** The executive summary states a headcount. Inferring the
  form's contents from it and scoring the row is guessing — and `../rules.md` § 2 requires a
  location in the package where the requirement was actually checked.
