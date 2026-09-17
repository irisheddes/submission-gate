# Submission Gate

An auditor that checks an application package against a published rulebook, and reports
**every** requirement as pass, fail or not applicable — each row quoting the provision it was
checked against and naming the file it was checked in.

It does not tell you whether your application is good. It tells you whether it conforms.

It reads the package in whatever form it was written — PDF, Word, spreadsheets, plain text —
and distinguishes three things most auditors collapse into one: a requirement that **failed**,
one whose material was **never supplied**, and one whose material **arrived unreadable**. Those
send you to three different places.

---

## This is not an auditor for one call

The standard is an **input**. `identity.md`, `rules.md`, `CONTEXT.md` and `CLAUDE.md` name no
funder, no programme and no provision number — check them. Everything specific to a rulebook
lives in `reference/`, and that folder is a slot.

`examples.md` is the exception, and deliberately so: its rows are real output from the run in
`runs/`, so they quote the provisions of whatever is loaded. It is rewritten on retarget —
invented examples would be cheaper and would prove nothing.

**Don't take that on trust. Run this:**

```sh
python3 _tools/unload.py          # lists what would go; changes nothing
```

It prints every file that belongs to the standard currently loaded — the rulebook, its index
and provision map, its derived requirements, the fixtures and citation tests built against it,
the runs made with it — and, separately, the files that are the auditor. *(This page used to
give counts here. They did not match what the script printed, and any count goes stale the
next time a run is added, so they are gone.)* Add `--yes` and the folder empties of BSC AI Factory Call 3 and
stays a working auditor with nothing loaded. `git checkout .` puts it back.

It leaves `examples.md` in place and tells you so: the rows are stale the moment the standard
goes, and rewriting them is step 8 of loading the next one.

Then `reference/LOADING.md` is eight steps for pointing it at your own rulebook: a published
standard, split at its own seams, indexed, with its obligations derived and fixtures rebuilt.

**Currently loaded:** Rules for Participation — BSC AI Factory Incubation Programme, Call 3
(Barcelona Supercomputing Center, under EuroHPC JU grant agreement 101234399). Public, vendored
from the publisher's own URL, SHA-256 in `reference/SOURCES.md` with a command to verify it
against the live document.

### Why the hash is there

`SOURCES.md` ships the standard's SHA-256 and the `curl` line that produced it, so anyone can
prove the vendored PDF is byte-identical to what the publisher serves. It also does a second
job: when the publisher revises the document the hash stops matching, and `_tools/status.py`
says so — because at that moment **every finding in `runs/` was made against a version that no
longer exists**. A clean report against a dead edition is worse than no report.

> **Correction, 2026-09-17: that only works if the publisher replaces the file at the same
> address. This one didn't.** It published a second edition under a new upload path and left
> the first one where it was, so the vendored copy still matches its URL byte for byte while no
> longer being the latest edition. A later run found this by checking the call's own page. See
> *What broke* and `reference/SOURCES.md`.

---

## Everything nine blind runs found — both directions

Nine sessions that had never seen this repository. Each opened in a folder holding only the
auditor, the standard, and one application — or so this page said until the correction below.

> **Correction, 2026-09-17: they were less blind than that sentence says.** The staged folders
> sat inside this repository, and a session reads every `CLAUDE.md` above the folder it opens
> in. So cases 1–11 could also read this repository's own `CLAUDE.md`, which names `fixtures/`
> and `EXPECTED.md`, plus the instruction files of the author's workspace above it. Nothing in
> any ledger shows a session opening the answer key, but nothing prevented it either. Found
> while preparing this resubmission. `_tools/stage.py` now stages outside the repository and
> refuses any folder with a `CLAUDE.md` or `AGENTS.md` above it.

Inside the staged folder itself: no answer key, no fixtures, no previous runs, no case name, and
— for six of the nine — no notice that it was a test. Each given one word: **`audit`**.

Ledgers in `runs/`, unedited. Scoring in `runs/blind-2026-09-11.md`. A tenth run re-tested two
fixes (`runs/blind-case-10-2026-09-11.md`), and an eleventh was run on 2026-09-17, after the
two corrections the judges found (the last rows of *What broke*) (`runs/blind-case-11-2026-09-17.md`).

