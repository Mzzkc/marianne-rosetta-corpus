---
name: "The Sealed Dissent"
scale: communication
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
  - "Accumulated Signal"
generators:
  - "Exploit Failure as Signal"
problem: "Systems erase rejected candidates, forcing every future chooser to pay full rediscovery price for the reasons the alternatives lost."
signals:
  - "selection stages: fan-out N candidates, fan-in picks one, the N−1 vanish"
  - "self-chains where iteration N must not re-derive what iteration N−1 already rejected"
  - "instrument probing: which backends can do X"
lifetime: "within-run only — the cross-run face is The Negative Ledger, a separate pattern with different lookup semantics"
stages:
  - name: candidates
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each produces one candidate artifact"
    fallback_friendly: true
    purpose: "Generate N candidates with typed ids."
    artifacts: ["candidate-{{ instance_id }}.json"]
  - name: selection
    sheets: 1
    instrument_guidance: "strong reasoner — picks the winner AND writes the ledger"
    fallback_friendly: false
    purpose: "Write rejection-ledger.md: candidate id, validator verdict, one-line reason, evidence path."
    artifacts: ["rejection-ledger.md"]
  - name: consult-gate
    sheets: 1
    instrument_guidance: "instrument: cli — exact-id grep against the ledger, zero AI"
    fallback_friendly: false
    purpose: "Before any later attempt on a rejected candidate id, surface the sealed dissent; non-empty match escalates."
    artifacts: []
dependencies:
  selection: ["candidates"]
  consult-gate: ["selection"]
composes_with:
  - pattern: "The Negative Ledger"
    how: "same discipline, cross-run lifetime and canonical signatures — see that pattern"
  - pattern: "Variant Apparatus"
    how: "the sealed dissent is the record under a synthesis that had to choose"
  - pattern: "Rejoinder Ledger"
    how: "each sealed dissent is a rejoinder recorded, not resolved"
config_features:
  - "fan_out"
  - "instrument: cli"
---

## The Sealed Dissent

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 6 (Talmudic jurisprudence — the minority opinion sealed in the page, *teyku*; negative-results publishing, Bik 2024). Unique divergence: no cousin in the other five expeditions or the prior 111-pattern pool. **Forces:** Partial Failure + Accumulated Signal.

### Core Dynamic

The Talmud does not delete the minority opinion — it seals it in the record, and marks unresolvable disputes *teyku*: "this tension is real and unresolved." The live system needs a decision to proceed, but **the reasons the alternatives lost are load-bearing for every future chooser.** Suppressed null findings become the next lab's sunk cost.

This pattern owns the **within-run lifetime**: exact candidate-id accounting — no prose matching, no signatures, ids the selection sheet itself minted. Matching is trivially reliable: the consult gate greps a candidate id string that cannot collide with prose. (Cross-run fencing needs canonical identity, versioning, and expiry — that is The Negative Ledger.)

### Marianne Score Structure

```yaml
sheets:
  - name: candidates
    instances: 3
    prompt: "Write candidate-{{ instance_id }}.json: {approach_id: 'cand-{{ instance_id }}', design, cost_estimate}."
  - name: selection
    capture_files: ["candidate-*.json"]
    prompt: "Pick the winner. Then append one line per LOSING candidate to rejection-ledger.md: 'REJECTED cand-N | verdict | one-line reason | evidence: candidate-N.json'."
    validations:
      - type: content_contains
        pattern: "REJECTED cand-"
  - name: consult-gate
    instrument: cli
    command: "! grep -E '^REJECTED cand-[0-9]+' rejection-ledger.md | grep -q \"cand-$1\" || (echo 'escalate: sealed dissent on ' \"$1\" && exit 1)"
```

**Negative control:** pre-seed the ledger with `REJECTED cand-2`; a downstream stage parametrized on `cand-2` must be escalated by the consult gate, not run. **Sentinel:** variant with the ledger write removed — the downstream stage runs `cand-2` unimpeded and a final validator fails on the known-rejected id appearing in output.

### When to Use

Selection stages; self-chains where iteration N must not re-derive what iteration N−1 falsified; instrument probing within a run.

### When NOT to Use

Archives growing faster than the decision rate (the page drowns in its own margins); write-only ledgers consulted by ritual but gating nothing.

### Composes With

The Negative Ledger (cross-run face), Variant Apparatus (record under forced choice), Rejoinder Ledger (recorded, not resolved)
