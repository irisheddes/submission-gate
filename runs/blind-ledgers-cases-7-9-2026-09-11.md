# Blind runs — cases 7–9 — 2026-09-11

Three more fresh sessions, same conditions as cases 1–6: only the auditor, the standard, and
one application in `package/`. No answer key, no fixtures, no previous runs, no case name, and
no notice that this was a test. One word each: **`audit`**.

These three ran against the corrected requirement list — `R-01`…`R-11`, including the
requirement a run in the first set had found missing.

Ledgers reproduced as delivered. Unedited.



---

## case-7 — `broken-03-age-justified`

# Cold run — 2026-09-11

First run against this package. No prior ledger in `runs/`, so no prior IDs to re-score
(`../rules.md` § 10).

**The package is not published here.** Rows cite locations by file and place; nothing from the
package is quoted back, and the applicant is not named (`../package/CONTEXT.md`,
`./CONTEXT.md`).

## 1 · The standard

| | |
| --- | --- |
| Document | Rules for Participation — BSC AI Factory, Incubation Programme, Call 3 |
| Edition | Call 3, published July 2026 by Barcelona Supercomputing Center (BSC-CNS) |
| Retrieval date | 2026-09-11 |

Read from `../reference/SOURCES.md`. This audit is bound to that edition.

## 2 · What was supplied to this run

Four files in `package/`:

- `registration-form.md`
- `executive-summary.md`
- `presentation-video.md` — a **declaration about** a video, not the video
- `signed-acceptance.md`

All four carry a self-description as fictional. That bears on provenance, not on conformity,
and changed no verdict below.

The package arrived as markdown. Three files state that what was submitted to the portal was a
PDF, an MP4 and a signed document; what is in `package/` is the text of those. This is read as
supplied — no conversion was requested (`../rules.md` § 9) — and where it limits a check the
row and § 6 say so.

## 3 · Requirement list

Loaded from `../reference/REQUIREMENTS.md`: `R-01`…`R-11`, plus `R-03b`. Twelve rows, walked in
the standard's own order. The scoped-out sections (§ I, § IV, § V, § VI, § VII, Annex 1,
Annex 2, Preamble) were read this run to confirm the exclusion: none places an obligation on an
*applicant* at application time. The exclusion holds.

## 4 · Where this run read Art. 3's preamble differently from `REQUIREMENTS.md`

Art. 3's preamble binds `R-01`…`R-06`: the criteria "must be verifiable at the time of
application". `REQUIREMENTS.md` reads that as *a claim the package asserts but does not evidence
is `PARTIAL`, not `PASS`*. Art. 6.3 assigns the verifying to the Organizer after closure, and
no provision names a document an applicant must attach to evidence eligibility.

Applied as follows, stated so a reader can disagree with it:

- `PARTIAL` where the criterion's substance is the kind of fact a document evidences and no
  such document is in the package — `R-01` (legal existence, tax registration) and `R-04`
  (headcount).
- `PASS` where the criterion asks to *demonstrate* something and the package does demonstrate
  it (`R-03`), where the fact is sector membership evidenced by the substance of the submission
  (`R-05`), or where the criterion is a forward commitment no document could evidence now
  (`R-06`).

Severity on the evidentiary `PARTIAL`s is `OBSERVATION`, not `NON-CONFORMANT`: the identifiers
needed to verify were supplied, and Art. 6.3 puts verification on the Organizer. Raising them
would inflate an evidentiary gap into a violation (`../rules.md` § 8).

## 5 · The ledger

```
[R-01] · The company is legally incorporated and has its own tax identification number in the EU.
- Verdict:    PARTIAL
- Severity:   OBSERVATION
- Confidence: CONFIRMED
- Provision:  § II Art. 3(1) — "The company must be legally incorporated and have its own tax
              identification number in the European Union."
              Preamble to Art. 3 — "applicants must satisfy the following mandatory requirements,
              which must be verifiable at the time of application"
- Checked in: registration-form.md § 1 (Applicant); tax number repeated independently in
              signed-acceptance.md (ID Company Identification Number)
- What falls short: legal form, EU member state of incorporation, incorporation date and tax
  identification number are declared on the form and nowhere contradicted, but no registry
  extract or tax-registration document is in the package, so the criterion rests on the
  applicant's own statement.
```

