#!/usr/bin/env python3
"""Remove the loaded standard, leaving the auditor intact.

    python3 _tools/unload.py            # list what would go, change nothing
    python3 _tools/unload.py --yes      # actually remove it

Run it to see the claim this repository makes about itself: that the standard is an input
and the auditor is not built around it. Everything specific to BSC AI Factory Call 3
disappears; identity.md, rules.md, examples.md and every contract stay exactly as they are.

Nothing is lost - this is a git repository, and `git checkout .` puts the standard back.

Then follow reference/LOADING.md to point it at your own rulebook.
"""
import shutil, sys, pathlib

R = pathlib.Path(__file__).resolve().parent.parent
yes = "--yes" in sys.argv

goes, stays = [], []
for p in sorted((R/"reference").iterdir()):
    (stays if p.name in ("CONTEXT.md", "LOADING.md") else goes).append(p)
for p in sorted((R/"fixtures").iterdir()):
    (stays if p.name in ("CONTEXT.md", "_build.py") else goes).append(p)
goes += sorted((R/"runs").glob("*-*.md"))
# The citation checker's test cases quote the loaded standard, so they leave with it.
goes += sorted((R/"_tools"/"tests"/"citations").glob("*.md"))

# Computed, not listed. A hand-maintained list of what survives goes stale the moment a file
# is added, and this script's whole job is to make a claim checkable.
KEEP = sorted(
    str(f.relative_to(R)) for f in R.rglob("*")
    if f.is_file()
    and ".git" not in f.parts and "_stage" not in f.parts
    and not any(g == f or g in f.parents for g in goes)
    and f.name != "examples.md"
    and not f.name.startswith(".DS")
)
STALE = "examples.md"

print("\nREMOVED - everything specific to the standard currently loaded")
print("=" * 62)
for p in goes:
    print(f"  {p.relative_to(R)}")
print(f"\n  {len(goes)} files: the rulebook, its index and provision map, its derived")
print("  requirements, the fixtures and citation tests built against it, and the runs made with it.")

print("\nKEPT - the auditor")
print("=" * 62)
for k in KEEP:
    print(f"  {k}")
print("\n  Not one of these names a funder, a programme or a provision number.")
print("  That is the whole claim, and this script is how you check it.")
print(f"\nSTALE - kept, but belongs to the standard that just left")
print("=" * 62)
print(f"  {STALE}")
print("  Its rows quote real provisions from a real run, so they go out of date with")
print("  the standard. Rewrite them from your own first run - LOADING.md step 8.")

if not yes:
    print("\n  Nothing changed. Re-run with --yes to actually unload.\n")
    sys.exit(0)

for p in goes:
    shutil.rmtree(p) if p.is_dir() else p.unlink()
print(f"\n  Unloaded. {len(goes)} files removed.")
print("  Next: reference/LOADING.md  |  Undo: git checkout .\n")
