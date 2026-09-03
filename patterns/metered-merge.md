---
name: Metered Merge
scale: adaptation
type: orchestration-pattern
status: approximation
forces:
- Finite Resources
- Convergence Imperative
generators:
- Measure Convergence Character
problem: A fixed merge admission rate either starves available capacity or overloads the consumer when measured congestion changes with delay.
signals:
- a queue feeds a bounded merge or review consumer
- occupancy can be measured periodically
- admission rate can change between leased batches
stages:
- name: measure
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — reads queue occupancy and prior admitted rate
  fallback_friendly: false
  purpose: Write the current congestion sample.
  artifacts:
  - merge-meter.json
- name: steer
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — evaluates the clamped ALINEA equation and spill override
  fallback_friendly: false
  purpose: Publish the next leased admission count.
  artifacts:
  - admission-lease.yaml
- name: merge
  sheets: 1
  instrument_guidance: codex-cli — processes no more than the leased count
  fallback_friendly: true
  purpose: Consume the admitted batch and record actuals.
  artifacts:
  - merge-results.json
- name: settle
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — appends actual throughput for the next cycle
  fallback_friendly: false
  purpose: Close the feedback loop.
  artifacts:
  - merge-history.jsonl
dependencies:
  steer:
  - measure
  merge:
  - steer
  settle:
  - merge
composes_with:
- pattern: Hutchinson's Warning
  how: substitution — both damp lagged feedback, but this controls admission flow while Hutchinson controls budget-driven degradation
---

## Metered Merge

`Status: Approximation` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A fixed merge admission rate either starves available capacity or overloads the consumer when measured congestion changes with delay. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

At each lease boundary compute `admit = clamp(k + gain × (target − measured), min, max)`. A queue-spill threshold overrides normal steering to the safe minimum. If the sensor is absent or stale, degrade to a logged pretimed rate rather than improvising.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: measure }
  2: { name: steer }
  3: { name: merge }
  4: { name: settle }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce merge-meter.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/merge-meter.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/merge-history.jsonl"
    condition: "stage == 4"
```

**Worked example.** A review queue targets 20 waiting items. With k=8, gain=0.25, and measured=32, the next batch admits 5. When occupancy exceeds the spill threshold, admission drops to 1 until the next clean sample.

### Failure Modes

Gain is too high for the sampling delay, the controller reacts to instantaneous noise, or missing telemetry is treated as zero congestion. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Review 2 reversed the attempted absorption into Hutchinson's Warning because the ALINEA equation and queue-spill behavior are constitutive. It remains archived and approximate because leased batch admission is not concurrent runtime backpressure. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Hutchinson's Warning:** substitution — both damp lagged feedback, but this controls admission flow while Hutchinson controls budget-driven degradation.