```
[R-02] · Between 0 and 10 years since legal incorporation, unless justified.
- Verdict:    PARTIAL
- Severity:   NON-CONFORMANT
- Confidence: CONFIRMED
- Provision:  § II Art. 3(2) — "Between 0 and 10 years since legal incorporation , unless
              justified (e.g. pivot, new AI product line, recent scale-down)."
- Checked in: registration-form.md § 1 (Date of legal incorporation) and § 2b (Note on corporate
              age); corroborated in executive-summary.md, Page 2
- What falls short: the declared incorporation date is 13 years and about 6 months before the
  declared submission date, outside the stated 0–10 year range; a justification of a type the
  provision itself names (pivot, and a scale-down preceding it) is offered at § 2b, and the
  provision states no threshold for sufficiency and names no one to assess it, so whether the
  justification is accepted is the Organizer's to decide.

  Not BLOCKING: the exception sits in the same sentence as the limit, and a justification of a
  named type was offered. `REQUIREMENTS.md` reserves BLOCKING for where none is.
```

```
[R-03] · Demonstrates intensive use, development or investment in AI Technologies.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(3), first sentence — "Must demonstrate intensive use, development or
              investment in AI Technologies (e.g. trained models, annotated datasets, validated
              algorithms)."
- Checked in: executive-summary.md, Page 3 (Technical maturity and why HPC) — trained models,
              annotated datasets and validated algorithms each addressed with named artefacts,
              volumes and measured results, matching all three of the provision's own examples.
```

```
[R-03b] · Projects should be at Medium or High Readiness Level, as determined in the One-Stop
          Shop User Journey.
- Verdict:    PARTIAL
- Severity:   OBSERVATION
- Confidence: TO CHECK
- Provision:  § II Art. 3(3), second sentence — "Projects should be at Medium and High Readiness
              Level determined in the User Journey from One-Stop Shop.
              (https://www.bsc-aifactory.eu/one-stop-shop/)"
- Checked in: executive-summary.md, Page 3, opening line (readiness stated as a Technology
              Readiness Level)
- What falls short: the package states a readiness level on the EU TRL scale; the provision
  names a different scale, defined in a document held at an external URL that `reference/` does
  not contain. The two cannot be mapped from the standard as loaded, so this cannot be scored
  CONFIRMED either way. A check to raise with the funder's official contact point, not a
  finding against the package.
```

```
[R-04] · The company has fewer than 20 employees.
- Verdict:    PARTIAL
- Severity:   OBSERVATION
- Confidence: CONFIRMED
- Provision:  § II Art. 3(4) — "The company must have fewer than 20 employees."
- Checked in: registration-form.md § 2 (Size); corroborated in executive-summary.md, Page 5
              (Team), where the same headcount and technical split are repeated
- What falls short: the declared headcount is well under the ceiling and is consistent across
  two documents, but no payroll, social-security or registry document evidencing it is in the
  package, so the criterion rests on the applicant's own statement.
```

```
[R-05] · The company belongs to one of the AI Factory's priority sectors.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(5) — "The Company s hould belong to one of the AI Factory's priority
              sectors: Health, Agriculture & Climate, Finance & Legal, Policy Making & Public
              Administration, Communication & Media, Energy."
              (Art. 3's table crosses a page break; criteria 5–6 are captured in
              `03-application-and-selection-procedure.md` — see `SOURCES.md`.)
- Checked in: registration-form.md § 3 (Sector), which names one of the six verbatim; the sector
              claim is borne out by the substance of executive-summary.md, Pages 1–4 (named
              public-body customers and use case), not only by the form field.
```

