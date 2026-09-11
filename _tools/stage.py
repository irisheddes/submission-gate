#!/usr/bin/env python3
"""Stage one or more fixtures for a BLIND audit.

    python3 _tools/stage.py                                  # list the cases
    python3 _tools/stage.py broken-04-sector clean-03-minimal ...

Builds _stage/case-1/, case-2/ ... each holding the auditor, the standard, and one case's
application files copied into package/. The cases are SHUFFLED, so the order you typed them
tells the reader nothing.

Why this exists. A fixture folder is named broken-07-non-eu and contains a README naming the
planted violation and the expected verdict. An auditor pointed at that folder is not finding
anything; it is being told. Instructing a session not to read the README is a request. This is
the constraint: nothing under _stage/ contains EXPECTED.md, runs/, _tools/, examples.md, the
fixture's README, or its name.

examples.md is withheld for a reason worth stating: its rows are genuine output from genuine
cases, which is what makes them worth shipping — and which also means they quote the very
packages being tested here. Real examples and a blind test set pull against each other, and
the test wins.

The mapping from case-N back to the fixture is written OUTSIDE the repository, so it cannot be
reached from a session working in _stage/.
"""
import shutil, sys, pathlib, random, json, os, tempfile

R = pathlib.Path(__file__).resolve().parent.parent
FIX, STAGE = R/"fixtures", R/"_stage"
cases = sorted(d.name for d in FIX.iterdir() if d.is_dir())

args = [a for a in sys.argv[1:] if not a.startswith("--")]
NOTICE = "--no-notice" not in sys.argv      # omit WHAT-IS-MISSING.md entirely
KEEP   = "--keep" in sys.argv               # do not wipe cases already staged
# Case numbers are never reused. A session transcript is stored by its folder path, so a
# second case-1 writes into the same history as the first and the two become impossible to
# tell apart later. Default to continuing past the highest number ever staged.
_seen = pathlib.Path(__file__).resolve().parent.parent/"_stage"/".case-counter"
_hi = int(_seen.read_text().strip()) if _seen.exists() else 0
START  = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--start=")), _hi + 1)
if not args:
    print("\nCases:\n")
    for c in cases: print(f"  {c}")
    print("\n  python3 _tools/stage.py <case> [<case> ...]\n")
    sys.exit(0)

unknown = [a for a in args if a not in cases]
if unknown: sys.exit(f"No such case(s): {', '.join(unknown)}")

def ledgers_in(path):
    """Any run output under path. A ledger is evidence; it is not ours to delete."""
    return sorted(f for f in path.rglob("runs/*.md") if f.name != "CONTEXT.md")

# Refuse to destroy a run. A staged case that has been audited holds the only copy of what
# that session found, and re-staging is a setup step, not a reason to lose it.
if STAGE.exists():
    # Only ledgers about to be destroyed matter. With --keep, cases below START are untouched,
    # so refusing on them would be a guard firing at nothing — which teaches people to bypass it.
    doomed = lambda f: (not KEEP) or int(f.relative_to(STAGE).parts[0].split("-")[1]) >= START
    held = [f for f in ledgers_in(STAGE) if doomed(f)]
    if held and "--discard-runs" not in sys.argv:
        print("\nREFUSED — staged cases hold ledgers that have not been collected:\n")
        for f in held: print(f"  {f.relative_to(STAGE.parent)}")
        print("""
These are the only copy of what those runs found. Collect them into runs/ first.

  cp _stage/case-*/runs/*.md runs/        (then rename, they are all called the same thing)

Re-run this command once they are safe. If you genuinely want them gone, pass
--discard-runs and say so out loud to whoever is relying on them.
""")
        sys.exit(1)

if STAGE.exists() and not KEEP: shutil.rmtree(STAGE)
STAGE.mkdir(exist_ok=True)
order = args[:]; random.shuffle(order)
key = {}
if KEEP:
    prev = pathlib.Path(os.environ.get("STAGE_KEY_DIR", tempfile.gettempdir()))/"submission-gate-stage-key.json"
    if prev.exists():
        key.update({k: v for k, v in json.loads(prev.read_text()).items()
                    if int(k.split("-")[1]) < START})
    # clear any case at or above START - they are about to be re-staged
    for d in STAGE.iterdir():
        if d.is_dir() and d.name.startswith("case-") and int(d.name.split("-")[1]) >= START:
            shutil.rmtree(d)

for i, case in enumerate(order, START):
    d = STAGE/f"case-{i}"
    (d/"package").mkdir(parents=True); (d/"runs").mkdir()
    for f in ["CLAUDE.md", "CONTEXT.md", "identity.md", "rules.md"]:
        shutil.copy2(R/f, d/f)
    shutil.copytree(R/"reference", d/"reference")
    shutil.copy2(R/"package/CONTEXT.md", d/"package/CONTEXT.md")
    shutil.copy2(R/"runs/CONTEXT.md", d/"runs/CONTEXT.md")
    n = 0
    for f in sorted((FIX/case).iterdir()):
        if f.name == "README.md" or f.is_dir(): continue
        shutil.copy2(f, d/"package"/f.name); n += 1
    if NOTICE: (d/"WHAT-IS-MISSING.md").write_text(
f"""# case-{i} — what this copy does not contain

Deliberately absent, so an audit run here cannot be informed by them:

- `fixtures/` — every case, and the name of the one staged here
- `fixtures/EXPECTED.md` — the answer key
- `runs/` — every previous run and its findings
- `_tools/` — including the script that built this
- `examples.md` — **its rows are real output from real cases**, and three of them quote the
  application files of cases in this very test set, expected verdict attached. An illustration
  drawn from the test set is an answer key wearing a different hat

`package/` holds one application, {n} file(s). **Nothing states which case this is, or whether
anything is wrong with it. It may be fully conformant — a third of the cases are.**

No instructions are given here on purpose. What to do with `package/` is the folder's job to
say, not this page's — see `CLAUDE.md`. If a reader has to be told, that is a finding about
the auditor.
""")
    key[f"case-{i}"] = case
    print(f"  case-{i}  <-  {n} application file(s)")

out = pathlib.Path(os.environ.get("STAGE_KEY_DIR", tempfile.gettempdir()))/"submission-gate-stage-key.json"
out.write_text(json.dumps(key, indent=1))
counter = STAGE/".case-counter"
counter.write_text(str(max([START + len(order) - 1] + [int(k.split("-")[1]) for k in key])))
print(f"\n  {len(order)} case(s) staged, shuffled.")
print(f"  Withheld from each: fixtures/, EXPECTED.md, runs/, _tools/, the fixture README and its name.")
print(f"  Key written outside the repo: {out}")
first, last = START, START + len(order) - 1
print(f"\n  Open _stage/case-{first}/ in a FRESH session and audit package/, then case-{first+1}"
      + (f" … case-{last}" if last > first + 1 else "") + ".\n")
