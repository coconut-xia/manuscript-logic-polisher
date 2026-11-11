#!/usr/bin/env python3
"""Read-only lexical audit; a clean report is NOT semantic consistency approval."""
from __future__ import annotations
import argparse
from bisect import bisect_right
import fnmatch
import json
from pathlib import Path
import re
import sys

def escaped(s, i):
    n = 0
    i -= 1
    while i >= 0 and s[i] == "\\":
        n += 1
        i -= 1
    return n % 2 == 1

def blank(chars, a, b):
    for i in range(a, min(b, len(chars))):
        if chars[i] not in "\r\n":
            chars[i] = " "

def space(s, i):
    while i < len(s) and s[i].isspace():
        i += 1
    return i

def end_arg(s, i, left="{", right="}"):
    if i >= len(s) or s[i] != left:
        return i
    depth = 0
    for j in range(i, len(s)):
        if escaped(s, j):
            continue
        if s[j] == left:
            depth += 1
        elif s[j] == right:
            depth -= 1
            if depth == 0:
                return j + 1
    return i

def options(s, i):
    i = space(s, i)
    while i < len(s) and s[i] == "[":
        j = end_arg(s, i, "[", "]")
        if j == i:
            break
        i = space(s, j)
    return i

def mask_tex(s):
    chars = list(s)
    for m in re.finditer("%", s):
        if not escaped(s, m.start()):
            e = s.find("\n", m.start())
            blank(chars, m.start(), len(s) if e < 0 else e)
    s = "".join(chars)
    for m in re.finditer(r"\\begin\{(verbatim\*?|lstlisting|minted|tikzpicture|thebibliography)\}.*?\\end\{\1\}", s, re.S):
        blank(chars, m.start(), m.end())
    for m in re.finditer(r"\\verb\*?([^\w\s]).*?\1", s):
        blank(chars, m.start(), m.end())
    s = "".join(chars)
    # Keep preamble titles/abstracts; hide macro bodies rather than all preamble text.
    for m in re.finditer(r"\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|DeclareMathOperator|newenvironment|renewenvironment|newcolumntype)\*?", s):
        i = space(s, m.end())
        if i < len(s) and s[i] == "{":
            i = end_arg(s, i)
        else:
            target = re.match(r"\\[A-Za-z@]+", s[i:])
            i += len(target.group()) if target else 0
        i = options(s, i)
        e = end_arg(s, i)
        if e > i:
            if "environment" in m.group():
                j = space(s, e)
                e = max(e, end_arg(s, j))
            blank(chars, m.start(), e)
    for m in re.finditer(r"\\(?:gdef|edef|xdef|def)\s*\\[A-Za-z@]+", s):
        i = s.find("{", m.end())
        if i >= 0:
            e = end_arg(s, i)
            if e > i:
                blank(chars, m.start(), e)
    for m in re.finditer(r"\\let\s*\\[A-Za-z@]+\s*=?\s*(?:\\[A-Za-z@]+|[^\s])", s):
        blank(chars, m.start(), m.end())
    s = "".join(chars)
    for pat in [r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}", r"\\\[.*?\\\]", r"\\\(.*?\\\)", r"(?<!\\)\$\$.*?(?<!\\)\$\$", r"(?<!\\)\$(?!\$).*?(?<!\\)\$"]:
        for m in re.finditer(pat, s, re.S):
            blank(chars, m.start(), m.end())
    s = "".join(chars)
    names = "label ref eqref autoref pageref cref Cref vref Vref nocite cite citep citet citealt citealp citeauthor citeyear bibitem url path input include includegraphics graphicspath bibliography bibliographystyle externaldocument documentclass usepackage RequirePackage hypersetup captionsetup color textcolor newlength href hyperlink hypertarget begin end".split()
    hidden = dict.fromkeys(names, 1)
    hidden.update(dict.fromkeys("PassOptionsToPackage setlength addtolength setcounter addtocounter multicolumn multirow".split(), 2))
    hidden["definecolor"] = 3
    for m in re.finditer(r"\\([A-Za-z@]+)\*?", s):
        name = m.group(1)
        if name == "hyperref":
            blank(chars, m.start(), options(s, m.end()))
            continue
        if name not in hidden:
            continue
        e = options(s, m.end())
        for _ in range(hidden[name]):
            i = space(s, e)
            j = end_arg(s, i)
            if j == i:
                break
            e = j
        blank(chars, m.start(), e)
    s = "".join(chars)
    for m in re.finditer(r"\\[A-Za-z@]+\*?", s):
        blank(chars, m.start(), m.end())
    return "".join(chars).replace("~", " ")