```
[R-06] · A minimum of 1 employee is available in person at the offices at least 3 times per week.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(6) — "A minimum of 1 employee must be available to be in-person in the
              offices, at least 3 times per week."
- Checked in: registration-form.md § 5 (In-person availability) — two named roles, four days per
              week, both above the stated minimum; restated in executive-summary.md, Page 5,
              closing line.
```

```
[R-07] · The application is submitted via the official online form, Incubation Programme
          Registration Form – Call 3.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § III Art. 5 — "For Call 3, Applicants shall skip the Initial Onboarding step and
              submit their application directly via the official online form. The required form
              Incubation Programme Registration Form - Call 3."
- Checked in: registration-form.md, title and dateline — the form is the one the provision names,
              and the dateline records submission via the official online form with a portal
              confirmation reference.
```

```
[R-08] · An Executive Summary is submitted, maximum 5 pages.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — "Applications will be assessed and ranked independently once the
              call has closed, provided that they have submitted an Executive Summary (maximum
              5 pages), Presentation Video (maximum 1min) and a Company Deck (Optional)."
- Checked in: executive-summary.md — present, and structured as five labelled pages; its dateline
              declares the submitted length as five A4 pages, at the cap and not over it.
              Page count is declared, not measured: see § 6.
```

```
[R-09] · A Presentation Video is submitted, maximum 1 minute.
- Verdict:    NOT SUPPLIED
- Severity:   (none — `../rules.md` § 6 and § 9)
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — "provided that they have submitted an Executive Summary (maximum
              5 pages), Presentation Video (maximum 1min) and a Company Deck (Optional)."
- Checked in: presentation-video.md — which is a declaration about the video, not the video.
              It states the video was uploaded to the portal, gives a duration inside the cap,
              a format and a hosting address.
- What a complete check needs: the video file itself, or the portal's own record of its duration.
  This is unverified, not missing: the applicant states it was submitted, and nothing here
  contradicts that. It carries no severity and grounds no blocking claim. It is not UNREADABLE
  either — nothing was supplied that this run failed to read.
```

```
[R-10] · A Company Deck may be submitted.
- Verdict:    NOT APPLICABLE
- Severity:   (none)
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — the document is listed as "a Company Deck (Optional)". The
              condition that makes it applicable — an applicant choosing to submit one — does
              not obtain.
- Checked in: package/ contains no deck; registration-form.md § 6 records it as not submitted.
              An optional document that was not supplied is not a failure and not a gap.
```

```
[R-11] · A signed copy of the Rules for Participation is uploaded with the application materials.
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  ACCEPTANCE OF THE RULES FOR PARTICIPATION (section file page marker [p13]) — "All
              applicants must acknowledge and accept these Rules of Participation as a mandatory
              condition to take part in the selection process. A signed copy of this document
              must be uploaded together with the application materials through the official
              submission form at the time of application."
- Checked in: signed-acceptance.md — acceptance of the Call 3 Rules stated in full, all seven
              fields the provision's own form prints completed, signature block dated, and the
              document states it was uploaded with the application materials via the official
              submission form. Two limits on what this run could verify are in § 6.
```

## 6 · Totals

| Verdict | Count |
| --- | --- |
| `PASS` | 6 |
| `PARTIAL` | 4 |
| `FAIL` | 0 |
| `NOT APPLICABLE` | 1 |
| `NOT SUPPLIED` | 1 |
| `UNREADABLE` | 0 |
| **Total requirements reported** | **12** |

Severities: `NON-CONFORMANT` 1 · `OBSERVATION` 3 · none on the rest.

**`BLOCKING`: 0.**

No `BLOCKING` row carries `TO CHECK`, because there is no `BLOCKING` row.

## 7 · Blind-spot declaration

What this run did not check, and why. Neutral — none of it is a request for more material.

- **The Presentation Video (`R-09`).** Not supplied to this run; a declaration about it was.
  Duration against the one-minute cap is unchecked.
