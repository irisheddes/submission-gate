# Fixture: clean-05-as-pdf — conformant, delivered as PDFs

**Cartulary is a fictional company.** Every fact here was invented for this repository.

The same conformant application as `../clean/`, **submitted the way a real one would be**:
three PDFs instead of three markdown files. Generated with reportlab, so they carry a real
text layer.

| | |
| --- | --- |
| **Expected** | No `FAIL`, no `PARTIAL` — the same result as `../clean/` |
| **Exercises** | Whether the auditor reads a package in its real submission format |

## Why one fixture is not markdown

Every other case here is markdown, which is convenient and is not what anyone submits. A real
application is PDFs and Word files. An auditor that has only ever been run on markdown has been
tested on a format its users do not have.

## What changes when the package is a PDF

**`R-08` becomes measurable.** In markdown there are no pages, so the Executive Summary
*declares* its length and the auditor can only record what it was told — `PASS · TO CHECK`.
Here the page count is a fact about the file: **3 pages**, against a maximum of 5. The right
verdict is `PASS · CONFIRMED`, and an auditor still reporting `TO CHECK` has not noticed that
it can now check.

*(The text inside still carries the line "Length as submitted: 5 pages" from the markdown
original. The PDF is 3 pages. Where a package's own claim about itself and the file disagree,
the file is the fact — and a run that repeats the claim without checking it has taken the
applicant's word for something it could have measured.)*

**`R-09` does not.** A video's duration is still only a declaration; a repository cannot hold
the file. It stays `PASS · TO CHECK`.

**Citations coarsen.** A finding in markdown names a section. In a PDF it names a page. That
is a real loss and it is the cost of the format, not a defect in the auditor.
