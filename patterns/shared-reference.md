---
name: "The Shared Reference"
scale: communication
status: working
forces: [Information Asymmetry, Producer-Consumer Mismatch]
generators: [Contract at Interfaces]
problem: "N independent workers must agree on terms without converging on content, and pairwise coordination is O(N²) chatter."
signals:
  - "wide fan-outs whose outputs must agree on terminology, schema, or phase without agreeing on content"
  - "stragglers from an earlier regime would otherwise merge silently with current-regime work"
  - "mixed instruments need cheap interoperability across a fan-out"
stages:
  - name: establish
    sheets: 1
    instrument_guidance: "strong reasoner — builds the minimal shared reference (glossary, schema set, phase descriptor)"
    fallback_friendly: true
    purpose: "Write reference.yaml (profile: datum) or pulse.v{k}.yaml (profile: pulse) plus its sha256."
  - name: verify-reference
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — schema check, closed-traverse consistency, digest pin"
    fallback_friendly: false
    purpose: "Verify the reference before anyone works from it; a separate sheet because the check must not live in skip_when (V1)."
  - name: work
    sheets: fan_out(N)
    instrument_guidance: "any instruments per the work; outputs cite reference entry IDs and the version/bar they performed against"
    fallback_friendly: true
    purpose: "Ornament the reference; never re-derive it."
  - name: merge
    sheets: 1
    instrument_guidance: "any-wrapped CLI — checks every input's cited version/bar before reconciling"
    fallback_friendly: false
    purpose: "Admit current-regime work; quarantine stragglers as data, never merge them."
dependencies:
  verify-reference: [establish]
  work: [verify-reference]
  merge: [work]
composes_with:
  - pattern: "The Misclosure Ledger"
    how: "closure arithmetic vs the shared reference that makes closure cheap"
  - pattern: "Serial Troponin"
    how: "the bar counter is the serial test transposed from time to space-of-work"
  - pattern: "Prefabrication"
    how: "the reference is the contract-first fan-out's shared contract page"
  - pattern: "Delphi Convergence"
    how: "the pulse is Delphi's missing metronome — which round are we in"
type: orchestration-pattern
---

## The Shared Reference (Datum Grid ⊕ Shared Pulse, folded)

**Status:** working · primitives-proven. **The fold (the Newcomer's cut):** the draft carried Datum Grid and Shared Pulse as fold-refused siblings at ~70% isomorphism — small shared reference artifact, typed citations, straggler detection at fan-in — with the entire refusal resting on one paragraph of failure semantics. Folded, each profile must pick exactly one semantics, which dissolves the draft's merge/quarantine contradiction (the draft's Core Dynamic quarantined cross-bar inputs while its Example merged them "under their old bar"; a newcomer implements whichever sentence they read second).

**Core Dynamic.** Everyone syncs to a shared reference instead of pairwise to each other: one edge per worker to the reference, zero worker-to-worker — O(1) per worker, O(N) total, never O(N²) chatter. The reference is cheaper and slower than the parts, which is exactly what makes high-rate local work safe. Two profiles with **different failure semantics — choose one per score, never both in one artifact**:

- **Datum (immutable):** pre-verified, digest-pinned, never mutated. Workers cite entries by ID; a worker that re-derives instead of citing is drift, caught cheaply. Swap the datum without re-pinning and all N workers fail loudly at launch — which is the point: tampering must be loud.
- **Pulse (monotone-versioned):** a stable, low-update-rate position artifact (`section`, monotone `bar`, decisions-of-record IDs, `version`), updated only at section boundaries, by its single owner (a CLI pulse-keeper with `per_sheet_fallbacks: []`). The clave change — a rare, typed, versioned rewrite — re-keys all downstream interpretation at once. New version = new file (`pulse.v2.yaml`); the old file persists, so in-flight stragglers are *admitted under their cited version and flagged for re-derivation* (merge-as-flagged), while inputs citing a version that never existed or a corrupted current file are *quarantined* (never merged). This is the profile split the fold forced, stated as typed transitions with timestamps — no ambiguity survives.

**Marianne Score Structure.** Four stages as in frontmatter. Datum profile: workers' first validation is a digest check against the pinned reference, outputs cite ≥1 datum entry ID (`content_regex`), merge runs a normalization-diff (jq) against cited entries. Pulse profile: `field_match` of each ornament's cited `bar`/`version` against the pulse; monotonicity check on `bar`. **Sentinels:** datum — swap `reference.yaml` without re-pinning → all N workers' digest checks fail, N failure receipts; pulse — inject an ornament citing a nonexistent version → quarantined as straggler data with a row in `stragglers.csv`, other inputs still merge, exit code reflects quarantine, not crash.

**Example.** 12-language localization fan-out (datum): the locked terminology glossary is the reference; 12 workers on 12 instrument profiles never exchange a message and still agree on every term; a swapped glossary fails all 12 at once, visibly. Quarter-long compliance-audit concert (pulse): the pulse holds the current regulation-snapshot id and phase; mid-quarter the snapshot is re-versioned; in-flight ornaments merge under their cited old version and are flagged for re-derivation instead of silently mixing regimes.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
