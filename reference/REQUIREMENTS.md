# Requirements — derived from the standard

**This file is derived, not source.** Every row is an obligation extracted from the verbatim
sections in this folder, with the provision it came from. It exists so `rules.md` § 10 can
hold: `R-07` is `R-07` in every run, which is impossible if the list is re-derived each time.

> **If this list and the section files disagree, the section files win.** Re-derive the list;
> never edit a row to match a finding. A derived index that has drifted from its source is
> worse than no index, because it still looks authoritative.

**Derived:** 2026-09-11, from the edition recorded in `SOURCES.md`.
**Re-derive when:** the SHA-256 in `SOURCES.md` stops matching the published document.

---

## Scope of this list

The standard governs an applicant **before** selection and a participant **after** it. Only
the first is auditable from an application package, so this list covers:

| Section | In this list | Why |
| --- | --- | --- |
| § II — Mandatory Elegible Criteria | ✅ R-01…R-06 | Obligations on the applicant, verifiable at application |
| § III — Application and Selection Procedure | ✅ R-07…R-10 | What the application must contain and how it is submitted |
| ACCEPTANCE OF THE RULES | ✅ R-11 | **A signed copy must be uploaded with the application.** An applicant obligation, at application time |
| § IV, § V, § VII, Annex 1 | ❌ | Bind a *Participant* after admission. Nothing in an application package can satisfy or breach them |
| § I, § VI, Annex 2, Preamble | ❌ | Definitions, timeline and value proposition — no obligation on the applicant |

> **`R-11` was missed when this list was first derived, and found by a blind run on
> 2026-09-11** — the auditor read the section and the list had not. The section was scoped out
> as carrying "no obligation on the applicant", which is plainly wrong: its first sentence says
> *must*, twice. Recorded here rather than quietly corrected, because a derived list that has
> been wrong once should be read as one that can be wrong again. See `../runs/`.

Out-of-scope sections stay in `reference/` because a finding may need to cite them, and
because a reader checking scope must be able to read what was excluded.

---

## The requirements

Severity is read off the standard's own verb, per `rules.md` § 6. **`must` bars; `should`
does not.**

| ID | Requirement | Provision | Verb | Severity if failed |
| --- | --- | --- | --- | --- |
| `R-01` | The company is legally incorporated and has its own tax identification number in the European Union | § II Art. 3(1) | must | `BLOCKING` |
| `R-02` | Between 0 and 10 years since legal incorporation — **unless justified** (e.g. pivot, new AI product line, recent scale-down) | § II Art. 3(2) | must, with named exception | `BLOCKING` only where no justification is offered; otherwise `NON-CONFORMANT` |
| `R-03` | Demonstrates intensive use, development or investment in AI Technologies (e.g. trained models, annotated datasets, validated algorithms) | § II Art. 3(3), first sentence | must | `BLOCKING` |
| `R-03b` | Projects are at Medium and High Readiness Level, as determined in the One-Stop Shop User Journey | § II Art. 3(3), second sentence | **should** | `NON-CONFORMANT` — and **never `CONFIRMED`**, see below |
| `R-04` | The company has fewer than 20 employees | § II Art. 3(4) | must | `BLOCKING` |
| `R-05` | The company belongs to one of the priority sectors: Health, Agriculture & Climate, Finance & Legal, Policy Making & Public Administration, Communication & Media, Energy | § II Art. 3(5) | **should** | `NON-CONFORMANT` — never `BLOCKING`. § II Art. 4 admits applicants outside these sectors at the Organizer's discretion |
| `R-06` | A minimum of 1 employee is available in person at the offices at least 3 times per week | § II Art. 3(6) | must | `BLOCKING` |
| `R-07` | The application is submitted via the official online form, *Incubation Programme Registration Form – Call 3* | § III Art. 5 | shall | `BLOCKING` |
| `R-08` | An Executive Summary is submitted, **maximum 5 pages** | § III Art. 6.1 | provided that | `BLOCKING` if absent; `NON-CONFORMANT` if over length |
| `R-09` | A Presentation Video is submitted, **maximum 1 minute** | § III Art. 6.1 | provided that | `BLOCKING` if absent; `NON-CONFORMANT` if over length |
| `R-10` | A Company Deck may be submitted | § III Art. 6.1 | **optional** | None. Absence is `NOT APPLICABLE`, never `FAIL` |
| `R-11` | A **signed copy of the Rules for Participation** is uploaded together with the application materials | ACCEPTANCE OF THE RULES (PDF p12) | must | `BLOCKING` — the provision calls acceptance "a mandatory condition to take part in the selection process" |

## Notes an auditor must not lose

- **`R-05` is the anti-inflation test.** The source says *should*, and Art. 4 names a
  discretionary route around it. An auditor that marks a non-priority sector `BLOCKING` has
  inflated a preference into a bar, which `rules.md` § 8 forbids.
- **`R-10` is the `NOT APPLICABLE` test.** An optional document that was not supplied is not
  a failure and not a gap. It has no severity at all.
- **`R-02` carries its own exception in the same sentence.** A finding that quotes the age
  limit without quoting *"unless justified"* has misquoted the provision. And a package that
  **meets** the exception is `PASS`, not `PARTIAL` — `rules.md` § 5a. An applicant thirteen
  years old who documents a pivot satisfies Art. 3(2); they are not a borderline case.
- **`R-03b` cites a definition this folder does not hold.** Art. 3(3) defines the readiness
  levels by pointing at the One-Stop Shop User Journey at an external URL. `rules.md` § 1 makes
  `reference/` the only authority, so readiness can be raised but never `CONFIRMED` — every
  `R-03b` row carries `TO CHECK` and names the missing document. *(Until 2026-09-17 this list
  said "Medium **or** High". The standard prints "Medium **and** High". Blind case 12 quoted
  the standard instead and pointed out the difference.)* Splitting it from `R-03` keeps
  one unverifiable half from dragging a verifiable one down with it.
- **`R-11` names its own mechanism.** Most "mandatory" labels in a document list are not a
  bar (`rules.md` § 6 forbids treating them as one). This one is: *"a mandatory condition to
  take part in the selection process"* states the consequence, so `BLOCKING` is earned rather
  than assumed.
- **Art. 3's preamble binds all of R-01…R-06:** the criteria *"must be verifiable at the time
  of application"*. **That means capable of verification, not accompanied by proof.** § III
  Art. 6.3 assigns the verifying to the Organizer after the call closes, and no provision in this
  standard names a document an applicant must attach to evidence eligibility. A fact stated on
  the required registration form is the applicant's declaration of a verifiable fact, and it is
  `PASS` where it is present, specific and not contradicted elsewhere in the package.

  `PARTIAL` is for a claim that falls short on its own terms — vague where the provision is
  precise, or undercut by another document in the package. Not for a claim that simply arrives
  undocumented, which describes every line of every application form ever submitted.

  *An earlier version of this note said any unevidenced claim was `PARTIAL`. Applied
  consistently — as a blind run did on 2026-09-11 — it makes the conformant control unpassable
  and no application can ever clear Art. 3. The run was right and the note was wrong. See
  `../runs/blind-2026-09-11.md`.*
