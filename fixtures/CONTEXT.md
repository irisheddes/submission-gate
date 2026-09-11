# fixtures/ — the test set

**One job: prove this auditor catches what it claims to catch, and stays quiet when there is
nothing to catch.**

## What it holds

| Path | What it is |
| --- | --- |
| `EXPECTED.md` | What each fixture should produce — the answer key |
| `clean/` | One conformant package. The control |
| `broken-<nn>/` | One package per planted violation, one violation each |

## Rules for this folder

- **Everything here is synthetic.** No real applicant material, ever — not a real package,
  not a real budget, not a real organisation's name. Every file was written for this
  repository.
- **One violation per fixture.** A fixture with two planted faults cannot tell you which one
  the auditor missed.
- **Every planted violation names the provision it breaks**, so a reader checks the expected
  result against `../reference/` rather than against the author's word.
- **The control is the most important fixture.** An auditor that finds problems in a
  conformant package trains its user to ignore it. `clean/` must produce zero `FAIL` and zero
  `PARTIAL`.

## They belong to the standard, not to the machinery

A fixture is a package built to break a *specific provision*. Retarget `../reference/` and
this whole folder must be rebuilt — see `../reference/CONTEXT.md`.

## Who reads it

Anyone verifying the auditor: run it against a fixture, compare its ledger to `EXPECTED.md`.
The auditor itself never reads this folder during a real audit.

## The human check

After any change to `../rules.md`: re-run every fixture. A rule change that makes the control
fail is a regression, however well it reads.