### What held

| | |
| --- | --- |
| **One word was enough** | No run asked what to do. The brief's own test — drop the folder in, Claude becomes the auditor |
| **It verified the standard unprompted** | Hashed the PDF against `SOURCES.md` before citing anything. Nothing instructs it to |
| **It loaded narrowly** | Sections opened one at a time as citations needed them, never the whole folder |
| **It refused to inflate** | `should` scored `NON-CONFORMANT`, never `BLOCKING`, under a preamble calling all criteria "mandatory" |
| **It read a scan by sight** | Zero extractable characters, read anyway, cited "by sight" |
| **It invented nothing about a locked file** | A password-protected form → `UNREADABLE`, **zero `FAIL`s** — though a guess would have been right |
| **It refused substitutes** | Other documents asserting the form was submitted were rejected as package content, not verification |
| **It did arithmetic** | A headcount never stated — 14 + 5 + 3 — found and scored |
| **It didn't equate short with incomplete** | A 2-page application passed clean |
| **It enforced a requirement it never saw discovered** | `R-11`, added that morning, blocked correctly by a later session |
| **Four refusals, four held** | And three corrected a false premise in the question before declining |

### What broke

| | |
| --- | --- |
| **An exception read as mitigation — twice** | "Unless justified" satisfied, justification cited, row still docked. Two sessions, same fixture — reproducible, not variance. **Fixed: `rules.md` § 5a, which says what a satisfied exception does. Nothing did before** |
| **10 of 65 citations quietly tidied** | Straight apostrophes for curly, ellipses added. Caught by `check-citations.py`, not by the rule. *Re-checked 2026-09-17 against the corrected text below: still 10 of 65, for the same reasons* |
| **A mandatory requirement was missing from our list** | `R-11`. A run read the section the list had skipped |
| **`UNREADABLE` was defined wrongly** | It covered a scan that was perfectly legible. A run refused the definition and was right |
| **An expected result credited a document nobody had** | `R-09`. The run applied § 9 harder than the answer key did |
| **Our own fixture instructed the auditor** | And cited a rule that said something else. Caught, ignored, scored correctly from the provision |
| **A note in `REQUIREMENTS.md` was too strong** | Taken literally, every self-declared fact is `PARTIAL` and no package can pass. **Fixed** — it contradicted Art. 6.3, which gives verification to the Organizer after closure |
| **A fixture was silently wrong** | Built to sit at a 10-year limit; it was 10 years 6 months, wrong the day it was written |
| **The author's scoring was wrong once** | Two runs with matching totals read as one duplicated folder. The transcripts disproved it |
| **One verdict boundary was unsettled** | For a datum inside an unreadable file, `NOT SUPPLIED` or `UNREADABLE`? § 9 did not say. **Settled 2026-09-17:** the file is there, so the row is `UNREADABLE` and names it, with a required reason, `CANNOT OPEN` or `ILLEGIBLE`, because the fix differs. It writes down what the answer key and blind case 8 already did. **Not yet re-tested blind.** Also corrected: two pages still described an image-only scan as `UNREADABLE`, from before the 2026-09-11 redefinition |
| **A fixture planted two things** | Case 11 (2026-09-17) found `broken-04-sector` contradicts itself: the form says logistics, and most of the Executive Summary still describes public administration, a priority sector. The run flagged it and declined to pick. **Fixed the same day:** the fixture's summary now describes freight logistics throughout, with `_build.py` checking it keeps every fact the other rows depend on. Blind case 12 ran the rebuilt fixture and found no contradiction |
| **The answer key cited a rule that does not exist** | `EXPECTED.md` said `rules.md` § 7 requires `TO CHECK` for a page count the package only declares. § 7 does not say that. Cases 11 and 12 both returned `CONFIRMED` and were following § 7 as written. *(An earlier version of this row called that "a misreading of a correct rule". It was not.)* **Open.** Adding the rule means re-running the fixtures it can affect, so the key now says it is an expectation, not a rule. Case 12 also caught `REQUIREMENTS.md` misquoting Art. 3(3) ("or" for "and"). **Fixed** |
| **The blind runs were not fully blind** | Staged inside the repository, so every case could read the `CLAUDE.md` that routes to the answer key. See the correction above. **Fixed:** staging moved outside, with a guard |
| **The rulebook loaded here is not the latest edition, and the hash check could not tell** | The publisher uploaded a second edition of the Call 3 Rules on 3 August 2026, under a new path (`/2026/08/`), and left the 14 July edition vendored here at its old path. The two differ only in the list of incubation sites (Guimarães, up to 12 places, became Porto, up to 5, in § I Art. 1(i) and § III Art. 6.2). No requirement in `reference/REQUIREMENTS.md` changes. The hash check was built for a replaced file, not an added one. **Found 2026-09-17 by a session that loaded the call from scratch** (`runs/cold-2026-09-17.md`). **Open:** the section files, provision map, fixtures and every run here are bound to the July edition. Re-vendoring means re-extracting and re-running, so the edition is documented rather than swapped. `reference/LOADING.md` step 1 now says to check the call page for newer editions |
| **The split words were an extraction bug, and we defended them** | `SOURCES.md` said `s hould` and `Program me` were the PDF's own kerning, and kept them "exactly as extracted". The PDF prints `should`. pypdf invented 9 split words and 17 stray spaces, and moved two tables into the wrong sections. `check-citations.py` then rejected any run that quoted the PDF correctly. This broke our own rule that the PDF is the authority. **Found by the Comp 12 judges, who measured the glyphs. Fixed 2026-09-17:** re-extracted with pdfplumber, checked word for word against pdftotext (`_tools/check-extraction.py`). The false claim is quoted and corrected in `reference/SOURCES.md`, not deleted. Two blind runs had already reported one symptom, an empty timeline file, and nobody traced it to the extractor |
| **The citation checker ignored the provision number** | It searched all of `reference/` for the quote. A citation changed from § II Art. 3(4) to 3(3), and then to 3(9), which does not exist, still passed. Half of `rules.md` § 2's double anchor was unguarded. **Found by the Comp 12 judges. Fixed 2026-09-17:** `reference/PROVISIONS.md` maps each provision to the exact text that holds it, and a quote must sit inside the provision it is cited to. `_tools/test-citations.py` proves that a neighbour swap, a non-existent provision and a broken map all fail. The old checker passed the first two |

