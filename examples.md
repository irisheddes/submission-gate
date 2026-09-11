# Examples

Rows from the run recorded in `runs/fixtures-2026-09-11.md`. Between them they show every
verdict and both confidence levels. The row shape is defined in `rules.md`, not here.

None of these is an invented illustration — each is a row the auditor produced against a
fixture, reproducible by running it again.

---

## `PASS` · `CONFIRMED` — a satisfied requirement, and where

```
[R-04] · The company has fewer than 20 employees
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(4) — "The company must have fewer than 20 employees."
- Checked in: fixtures/clean/registration-form.md § 2 · Size — "Total employees | 7"
```

A pass gets a row. An audit that lists only problems is a complaint.

## `PASS` · `TO CHECK` — satisfied, but not verifiable here

```
[R-09] · A Presentation Video is submitted, maximum 1 minute
- Verdict:    PASS
- Confidence: TO CHECK
- Provision:  § III Art. 6.1 — "provided that they have submitted an Executive Summary
              (maximum 5 pages), Presentation Video (maximum 1min) and a Company Deck
              (Optional)."
- Checked in: fixtures/clean/presentation-video.md — duration declared as 58 seconds
- Note:       The duration is declared, not measured. This row rests on the package's own
              statement. Confirm against the submitted file.
```

The auditor cannot play a video. Saying so is the difference between an audit and a guess.

## `FAIL` · `BLOCKING` — quoting the passage that actually bars

```
[R-01] · The company is legally incorporated and has its own tax identification number
         in the European Union
- Verdict:    FAIL
- Severity:   BLOCKING
- Confidence: CONFIRMED
- Provision:  § II Art. 3(1) — "The company must be legally incorporated and have its own
              tax identification number in the European Union."
- Checked in: fixtures/broken-07-non-eu/registration-form.md § 1 · Applicant —
              "Country of incorporation | United States (Delaware)"; "Tax identification
              number | EIN 88-4013967"
- What falls short: Incorporation is outside the Union and the tax identifier is a US
              federal EIN, not an EU number. Art. 3 requires these to be "verifiable at the
              time of application", and both fail on the face of the form.
```

## `FAIL` · `NON-CONFORMANT` — a violation that is not a bar

```
[R-05] · The company belongs to one of the priority sectors
- Verdict:    FAIL
- Severity:   NON-CONFORMANT
- Confidence: CONFIRMED
- Provision:  § II Art. 3(5) — "The Company s hould belong to one of the AI Factory’s
              priority sectors: Health, Agriculture & Climate, Finance & Legal, Policy
              Making & Public Administration, Communication & Media, Energy."
              [reference/03-application-and-selection-procedure.md — Art. 3's table
              continues past a page break into the next section's file]
- Checked in: fixtures/broken-04-sector/registration-form.md § 3 · Sector —
              "Primary sector: Logistics & Freight Optimisation"
- What falls short: Not one of the six named sectors. Not BLOCKING: the provision says
              "should", and § II Art. 4 provides that applicants "operating outside the
              defined strategic sectors may be considered, provided they demonstrate
              intensive use, development or investment of AI."
```

**The severity is the finding here.** Marking this `BLOCKING` would turn a stated preference
into a rejection, which `rules.md` § 8 forbids.

**And note "s hould".** The PDF's text layer breaks words at kerning boundaries, and the quote
carries the break because that is what the source file says. An earlier version of this page
tidied it to "should" — `_tools/check-citations.py` rejected it, which is the entire reason
that script exists. A citation that has been cleaned up is no longer a citation.

## `PASS` — where the provision carries its own exception

```
[R-02] · Between 0 and 10 years since legal incorporation, unless justified
- Verdict:    PASS
- Confidence: CONFIRMED
- Provision:  § II Art. 3(2) — "Between 0 and 10 years since legal incorporation , unless
              justified (e.g. pivot, new AI product line, recent scale-down)."
- Checked in: fixtures/broken-03-age-justified/registration-form.md — incorporated
              14 March 2013 (12 years 6 months), with § 2b · Note on corporate age
              recording a 2023 pivot, the winding-down of the prior service line, and a
              fall from 31 to 4 employees before rebuilding.
- Note:       Outside the range on its face. The exception named in the same sentence is
              met, so there is no finding.
```

Reading the age limit without the rest of its own sentence produces a violation that does not
exist. The fixture is named `broken-03` on purpose.

## `NOT APPLICABLE` — an optional document, absent

```
[R-10] · A Company Deck may be submitted
- Verdict:    NOT APPLICABLE
- Provision:  § III Art. 6.1 — "and a Company Deck (Optional)."
- Checked in: fixtures/clean/ — no Company Deck present; the registration form records
              "Company Deck | No | Optional; not submitted"
```

No severity. Absence of an optional document is not a failure and not a gap.

## `NOT SUPPLIED` — unverified, not missing

```
[R-08] · An Executive Summary is submitted, maximum 5 pages
- Verdict:    NOT SUPPLIED
- Confidence: TO CHECK
- Provision:  § III Art. 6.1 — "an Executive Summary (maximum 5 pages)"
- Checked in: package/ — no Executive Summary was given to this run
- Note:       The applicant has not stated that no Executive Summary will be submitted.
              This is material not provided to the auditor, not a document that is absent
              from the application.
```

**The distinction this folder exists for.** `NOT SUPPLIED` carries no severity and never
counts toward the `BLOCKING` total. Treating it as a failure inflates every audit run before
a package is complete — which is most of the time a package is actually worth auditing.
