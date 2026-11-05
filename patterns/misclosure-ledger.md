---
name: "The Misclosure Ledger"
scale: within-stage
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Structured Disagreement"
generators:
  - "Verify through Diverse Observers"
problem: "N parallel measurements of an additive quantity disagree within tolerance, and the system either fights over which is right or averages the disagreement away, when the residual is a quantity belonging to the whole system that should be measured, published, and allocated."
signals:
  - "N independent estimates of the same quantity with declared per-measurer weights"
  - "a fan-in tempted to average, vote, or argue"
  - "the disagreement budget can be declared in advance"
scope_fence: "additive quantities with a real closure constraint only — free-standing estimates belong to One Field, Many Cores or Delphi Convergence"
stages:
  - name: measure
    sheets: "fan_out(3)"
    instrument_guidance: "per_sheet_instruments across vendor families; stagger launches so correlated measurers don't stampede one vendor"
    fallback_friendly: true
    purpose: "Same brief, independent scalar estimates."
    artifacts: ["estimate-{{ instance_id }}.json"]
  - name: close
    sheets: 1
    instrument_guidance: "instrument: cli — no LLM allocates its own errors; computes residual, compares to tolerance, allocates by declared weights"
    fallback_friendly: false
    purpose: "Write corrections-{n}.json and the published misclosure ledger, or raise the blunder flag."
    artifacts: ["misclosure.md", "corrections.json"]
  - name: settle
    sheets: 1
    instrument_guidance: "instrument: cli — emits the adjusted record"
    fallback_friendly: false
    purpose: "Write adj-consensus.json; every sheet id present (no silent drops)."
    artifacts: ["adj-consensus.json"]
dependencies:
  close: ["measure"]
  settle: ["close"]
composes_with:
  - pattern: "Concurrent Count"
    how: "a second CLI recomputes the residual — the published ledger cannot lie"
  - pattern: "Condorcet's Premise"
    how: "family-probe the panel when weights cannot be justified by track record"
  - pattern: "The Dropped Axiom"
    how: "the allocation table IS the declared aggregation function — typed, not concealed"
config_features:
  - "fan_out"
  - "per_sheet_instruments"
  - "instrument: cli"
---

## The Misclosure Ledger

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 2 (geodetic traverse adjustment — 300 years of surveying practice; Bowditch/least-squares); the brief named it "the deepest unclaimed structure in the whole audit." Narrowed per adversarial review to additive closed systems. **Force:** Structured Disagreement.

### Core Dynamic

Close a loop around a field and the endpoint does not land on the startpoint. The misclosure is not a scandal — it is the **sum of all the small honest errors**, and classical practice measures it, publishes it, and **allocates it back to the legs by declared weight**. Fan-in as bookkeeping, not voting: no judge, no quorum, an allocation table with weights declared before the loop was walked.

The blunder/tolerance split is the second spine: within tolerance, distribute; beyond tolerance, quarantine the outlier leg and re-measure — never spread a blunder across honest legs.

**Scope fence (review-driven):** misclosure exists because measurements participate in a known algebraic closure constraint. Independent estimates do not owe a conserved sum, and "allocating residual back" across free-standing estimates manufactures agreement. Use this pattern for component estimates that must sum to a declared total (effort hours across phases, cost across line items, coverage across partitions); each dimension closes against its own declared total, weighted independently. The weight ledger is a named committed artifact (`tolerance.yaml`: weights, tolerance, closure total) authored before measurement; weight retuning writes dated amendments — an auditable trail.

### Marianne Score Structure

```yaml
sheets:
  - name: measure
    instances: 3
    prompt: "Estimate the migration effort in hours for phase P-{{ instance_id }} ONLY. Write estimate-{{ instance_id }}.json {hours: N}."
    response_format: { type: json_object }
  - name: close
    instrument: cli
    instrument_fallbacks: []
    command: "python3 scripts/close_loop.py estimates/ tolerance.yaml --out corrections.json --ledger misclosure.md"
    validations:
      - type: command_succeeds
      - type: content_contains
        path: "misclosure.md"
        pattern: "published-misclosure:"
  - name: settle
    instrument: cli
    command: "python3 scripts/settle.py corrections.json --out adj-consensus.json && jq -e '(.total | length) >= 3' adj-consensus.json"
    validations:
      - type: command_succeeds
```

`close_loop.py` publishes the recomputed residual and fails if the ledger's stated misclosure disagrees with the recomputed one — the ledger cannot lie.

**Negative control:** inject one estimate off by 10× tolerance — the closer must exit non-zero and write `blunder-flag.txt` naming the outlier leg; allocation must NOT occur.

### When to Use

N parallel sheets measured the same additive territory with different instruments and disagree within a declared tolerance; weights declarable before measurement.

### When NOT to Use

Misclosure beyond tolerance (that is a blunder — allocation is exactly wrong); no honest tolerance declarable; fewer than three independent measurements; free-standing (non-closed) estimates — use a different fan-in pattern.

### Composes With

Concurrent Count (recomputed residual), Condorcet's Premise (panel probing), The Dropped Axiom (declared aggregation)