**Most of those were found by the auditor's own runs, not by its author. The last two were
found by the judges.** No check in this repository could have caught them: every check compared against the
same wrong text, and the citation check tested only half of what the rule requires.
`runs/recheck-2026-09-17.md` records how each fix was proved and what the corrected checker says
about every earlier ledger. Each correction is dated in the file it touched, names the run or
letter that found it, and lands in its own commit, so the git log shows the order things
happened in.

**Two were argued about before being fixed.** The first instinct was to leave the exception
weakness and the over-strong note alone, on the grounds that patching a rule after one run is
writing a rule to pass a test. That principle is real but was applied to the wrong cases. The
test it should have been put to: *would the fix be worth having if the fixture did not exist?*
For both, yes — one note contradicted the standard outright, and the other rule was simply
missing a sentence about what a satisfied exception does. Neither fix is fixture-shaped.

**Both fixes were then re-tested, blind.** A tenth session — same conditions, no answer key,
no notice it was a test — audited the fixture that produced both defects and returned
**9 `PASS`, 0 `FAIL`, 0 `PARTIAL`**. `R-02` passed, citing § 5a by name; the four evidentiary
`PARTIAL`s are gone. `runs/blind-case-10-2026-09-11.md`.

What that shows is narrow and worth stating narrowly: **two rules that were wrong are now
right, and a session that never saw the argument applies both correctly.** What it does not
show is that either rule is right in general — a fix tested only on the case it was written
for is a fix tested on nothing else.

## What it found when it was run

**Start with `runs/blind-2026-09-11.md`** — **ten sessions** that had never seen this
repository, each given one word (`audit`), each denied the answer key, the fixtures, the
previous runs and its own case name. Eight correct, two misses, both described in full — and
the tenth run exists to check that the fixes for those two misses actually work. The ledgers as
delivered are in `runs/blind-*.md`, unedited.

