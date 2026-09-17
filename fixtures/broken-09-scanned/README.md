# Fixture: broken-09-scanned — a scan that must be read by sight

> **Corrected 2026-09-17. The table and the section below it describe what this fixture was
> built to expect, and that expectation was wrong.** A blind run on 2026-09-11 read the scan by
> sight, and `../../rules.md` § 9 was redefined: a legible scan is read, not `UNREADABLE`. The
> expected result is the control's, as `../EXPECTED.md` says. This page was not updated at the
> time. `UNREADABLE` is now tested by `../broken-11-encrypted/`. What follows is kept as it was
> written.

**Cartulary is a fictional company.** Every fact here was invented for this repository.

`registration-form.pdf` is an **image-only scan** — the page rendered as a picture, faintly
skewed, with no text layer. Extracting text from it returns zero characters. The other two
files are normal PDFs.

| | |
| --- | --- |
| **Requirement touched** | `R-01`, `R-02`, `R-04`, `R-05`, `R-06`, `R-07` — everything the registration form evidences |
| **Expected verdict** | `UNREADABLE` on each. **Never `NOT SUPPLIED`, never `FAIL`** |
| **Severity** | None. `UNREADABLE` carries no severity (`../rules.md` § 6) |

## What this catches

An auditor that extracts nothing from a file and concludes the requirement was not met is
**confidently wrong**. So is one that reports `NOT SUPPLIED`: the form was supplied. It is
sitting in the package. It simply did not arrive legible.

The three outcomes send an applicant to three different places:

| | The applicant should |
| --- | --- |
| `FAIL` | fix the application |
| `NOT SUPPLIED` | find a document and send it |
| `UNREADABLE` | re-send a document they already sent, in a readable form |

Reporting this case as `NOT SUPPLIED` sends someone hunting for a file they are holding.

## The honest note

The form here is a scan of `../paraphrase-a/registration-form.md` — which states 22 employees
and would fail `R-04` if it could be read. **That is deliberate and it must not change the
verdict.** An auditor cannot know what it cannot read, and guessing at the contents of an
unreadable file is worse than reporting it unreadable, even when the guess would be right.

If a run reports `R-04 FAIL` here, it did not read the scan — it inferred. Say so.
