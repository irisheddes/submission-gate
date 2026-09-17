# Provisions — where each citation's text lives

**A navigation map, never the authority.** It says which stretch of which section file holds
each provision, so `../_tools/check-citations.py` can confirm that a quote sits under the
provision it is cited to, not just somewhere in the standard. The text itself is in the section
files, and where this map and a section file disagree, the section file wins.

**Why it exists.** Before 2026-09-17 the checker searched the whole of `reference/` for a quote.
A citation changed from § II Art. 3(4) to 3(3), and then to 3(9), which does not exist, still
passed if the quote was left alone. `../rules.md` § 2 anchors every row to the provision *and*
the quote, and only the quote was being checked. The judges of Clief Notes Competition 12 found
this. See `../runs/`.

**Written by hand, not worked out from filenames or headings.** A rule like "§ II → file 02"
breaks as soon as a table runs over a page or two clauses share a number, and this document does
both (two clauses are numbered 6.4; Article 16's clauses are numbered 15.1 and 15.2; the article
after 18 is printed "Article 59" and its clauses are 19.1–19.4). Each row is a decision someone
can read.

## How a row is read

- **Provision**: the citation as a run writes it, with the numbering printed on the standard.
  A citation matches the longest key it starts with. Anything after the key that continues the
  number (`(9)`, `.10`, `0`) makes it a **different provision**, and that provision must have
  its own row or the citation fails. Anything else after the key, like `, first sentence` or
  ` (PDF p12)`, is a note and is ignored.
- **From** / **Up to**: exact text from the file. The span starts where **From** starts and
  stops where the first **Up to** after it starts. `end` means the end of the file. Both are
  matched with whitespace collapsed and with the page markers, the provenance comment and the
  `# ` title removed.
- **From** must appear exactly once in its file. The checker refuses to run if it doesn't.

A parent's span contains its children, so a quote from Art. 3(5) cited to Art. 3 passes. The
reverse fails.

## The map

