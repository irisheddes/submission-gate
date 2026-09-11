#!/usr/bin/env python3
"""Verify that every provision a run quotes appears VERBATIM in reference/.

    python3 _tools/check-citations.py runs/cold-2026-09-11.md
    python3 _tools/check-citations.py --all

Exit 0 if every quote resolves, 1 if any does not.

rules.md § 1 says a provision may only be cited after re-reading it. That is a rule written in
markdown, which makes it a request. This makes it a constraint: a quote that is not a real
substring of the standard fails the check, and a run that fails the check is not evidence of
anything.

It compares on whitespace-normalised text, because the standard was extracted from a PDF and
its line breaks fall in arbitrary places. Everything else - wording, spelling, punctuation -
must match exactly. The source prints "ELEGIBLE"; a run that tidies it up fails here, which is
the point.

Only the verbatim section files are authority. REQUIREMENTS.md is derived and cannot vouch
for a quote.
"""
import re, sys, pathlib

R = pathlib.Path(__file__).resolve().parent.parent
norm = lambda s: re.sub(r"\s+", " ", s).strip()

sections = sorted((R/"reference").glob("[0-9][0-9]-*.md"))
if not sections:
    sys.exit("No standard loaded in reference/ - nothing to check against.")
corpus = {p.name: norm(p.read_text()) for p in sections}

# Accept paths relative to the repo root or to wherever the caller is standing.
def resolve_target(a):
    for cand in (pathlib.Path(a), R/a, pathlib.Path.cwd()/a):
        if cand.exists(): return cand.resolve()
    return pathlib.Path(a)

targets = sorted((R/"runs").glob("*-*.md")) if "--all" in sys.argv else \
          [resolve_target(a) for a in sys.argv[1:] if not a.startswith("--")]
if not targets:
    sys.exit("Usage: check-citations.py <run.md> | --all")

# A quote may be plain ("...") or emphasised (*"..."* / _"..."_), and the dash before it may
# be an em dash or a hyphen. Runs are written by a model, not a formatter; the check must not
# depend on which it chose.
QUOTE = re.compile(r'[\u2014\u2013-]\s*[*_]{0,2}"(.+?)"[*_]{0,2}', re.S)
bad = total = 0

for t in targets:
    if not t.exists():
        print(f"  MISSING  {t}"); bad += 1; continue
    text = t.read_text()
    # only lines that claim to be a provision citation
    claims = [m for line in re.findall(r"^.*\*{0,2}Provision:?\*{0,2}.*(?:\n(?!\s*[-*]\s|\s*```).*)*$",
                                       text, re.M)
                for m in QUOTE.findall(line)]
    rt = t.resolve()
    label = rt.relative_to(R) if R in rt.parents else rt.name
    print(f"\n{label}  -  {len(claims)} citation(s)")
    for q in claims:
        total += 1
        nq = norm(q)
        hit = next((n for n, c in corpus.items() if nq in c), None)
        if hit:
            print(f"  ok    {hit:44s} \"{nq[:46]}...\"" if len(nq) > 46 else f"  ok    {hit:44s} \"{nq}\"")
        else:
            bad += 1
            print(f"  FAIL  not found in any section        \"{nq[:60]}\"")
            close = [n for n, c in corpus.items() if nq[:28] in c]
            if close:
                print(f"        opens like text in {close[0]} - altered after that point?")

print(f"\n{'=' * 58}\n{total} citation(s) checked, {bad} unresolved")
if bad:
    print("A run with an unresolved citation is not evidence. Fix the run, not this check.\n")
sys.exit(1 if bad else 0)
