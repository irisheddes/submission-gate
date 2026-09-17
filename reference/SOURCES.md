# Sources — the standard loaded here

The registry for the rulebook currently in this folder. How the folder is laid out, how
provisions are cited, and how to swap the standard are in `CONTEXT.md`.

| | |
| --- | --- |
| **Document** | Rules for Participation — BSC AI Factory, Incubation Programme, Call 3 |
| **Publisher** | Barcelona Supercomputing Center (BSC-CNS), for the BSC AI Factory consortium, under EuroHPC JU grant agreement 101234399 (Horizon Europe) |
| **Edition** | Call 3. Published July 2026 (from the publisher's own upload path, `/2026/07/`) |
| **Retrieved from** | https://bsc-aifactory.eu/wp-content/uploads/2026/07/BSC_AI_Factory_Rules_for_Participation_Call_3.pdf |
| **Date read** | 2026-09-11 |
| **Public?** | **Confirmed.** Linked from the publisher's own call page, https://bsc-aifactory.eu/call-for-startups/ — no login, no registration |
| **Language** | English, as published. Nothing here is translated |
| **Call status when read** | Open. Applications 15 July – 15 September 2026 |
| **SHA-256** | `efa748d788cfb86ba4454260774612c60cc8d6dfd94d42839cf9b7fb53734184` |
| **Size** | 769198 bytes · 18 pages |

## Verify this copy yourself

The vendored PDF must be byte-identical to what the publisher serves. Anyone can check:

```sh
curl -sL -o /tmp/rfp.pdf \
  "https://bsc-aifactory.eu/wp-content/uploads/2026/07/BSC_AI_Factory_Rules_for_Participation_Call_3.pdf"
shasum -a 256 /tmp/rfp.pdf reference/rules-for-participation.pdf
```

If the hashes differ, the publisher has revised the document and **every finding in `runs/`
was made against a version that no longer exists.** Re-section the folder before auditing
again. A clean report against a dead edition is the failure this page exists to prevent.

**Matching hashes do not prove this is the latest edition.** It happened with this document.

## A later edition exists — found 2026-09-17

The publisher serves two PDFs with the same filename:

| Upload path | PDF created | SHA-256 | Here |
| --- | --- | --- | --- |
| `/2026/07/` | 14 July 2026 | `efa748d788cfb86ba4454260774612c60cc8d6dfd94d42839cf9b7fb53734184` | **Vendored.** Every section file, the provision map, the fixtures and every run are bound to it |
| `/2026/08/` | 3 August 2026 | `4de107b683ebffab8198459c1a6fd656ec40c162ce04fab8d745e27740be730f` | Not vendored |

Compared word for word, they differ **only in the list of incubation sites**: "Guimarães
(Portugal) – up to 12 Participants" in July is "Porto (Portugal) – up to 5 Participants" in
August, in § I Art. 1(i) and in § III Art. 6.2. One line in Annex 1 Art. 15.1 is re-wrapped. The
total in Art. 6.2, "thirty-six (36)", is unchanged, and so is every provision
`REQUIREMENTS.md` derives a requirement from. Findings about applicant eligibility and the
package are unaffected; anything citing the site list is July's.

Found by a session that loaded the call from scratch and checked the call's own page rather than
trusting the file it was given. The July copy is kept, and this is recorded, because swapping the
edition means re-extracting, re-mapping and re-running everything bound to it.

## How the text was extracted, and a claim this page used to make that was wrong

**The section files were extracted on 2026-09-17 with pdfplumber 0.11.9, and checked word for
word, page by page, against pdftotext (poppler 26.04.0).** Tables are written out one cell at a
time, so a quoted cell stays whole. `../_tools/check-extraction.py` repeats the comparison for
anyone who wants to check it.

The two extractors agree on every word of pages 3–18 except in two places, and in both the
page decides:

| Where | pdfplumber | pdftotext | The page prints | Kept |
| --- | --- | --- | --- | --- |
| Four words hyphenated across a line break (p3, p13, p15) | `non-` / `discriminatory` | `nondiscriminatory` | the hyphen | pdfplumber |
| The dashes that open the list in Art. 10 (p10) | `-` | dropped | a dash on each item | pdfplumber |

### The earlier claim, and why it was wrong

Until 2026-09-17 the sections came from **pypdf**, and this page said:

> *"The PDF's text layer splits words. `s hould`, `Program me`, `Incu bation`, `Particip ant`
> and others appear with a space inside them. These are artefacts of the source file's
> kerning, not the publisher's spelling, and they are left exactly as extracted."*

**That was false.** The PDF prints `should` and `Programme`. The judges of Clief Notes
Competition 12 measured the glyph boxes and found no gap and no span boundary inside any of
those words. Re-extracting with two other tools confirmed it: pdfplumber and pdftotext produce
none of the splits. pypdf put them there, and nobody checked it against a second tool.

The claim did damage beyond one wrong paragraph. It broke this folder's own precedence rule
(*where the two differ, the PDF is authority*), and `../_tools/check-citations.py` enforced
it. The checker failed any run that quoted the PDF correctly and passed any run that copied the
artefact. The passages quoted most often in `../runs/` (Art. 3(2) and Art. 3(5)) were the
ones that did not match the published document.

What pypdf got wrong, all of it now corrected:

- **Nine words split** by a space the PDF does not have: `s hould`, `s ame`, `Program me` (five
  times), `Progra mme`, `Incu bation`. The list above also named `Particip ant`, which never
  appeared in the old files either.
- **Seventeen spaces added** before a hyphen, colon or comma: `high -potential`,
  `day -to-day`, `Organizer :`, `incorporation , unless justified`, and others.
- **Two tables moved into the wrong section.** The last two rows of Art. 3's table (criteria 5
  and 6) were placed inside § III Art. 6.3. The Art. 12 timeline table was placed inside
  § VII, which left `06-timeline.md` as a heading with no body. Two blind runs reported the
  empty timeline file on 2026-09-11 (see `../runs/blind-ledgers-2026-09-11.md` and
  `../runs/blind-ledgers-cases-7-9-2026-09-11.md`). Nobody traced it back to the extractor.
