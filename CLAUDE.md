# Submission Gate

A conformity auditor for public-funding application packages. It checks one package against the
rulebook in `reference/` — which is an input, not a property of this folder — and reports every
requirement, passes included, each row quoting its provision. Method: `rules.md`. System: `CONTEXT.md`.

## If you were opened here with no instruction

**Audit whatever is in `package/`.** That is the job this folder exists to do, and it is the
default — nobody should have to say it.

Read `identity.md`, then `rules.md`, then `reference/REQUIREMENTS.md`. Work through
`rules.md` § *The run, in order*. Report **every** requirement, passes included, each with a
verdict, a severity where one applies, a confidence, the provision quoted from `reference/`,
and the place in the package you checked. Write the result to `runs/`.

**Two things arrive here, and they go in different places.** A rulebook goes in `reference/`
and stays until it is swapped. An application goes in `package/` and leaves after one run.

- `package/` empty → say so and ask for the application.
- `reference/` holds a document that has not been sectioned — a loose PDF, a page of text, a
  URL someone gave you → **run `reference/LOADING.md` on it first.** Do not audit against an
  unsectioned document: it cannot be cited by section and its requirements have no stable IDs.
- `reference/` empty → say so and stop. There is no standard, so there is nothing to enforce
  and nothing to find.

## Route by what you are doing

| Task | Go to | Read |
| --- | --- | --- |
| **Audit a package** | root, then `reference/` | `identity.md` → `rules.md` → `reference/REQUIREMENTS.md` → `reference/INDEX.md`, then only the sections you cite |
| Put a package in to be audited | `package/` | its `CONTEXT.md` |
| Understand the system before changing it | root | `CONTEXT.md` |
| See what a finished row looks like | root | `examples.md` |
| **Point this at a different standard** | `reference/` | `LOADING.md` — eight steps, setup only |
| Strip the current standard out | run `_tools/unload.py` | its `--help`; `git checkout .` undoes it |
| Check the auditor still works | `fixtures/` | its `CONTEXT.md`, then `EXPECTED.md` |
| Read what past runs found | `runs/` | its `CONTEXT.md` |
| Use it as a person, arriving from GitHub | root | `README.md` |

## Naming

| Thing | Name | Where |
| --- | --- | --- |
| A requirement | `R-01`, `R-02`, … — stable for the life of the standard's edition | `reference/REQUIREMENTS.md` |
| A section of the standard | `<nn>-<slug>.md`, `<nn>` following the document's own order | `reference/` |
| A fixture | `clean/`, or `broken-<nn>-<what-it-breaks>/` | `fixtures/` |
| A run against the fixtures | `fixtures-<YYYY-MM-DD>.md` | `runs/` |
| A run against a real package | `cold-<YYYY-MM-DD>.md` | `runs/` |

## The loading rule

**Never load the whole of `reference/`.** Rule 1 requires re-reading a provision in the same
turn you cite it — open `reference/INDEX.md`, load the one section, quote it, move on. A run
that slurps the standard has spent its context before it reaches the package.

## Status

`python3 _tools/status.py` — reports which of the four setup steps in `reference/LOADING.md`
are done, by scanning. Generated, never hand-maintained. It fails loudly when the standard's
hash stops matching `SOURCES.md`, or when fixtures changed after the last run.

An empty `package/` means nothing to audit: ask for it, or point at a fixture.

## The gate

This auditor never decides whether to submit — see `CONTEXT.md`, *The human check*.
