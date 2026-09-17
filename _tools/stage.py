#!/usr/bin/env python3
"""Stage one or more fixtures for a BLIND audit.

    python3 _tools/stage.py                                  # list the cases
    python3 _tools/stage.py broken-04-sector clean-03-minimal ...

Builds case-1/, case-2/ ... each holding the auditor, the standard, and one case's application
files copied into package/. They are built OUTSIDE this repository, in ~/submission-gate-stage/
(or $SUBMISSION_GATE_STAGE). The cases are SHUFFLED, so the order you typed them
tells the reader nothing.

Why this exists. A fixture folder is named broken-07-non-eu and contains a README naming the
planted violation and the expected verdict. An auditor pointed at that folder is not finding
anything; it is being told. Instructing a session not to read the README is a request. This is
the constraint: nothing in a staged case contains EXPECTED.md, runs/, _tools/, examples.md, the
fixture's README, or its name.

Why outside the repository. A session reads every CLAUDE.md in the folders above the one it is
opened in. Until 2026-09-17 cases were staged in _stage/ inside this repository, so cases 1-11
also loaded this repository's own CLAUDE.md - which routes to fixtures/ and EXPECTED.md - and the
instruction files of every folder above it. They were never as blind as runs/ says. This script
now refuses any location with a CLAUDE.md or AGENTS.md above it.

examples.md is withheld for a reason worth stating: its rows are genuine output from genuine
cases, which is what makes them worth shipping — and which also means they quote the very
packages being tested here. Real examples and a blind test set pull against each other, and
the test wins.

The mapping from case-N back to the fixture is written OUTSIDE the repository, so it cannot be
reached from a session working in a staged case.
"""
import shutil, sys, pathlib, random, json, os, tempfile

R = pathlib.Path(__file__).resolve().parent.parent
FIX = R/"fixtures"
STAGE = pathlib.Path(os.environ.get("SUBMISSION_GATE_STAGE") or pathlib.Path.home()/"submission-gate-stage").resolve()
cases = sorted(d.name for d in FIX.iterdir() if d.is_dir())

args = [a for a in sys.argv[1:] if not a.startswith("--")]
NOTICE = "--no-notice" not in sys.argv      # omit WHAT-IS-MISSING.md entirely
KEEP   = "--keep" in sys.argv               # do not wipe cases already staged
# Case numbers are never reused. A session transcript is stored by its folder path, so a
# second case-1 writes into the same history as the first and the two become impossible to
# tell apart later. Default to continuing past the highest number ever staged.
# The old in-repo counter is read too, so numbering carries on past case 11 rather than restarting.
_counters = [STAGE/".case-counter", R/"_stage"/".case-counter"]
_hi = max([int(c.read_text().strip()) for c in _counters if c.exists()] or [0])
START  = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--start=")), _hi + 1)
if not args:
    print("\nCases:\n")
    for c in cases: print(f"  {c}")
    print("\n  python3 _tools/stage.py <case> [<case> ...]\n")
    sys.exit(0)

unknown = [a for a in args if a not in cases]
if unknown: sys.exit(f"No such case(s): {', '.join(unknown)}")

# A blind case must inherit no instructions. Any CLAUDE.md or AGENTS.md above it would be read.
if R == STAGE or R in STAGE.parents:
    sys.exit(f"REFUSED - {STAGE} is inside this repository, whose CLAUDE.md routes to the answer key.")
inherited = [p/n for p in STAGE.parents for n in ("CLAUDE.md", "AGENTS.md") if (p/n).exists()]
if inherited:
    sys.exit("REFUSED - a session opened under " + str(STAGE) + " would also read:\n  "
             + "\n  ".join(map(str, inherited))
             + "\nSet SUBMISSION_GATE_STAGE to a folder with no instruction files above it.")

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
        for f in held: print(f"  {f}")
        print("""
These are the only copy of what those runs found. Collect them into runs/ first.

  cp <stage>/case-*/runs/*.md runs/        (then rename, they are all called the same thing)

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
print(f"\n  Open {STAGE}/case-{first}/ in a FRESH session and audit package/, then case-{first+1}"
      + (f" … case-{last}" if last > first + 1 else "") + ".\n")
