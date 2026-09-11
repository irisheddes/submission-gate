# Fixture: clean — a conformant application

**Cartulary AI is a fictional company. Every fact in this folder was invented for this
repository.** No real organisation, person, tax identifier or funding application is
represented here.

This is the **control**: an application that satisfies every requirement in
`../../reference/REQUIREMENTS.md`. The auditor must return zero `FAIL` and zero `PARTIAL`
against it. Anything else is a false positive, and a false positive is the failure that
trains a user to stop reading the ledger.

Two requirements are set deliberately at their limits, so the control is not a soft pass:

- **`R-08`** — the Executive Summary is exactly **5 pages**, the maximum permitted.
- **`R-09`** — the Presentation Video is **58 seconds**, against a 1-minute cap.

And one is deliberately absent:

- **`R-10`** — no Company Deck. It is optional, so its absence must read `NOT APPLICABLE`,
  never `FAIL` and never a gap.

## Files

| File | Stands for |
| --- | --- |
| `registration-form.md` | The *Incubation Programme Registration Form – Call 3* (`R-07`) |
| `executive-summary.md` | The Executive Summary (`R-08`) |
| `presentation-video.md` | The Presentation Video (`R-09`) — see the limit below |
| — | No Company Deck, on purpose (`R-10`) |

## A declared limit

A repository cannot hold a real video, so `presentation-video.md` **declares** its duration
and the auditor audits the declaration. It cannot measure the file. The same is true of the
Executive Summary's page count, which is declared rather than paginated.

This is a real limit of the fixture, not a trick: it is listed in `../../README.md` under
*what this auditor cannot catch*. An auditor that reports a declared duration as if it had
measured one is lying, and `rules.md` § 7 requires it to carry `TO CHECK` instead.
