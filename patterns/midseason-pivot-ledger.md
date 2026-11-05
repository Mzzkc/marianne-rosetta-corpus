---
name: "The Midseason Pivot Ledger"
scale: concert-level
status: approximation
forces: [Information Asymmetry, Progressive Commitment]
generators: [Accumulate Knowledge]
problem: "Campaigns long enough that the plan can be wrong pivot by thrash or by retcon-that-discards; neither reconciles the new frame with completed evidence."
signals:
  - "multi-movement scores, self-chains, concert chains where mid-flight discovery re-shapes later phases"
  - "early discoveries invalidate later decomposition, but completed movements' artifacts are still true"
  - "plans are hypotheses, and the score pretends otherwise"
stages:
  - name: break-arc
    sheets: 1
    instrument_guidance: "strong reasoner — decomposes the goal into ordered beats; writes arc.md + canon-ledger.json (facts as enforceable predicates: typed fact, source artifact digest, weight load-bearing|negotiable)"
    fallback_friendly: false
    purpose: "Planned-arc decomposition with a typed ledger of established facts."
  - name: execute-beat
    sheets: 1
    instrument_guidance: "the workhorse; each beat completes with its facts appended to the canon ledger"
    fallback_friendly: true
    purpose: "Accumulate canon; every fact digest-anchored."
  - name: pivot-review
    sheets: 1
    instrument_guidance: "strong reasoner from a DIFFERENT family than break-arc (the self-dealing rule); scheduled between movements — reads arc + canon + recent beats; either confirms (pivot-continue.marker — the logged absence, a typed draw) or writes pivot.md citing every load-bearing fact it preserves and marking any it reinterprets"
    fallback_friendly: false
    purpose: "The scheduled, non-emergency recontextualization."
  - name: continuity-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — verifies pivot.md contradicts no load-bearing fact (facts are predicates, so contradiction is computable, not vibes); contradiction or missing citation → exit 1"
    fallback_friendly: false
    purpose: "The hard gate between pivot and splice."
  - name: re-break-remaining
    sheets: 1
    instrument_guidance: "CONCERT-LEVEL by construction: generates the next movement's score file with the new arc spliced in; completed beats' artifacts re-cited with original digests, never re-run"
    fallback_friendly: false
    purpose: "Retcon, not deletion — reinterpretation with continuity accounting."
dependencies:
  execute-beat: [break-arc]
  pivot-review: [execute-beat]
  continuity-check: [pivot-review]
  re-break-remaining: [continuity-check]
composes_with:
  - pattern: "Season Bible"
    how: "bible carries context; ledger carries constraints with weights"
  - pattern: "Continuity Ledger"
    how: "nearest permanent neighbor (the Newcomer's catch) — Continuity Ledger owns the typed serialized assertion boundary among parallel authors; this owns revision-under-canon across campaign phases; compose the ledger INTO the pivot machinery"
  - pattern: "The Graded Ladder"
    how: "pivot-on-failure composes as the top rung's destination"
  - pattern: "Fork-Evident History"
    how: "versioned arc files (arc.v1.md, arc.v2.md)"
  - pattern: "The Change-Order Ledger"
    how: "nearest engineering kin, fold-refused — the change order executes an authorized delta; the pivot executes an interpretation under canon constraints; distinct data model and checker"
type: orchestration-pattern
---

## The Midseason Pivot Ledger

**Status:** approximation — **concert-level, reframed per the Practitioner's kill of the single-score form:** a running score cannot splice a new arc into its own DAG; the splice is a new score file generated at the pivot boundary and launched through the concert chain or self-chaining. The emergency `on_fail → goto` form stays flagged native-unproven (shared with the Graded Ladder and Transfer of Command — one proof services three patterns).

**Core Dynamic.** Every writers' room knows episodes air in order, feedback arrives mid-season, and long series pivot: a character intended for three episodes becomes the center. The instrument is the **board plus the arc ledger**; a pivot does not discard aired episodes, it **retcons** — reconciles the new frame with everything already on screen, the ledger tracking which established facts are load-bearing (cannot be contradicted) versus negotiable. Retcon is not deletion; it is reinterpretation with continuity accounting — and the accounting is what distinguishes a disciplined pivot from thrash. The iteration-scale face (the folded Kishōtenketsu reframe): a scheduled, non-emergency recontextualization cycle where the reframe sheet has authority to re-scope but **not** to invalidate, and the no-reframe outcome is a valid, logged terminal (C8).

**The Skeptic's two repairs, applied:** canon facts are **enforceable predicates**, not prose — each fact is a typed, checker-computable statement (schema-valid, digest-anchored, referentially complete), so the continuity check is a real join, not a vibe; and citation percentage was never continuity — the check is contradiction-freedom over load-bearing predicates plus complete citation, nothing looser. **The Newcomer's neighbor debt, paid:** Continuity Ledger (`patterns/continuity-ledger.md`) is named and composed — it owns the assertion boundary this pattern's canon ledger instantiates.

**Sentinel.** Plant a pivot.md that silently contradicts one load-bearing fact → continuity-check exits 1, `continuity-report.json` carries `"violations": [{"fact_digest": …, "type": "contradicted"}]`. **Anti-orphan validation:** `file_sha256` over the pre-pivot artifact set proves completed beats unchanged post-pivot — a pivot that orphans completed evidence is thrash wearing continuity's clothes, caught by digest.

**Example.** 20-sheet regulatory-compliance campaign: movements 1–3 map data flows; movement 4 discovers an entire unlogged pipeline, invalidating movements 5–20's decomposition. The pivot ledger re-breaks 5–20 around the discovery; movements 1–3's artifacts become canon facts (load-bearing, digest-anchored) cited by the new plan rather than re-executed at 3× cost.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
