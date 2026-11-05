---
name: "Admission by First Cycle"
scale: concert-level
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Progressive Commitment"
  - "Exponential Defect Cost"
generators:
  - "Incremental Exposure"
problem: "A fleet bets repetition on a member after one instance — and one validated instance proves only that one instance passed, unless the instance ran at full strength and the proof is fresh."
signals:
  - "fleet groups consume one another's outputs — corpus pipelines, data platforms, release trains"
  - "fleet-growth moments: this is how a new score earns its seat"
  - "members with decaying prerequisites where 'worked last week' is a claim, not evidence"
stages:
  - name: proving-cycle
    sheets: "fleet group"
    instrument_guidance: "each member score runs its REAL validations — a first cycle with gates removed is the fleet-level luck-passing content_regex"
    fallback_friendly: false
    purpose: "One full validated cycle per member, per member's own validation set."
    artifacts: ["receipts/"]
  - name: admission-gate
    sheets: 1
    instrument_guidance: "instrument: cli — fail-closed jq over the receipt ledger; every member present, every receipt recording the FULL validation set, every timestamp inside the staleness bound"
    fallback_friendly: false
    purpose: "Consume evidence of completion (receipts), not merely the conductor's group transition."
    artifacts: []
  - name: production
    sheets: "fleet group"
    instrument_guidance: "the working groups; depends_on proving"
    fallback_friendly: true
    purpose: "The admitted cohort runs the recurring work."
    artifacts: []
dependencies:
  admission-gate: ["proving-cycle"]
  production: ["admission-gate"]
composes_with:
  - pattern: "Capability Census"
    how: "census = CAN RUN; first cycle = DOES RUN, validated — compose both before admitting"
  - pattern: "Sign-Off Chain Against the Hard Date"
    how: "the receipt is a sign-off against a specific obligation, with a TTL"
  - pattern: "The Validity Window"
    how: "receipt TTL — a first-cycle receipt from last week is evidence about last week"
config_features:
  - "fleet groups + depends_on (UNPROVEN — zero proof-score exercise)"
  - "instrument: cli (fail-closed admission)"
---

## Admission by First Cycle

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 4 (OFRP phase ordering — basic before integrated before sustainment). Split from the Readiness Cycle (refit → solo-prove → joint-exercise → standing-watch), which moved to candidates owing its own proof. **Forces:** Progressive Commitment + Exponential Defect Cost.

### Core Dynamic

The engine already encodes the theorem — fleet groups with `depends_on` wait for named groups' first cycle — the pattern is the discipline that makes the wait meaningful. Three clauses: the proving group's first cycle runs under the member's *real* validations, never degraded ones; admission consumes *evidence* (receipts recording the full validation set), not merely the conductor's transition; **the proof ages** — admission carries a staleness bound. The deep structure is induction's: one validated instance establishes the member *can* complete; the fleet bets repetition on it — sound only if the instance was validated at full strength, because integration multiplies any single member's defect across every other member.

Receipts are **engine-authored**: written by the member score's terminal CLI act with its validation set recorded — never self-reported prose. Gate direction: admission gates are **fail-closed validations**; `skip_when` is reserved for repair-path routing where fail-open toward repair is intended (the fail-open-on-timeout behavior is on the citation-owing list — verify before relying on it).

### Marianne Score Structure

```yaml
fleet:
  groups:
    - name: proving
      members: [ingest-a, ingest-b, ingest-c]     # each runs its own full validations
    - name: production
      members: [model, publish]
      depends_on: [proving]
# The admission gate (first sheet of the production group's entry):
  - name: admission-gate
    instrument: cli
    command: "python3 scripts/admit.py receipts/ roster.jsonl --require-validation-set full --staleness 7d"
    validations:
      - type: command_succeeds
```

**Negative controls:** (a) a variant with one proving member's validations removed — the admission gate must reject its receipt (validation-set field mismatch); (b) a receipt older than the staleness bound must be rejected — freshness is load-bearing, not decorative.

### When to Use

Fleets where groups consume one another's outputs; fleet-growth moments; members with decaying prerequisites.

### When NOT to Use

Genuinely independent groups (the dependency serializes for nothing); first cycles expensive relative to the work; weakened first-cycle validations ("first-cycle-lite" is the failure mode, and the gate must check the receipt records the full validation set).

### Composes With

Capability Census (can-run vs. does-run), Sign-Off Chain Against the Hard Date (receipt as sign-off), The Validity Window (receipt TTL)
