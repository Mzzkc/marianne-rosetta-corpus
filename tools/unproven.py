#!/usr/bin/env python3
"""List the corpus patterns no proof score names, so the prove loop can
reach past the familiar seven (GH #354).

Usage: unproven.py [CORPUS_DIR] [--json] [--check PATTERN_NAME]

A pattern counts as proven when a file under proof-scores/ names it as
PRIMARY PATTERN in its header. It counts as composed-in when any proof
header names it at all. --check exits 1 when PATTERN_NAME is already a
primary of some proof (the selection gate), 0 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def pattern_names(corpus: Path) -> dict[str, str]:
    names: dict[str, str] = {}
    for path in sorted((corpus / "patterns").glob("*.md")):
        head = path.read_text(errors="replace")[:400]
        m = re.search(r'^name:\s*"?([^"\n]+)"?', head, re.M)
        if m:
            names[path.stem] = m.group(1).strip()
    return names


def proof_headers(corpus: Path) -> dict[str, str]:
    return {
        path.stem: path.read_text(errors="replace")[:8000]
        for path in sorted((corpus / "proof-scores").glob("*.yaml"))
    }


def classify(corpus: Path) -> dict[str, dict[str, list[str]]]:
    names = pattern_names(corpus)
    heads = proof_headers(corpus)
    primary: dict[str, list[str]] = {}
    composed: dict[str, list[str]] = {}
    for proof, head in heads.items():
        m = re.search(r"PRIMARY PATTERN\s*:\s*([^\n]+)", head)
        primary_line = m.group(1) if m else ""
        for slug, name in names.items():
            if re.search(re.escape(name), head, re.I):
                composed.setdefault(slug, []).append(proof)
                if re.search(re.escape(name), primary_line, re.I):
                    primary.setdefault(slug, []).append(proof)
    return {
        "primary": primary,
        "composed": {k: v for k, v in composed.items() if k not in primary},
        "unproven": {k: [] for k in names if k not in composed},
        "names": {k: [v] for k, v in names.items()},
    }


def main() -> int:
    args = sys.argv[1:]
    as_json = "--json" in args
    check = None
    if "--check" in args:
        i = args.index("--check")
        check = args[i + 1].strip().lower()
        del args[i:i + 2]
    args = [a for a in args if a != "--json"]
    corpus = Path(args[0]) if args else Path(__file__).resolve().parents[1]
    result = classify(corpus)
    if check is not None:
        for slug, proofs in result["primary"].items():
            name = result["names"][slug][0].lower()
            if check in (slug, name) or check == name.removeprefix("the "):
                print(f"ALREADY PROVEN as primary by: {', '.join(proofs)}")
                return 1
        print("not yet a primary of any proof")
        return 0
    if as_json:
        json.dump(result, sys.stdout, indent=1, sort_keys=True)
        print()
        return 0
    names = result["names"]
    print(f"# Proof ledger ({len(names)} patterns, {len(proof_headers(corpus))} proof scores)\n")
    print(f"## Proven as PRIMARY ({len(result['primary'])}) — do not re-prove\n")
    for slug, proofs in sorted(result["primary"].items()):
        print(f"- {names[slug][0]} — {', '.join(proofs)}")
    print(f"\n## Composed into a proof but never primary ({len(result['composed'])})\n")
    for slug in sorted(result["composed"]):
        print(f"- {names[slug][0]}")
    print(f"\n## Never named by any proof ({len(result['unproven'])}) — reach here first\n")
    for slug in sorted(result["unproven"]):
        print(f"- {names[slug][0]} (patterns/{slug}.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