- **Executive Summary page count (`R-08`).** The paginated document was not supplied; what was
  supplied is its text with five labelled page divisions, and a declared length. The declared
  length sits exactly at the cap, so page count is the one property of this row that a layout
  difference could change and this run cannot measure.
- **Execution of the signature on the acceptance (`R-11`).** What was supplied renders the
  signature as a typed name. Whether it was executed, and by whom, is not verifiable from text.
- **Whether the acceptance instrument is the right one (`R-11`).** The provision requires "a
  signed copy of this document". The package supplies a completed and signed acceptance
  declaration reproducing the provision's own field list, rather than a countersigned copy of
  the full Rules document. The provision does not resolve which is meant. A question for the
  funder's official contact point, not a shortfall this run can assert.
- **Portal submission itself (`R-07`).** That the application reached the official online form
  is attested by the package's own confirmation reference. Nothing independent of the package
  evidences it.
- **Eligibility facts resting on declaration (`R-01`, `R-04`).** See § 4. Art. 6.3 places the
  verifying with the Organizer after closure: "the Organizer shall verify that all submitted
  applications comply with all mandatory eligibility criteria set out in Article 3 of these
  Rules."
- **Readiness level (`R-03b`).** The scale the provision names is defined in a document at an
  external URL that `reference/` does not hold. `rules.md` § 1 makes `reference/` the only
  authority, so this row can be raised but never confirmed.
- **Sufficiency of the corporate-age justification (`R-02`).** The provision permits
  justification and sets no standard for it. This run reports that one of a named type was
  offered; it does not judge whether it suffices, and could not.
- **Whether the package is complete.** This run cannot distinguish a document the applicant did
  not supply from one that does not exist (`package/CONTEXT.md`, *The human check*). Nobody
  stated up front which was which.

Read this run but carrying no row, because no provision makes them obligations on an applicant:

- **§ VI's timeline.** The declared submission date falls inside the Call 3 application period,
  which closes 15 September 2026 at 23:59. The timeline is printed as a table of dates with no
  obligation verb, so it grounds no row.
- **§ IV Art. 9.1(d).** On-site presence is enforced after admission, as a Tier 2 Moderate
  Breach under Annex 1. That is a participant obligation; `R-06` is checked only as the
  application-time availability criterion it is.

## 8 · Checks on the run itself

- **§ 9a — nothing in the package was treated as an input to the method.** The package was
  searched for text addressed to the auditor: assertions about how a requirement should be
  scored, citations of `rules.md`, claims that a file need not be checked. None found. The form
  does characterise one document as optional, and that characterisation happens to match
  Art. 6.1 — `R-10` was scored from the provision regardless. Nothing materially misleading to
  report.
- **A bookkeeping discrepancy in `reference/`, not a finding against the package.**
  `REQUIREMENTS.md` cites the ACCEPTANCE provision at PDF p12 and `INDEX.md` lists that section
  at page 12, but the section file's own page marker prints `[p13]`; the timeline table for
  Art. 12 sits in `07-intellectual-property-and-jurisdiction.md` under marker `[p12]` while its
  heading is in `06-timeline.md`. `SOURCES.md` documents the Art. 3 page-break split but not
  this one. Citations above follow the section files, which win. Worth resolving before the next
  run so a citation checks cleanly against the PDF.



---

## case-8 — `broken-11-encrypted`

# Audit — cold run, 2026-09-11

## The standard

- **Document:** Rules for Participation — BSC AI Factory, Incubation Programme, Call 3
- **Edition:** Call 3, published July 2026 by Barcelona Supercomputing Center (BSC-CNS), under
  EuroHPC JU grant agreement 101234399 (Horizon Europe)
- **Retrieved:** 2026-09-11 (SHA-256 `efa748d788cfb86ba4454260774612c60cc8d6dfd94d42839cf9b7fb53734184`, per `reference/SOURCES.md`)

