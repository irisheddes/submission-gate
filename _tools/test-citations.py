#!/usr/bin/env python3
"""Prove that check-citations.py fails what it should fail and passes what it should pass.

    python3 _tools/test-citations.py

Exit 0 only if every case behaves as its file says it must.

A checker nobody has watched fail is not known to work. Each file in _tools/tests/citations/
opens with the exit code it must produce and the phrases its output must contain - so a case
that fails for the wrong reason also fails the test. Then the map itself is broken on purpose,
in a throwaway copy of reference/, to prove the checker refuses to run on a bad map rather than
quietly passing citations against it.

These cases quote the standard currently loaded. They belong to it, like fixtures/, and must be
rewritten when the standard changes - reference/LOADING.md, step 6.
"""
import re, sys, shutil, pathlib, subprocess, tempfile

R = pathlib.Path(__file__).resolve().parent.parent
CHECK = R/"_tools"/"check-citations.py"
CASES = sorted((R/"_tools"/"tests"/"citations").glob("*.md"))


def run(*args):
    p = subprocess.run([sys.executable, str(CHECK), *map(str, args)], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


failed = 0
def verdict(name, ok, why=""):
    global failed
    failed += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{'' if ok else '  -  ' + why}")


print("\nCitation cases")
for case in CASES:
    head = re.search(r"<!--\s*expect:(.*?)-->", case.read_text(), re.S)
    if not head:
        verdict(case.name, False, "no <!-- expect: --> line"); continue
    want_exit = int(re.search(r"exit (\d)", head.group(1)).group(1))
    phrases = [p.replace('\\"', '"') for p in re.findall(r'"((?:[^"\\]|\\.)*)"', head.group(1))]
    code, out = run(case)
    missing = [p for p in phrases if p not in out]
    verdict(case.name, code == want_exit and not missing,
            f"exit {code}, expected {want_exit}" if code != want_exit else f"output lacks {missing}")
    if code != want_exit or missing:
        print("\n".join("        | " + l for l in out.strip().split("\n")))

print("\nA broken map must be refused (exit 2), never trusted")
sample = next(c for c in CASES if c.name.startswith("pass-"))
breakages = {
    "From text that is not in the file":
        lambda t: t.replace("`4.Company Size` |", "`4. Company Size` |", 1),
    "From text that appears twice":
        lambda t: t.replace("`1.Legal Status` |", "`must` |", 1),
    "a section file that does not exist":
        lambda t: t.replace("`02-mandatory-elegible-criteria.md` | `5.Sector",
                            "`02-mandatory-eligible-criteria.md` | `5.Sector", 1),
    "Up to text that never follows From":
        lambda t: t.replace("| `5.Sector Priority` | `6.In-person Availability` |",
                            "| `5.Sector Priority` | `1.Legal Status` |", 1),
}
for name, breakit in breakages.items():
    with tempfile.TemporaryDirectory() as tmp:
        ref = pathlib.Path(tmp)/"reference"
        shutil.copytree(R/"reference", ref)
        mp = ref/"PROVISIONS.md"
        before = mp.read_text(); mp.write_text(breakit(before))
        if mp.read_text() == before:
            verdict(name, False, "the breakage did not apply - the map changed, update this test"); continue
        code, out = run("--reference", ref, sample)
        verdict(name, code == 2 and "PROVISIONS.md is broken" in out, f"exit {code}")

print(f"\n{'=' * 58}")
print(f"{len(CASES) + len(breakages)} test(s), {failed} failed")
sys.exit(1 if failed else 0)