def mask_markdown(s):
    chars = list(s)
    fence, start, offset = None, 0, 0
    pat = re.compile(r"^[ \t]{0,3}(" + chr(96) + r"{3,}|~{3,})([^\r\n]*)")
    for line in s.splitlines(keepends=True):
        m = pat.match(line)
        if m:
            token, rest = m.groups()
            if fence is None:
                fence, start = (token[0], len(token)), offset
            elif token[0] == fence[0] and len(token) >= fence[1] and not rest.strip():
                blank(chars, start, offset + len(line))
                fence = None
        offset += len(line)
    if fence:
        blank(chars, start, len(s))
    for pat in [r"<!--.*?-->", r"(?<=\])\([^)\n]*\)", r"(?m)^[ \t]*\[[^\]\n]+\]:[^\n]*", r"https?://[^\s<>]+"]:
        for m in re.finditer(pat, s, re.S):
            blank(chars, m.start(), m.end())
    return "".join(chars)

def pattern(form, sensitive=True):
    body = r"\s+".join(re.escape(p) for p in form.split())
    return re.compile(r"(?<!\w)" + body + r"(?!\w)", 0 if sensitive else re.I)

def validate(x):
    if not isinstance(x, dict) or x.get("version") != 1:
        raise ValueError("ledger must be an object with version: 1")
    terms, checks = x.get("terms", []), x.get("concept_checks", [])
    if not isinstance(terms, list) or not isinstance(checks, list):
        raise ValueError("terms and concept_checks must be arrays")
    ids = set()
    for t in terms:
        if not isinstance(t, dict):
            raise ValueError("each term must be an object")
        for k in ("id", "canonical"):
            if not isinstance(t.get(k), str) or not t[k].strip():
                raise ValueError(f"each term needs a non-empty {k}")
        if t["id"] in ids:
            raise ValueError(f"duplicate id: {t['id']}")
        ids.add(t["id"])
        if not isinstance(t.get("case_sensitive", True), bool):
            raise ValueError("case_sensitive must be true or false")
        a, ws = t.get("allowed_forms", []), t.get("watch_forms", [])
        if not isinstance(a, list) or any(not isinstance(f, str) or not f.strip() for f in a):
            raise ValueError("allowed_forms must contain non-empty strings")
        if not isinstance(ws, list):
            raise ValueError("watch_forms must be an array")
        for w in ws:
            f = w if isinstance(w, str) else w.get("form") if isinstance(w, dict) else None
            if not isinstance(f, str) or not f.strip():
                raise ValueError("each watch form must be a string or object with form")
            if isinstance(w, dict) and any(k in w and not isinstance(w[k], str) for k in ("suggestion", "reason")):
                raise ValueError("watch suggestion and reason must be strings")
        scope = t.get("scope", {})
        if not isinstance(scope, dict) or any(k not in ("files", "exclude_files") for k in scope):
            raise ValueError("scope supports files and exclude_files only")
        if any(not isinstance(v, list) or any(not isinstance(g, str) for g in v) for v in scope.values()):
            raise ValueError("scope values must be arrays of globs")
    if any(not isinstance(c, dict) for c in checks):
        raise ValueError("concept_checks must contain objects for manual review")
    return x

