#!/usr/bin/env python3
"""Print what state this auditor is in, by scanning. Nothing here is hand-maintained.

    python3 _tools/status.py

The four steps are the ones in reference/LOADING.md. Each is reported from what exists on
disk, never from a file someone remembered to update.
"""
import re, sys, pathlib, hashlib, datetime

R = pathlib.Path(__file__).resolve().parent.parent
REF, FIX, RUNS, PKG = R/"reference", R/"fixtures", R/"runs", R/"package"
OK, NO, WARN = "[x]", "[ ]", "[!]"

def field(text, name):
    m = re.search(rf"\|\s*\*\*{re.escape(name)}\*\*\s*\|\s*(.+?)\s*\|", text)
    v = m.group(1).strip() if m else ""
    return "" if v.startswith("*(fill") else v

print(f"\nSubmission Gate — status at {datetime.date.today()}\n" + "=" * 58)

# 1 - is a standard loaded
src = (REF/"SOURCES.md").read_text() if (REF/"SOURCES.md").exists() else ""
sections = sorted(REF.glob("[0-9][0-9]-*.md"))
doc, edition, url, read, public = (field(src, k) for k in
                                   ("Document", "Edition", "Retrieved from", "Date read", "Public?"))
loaded = bool(sections and (REF/"INDEX.md").exists() and doc)
print(f"\n1. STANDARD           {OK if loaded else NO}")
if loaded:
    print(f"   {doc}")
    print(f"   edition       {edition}")
    print(f"   retrieved     {read}   {url[:58]}")
    print(f"   public        {public}")
    print(f"   sections      {len(sections)} files")
    pmap = REF/"PROVISIONS.md"
    mapped = len(re.findall(r"^\| `[^`]+` \| `\d\d-", pmap.read_text(), re.M)) if pmap.exists() else 0
    print(f"   provisions    {mapped} mapped in PROVISIONS.md" if mapped else
          f"   {WARN} no PROVISIONS.md - quotes cannot be checked against the provision cited")
    pdf = next(REF.glob("*.pdf"), None)
    if pdf:
        h = hashlib.sha256(pdf.read_bytes()).hexdigest()
        match = h in src
        print(f"   {pdf.name}")
        print(f"   sha-256       {h[:32]}...  {'matches SOURCES.md' if match else 'DOES NOT MATCH SOURCES.md'}")
        if not match:
            print(f"   {WARN} the vendored file is not the one SOURCES.md describes.")
            print(f"       Every finding in runs/ was made against a different document.")
else:
    print("   No standard loaded. The auditor has nothing to enforce.")
    print("   -> reference/LOADING.md")

# 2 - requirements derived
req = (REF/"REQUIREMENTS.md")
ids = sorted(set(re.findall(r"`(R-\d+[a-z]?)`", req.read_text()))) if req.exists() else []
print(f"\n2. REQUIREMENTS       {OK if ids else NO}")
print(f"   {len(ids)} derived: {', '.join(ids)}" if ids else "   Not derived. -> reference/LOADING.md step 5")

# 3 - fixtures
dirs = sorted(d for d in FIX.iterdir() if d.is_dir()) if FIX.exists() else []
conf = [d for d in dirs if d.name.startswith("clean")]
plant = [d for d in dirs if d.name.startswith("broken")]
para = [d for d in dirs if d.name.startswith("paraphrase")]
print(f"\n3. FIXTURES           {OK if dirs else NO}")
if dirs:
    print(f"   {len(dirs)} total - {len(conf)} conformant, {len(plant)} planted, {len(para)} paraphrase")
    if not conf: print(f"   {WARN} no conformant fixture: false positives cannot be detected.")
else:
    print("   None built. -> reference/LOADING.md step 6")

# 4 - runs
fx = sorted(RUNS.glob("fixtures-*.md")) if RUNS.exists() else []
cold = sorted(RUNS.glob("cold-*.md")) if RUNS.exists() else []
print(f"\n4. RUNS               {OK if fx else NO}")
print(f"   fixture runs  {fx[-1].name if fx else 'none - the auditor is untested'}")
print(f"   cold runs     {cold[-1].name if cold else 'none'}")
if dirs and fx and fx[-1].stat().st_mtime < max(d.stat().st_mtime for d in dirs):
    print(f"   {WARN} fixtures changed after the last run. Re-run before trusting it.")

# package - transient, never committed
held = [p for p in PKG.iterdir() if p.name not in ("CONTEXT.md", ".gitkeep")] if PKG.exists() else []
print(f"\n   package/          {len(held)} file(s) awaiting audit" if held else "\n   package/          empty")

# a staged copy older than the auditor would test a version that no longer exists
stage = R/"_stage"
if stage.exists():
    stale = []
    for c in sorted(d for d in stage.iterdir() if d.is_dir()):
        for f in ("CLAUDE.md", "identity.md", "rules.md", "CONTEXT.md"):
            a, b = R/f, c/f
            if b.exists() and a.read_text() != b.read_text():
                stale.append(f"{c.name}/{f}"); break
    cases = [d for d in stage.iterdir() if d.is_dir() and d.name.startswith("case-")]
    print(f"\n   _stage/          {len(cases)} case(s) staged")
    if stale:
        print(f"   {WARN} STALE - the auditor changed after staging: {', '.join(stale)}")
        print(f"       Re-stage before running, or the run tests a version that no longer exists.")

# sync artefacts - Finder/iCloud leave "name 2.md" copies that would ship
dupes = sorted(x for x in R.rglob("* [0-9].*") if ".git" not in x.parts)
if dupes:
    print(f"\n   {WARN} {len(dupes)} duplicate file(s) from a sync conflict - delete before pushing:")
    for d in dupes[:6]:
        print(f"       {d.relative_to(R)}")

ready = loaded and mapped and ids and dirs and fx and not dupes
print("\n" + "=" * 58)
print("READY TO AUDIT" if ready else "NOT READY - see the unchecked steps above")
print()
sys.exit(0 if ready else 1)