Those runs found **five** things wrong with this auditor that its author had not. The judges found two more, after the round closed:

| What was wrong | Found by |
| --- | --- |
| A mandatory requirement missing from the requirement list (`R-11`) | a blind run reading the standard the list had skipped |
| `UNREADABLE` defined wrongly — it covered a scan that was perfectly legible | a blind run that read the scan and said so |
| An expected result crediting a document nobody had supplied | a blind run applying § 9 more strictly than the key did |
| Instructions to the auditor embedded in the audited document | a blind run that spotted the embedded citation was false |
| 10 of 65 citations quietly tidied — apostrophes, ellipses | `_tools/check-citations.py`, not the rule |
| The standard's text held words the PDF does not: an extractor's splits, defended as the source's | the Comp 12 judges, measuring the PDF's glyphs |
| The citation check ignored which provision a quote was cited to | the Comp 12 judges, changing a citation's number and leaving the quote alone |

Each correction is dated and says which run found it. `runs/refusals-2026-09-11.md` covers what
happens when it is asked to do something it refuses to do — one of four stated boundaries
tested, three still untested and labelled as such.


`runs/fixtures-2026-09-11.md` — 15 fixtures, 15 expected verdicts. Including the paraphrase
set, where the same violation is worded three ways and `-c` never states the total at all.

**That is the least interesting sentence in this repository.** The run was carried out by the
session that wrote the auditor *and* the answer key, which is worth much less than a run by a
stranger. What matters is what it got wrong:

**1 · A fixture was wrong, and the run found it.** `clean-04-age-at-limit` was built to sit
exactly at the 10-year incorporation limit and was dated 14 March 2016 — which on the day of
the run is ten years and *six months*. It claimed to test an inclusive boundary and actually
tested an unjustified violation, duplicating another fixture. Corrected to the day. The general
lesson is worse than the bug: **a date-relative fixture expires**, and this one was wrong the
moment it was written.

**2 · The answer key was underspecified.** It expected `R-08` and `R-09` to `PASS` and said
nothing about confidence. Neither can be verified inside a repository — a page count and a video
duration are *declared* by the fixture. The correct result for the control is eight
`PASS · CONFIRMED`, two `PASS · TO CHECK`, one `NOT APPLICABLE`. An auditor returning
`CONFIRMED` there would have passed a test that was not asking the right question.

**3 · One requirement points outside this folder.** Art. 3(3) requires projects to be at
*"Medium and High Readiness Level determined in the User Journey from One-Stop Shop"* — and
defines that by a URL this repository does not hold. Under `rules.md` § 1 the folder is the only
authority, so readiness can be raised but never `CONFIRMED`. **This is the round's own named
failure appearing inside our entry:** we hold the standard in full, and the standard points
outward at something we do not hold. It is split out as `R-03b` and carries `TO CHECK` in every
row rather than being quietly dropped.

## What this auditor cannot catch

- **Anything measured rather than stated.** Page counts and video durations are read from what
  the package declares. It cannot open a PDF and count, or play a file and time it. Such a row
  should carry `TO CHECK`. **But no rule says so yet.** Two blind runs marked a declared page
  count `CONFIRMED`, and `rules.md` § 7 as written allowed it. See *What broke*.
- **Readiness level (`R-03b`).** The defining document is outside `reference/`. See above.
- **Whether a claim is true.** It checks that a package says what the standard requires and that
  the statement is present and located. It has no way to know whether the company really has
  seven employees.
- **Interacting failures.** Every fixture carries exactly one planted violation, so nothing here
  shows how it behaves when four requirements fail at once and the failures compound.
- **What a package does not contain.** It cannot tell a document you chose not to supply from
  one that does not exist. Both read `NOT SUPPLIED`, which carries no severity — deliberately.
