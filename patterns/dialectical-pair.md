---
name: "The Dialectical Pair"
scale: within-stage
status: approximation
forces: [Structured Disagreement, Convergence Imperative]
generators: [Frame Multiplication]
problem: "Two-agent debate collapses into position-holding by silence unless engagement is mechanically checkable and the stalemate is a typed terminal."
signals:
  - "risk concentrates in one contested judgment where a single reviewer's blind spot is the danger"
  - "a full jury is overkill but one voice is not enough"
  - "unstructured debate has ended in 'we agree to disagree' with no record of what was contested"
stages:
  - name: thesis-r1
    sheets: 1
    instrument_guidance: "strong reasoner, family A — opens with typed CLAIMs, one per file moves/r1-a.json"
    fallback_friendly: true
    purpose: "State the thesis in checkable parts."
  - name: antithesis-r1
    sheets: 1
    instrument_guidance: "strong reasoner, family B (Independence Law) — OBJECTION or CONCESSION per claim, one per file moves/r1-b.json"
    fallback_friendly: true
    purpose: "Engage every claim; silence is illegal."
  - name: thesis-r2 / antithesis-r2 / thesis-r3 / antithesis-r3
    sheets: 1 each
    instrument_guidance: "alternating, strict dependency order — ANSWER/COUNTER must cite the objection's move id"
    fallback_friendly: true
    purpose: "Bounded exchange; max 3 rounds is structural, not tunable."
  - name: close
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes the engagement join over moves/*, emits the typed terminal"
    fallback_friendly: false
    purpose: "RESOLVED-for-A / RESOLVED-for-B / TEYKU with open objections preserved."
dependencies:
  antithesis-r1: [thesis-r1]
  thesis-r2: [antithesis-r1]
  close: [antithesis-r3]
composes_with:
  - pattern: "Rejoinder Ledger"
    how: "its bijection applied mid-debate rather than post-review"
  - pattern: "Rashomon Gate"
    how: "the pair is the binary case with engagement rules Rashomon lacks"
  - pattern: "The Editor's Disposition"
    how: "a TEYKU is the strongest possible advisory input — a typed stalemate with a transcript"
  - pattern: "The Sealed Dissent"
    how: "the non-engaging sibling"
type: orchestration-pattern
---

## The Dialectical Pair

**Status:** approximation — typed moves via `response_format` are native-unproven (V5 schema-validated per attempt, zero end-to-end executions; this and the Editor's Disposition are the tied minimal exercises). **Repair applied (the Practitioner's):** the pattern is now explicitly an **unrolled static DAG of 7 sheets** — not a span loop; alternating two instrument families inside one looped block is Jinja gymnastics nobody should attempt, and the pattern says so.

**Core Dynamic.** Two agents, opposite theses, one artifact, a **closed move vocabulary**: CLAIM, OBJECTION (must cite the claim span), ANSWER (must cite the objection), CONCESSION (withdraw, recorded), COUNTER. Every OBJECTION must receive ANSWER, CONCESSION, or COUNTER before the round ends — *silence is illegal*, and because moves are typed artifacts, engagement is mechanically checkable: the closer computes a join (the Rejoinder Ledger's bijection mid-debate). The typed terminal **TEYKU** — the admitted draw, recorded with open objections — is a first-class outcome 1,500 years old that the corpus's success/fail vocabulary lacked (C8, the Typed-Draw Law). More than ~2.5 viable positions means a pair compresses a 4-way question into false binarity — promote to Rashomon. Empirical questions are not debated; the Etiquette Law runs the test.

**Concurrency repair (the Skeptic's):** no shared append-only transcript — each move is its **own file** (`moves/{round}-{side}.json`), written by exactly one sheet in strict dependency order; the DAG supplies the serialization; the join is computed by the closer over the directory. **Sentinel repair (the Newcomer's):** the sentinel runs on a **hand-crafted fixture transcript** — a `moves/` directory with a deliberate orphan claim — never on a live debate; model behavior cannot be seeded deterministically, and a live-behavior sentinel would be flaky on arrival. `moves-lint.py` exits 1 with `{"orphan_claims": ["c-3"], "rule": "every claim must be engaged"}` — catching position-holding-by-silence, which unstructured debate lets pass.

**Example.** Security-severity debate: A argues "critical, exploitable pre-auth," B argues "low, requires local access." Three rounds of typed moves; two claims survive all objections, one stands contested → TEYKU recorded with the contested claim exposed. The CVE triage proceeds on resolved claims; the contested one goes to a human with the transcript.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
