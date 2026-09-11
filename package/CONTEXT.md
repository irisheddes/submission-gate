# package/ — the artifact under audit

**One job: hold the thing being checked, for as long as one audit takes.**

This is the transient half of the auditor's input. `reference/` holds the standard and stays;
this folder holds one applicant's package and does not.

## What goes here

The files the applicant intends to submit — the application form, the annexes, the budget,
the declarations, whatever the standard requires. **Files, not descriptions of files.** A
described budget is not a budget: `rules.md` § 9 reports what was not supplied as
`NOT SUPPLIED`, never as a failure.

Put them here in the shape they will be submitted in, filenames included. Filenames are often
themselves a requirement, and renaming them to be tidy destroys the thing being audited.

**Any format.** Put the package here as it will be submitted — PDF, Word, spreadsheets,
images, plain text. The auditor reads what it is given and never asks for a conversion first: a
converted package is not the package, and the conversion is a step nobody has checked.

Two honest caveats. A citation into a PDF is coarser than one into text — "around page 4"
rather than a named section. And material that cannot be read takes `UNREADABLE`, not
`NOT SUPPLIED` (`../rules.md` § 9): an image-only scan is a file you sent that did not arrive
legible, not a file you failed to send, and the two send you to different places.

## This folder is never committed

`.gitignore` keeps everything here out of git except this contract. That is structural, not a
matter of care: an application package holds an organisation's legal identity, its finances
and its unpublished work, and a public repository is the last place any of it should reach.

The auditor reads this folder. It never copies from it into `runs/` — a ledger cites
locations, it does not quote the package back.

## Auditing a fixture instead

Point the auditor at `../fixtures/<name>/` directly. Fixtures are synthetic and committed on
purpose; they do not pass through here.

## Who reads it

Every run, in full. This is the only folder the auditor is expected to read completely — the
standard is read selectively (`../reference/CONTEXT.md`), the package is not.

## The human check

Before a run: is what is in here the whole package, or part of it? The auditor cannot tell
the difference between a document you did not supply and one that does not exist, and it will
say `NOT SUPPLIED` for both. Saying which up front is what makes that column meaningful.
