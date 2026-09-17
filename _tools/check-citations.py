#!/usr/bin/env python3
"""Verify that every provision a run quotes appears VERBATIM, under the provision it is cited to.

    python3 _tools/check-citations.py runs/cold-2026-09-11.md
    python3 _tools/check-citations.py --all        # every ledger in runs/, plus examples.md
    python3 _tools/test-citations.py               # proves the checks below actually fire

Exit 0 if every citation resolves, 1 if any does not, 2 if the provision map itself is broken.

rules.md § 1 says a provision may only be cited after re-reading it. That is a rule written in
markdown, which makes it a request. This makes it a constraint.

rules.md § 2 anchors every row twice: the provision number, and the sentence quoted from it.
Both halves are checked. A quote must be a real substring of the standard AND sit inside the span
reference/PROVISIONS.md gives for the provision it is cited to. Until 2026-09-17 only the first
half was checked: the quote was searched across the whole of reference/, so a row citing
§ II Art. 3(3) or § II Art. 3(9) for text from Art. 3(4) passed. The judges of Clief Notes
Competition 12 found that.

A citation fails, and says why, when:
  - the cited provision is not in the map    (a number that does not exist, one never mapped,
                                              or a label that is not a printed number at all)
  - the quote is not in the cited span, but is somewhere else in the standard  (prints where)
  - the quote is not in the standard at all  (altered, tidied, or invented)
  - a quote has no provision number in front of it

Comparison is on whitespace-normalised text, with the declared page markers [pN] removed,
because the standard was extracted from a PDF and its line breaks fall where the page put them.
Everything else - wording, spelling, punctuation, curly or straight apostrophes - must match
exactly. The source prints "ELEGIBLE"; a run that tidies it up fails here, which is the point.

Only the verbatim section files are authority. REQUIREMENTS.md is derived and cannot vouch for
a quote. PROVISIONS.md says where a provision's text lives; it does not hold any text itself.

This script names no funder and no provision. Everything specific to the standard comes from
reference/PROVISIONS.md.
"""
import re, sys, pathlib