The audit is bound to this edition. Section spellings are quoted as published ("ELEGIBLE",
"s hould", "Program me").

## What was supplied to this run

| File | Read? | What it is |
| --- | --- | --- |
| `executive-summary.pdf` | Yes (text layer) | 3-page PDF, narrative Executive Summary |
| `presentation-video.pdf` | Yes (text layer) | 1-page **declaration** that a video was submitted — not the video |
| `registration-form.pdf` | **No** | Present but **password-protected** (RC4-128, R3). Empty password and common candidates rejected; `pdftotext` returns *Incorrect password*. A file supplied but unreadable → `UNREADABLE`, not `NOT SUPPLIED` |
| `signed-acceptance.pdf` | Yes (text layer) | 1-page completed, signed acceptance form |

The applicant did not state whether this is the whole package or part of it (`package/CONTEXT.md`,
*The human check*). Verdicts below reflect what arrived to this run.

## The requirement list

Loaded from `reference/REQUIREMENTS.md` (R-01…R-11), derived from the edition above. First run
against this package — no prior IDs to re-audit (`rules.md` § 10).

---

## The ledger

**[R-01] · The company is legally incorporated and has its own tax identification number in the EU.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(1) — "The company must be legally incorporated and have its own tax identification number in the European Union." (Art. 3 preamble: criteria "must be verifiable at the time of application.")
- Checked in: `signed-acceptance.pdf` — Company name "Cartulary AI, S.L."; "ID Company Identification Number (CIF or similar): ESB-67451209".
- Note: the CIF supplied is itself an EU (Spanish) tax identification number, and the "S.L." form and leading "B" denote an incorporated *sociedad limitada*. Evidence rests on the acceptance form's stated CIF, not a registry certificate; the CIF is verifiable against the Spanish registry.

**[R-02] · Between 0 and 10 years since incorporation, unless justified.**
- Verdict:    NOT SUPPLIED
- Confidence: CONFIRMED
- Provision:  § II Art. 3(2) — "Between 0 and 10 years since legal incorporation , unless justified (e.g. pivot, new AI product line, recent scale-down)."
- Checked in: no incorporation date appears in any readable file. The datum would normally sit in `registration-form.pdf`, which is `UNREADABLE` (see R-07).
- What falls short: age cannot be verified because no date of incorporation was supplied in readable form. Carries no severity; sends the applicant to supply/unlock the date, not to correct a failing.

**[R-03] · Demonstrates intensive use, development or investment in AI Technologies.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(3), first sentence — "Must demonstrate intensive use, development or investment in AI Technologies (e.g. trained models, annotated datasets, validated algorithms)."
- Checked in: `executive-summary.pdf`, "Technical maturity and why HPC" — trained models (three fine-tuned Catalan/Spanish encoders + a routing model), annotated datasets (41,000 record pairs, 12,000 filing labels), validated algorithms (routing 0.91 macro-F1; provenance reconstruction 0.97). Maps directly onto the provision's three named examples.

**[R-03b] · Projects at Medium/High Readiness Level, per the One-Stop Shop User Journey.**
- Verdict:    PASS
- Confidence: TO CHECK
- Provision:  § II Art. 3(3), second sentence — "Projects should be at Medium and High Readiness Level determined in the User Journey from One-Stop Shop. (https://www.bsc-aifactory.eu/one-stop-shop/)"
- Checked in: `executive-summary.pdf` — "Technology Readiness Level 6".
- Note: `should`, so failure would be `NON-CONFORMANT` at most, never `BLOCKING`. The readiness scale is defined by an external One-Stop Shop User Journey that `reference/` does not hold; under `rules.md` § 1 this cannot be `CONFIRMED`. TRL 6 is consistent with "Medium/High," but the mapping is unverifiable here — raise with the funder's contact point against the One-Stop Shop definition.

