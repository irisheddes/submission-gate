# runs/ — the output

**One job: hold what this auditor actually found, so a claim about it can be checked.**

## What it holds

| File | What it is |
| --- | --- |
| `fixtures-<YYYY-MM-DD>.md` | The ledger produced against every fixture, with expected vs. actual |
| `cold-<YYYY-MM-DD>.md` | Totals from a run against a live application package |

## Rules for this folder

- **A cold run carries numbers only** — requirements checked, verdicts by type, false
  positives found, and what changed in `../rules.md` as a result. The package it ran against
  is not published and never enters this repository.
- **Nothing is edited after the fact.** A ledger is the evidence of what the auditor said on
  a date. A later fix goes in a later run, and the earlier one stays as it was.
- **A run where the auditor was wrong is worth more than one where it was right.** It belongs
  in `../README.md` on the front page, not only here.

## Who reads it

A person deciding whether to submit, reading the most recent ledger. And a re-audit, which
reads the previous ledger to score prior IDs (`../rules.md` § 10) — the immediately preceding
run only.

## The human check

The applicant reads the ledger and decides. This folder records; it does not instruct.