R = pathlib.Path(__file__).resolve().parent.parent
REF = R/"reference"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def body(text):
    """A section file as the checker reads it: no provenance comment, no # title, no [pN]."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = "\n".join(l for l in text.split("\n") if not l.startswith("# "))
    return norm(re.sub(r"\[p\d+\]", " ", text))


class MapError(Exception):
    pass


def load_map(ref=REF):
    """reference/PROVISIONS.md -> {provision: [(file, start, end)]} and the section texts."""
    sections = {p.name: body(p.read_text()) for p in sorted(ref.glob("[0-9][0-9]-*.md"))}
    if not sections:
        raise MapError("No standard loaded in reference/ - nothing to check against.")
    src = ref/"PROVISIONS.md"
    if not src.exists():
        raise MapError("reference/PROVISIONS.md is missing. Without it a quote cannot be checked "
                       "against the provision it is cited to - reference/LOADING.md, step 4.")
    spans, errors = {}, []
    tick = lambda cell: cell.strip().strip("`").strip()
    for n, line in enumerate(src.read_text().split("\n"), 1):
        cells = line.split("|")[1:-1]
        if len(cells) != 4 or not cells[0].strip().startswith("`"):
            continue
        prov, fname, frm, upto = (tick(c) for c in cells)
        where = f"PROVISIONS.md line {n} ({prov})"
        if fname not in sections:
            errors.append(f"{where}: no section file named {fname}"); continue
        text, f = sections[fname], norm(frm)
        count = text.count(f)
        if count != 1:
            errors.append(f"{where}: From text {frm!r} appears {count} times in {fname}, "
                          "must appear exactly once"); continue
        a = text.index(f)
        if upto == "end":
            b = len(text)
        else:
            b = text.find(norm(upto), a + len(f))
            if b < 0:
                errors.append(f"{where}: Up to text {upto!r} not found after From in {fname}"); continue
        spans.setdefault(prov, []).append((fname, a, b))
    if not spans and not errors:
        errors.append("PROVISIONS.md has no rows")
    if errors:
        raise MapError("reference/PROVISIONS.md is broken - fix the map before trusting any result:\n"
                       + "\n".join(f"  {e}" for e in errors))
    return spans, sections


def printed_to_short(s):
    """Read a citation written the way a standard prints it as the map's short form.

    "SECTION II, Article 3, criterion 5 (Sector Priority)" -> "§ II Art. 3(5) (Sector Priority)"
    "SECTION III, Article 6, 6.1"                           -> "§ III Art. 6.1"

    rules.md asks for the number "as printed on the standard" and fixes no notation, so both
    forms are correct. Until 2026-09-17 only the short one was accepted, and blind case 12, which
    wrote the long one with every quote in the right place, failed 13 of 14 citations. Only the
    words change here; the numbers are kept, so a criterion or clause that does not exist still
    fails.
    """
    s = re.sub(r"\bSECTION\s+([IVXLC]+)\b", r"§ \1", s)
    s = re.sub(r"\bArticle\s+(\d)", r"Art. \1", s)
    s = re.sub(r"(§ [IVXLC]+),\s*(Art\.)", r"\1 \2", s)
    s = re.sub(r"\bArt\. (\d+),\s*\1\.(\d+)", r"Art. \1.\2", s)       # Article 6, 6.1 -> Art. 6.1
    s = re.sub(r"\bArt\. (\d+(?:\.\d+)?),\s*(?:criterion|point|paragraph)\s+(\w+)", r"Art. \1(\2)", s)
    return s


def provision_in(segment, keys):
    """The provision a stretch of text names, or why it names none.

    Returns (key, None) on a match, (None, label) for anything that reads as a label but is not
    a mapped provision, and (None, None) when the segment holds no words at all.
    The longest key wins. A key followed by more numbering - "(9)", ".10", "0" - is a different,
    unmapped provision, never the shorter one: § II Art. 3(9) is not § II Art. 3.
    Words that are not a key - "Preamble to Art. 3" - are a label the map cannot confirm. They
    fail rather than silently inherit the provision before them, which would report the quote
    as cited to something the run never wrote.
    """
    s = printed_to_short(norm(segment.replace("*", "").replace("`", "")))
    best = None
    for k in keys:
        i = s.find(k)
        while i >= 0:
            if best is None or len(k) > len(best[0]) or (len(k) == len(best[0]) and i < best[1]):
                best = (k, i)
            i = s.find(k, i + 1)
    if best:
        k, i = best
        rest = s[i + len(k):]
        if re.match(r"\(|\.?\d", rest):
            more = re.match(r"[\w().]*", rest).group(0).rstrip(".")
            return None, f"{k}{more}"
        return k, None
    label = s.strip(" :;,.—–-")
    return (None, label) if re.search(r"[^\W\d_]", label) else (None, None)


# Lines that claim to be a provision citation, with any continuation lines that are not a new
# bullet or a code fence. Both ledger shapes seen in real runs are accepted:
#   - Provision:  § II Art. 3(4) — "The company must have fewer than 20 employees."
#   - **Provision:** § II Art. 3(4) — *"The company must have fewer than 20 employees."*
BLOCK = re.compile(r"^.*\*{0,2}Provision:?\*{0,2}.*(?:\n(?!\s*[-*]\s|\s*```).*)*$", re.M)
# A quote may be plain ("...") or emphasised (*"..."* / _"..."_), and the dash before it may be an
# em dash or a hyphen. Runs are written by a model, not a formatter.
QUOTE = re.compile(r'[—–-]\s*[*_]{0,2}"(.+?)"[*_]{0,2}', re.S)


def citations(text):
    """Yield (provision_key_or_None, reason_or_None, quote) for every quoted provision."""
    for block in BLOCK.findall(text):
        block = block.split("Provision", 1)[1]
        prev, pos = None, 0
        for m in QUOTE.finditer(block):
            key, bad = provision_in(block[pos:m.start()], KEYS)
            if key:
                prev = key
            elif bad:
                prev = None
                yield None, f"cites \"{bad}\", which is not a provision in reference/PROVISIONS.md", m.group(1)
                pos = m.end(); continue
            if prev is None:
                yield None, "quote has no provision number in front of it", m.group(1)
            else:
                yield prev, None, m.group(1)
            pos = m.end()


def where_it_lives(nq):
    """Every mapped provision whose span holds the quote, most specific first."""
    hits = [(b - a, prov) for prov, spans in SPANS.items()
            for f, a, b in spans if nq in SECTIONS[f][a:b]]
    return [p for _, p in sorted(hits)]


def check(key, reason, quote):
    nq = norm(quote)
    short = f"\"{nq[:46]}...\"" if len(nq) > 46 else f"\"{nq}\""
    if reason:
        found = where_it_lives(nq)
        extra = f"\n        the quote is in {found[0]}" if found else ""
        return False, f"  FAIL  {reason}{extra}\n        {short}"
    if any(nq in SECTIONS[f][a:b] for f, a, b in SPANS[key]):
        return True, f"  ok    {key:24s} {short}"
    found = where_it_lives(nq)
    if found:
        return False, (f"  FAIL  cited to {key}, but the quote is not in it\n"
                       f"        it is in {found[0]}\n        {short}")
    loose = [f for f, t in SECTIONS.items() if nq in t]
    if loose:
        return False, (f"  FAIL  cited to {key}; the quote is in {loose[0]} but under no mapped "
                       f"provision\n        {short}")
    close = [f for f, t in SECTIONS.items() if nq[:28] in t]
    hint = f"\n        opens like text in {close[0]} - altered after that point?" if close else ""
    return False, f"  FAIL  cited to {key}; not found anywhere in the standard{hint}\n        \"{nq[:60]}\""


def resolve_target(a):
    for cand in (pathlib.Path(a), R/a, pathlib.Path.cwd()/a):
        if cand.exists():
            return cand.resolve()
    return pathlib.Path(a)


if __name__ == "__main__":
    # --reference DIR checks against another copy of the standard. Used by test-citations.py to
    # prove a broken map is refused; an audit never needs it.
    ref = REF
    if "--reference" in sys.argv:
        i = sys.argv.index("--reference")
        ref = pathlib.Path(sys.argv[i + 1]).resolve()
        del sys.argv[i:i + 2]
    try:
        SPANS, SECTIONS = load_map(ref)
    except MapError as e:
        print(e); sys.exit(2)
    KEYS = sorted(SPANS, key=len, reverse=True)

    if "--all" in sys.argv:
        targets = sorted((R/"runs").glob("*-*.md")) + [R/"examples.md"]
    else:
        targets = [resolve_target(a) for a in sys.argv[1:] if not a.startswith("--")]
    if not targets:
        sys.exit("Usage: check-citations.py <run.md> | --all")

    bad = total = 0
    for t in targets:
        if not t.exists():
            print(f"  MISSING  {t}"); bad += 1; continue
        found = list(citations(t.read_text()))
        rt = t.resolve()
        label = rt.relative_to(R) if R in rt.parents else rt.name
        print(f"\n{label}  -  {len(found)} citation(s)")
        for key, reason, quote in found:
            total += 1
            ok, line = check(key, reason, quote)
            bad += not ok
            print(line)

    print(f"\n{'=' * 58}\n{total} citation(s) checked, {bad} unresolved")
    if bad:
        print("A run with an unresolved citation is not evidence. Fix the run, not this check.\n")
    sys.exit(1 if bad else 0)
