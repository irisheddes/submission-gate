# reference/ — the input slot

**One job: hold the standard this auditor is currently pointed at, as text a reader can
open.**

This folder is the auditor's input. Replacing its contents retargets the auditor. Nothing
outside it needs to change.

## What it holds

| File | What it is |
| --- | --- |
| `SOURCES.md` | The registry — title, publisher, edition, URL, date read, language, SHA-256 |
| `INDEX.md` | Navigation — section list, topic map, and what is stored |
| `PROVISIONS.md` | Navigation — each citable provision mapped to the exact stretch of its section file. Used by `../_tools/check-citations.py` to check a quote is under the provision it is cited to |
| `REQUIREMENTS.md` | **Derived, not source.** The obligation list the auditor works from, each row citing the section it came from |
| `LOADING.md` | The setup procedure for pointing this auditor at a different rulebook |
| `<nn>-<slug>.md` | One file per section of the standard, verbatim |
| `<slug>.pdf` | The document as published, unaltered |

## Why sections, not one file

`rules.md` § 1 requires re-reading a provision in the same turn it is cited. One file per
section is what makes that affordable — how to load them is `CLAUDE.md`, *The loading rule*.

## Rules for this folder

- **Verbatim only — with one declared exception.** `REQUIREMENTS.md` is derived from the
  sections and says so on its first line; where it and a section disagree, the section wins
  and the list is re-derived. Everything else here is the source's own words.
- **Nothing is authored, summarised or paraphrased.** Where a passage is
  abridged, mark the omission `[...]` and keep the full text in the source file beside it.
- **The document's own numbering.** Findings cite the section numbers printed on the
  standard, never a scheme invented here. An unnumbered heading is cited by its heading text
  in quotes, and noted as unnumbered in its file.
- **The language of publication.** A translation is not the standard and may not be shipped
  as one. If a rendering is useful, it sits beside the original, labelled, and is never
  cited.
- **One standard at a time.** Two rulebooks in this folder means the auditor cannot say what
  it enforces.

## Putting a new rulebook in

Drop the document here and say to load it. The agent runs `LOADING.md` — verifies it is
publicly available, vendors it with a hash, splits it at its own seams, writes `SOURCES.md` and
`INDEX.md`, and derives `REQUIREMENTS.md`. Steps 6 to 8 — rebuilding the fixtures, running
them, and rewriting `../examples.md` — need a person, because a test set is a judgement about
what is worth testing.

Until that has happened the folder holds a document, not a standard, and the auditor says so
rather than auditing against it.

## Pointing this at a different standard

`LOADING.md`, beside this file — eight steps, run **once at setup and never during an audit**.
A standard that arrives mid-run is not resident: it cannot be cited by section and cannot carry
stable requirement IDs.

`../identity.md`, `../rules.md` and the row shape are unaffected by a swap. `../fixtures/`
never survives one.

## Who reads it

Every run, selectively.

## The human check

Before the first run against a new standard: is the document here the edition named in
`SOURCES.md`, and is it publicly available at the URL recorded there? A finding citing a
provision nobody else can open is not checkable, which is the failure this folder exists to
prevent.