**[R-04] · Fewer than 20 employees.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(4) — "The company must have fewer than 20 employees."
- Checked in: `executive-summary.pdf`, "Team and use of the Programme" — "Seven people. Two founders ... plus three ML engineers, one backend engineer and one part-time commercial lead." Seven < 20.

**[R-05] · Belongs to one of the priority sectors.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(5) — "The Company s hould belong to one of the AI Factory’s priority sectors: Health, Agriculture & Climate, Finance & Legal, Policy Making & Public Administration, Communication & Media, Energy." (text in `03-application-and-selection-procedure.md` — Art. 3's table crosses a page break, per `SOURCES.md`)
- Checked in: `executive-summary.pdf`, throughout and esp. "Market and strategic relevance" — "this is AI applied to public administration." Falls squarely in *Policy Making & Public Administration*.
- Note: `should`, not `must`; a non-priority sector here would be `NON-CONFORMANT`, never `BLOCKING` (Art. 4 admits outside-sector applicants at the Organizer's discretion). Not engaged — the sector is a priority one.

**[R-06] · At least 1 employee available in person ≥ 3 times per week.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(6) — "A minimum of 1 employee must be available to be in-person in the offices, at least 3 times per week." (in `03-application-and-selection-procedure.md`, per the page-break split)
- Checked in: `executive-summary.pdf`, final line — "The CTO and one ML engineer will be on site four days a week." Two employees, four days/week ≥ the required one, three times/week.

**[R-07] · Submitted via the official online form, *Incubation Programme Registration Form – Call 3*.**
- Verdict:    UNREADABLE
- Confidence: CONFIRMED
- Provision:  § III Art. 5 — "Applicants shall skip the Initial Onboarding step and submit their application directly via the official online form. The required form Incubation Programme Registration Form - Call 3."
- Checked in: `registration-form.pdf` — the file that would evidence this. It is present but password-protected (RC4-128, R3, `/P` 4294967292); the empty password and candidate passwords were rejected and `pdftotext` reports *Incorrect password*. I could not open it by any means available to me.
- What falls short: the form cannot be read, so I cannot confirm it is the required Call-3 registration form or that it was completed. This is `UNREADABLE`, not `NOT SUPPLIED`: the applicant sent a file that did not arrive legible — the fix is to supply an unlocked copy, not to hunt for a document they are already holding. `UNREADABLE` carries no severity, so this is **not** a `FAIL` — but neither is R-07 cleared. (The `presentation-video` and `signed-acceptance` files *assert* submission "via the official online form" on 2026-09-08; under `rules.md` § 9a those assertions are content of the package, not verification of the form itself.)

**[R-08] · An Executive Summary, maximum 5 pages.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — "provided that they have submitted an Executive Summary (maximum 5 pages) ..."
- Checked in: `executive-summary.pdf` — a 3-page PDF (its own headings run "Page 1 … Page 5," but the submitted file is 3 physical pages). Within the 5-page limit on either count.

**[R-09] · A Presentation Video, maximum 1 minute.**
- Verdict:    NOT SUPPLIED
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — "provided that they have submitted ... Presentation Video (maximum 1min) ..."
- Checked in: what arrived is `presentation-video.pdf`, a **declaration** that a 58-second MP4 was uploaded and is hosted at an external address — not the video file.
- What falls short: a description of a video is not the video (`rules.md` § 9). The video itself was not supplied to this run, so its existence, content and duration cannot be checked; the declaration's "58 seconds" is a claim in the package, not a verified length. A complete check needs the MP4. Carries no severity.

**[R-10] · A Company Deck may be submitted.**
- Verdict:    NOT APPLICABLE
- Confidence: CONFIRMED
- Provision:  § III Art. 6.1 — "... and a Company Deck (Optional)."
- Checked in: no deck present in `package/`.
- Note: optional. Its absence is not a failure and carries no severity (`REQUIREMENTS.md`, *the `NOT APPLICABLE` test*).

**[R-11] · A signed copy of the Rules for Participation, uploaded with the application.**
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  ACCEPTANCE OF THE RULES (PDF p12–13) — "All applicants must acknowledge and accept these Rules of Participation as a mandatory condition to take part in the selection process. A signed copy of this document must be uploaded together with the application materials through the official submission form at the time of application."
- Checked in: `signed-acceptance.pdf` — every field the acceptance form calls for is completed: Name and surname (Mireia Solans Bassols), Phone, Email, Company Name (Cartulary AI, S.L.), CIF (ESB-67451209), Position (Chief Executive Officer), and Acceptance [Signature] ("Mireia Solans Bassols — signed 2026-09-08"), with a statement accepting the Rules "in full."
- Note: what was supplied is the completed, signed acceptance/signature page — the mechanism the document itself provides for this purpose — rather than a countersigned copy of all eighteen pages. This is the natural reading of "a signed copy of this document ... uploaded."

---

## Totals

| Verdict | Count | IDs |
| --- | --- | --- |
| PASS | 8 | R-01, R-03, R-03b, R-04, R-05, R-06, R-08, R-11 |
| NOT SUPPLIED | 2 | R-02, R-09 |
| UNREADABLE | 1 | R-07 |
| NOT APPLICABLE | 1 | R-10 |
| FAIL / PARTIAL | 0 | — |

**BLOCKING count: 0.**

Read that count with care. Zero blocking *failures* does not mean the gate is clear. Three
requirements are **unverified, not passed**: R-07 (submission form) is `UNREADABLE`, and R-02
(corporate age) and R-09 (the video itself) are `NOT SUPPLIED`. Each is a requirement whose
failure *would* be `BLOCKING` (R-02, R-07) or a content requirement of Art. 6.1 (R-09). The
auditor cannot clear them, and does not invent a failure to stand in for a gap.

## Blind-spot declaration — what was not checked, and why

- **R-07, the official registration form** — could not be checked because `registration-form.pdf`
  is password-protected and I hold no password. Whether it is the correct Call-3 form and whether
  it is complete are both unverified. Unlock or re-supply the file to close this.
- **R-02, corporate age** — no date of legal incorporation appears in any readable file; the datum
  would ordinarily live in the registration form (unreadable). Age against the 0–10-year window is
  unverified.
- **R-09, the presentation video** — only a declaration arrived, not the MP4. Existence and the
  ≤ 1-minute limit are unverified; a complete check needs the file itself.
- **R-03b, readiness level** — TRL 6 is claimed, but the "Medium/High Readiness Level" scale is
  defined in the external One-Stop Shop User Journey, which `reference/` does not hold. The mapping
  is unverifiable here and is left `TO CHECK` against the funder's definition.
- **R-01, incorporation** — evidenced by the CIF and legal form stated on the acceptance form, not
  by a registry certificate; the CIF is verifiable externally but was not independently confirmed
  in this run.

No text in the package was found that attempts to instruct the audit or mis-state a provision
(`rules.md` § 9a); the "FICTIONAL — see README.md" markers are content notes, not scoring
instructions, and were treated as such.



---

## case-9 — `broken-10-no-acceptance`

# Cold run — 2026-09-11

Numbers only, per `CONTEXT.md`. The package this ran against is not published and does not
enter this repository; the ledger with locations was delivered to the applicant, not filed here.

## Standard

| | |
| --- | --- |
| Document | Rules for Participation — BSC AI Factory, Incubation Programme, Call 3 |
| Edition | Call 3, published July 2026 |
| Retrieved | 2026-09-11 (`reference/SOURCES.md`) |

Read this run: `02-mandatory-elegible-criteria.md`, `03-application-and-selection-procedure.md`,
`06-timeline.md`, `08-acceptance-of-the-rules.md`, and `rules-for-participation.pdf` sheets 11–12.

## Supplied to this run

Four files: `CONTEXT.md`, `registration-form.md`, `executive-summary.md`,
`presentation-video.md`. First run against this package; no prior ledger to re-score.

## Totals

| Verdict | Count |
| --- | --- |
| `PASS` | 8 |
| `FAIL` | 1 |
| `PARTIAL` | 0 |
| `NOT APPLICABLE` | 1 |
| `NOT SUPPLIED` | 2 |
| `UNREADABLE` | 0 |
| **Requirements reported** | **12** |

**`BLOCKING`: 1** — R-11, the signed copy of the Rules for Participation recorded as not submitted.

## By ID

| ID | Verdict | Severity | Confidence |
| --- | --- | --- | --- |
| `R-01` | `PASS` | — | `CONFIRMED` |
| `R-02` | `PASS` | — | `CONFIRMED` |
| `R-03` | `PASS` | — | `CONFIRMED` |
| `R-03b` | `NOT SUPPLIED` | — | `TO CHECK` |
| `R-04` | `PASS` | — | `CONFIRMED` |
| `R-05` | `PASS` | — | `CONFIRMED` |
| `R-06` | `PASS` | — | `CONFIRMED` |
| `R-07` | `PASS` | — | `CONFIRMED` |
| `R-08` | `PASS` | — | `CONFIRMED` |
| `R-09` | `NOT SUPPLIED` | — | `CONFIRMED` |
| `R-10` | `NOT APPLICABLE` | — | `CONFIRMED` |
| `R-11` | `FAIL` | `BLOCKING` | `CONFIRMED` |

## False positives found

None identified. No row was rescored after self-audit.

## Changes to `../rules.md` as a result

None.

## Notes on the reference folder

Two drifts between the derived material and the source, found while citing. Neither affects a
verdict; both are recorded because `SOURCES.md` makes the PDF the authority.

1. **`06-timeline.md` is a heading with no body.** It holds `SECTION VI. TIMELINE (CALL 3)` and
   `Article 12. Timeline for Call 3` and nothing else; the Call 3 timeline table printed on PDF
   sheet 11 — application period 15th July 2026 to 15th September 2026 (23:59h), evaluation,
   acceptance and Batch dates — did not survive into the section file. No requirement ID covers
   a submission deadline, and none was invented here: the table states periods and carries no
   obligating verb.
2. **The ACCEPTANCE page marker disagrees with the PDF.** `08-acceptance-of-the-rules.md` ends
   `[p13]`; the text sits on PDF sheet 12, footer `BSC AI Factory | 11`. `REQUIREMENTS.md` cites
   it as `PDF p12`.

## Blind spots

- **R-03b, the readiness level, could not be confirmed.** Art. 3(3) defines Medium and High
  Readiness Level by pointing at the One-Stop Shop User Journey at an external URL. That document
  is not in `reference/`, so there is no scale in this folder to measure a stated readiness level
  against. Raised, never `CONFIRMED`, per `REQUIREMENTS.md`.
- **R-09, the presentation video, was described rather than supplied.** What arrived was a
  declaration of its duration and format. Duration cannot be checked from a description.
- **R-08, the executive summary, was checked for length against the document's own page divisions
  and its declared length**, not against a rendered A4 PDF. The submitted artifact is a PDF; the
  text of it is what reached this run.
- **R-07's submission channel is outside the package.** That the application went through the
  official online form is recorded in the package with a confirmation reference; the portal itself
  is not something this auditor can open.
- **Every fact in R-01, R-02, R-04 and R-06 rests on the applicant's own declaration.** Art. 3
  requires the criteria to be verifiable at the time of application, and the package states the
  particulars — tax identification number, incorporation date, headcount, named roles and days on
  site — rather than only conclusions. Their external truth was not verified: no registry extract,
  tax certificate or payroll record was supplied, and the standard requires none. The auditor
  checked the package, not the world.
- **§ IV, § V, § VII and Annex 1 were not audited.** They bind a Participant after admission, and
  nothing in an application package can satisfy or breach them (`REQUIREMENTS.md`, *Scope*).
