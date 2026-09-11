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

## Two properties of this extraction

**The PDF's text layer splits words.** `s hould`, `Program me`, `Incu bation`, `Particip ant`
and others appear with a space inside them. These are artefacts of the source file's kerning,
not the publisher's spelling, and they are **left exactly as extracted** — correcting them
would make the section files disagree with the PDF beside them, and a quote could then be
"verbatim" against neither. Where the two ever differ, **the PDF is authority.**

`_tools/check-citations.py` enforces this: a run that quietly tidies a quote fails it.

**Article 3's table crosses a page break.** Criteria 1–4 sit in
`02-mandatory-elegible-criteria.md`; criteria 5 (Sector Priority) and 6 (In-person
Availability) continue on the next page and were captured in
`03-application-and-selection-procedure.md`. The split follows the PDF's pages, not the
document's logic. A citation to § II Art. 3(5) is correct and its text is in the 03 file.

## Sections held

Eleven, the document's own, listed in `INDEX.md`. The extraction is verbatim, including two
spellings printed in the source — "ELEGIBLE" (Section II) and "JURISDICITION" (Section VII).
They are left as published: a citation that silently corrects its source is no longer a
citation.
