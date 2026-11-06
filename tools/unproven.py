#!/usr/bin/env python3
"""List the corpus patterns no proof score names, so the prove loop can
reach past the familiar seven (GH #354).

Usage: unproven.py [CORPUS_DIR] [--json] [--check PATTERN_NAME] [--usage [DIR]]

A pattern counts as proven when a file under proof-scores/ names it as
PRIMARY PATTERN in its header. It counts as composed-in when any proof
header names it at all. --check exits 1 when PATTERN_NAME is already a
primary of some proof (the selection gate), 0 otherwise.

--usage counts YAML compositions citing each canonical pattern name, once per
file (case-insensitive literal matching). By default it scans the repository's
scores/ tree except this corpus's proof-scores/. An explicit DIR scans all YAML
there, including proofs if requested. Counts measure citations, not execution
or successful adoption; an uncited pattern may still have been used.
"""

from __future__ import annotations

import argparse
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


def usage_counts(corpus: Path, root: Path, *, exclude_proofs: bool) -> dict[str, int]:
    """Count citing files, keeping proof evidence separate from ordinary usage."""
    names = pattern_names(corpus)
    counts = dict.fromkeys(names, 0)
    matchers = [(slug, re.compile(re.escape(name), re.I)) for slug, name in names.items()]
    proofs = (corpus / "proof-scores").resolve()
    for path in sorted(root.rglob("*.yaml")):
        if exclude_proofs and path.resolve().is_relative_to(proofs):
            continue
        text = path.read_text(errors="replace")
        for slug, matcher in matchers:
            if matcher.search(text):
                counts[slug] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check")
    mode.add_argument("--usage", nargs="?", const="", metavar="DIR")
    args = parser.parse_args()
    corpus = args.corpus
    if not (corpus / "patterns").is_dir():
        parser.error(f"corpus patterns directory does not exist: {corpus / 'patterns'}")
    if args.usage is not None:
        root = Path(args.usage) if args.usage else corpus.resolve().parent
        if not root.is_dir():
            parser.error(f"usage directory does not exist: {root}")
        names = pattern_names(corpus)
        counts = usage_counts(corpus, root, exclude_proofs=not args.usage)
        if args.json:
            json.dump(counts, sys.stdout, indent=1, sort_keys=True)
            print()
        else:
            print("# Usage citations (compositions naming a pattern, not proven executions)")
            print("\n## Most-cited\n")
            for slug in sorted(counts, key=lambda slug: (-counts[slug], slug)):
                if counts[slug]:
                    print(f"- {names[slug]}: {counts[slug]}")
            print("\n## Never-cited in usage\n")
            for slug, count in counts.items():
                if not count:
                    print(f"- {names[slug]} (patterns/{slug}.md)")
        return 0
    check = args.check.strip().lower() if args.check else None
    result = classify(corpus)
    if check is not None:
        for slug, proofs in result["primary"].items():
            name = result["names"][slug][0].lower()
            if check in (slug, name) or check == name.removeprefix("the "):
                print(f"ALREADY PROVEN as primary by: {', '.join(proofs)}")
                return 1
        print("not yet a primary of any proof")
        return 0
    if args.json:
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
