---
name: "The Precedent Bench"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Convergence Imperative"
generators:
  - "Accumulate Knowledge"
problem: "A long campaign re-litigates settled decisions every score, or contradicts them silently — because decisions carry no typed force and no supersession record."
signals:
  - "'what have we already decided?' answered by archaeology"
  - "later scores contradicting earlier load-bearing decisions unknowingly"
  - "corrections and overrulings indistinguishable in the record"
config_features:
  - "cadenzas"
  - "instrument: cli"
stages:
  - name: cite-check
    sheets: 1
    instrument_guidance: "instrument: cli — dangling citations rejected before reasoning is paid for"
    fallback_friendly: false
    purpose: "Join the motion's citations against the precedent index."
    artifacts: []
  - name: brief
    sheets: 1
    instrument_guidance: "any — argues follow | distinguish | overrule; receives the live index by required cadenza"
    fallback_friendly: true
    purpose: "Argue the motion; overrule requires named factors."
    artifacts: ["brief.md"]
  - name: bench
    sheets: 1
    instrument_guidance: "ONE named adjudication authority (strong reasoner); advisory seats are Dropped-Axiom-typed inputs, never undisclosed votes"
    fallback_friendly: false
    purpose: "Grant or deny; dicta may be declined without ceremony."
    artifacts: ["ruling.md"]
  - name: enroll
    sheets: 1
    instrument_guidance: "instrument: cli — ONE serialized writer; append holding + supersession edges atomically"
    fallback_friendly: false
    purpose: "The ledger transition: enrolled, or superseded-visibly — never edited."
    artifacts: ["precedent/index.jsonl"]
  - name: notify
    sheets: 1
    instrument_guidance: "instrument: cli — supersession flags across the precedent corpus"
    fallback_friendly: false
    purpose: "Every consumer of an overruled holding learns it moved."
    artifacts: []
dependencies:
  brief: ["cite-check"]
  bench: ["brief"]
  enroll: ["bench"]
  notify: ["enroll"]
composes_with:
  - pattern: "Typed Force"
    how: "its richest form — binding/persuasive force with visible supersession"
  - pattern: "The Errata Ledger"
    how: "contrast — errata correct errors; precedent governs decisions that were right and must yield anyway"
  - pattern: "Fork-Evident History"
    how: "enrollment rides the append-only chain"
---

## The Precedent Bench (Stare Decisis Binding)

`Status: Working` · **Source:** iteration 6 (Expedition 6 — appellate practice, stare decisis, overruling factors). **Scale:** concert-level. **Forces:** Information Asymmetry, Convergence Imperative.

### Core Dynamic

A long campaign accumulates decisions the way a court accumulates cases. Stare decisis resolves the re-litigation tension by giving decisions **typed force**: a decision *necessary to the outcome* of its score (a holding) binds later scores until explicitly overruled; an incidental decision (dictum) persuades and may be declined without ceremony. A score that wants to contradict a holding files a typed motion — **distinguish** (conditions differ in a load-bearing way) or **overrule** (citing reliance, workability, changed circumstances) — and the bench grants or denies. The signature property: **the overruled precedent stays on the books, visibly superseded.** The Errata Ledger corrects errors; only law governs decisions that were correct when made, remain correct as history, and must yield anyway.

The narrowing: one named adjudication authority decides — advisory benches may fan out, but their aggregate arrives as a Dropped Axiom-typed input with a declared rule, never as an undisclosed vote. The typing decision (`necessary_to_outcome`) is judgment by the *emitting* score under the Typed Force law's provenance rule — assigned by a named authority at creation, contestable by motion, never silently re-typed by a gate. Delivery: the live precedent index reaches the *brief* and *bench* sheets by required cadenza keyed to their expanded sheet numbers. Enrollment: one serialized CLI writer appends the holding row and its supersession edges atomically; an overrule without a named factor does not enroll. Registration-time/runtime delivery, stated honestly: spec-corpus fragments inject as they stood at registration; the cadenza injects the live index at runtime — and a score citing precedent that moved between the two is exactly what the cite-join gate catches.

### When to Use / When NOT to Use

Use: long concerts accumulating design decisions with compounding dependencies — architecture campaigns, corpus curation, agent memory governance, platform policy evolution.

Not: short runs (the bench costs more than a fresh decision); decisions that don't constrain later work (no reliance to protect); holdings that cannot be typed mechanically at decision time; overrule motions so cheap the bench is a queue, not a court — **the overrule bar must be higher than the distinguish bar**.

### Marianne Score Structure

```yaml
movements:
  1: { name: cite-check, instrument: cli, instrument_fallbacks: [] }
  2: { name: brief }
  3: { name: bench }
  4: { name: enroll, instrument: cli, instrument_fallbacks: [] }
  5: { name: notify, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 5
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }
  cadenzas:
    2:
      - file: "{{ workspace }}/precedent/INDEX.md"
        as: context
        required: true
    3:
      - file: "{{ workspace }}/precedent/INDEX.md"
        as: context
        required: true
  per_sheet_fallbacks: { 1: [], 4: [], 5: [] }
prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/cite-join.sh" --motions "{{ workspace }}/motions/current.json" \
      --index "{{ workspace }}/precedent/index.jsonl"
    {% elif stage == 2 %}
    Argue the motion: follow | distinguish | overrule. Overrule REQUIRES named factors
    from {reliance, workability, changed-circumstances}. Write {{ workspace }}/brief.md.
    {% elif stage == 3 %}
    You are the adjudication authority. Grant or deny. Write {{ workspace }}/ruling.md
    with force and assigned_by fields.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/enroll.sh" --ruling "{{ workspace }}/ruling.md" \
      --index "{{ workspace }}/precedent/index.jsonl" --atomic
    {% else %}
    bash "{score_dir}/scripts/notify.sh" --supersession-flags "{{ workspace }}/precedent/"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/cite-join.sh --motions {workspace}/motions/current.json --index {workspace}/precedent/index.jsonl'
    condition: "stage == 1"
  - type: content_contains
    path: "{workspace}/ruling.md"
    pattern: "force:"
    condition: "stage == 3"
```

Enroll self-test: an overrule motion lacking a named factor must refuse to enroll; a dangling-citation fixture must die at movement 1, before any reasoning is paid for.

### Example

A refactoring campaign where early scores decided "no new dependencies," "errors at exit 0 are still failing," "unify, never fork." Typed as holdings, they bind later scores until explicitly overruled; a later score wanting a new dependency distinguishes or moves to overrule; the ledger shows the one overrule superseding its predecessor while both remain readable.

### Review Integration

Iteration 6: narrowed per Review 1 ("narrow it to a typed append-only decision registry") and Review 2 (one final adjudication authority; the draft's three-seat bench had no aggregation rule). The cadenza placement fix (index injected into the brief/bench sheets, not the cite-check) is Review 1's. The registration-time vs runtime delivery claim is stated as the two mechanisms they are, per Review 1's demand for an execution trace before claiming more.
