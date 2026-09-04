#!/usr/bin/env python3
"""Deterministic primitives-coverage audit for the Rosetta corpus.

Compares a ground-truth inventory (sheet 1 of primitives-audit.yaml)
against the corpus's extracted claims (sheet 2) and emits a gap report.

Design contract (matches the corpus's own thesis: judgment upstream,
arithmetic downstream):
  - The INVENTORY carries each primitive's canonical name plus `aliases`
    (the judgment: how humans and the corpus word that primitive).
  - This script only matches: normalized token-boundary containment in
    either direction between claim text and name/aliases.
  - Outcomes per inventory primitive: MATCHED / MISSING.
    Per claim: mapped-to-existing / FABRICATED (mapped to a primitive the
    inventory does not carry) / UNRESOLVED (sheet 2 could not map it).
  - Exit code is always 0 unless the inputs are unreadable or malformed —
    findings are the deliverable, not an error.

Usage:
    audit_primitives.py <inventory.yaml> <claims.yaml> [> report.md]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

MIN_PRIMITIVES = 30
MIN_CLAIMS = 50


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def token_contains(haystack: str, needle: str) -> bool:
    """True if needle's normalized form appears in haystack on token boundaries."""
    h = normalize(haystack)
    n = normalize(needle)
    if not h or not n:
        return False
    if f" {n} " in f" {h} ":
        return True
    return h == n


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    inv_path, claims_path = Path(argv[1]), Path(argv[2])
    try:
        inventory = yaml.safe_load(inv_path.read_text(encoding="utf-8"))
        claims_doc = yaml.safe_load(claims_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report, don't traceback
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        return 2

    primitives = inventory.get("primitives") or []
    claims = claims_doc.get("claims") or []
    if len(primitives) < MIN_PRIMITIVES:
        print(f"INPUT ERROR: inventory carries only {len(primitives)} primitives", file=sys.stderr)
        return 2
    if len(claims) < MIN_CLAIMS:
        print(f"INPUT ERROR: claims file carries only {len(claims)} claims", file=sys.stderr)
        return 2

    inv_names = {p.get("name", ""): p for p in primitives}

    # --- claims -> inventory resolution -------------------------------
    matched_claims: dict[str, list[str]] = {}
    fabricated: list[tuple[str, str]] = []
    unresolved: list[str] = []
    for c in claims:
        claim_text = str(c.get("claim", ""))
        mapped = c.get("mapped_primitive")
        sources = c.get("where") or []
        src = ", ".join(str(s) for s in sources) if sources else "unlocated"
        if mapped is None:
            unresolved.append(f"{claim_text}  [{src}]")
            continue
        mapped = str(mapped)
        if mapped not in inv_names:
            fabricated.append((claim_text, mapped))
            continue
        matched_claims.setdefault(mapped, []).append(f"{claim_text}  [{src}]")

    # --- inventory -> claims coverage ---------------------------------
    missing: list[dict] = []
    for name, p in inv_names.items():
        aliases = [name] + [str(a) for a in (p.get("aliases") or [])]
        hit = None
        # 1) explicit mapping by sheet 2
        if name in matched_claims:
            hit = "mapped"
        else:
            # 2) alias containment against every claim text
            for c in claims:
                text = str(c.get("claim", ""))
                if any(token_contains(text, a) for a in aliases):
                    hit = "alias"
                    matched_claims.setdefault(name, []).append(
                        f"{text}  [alias-match, {', '.join(str(s) for s in (c.get('where') or ['unlocated']))}]"
                    )
                    break
        if hit is None:
            missing.append(
                {
                    "name": name,
                    "kind": p.get("kind", "?"),
                    "aliases": p.get("aliases") or [],
                    "refs": p.get("source_refs") or [],
                }
            )

    # --- report --------------------------------------------------------
    n_missing, n_fab, n_unres = len(missing), len(fabricated), len(unresolved)
    lines = [
        "# Primitives Coverage Audit — ground truth vs corpus claims",
        "",
        f"- Inventory: {inv_path} ({len(primitives)} primitives)",
        f"- Claims: {claims_path} ({len(claims)} claims)",
        "",
        "## MISSING — primitive exists in Marianne, corpus never claims it",
        "",
    ]
    if missing:
        for m in missing:
            lines.append(
                f"- **{m['name']}** ({m['kind']}) — aliases: "
                f"{', '.join(map(str, m['aliases'])) or 'none'}; refs: "
                f"{', '.join(map(str, m['refs'])) or 'none'}"
            )
    else:
        lines.append("- none")
    lines += [
        "",
        "## FABRICATED — corpus claims a primitive the inventory does not carry",
        "",
    ]
    if fabricated:
        for text, mapped in fabricated:
            lines.append(f"- **{text}** -> mapped to `{mapped}` (not in inventory)")
    else:
        lines.append("- none")
    lines += ["", "## UNRESOLVED — claims sheet 2 could not map (conductor judgment)", ""]
    if unresolved:
        lines.extend(f"- {u}" for u in unresolved)
    else:
        lines.append("- none")
    lines += [
        "",
        "## Matched (for traceability)",
        "",
    ]
    for name in sorted(matched_claims):
        lines.append(f"- `{name}`:")
        lines.extend(f"    - {c}" for c in matched_claims[name][:5])
        if len(matched_claims[name]) > 5:
            lines.append(f"    - … {len(matched_claims[name]) - 5} more")
    lines += [
        "",
        "---",
        f"FINDINGS: {n_missing + n_fab + n_unres} "
        f"(missing={n_missing} fabricated={n_fab} unresolved={n_unres})",
        "AUDIT COMPLETE",
        "",
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