| Provision | File | From | Up to |
| --- | --- | --- | --- |
| `PREAMBLE AND LEGAL BASIS` | `00-preamble-and-legal-basis.md` | `PREAMBLE AND LEGAL BASIS` | `end` |
| `§ I Art. 1` | `01-definitions-and-scope.md` | `Article 1. Definitions` | `Article 2. Scope` |
| `§ I Art. 1(a)` | `01-definitions-and-scope.md` | `a. The Incubation Programme:` | `b. The Organizer:` |
| `§ I Art. 1(b)` | `01-definitions-and-scope.md` | `b. The Organizer:` | `c. Applicant:` |
| `§ I Art. 1(c)` | `01-definitions-and-scope.md` | `c. Applicant:` | `d. Participant/Beneficiary:` |
| `§ I Art. 1(d)` | `01-definitions-and-scope.md` | `d. Participant/Beneficiary:` | `e. Batch:` |
| `§ I Art. 1(e)` | `01-definitions-and-scope.md` | `e. Batch:` | `f. Hot desk:` |
| `§ I Art. 1(f)` | `01-definitions-and-scope.md` | `f. Hot desk:` | `g. Occupancy Rate:` |
| `§ I Art. 1(g)` | `01-definitions-and-scope.md` | `g. Occupancy Rate:` | `h. Space Manager:` |
| `§ I Art. 1(h)` | `01-definitions-and-scope.md` | `h. Space Manager:` | `i. Incubation Site:` |
| `§ I Art. 1(i)` | `01-definitions-and-scope.md` | `i. Incubation Site:` | `Article 2. Scope` |
| `§ I Art. 2` | `01-definitions-and-scope.md` | `Article 2. Scope` | `end` |
| `§ II Art. 3` | `02-mandatory-elegible-criteria.md` | `Article 3. Criteria for Applicants` | `Article 4. Discretionary Consideration` |
| `§ II Art. 3(1)` | `02-mandatory-elegible-criteria.md` | `1.Legal Status` | `2. Corporate Age` |
| `§ II Art. 3(2)` | `02-mandatory-elegible-criteria.md` | `2. Corporate Age` | `3. AI Technology` |
| `§ II Art. 3(3)` | `02-mandatory-elegible-criteria.md` | `3. AI Technology` | `4.Company Size` |
| `§ II Art. 3(4)` | `02-mandatory-elegible-criteria.md` | `4.Company Size` | `5.Sector Priority` |
| `§ II Art. 3(5)` | `02-mandatory-elegible-criteria.md` | `5.Sector Priority` | `6.In-person Availability` |
| `§ II Art. 3(6)` | `02-mandatory-elegible-criteria.md` | `6.In-person Availability` | `Article 4. Discretionary Consideration` |
| `§ II Art. 4` | `02-mandatory-elegible-criteria.md` | `Article 4. Discretionary Consideration` | `end` |
| `§ III Art. 5` | `03-application-and-selection-procedure.md` | `Article 5. Application Process` | `Article 6. Selection Mechanism` |
| `§ III Art. 6` | `03-application-and-selection-procedure.md` | `Article 6. Selection Mechanism` | `Article 7. Resolution` |
| `§ III Art. 6.1` | `03-application-and-selection-procedure.md` | `6.1 Applications will be assessed` | `6.2. For Call 3` |
| `§ III Art. 6.2` | `03-application-and-selection-procedure.md` | `6.2. For Call 3` | `6.3. Eligibility Verification` |
| `§ III Art. 6.3` | `03-application-and-selection-procedure.md` | `6.3. Eligibility Verification` | `6.4. Direct Admission` |
| `§ III Art. 6.4` | `03-application-and-selection-procedure.md` | `6.4. Direct Admission` | `6.5. Evaluation Criteria` |
| `§ III Art. 6.5` | `03-application-and-selection-procedure.md` | `6.5. Evaluation Criteria` | `6.6. Ranking and Selection` |
| `§ III Art. 6.6` | `03-application-and-selection-procedure.md` | `6.6. Ranking and Selection` | `6.7. Waiting List` |
| `§ III Art. 6.7` | `03-application-and-selection-procedure.md` | `6.7. Waiting List` | `6.8 Site-specific Evaluation` |
| `§ III Art. 6.8` | `03-application-and-selection-procedure.md` | `6.8 Site-specific Evaluation` | `Article 7. Resolution` |
| `§ III Art. 7` | `03-application-and-selection-procedure.md` | `Article 7. Resolution` | `end` |
| `§ III Art. 7.1` | `03-application-and-selection-procedure.md` | `7.1. The final resolution` | `7.2. Selected Applicants` |
| `§ III Art. 7.2` | `03-application-and-selection-procedure.md` | `7.2. Selected Applicants` | `7.3. Applicants who disagree` |
| `§ III Art. 7.3` | `03-application-and-selection-procedure.md` | `7.3. Applicants who disagree` | `end` |
| `§ IV Art. 8` | `04-participant-rights-and-mandatory-commitments.md` | `Article 8. Rights of the Participant` | `Article 9. 9.1 Mandatory Commitments` |
| `§ IV Art. 8(a)` | `04-participant-rights-and-mandatory-commitments.md` | `a) Access to a Hot Desk area` | `b) Office facilities` |
| `§ IV Art. 8(b)` | `04-participant-rights-and-mandatory-commitments.md` | `b) Office facilities` | `c) Shared meeting rooms` |
| `§ IV Art. 8(c)` | `04-participant-rights-and-mandatory-commitments.md` | `c) Shared meeting rooms` | `Article 9. 9.1 Mandatory Commitments` |
| `§ IV Art. 9` | `04-participant-rights-and-mandatory-commitments.md` | `Article 9. 9.1 Mandatory Commitments` | `end` |
| `§ IV Art. 9.1` | `04-participant-rights-and-mandatory-commitments.md` | `9.1 Mandatory Commitments` | `Article 9.2 Occupancy Requirement` |
| `§ IV Art. 9.1(a)` | `04-participant-rights-and-mandatory-commitments.md` | `a. Active participation` | `b. Mandatory attendance` |
| `§ IV Art. 9.1(b)` | `04-participant-rights-and-mandatory-commitments.md` | `b. Mandatory attendance` | `c. Mandatory membership` |
| `§ IV Art. 9.1(c)` | `04-participant-rights-and-mandatory-commitments.md` | `c. Mandatory membership` | `d. Repetitive failure` |
| `§ IV Art. 9.1(d)` | `04-participant-rights-and-mandatory-commitments.md` | `d. Repetitive failure` | `e. After being selected` |
| `§ IV Art. 9.1(e)` | `04-participant-rights-and-mandatory-commitments.md` | `e. After being selected` | `Article 9.2 Occupancy Requirement` |
| `§ IV Art. 9.2` | `04-participant-rights-and-mandatory-commitments.md` | `Article 9.2 Occupancy Requirement` | `end` |
| `§ IV Art. 9.2(a)` | `04-participant-rights-and-mandatory-commitments.md` | `a) Only Participants that achieve` | `b) The Occupancy Rate shall be calculated` |
| `§ IV Art. 9.2(b)` | `04-participant-rights-and-mandatory-commitments.md` | `b) The Occupancy Rate shall be calculated` | `c) The Organizer reserves the right` |
| `§ IV Art. 9.2(c)` | `04-participant-rights-and-mandatory-commitments.md` | `c) The Organizer reserves the right` | `end` |
| `§ V Art. 10` | `05-code-of-conduct-and-termination.md` | `Article 10. Code of Conduct` | `Article 11. Termination and exclusion` |
| `§ V Art. 11` | `05-code-of-conduct-and-termination.md` | `Article 11. Termination and exclusion` | `end` |
| `§ VI Art. 12` | `06-timeline.md` | `Article 12. Timeline for Call 3` | `end` |
| `§ VII Art. 13` | `07-intellectual-property-and-jurisdiction.md` | `Article 13. Intellectual Property` | `Article 14. Applicable law` |
| `§ VII Art. 14` | `07-intellectual-property-and-jurisdiction.md` | `Article 14. Applicable law` | `end` |
| `ACCEPTANCE OF THE RULES` | `08-acceptance-of-the-rules.md` | `ACCEPTANCE OF THE RULES FOR PARTICIPATION` | `end` |
| `ANNEX 1: CODE OF CONDUCT AND DISCIPLINARY POLICY` | `09-annex-1-code-of-conduct.md` | `ANNEX 1: CODE OF CONDUCT AND DISCIPLINARY POLICY` | `end` |
| `Annex 1 Art. 15` | `09-annex-1-code-of-conduct.md` | `Article 15. Principles of professionalism` | `Article 16. Confidentiality` |
| `Annex 1 Art. 15.1` | `09-annex-1-code-of-conduct.md` | `15.1. The Programme operates` | `15.2. All Participants must strictly adhere` |
| `Annex 1 Art. 15.2` | `09-annex-1-code-of-conduct.md` | `15.2. All Participants must strictly adhere` | `15.3. All interactions` |
| `Annex 1 Art. 15.3` | `09-annex-1-code-of-conduct.md` | `15.3. All interactions` | `Article 16. Confidentiality` |
| `Annex 1 Art. 16` | `09-annex-1-code-of-conduct.md` | `Article 16. Confidentiality` | `Article 17. Facilities use` |
| `Annex 1 Art. 17` | `09-annex-1-code-of-conduct.md` | `Article 17. Facilities use` | `Article 18. Health, Safety` |
| `Annex 1 Art. 17.1` | `09-annex-1-code-of-conduct.md` | `17.1. All provided facilities` | `17.2. Participants are obligated` |
| `Annex 1 Art. 17.2` | `09-annex-1-code-of-conduct.md` | `17.2. Participants are obligated` | `17.3. Participants shall be held` |
| `Annex 1 Art. 17.3` | `09-annex-1-code-of-conduct.md` | `17.3. Participants shall be held` | `Article 18. Health, Safety` |
| `Annex 1 Art. 18` | `09-annex-1-code-of-conduct.md` | `Article 18. Health, Safety` | `Article 59. Communication` |
| `Annex 1 Art. 18.1` | `09-annex-1-code-of-conduct.md` | `18.1. The consumption or presence` | `18.2. Participants are prohibited` |
| `Annex 1 Art. 18.2` | `09-annex-1-code-of-conduct.md` | `18.2. Participants are prohibited` | `18.3. Participants must strictly adhere` |
| `Annex 1 Art. 18.3` | `09-annex-1-code-of-conduct.md` | `18.3. Participants must strictly adhere` | `Article 59. Communication` |
| `Annex 1 Art. 59` | `09-annex-1-code-of-conduct.md` | `Article 59. Communication` | `Article 20. Disciplinary actions` |
| `Annex 1 Art. 19.1` | `09-annex-1-code-of-conduct.md` | `19.1. Participants shall not publish` | `19.2. This obligation applies to:` |
| `Annex 1 Art. 19.2` | `09-annex-1-code-of-conduct.md` | `19.2. This obligation applies to:` | `19.3. Where authorization is granted` |
| `Annex 1 Art. 19.3` | `09-annex-1-code-of-conduct.md` | `19.3. Where authorization is granted` | `19.4. Any publication` |
| `Annex 1 Art. 19.4` | `09-annex-1-code-of-conduct.md` | `19.4. Any publication` | `Article 20. Disciplinary actions` |
| `Annex 1 Art. 20` | `09-annex-1-code-of-conduct.md` | `Article 20. Disciplinary actions` | `end` |
| `Annex 1 Art. 20.1` | `09-annex-1-code-of-conduct.md` | `20.1. The authority responsible` | `20.2. Violations of this Code` |
| `Annex 1 Art. 20.2` | `09-annex-1-code-of-conduct.md` | `20.2. Violations of this Code` | `20.3. The Procedure` |
| `Annex 1 Art. 20.3` | `09-annex-1-code-of-conduct.md` | `20.3. The Procedure` | `end` |
| `Annex 1 Art. 20.3(a)` | `09-annex-1-code-of-conduct.md` | `a. Upon notification of a potential breach` | `b. The accused Participant` |
| `Annex 1 Art. 20.3(b)` | `09-annex-1-code-of-conduct.md` | `b. The accused Participant` | `c. The BSC AI Factory Commission will evaluate` |
| `Annex 1 Art. 20.3(c)` | `09-annex-1-code-of-conduct.md` | `c. The BSC AI Factory Commission will evaluate` | `d. Disciplinary action taken` |
| `Annex 1 Art. 20.3(d)` | `09-annex-1-code-of-conduct.md` | `d. Disciplinary action taken` | `end` |
| `ANNEX 2: VALUE PROPOSITON & ECONOMIC VALUE` | `10-annex-2-value-proposition.md` | `ANNEX 2: VALUE PROPOSITON & ECONOMIC VALUE` | `end` |

## What is deliberately not mapped

- **Article 16's clauses.** They are printed "15.1." and "15.2.", the same numbers as Article
  15's first two clauses. A citation to "Annex 1 Art. 15.1" can only mean one of them, so it
  means Article 15's. Cite Article 16's clauses as `Annex 1 Art. 16` and quote them.
- **Whole sections** (`§ II` with no article). A row cites the provision it relies on, and in
  this document that is always an article or an unnumbered heading. Leaving whole sections out
  also means `§ II Art. 7`, which does not exist, cannot slip through as "somewhere in § II".
- **The cover page and table of contents** (PDF pages 1–2). They are not stored. See `INDEX.md`.