def in_scope(path, t):
    parts = path.as_posix().split("/")
    choices = [path.name] + ["/".join(parts[i:]) for i in range(len(parts))]
    match = lambda pats: any(fnmatch.fnmatchcase(s, p) for s in choices for p in pats)
    scope = t.get("scope", {})
    return match(scope.get("files", ["*"])) and not match(scope.get("exclude_files", []))

def audit(path, rules):
    raw = path.read_text(encoding="utf-8-sig")
    s = mask_tex(raw) if path.suffix.lower() == ".tex" else mask_markdown(raw) if path.suffix.lower() == ".md" else raw
    starts = [0] + [m.end() for m in re.finditer("\n", raw)]
    found = []
    for t in rules:
        if not in_scope(path, t):
            continue
        protected = [m.span() for f in [t["canonical"]] + t.get("allowed_forms", []) for m in pattern(f).finditer(s)]
        for w in t.get("watch_forms", []):
            w = {"form": w} if isinstance(w, str) else w
            for m in pattern(w["form"], t.get("case_sensitive", True)).finditer(s):
                if any(a <= m.start() and m.end() <= b for a, b in protected):
                    continue
                line = bisect_right(starts, m.start()) - 1
                e = raw.find("\n", starts[line])
                text = raw[starts[line]:len(raw) if e < 0 else e]
                col = m.start() - starts[line]
                left = max(0, col - 60)
                found.append({"file": str(path), "line": line + 1, "column": col + 1,
                    "term_id": t["id"], "canonical": t["canonical"],
                    "matched_text": raw[m.start():m.end()], "suggestion": w.get("suggestion", t["canonical"]),
                    "reason": w.get("reason", "Review this variant against the paper's established terminology."),
                    "snippet": text[left:left + 220]})
    return sorted(found, key=lambda f: (f["line"], f["column"], f["term_id"]))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger", type=Path, required=True)
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.add_argument("--fail-on-match", action="store_true")
    p.add_argument("files", nargs="+", type=Path)
    args = p.parse_args()
    try:
        ledger = validate(json.loads(args.ledger.read_text(encoding="utf-8-sig")))
        if any(f.suffix.lower() not in (".tex", ".md", ".txt") for f in args.files):
            raise ValueError("unsupported source format; use UTF-8 tex/md/txt or extracted text")
        findings = [item for f in args.files for item in audit(f, ledger.get("terms", []))]
    except (OSError, UnicodeError, ValueError, re.error) as e:
        p.error(str(e))
    out = {"status": "lexical_findings" if findings else "no_configured_variants_found",
        "source_files": [str(f) for f in args.files],
        "configured_term_rules": len(ledger.get("terms", [])), "findings": findings,
        "semantic_consistency": "not_checked", "manual_review_required": ledger.get("concept_checks", []),
        "limitations": [
            "Lexical diagnostic only. No matches do not establish semantic or cross-document consistency.",
            "Custom macros, included files, mathematical symbols and scientific definitions require manual review.",
            "Sources were read only; no replacements or formatting changes were made."]}
    if not out["configured_term_rules"]:
        out["limitations"].append("No active term rules were configured.")
    if args.format == "json":
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"Lexical status: {out['status']} ({len(findings)} findings)")
        for f in findings:
            print(f"{f['file']}:{f['line']}:{f['column']} [{f['term_id']}] {f['matched_text']!r} -> review {f['suggestion']!r}; {f['reason']}")
        print("Semantic consistency: NOT CHECKED; definitions, metrics, symbols and cross-document roles require manual review.")
        for c in out["manual_review_required"]:
            print("MANUAL REVIEW: " + json.dumps(c, ensure_ascii=False))
        for note in out["limitations"]:
            print("NOTE: " + note)
    return 1 if args.fail_on_match and findings else 0

if __name__ == "__main__":
    sys.exit(main())