- **Word files, spreadsheets and truly unreadable material.** PDFs have been run, including an
  image-only scan (`runs/blind-2026-09-11.md`). Other binary formats have not. `UNREADABLE` has
  fired once, on a password-protected form (case 8). It has not met a corrupt file, and the
  `ILLEGIBLE` reason has never been exercised by any fixture. *(This line used to say
  `UNREADABLE` had never fired and no locked file was in the test set. Both stopped being true on
  2026-09-11.)*
- **Citation granularity in a PDF.** A finding in text names a section; in a PDF it names a
  page, and in a scan it is "by sight" to a numbered section. That is a real loss of precision
  and it is the cost of the format, not a defect in the auditor.
- **Obligations after admission.** Sections IV, V, VII and Annex 1 bind a *participant*, not an
  applicant. They are stored, and excluded from audit. See `reference/REQUIREMENTS.md`, *Scope*.

## Is it ready?

```sh
python3 _tools/status.py
```

Scans the folder and reports which of the four setup steps are done. Nothing in it is
hand-maintained, so it cannot drift. It fails loudly on the two states that invalidate every
past finding: the standard's hash no longer matching `SOURCES.md`, and fixtures changed since
the last run.

## How to use it

1. Drop this folder into a Claude project.
2. Put your application package in `package/` — the files you intend to submit, filenames
   included. It is gitignored, so it cannot be committed by accident.
3. Ask it to audit the package against the standard in `reference/`.

It returns a conformity ledger: one row per requirement, each carrying a verdict, the
provision quoted from `reference/`, and where in your package it was checked.

**Feed it files, not descriptions.** A described budget is not a budget; the auditor reports
what it was given as `NOT SUPPLIED`, never as a failure.

## How to check it works

`fixtures/` holds synthetic application packages: one conformant control and several with a
single planted violation each. `fixtures/EXPECTED.md` says what each one should produce.

Run the auditor against any fixture and compare. The control must pass silently — an auditor
that finds problems in a clean package is worse than no auditor.

`python3 _tools/stage.py <fixture>` builds a blind copy outside the repository, with the answer
key, the fixture's name and the earlier runs left out. Open it in a fresh session and say `audit`.

Three scripts check the machinery itself, not an audit:

```sh
python3 _tools/test-citations.py      # expect: "0 failed"
python3 _tools/check-citations.py --all
python3 _tools/check-extraction.py    # needs: pip install pdfplumber, and poppler (pdftotext)
```

**`check-citations.py --all` exits 1, and that is expected.** It re-checks every ledger in
`runs/`, and those are kept exactly as the sessions delivered them, including quotes they
tidied and quotes that copied an extraction error this repository has since fixed. Each failure
is broken down by cause in `runs/recheck-2026-09-17.md`. Point it at a new ledger
(`check-citations.py runs/<file>.md`) and that ledger must come back clean.

`check-extraction.py` stops with exit 3 if pdfplumber or pdftotext is missing, rather than
reporting a result it could not compute.

## What is in here

| Path | What it is |
| --- | --- |
| `CLAUDE.md` | The router — where to go for which task. Start here if you are an agent |
| `CONTEXT.md` | The system: input slot, machinery, output, and the flow between them |
| `identity.md` | Who the auditor is, what it enforces, and what it refuses to do |
| `rules.md` | How it audits: order, citation discipline, verdicts, severity |
| `examples.md` | Worked audits showing every verdict, with citations |
| `reference/` | **The standard itself**, as provision-numbered text. `LOADING.md` retargets it |
| `package/` | The artifact under audit. Gitignored — its contents never leave your machine |
| `fixtures/` | Synthetic packages for testing, plus expected results |
| `runs/` | What past runs actually found |
| `_tools/status.py` | Which setup steps are done — generated by scanning |
| `_tools/unload.py` | Removes the loaded standard, leaving the auditor. Proof the two are separable |
| `_tools/check-citations.py` | Every quote verbatim, and under the provision it is cited to (`reference/PROVISIONS.md`) |
| `_tools/test-citations.py` | Proves that check fails a neighbour swap, a non-existent provision and a broken map |
| `_tools/check-extraction.py` | The stored text against the PDF, by two extractors, page by page |
| `_tools/stage.py` | Builds a blind test case outside the repository |