- The Art. 6.5 scoring table was split, with criteria 3–5 printed inside Art. 6.7.

**This page also said criteria 5–6 "continue on the next page and were captured in
`03-application-and-selection-procedure.md`", and called that split one that "follows the
PDF's pages".** That was only half true. The table does cross from page 4 to page 5, but on
page 5 criteria 5–6 come *before* Art. 4 and Section III. They are now in
`02-mandatory-elegible-criteria.md`, where the document puts them. A citation to § II Art. 3(5)
was correct then and is correct now; only the file holding its text has changed.

### What the text layer holds

- **Apostrophes:** nine curly `’` in the whole PDF. Eight are in the stored sections and one is on
  the cover, which is not stored. One straight `'` appears, in *"the Participant's defense"*
  (Annex 1 Art. 20.3(c)). Each is kept exactly as the PDF has it. Five blind runs typed a
  straight apostrophe where the source has a curly one, and the checker was right to reject
  them.
- **Double quotes:** curly `“ ”` in the body of the Rules, straight `" "` in Annex 1. Both kept.
- **Publisher's own errors, kept as printed:** "ELEGIBLE" (Section II), "JURISDICITION"
  (Section VII), "VALUE PROPOSITON" (Annex 2), two clauses numbered 6.4, Article 16's clauses
  numbered 15.1 and 15.2, and "Article 59" between Articles 18 and 20.

**The PDF did not change.** Its SHA-256 above is the same file. Only the text taken from it
changed.

## Sections held

Eleven, the document's own, listed in `INDEX.md`. Which stretch of which file holds each
provision is in `PROVISIONS.md`. The extraction is verbatim, including the publisher's own
misspellings listed above. They are left as published: a citation that silently corrects its
source is no longer a citation.
