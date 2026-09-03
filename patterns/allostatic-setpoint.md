---
name: Allostatic Setpoint
scale: adaptation
type: orchestration-pattern
status: approximation
forces:
- Accumulated Signal
- Finite Resources
generators:
- Threshold-Triggered Switch
problem: A system holds a fixed quality or throughput target while cumulative wear rises invisibly until performance collapses.
signals:
- meeting the target consumes a degrading reserve
- maintenance debt accumulates across cycles
- the safe target should change with measured wear
stages:
- name: wear-account
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — computes cumulative wear from durable usage evidence
  fallback_friendly: false
  purpose: Write the current reserve and debt.
  artifacts:
  - wear-state.yaml
- name: setpoint
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — selects a bounded target from the wear ladder
  fallback_friendly: false
  purpose: Publish the active setpoint and rationale code.
  artifacts:
  - setpoint.yaml
- name: work
  sheets: 1
  instrument_guidance: opencode — cost-aware execution under the declared target
  fallback_friendly: true
  purpose: Perform only the work admitted by the current reserve.
  artifacts:
  - work-output.md
dependencies:
  setpoint:
  - wear-account
  work:
  - setpoint
composes_with:
- pattern: Hutchinson's Warning
  how: layering — wear moves the target; damped feedback controls movement toward it
---

## Allostatic Setpoint

`Status: Approximation` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A system holds a fixed quality or throughput target while cumulative wear rises invisibly until performance collapses. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Track the cost of maintaining apparent stability, then move the target before the reserve is exhausted. Setpoint changes are monotone within a recovery window and reversible only after measured replenishment.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: wear-account }
  2: { name: setpoint }
  3: { name: work }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce wear-state.yaml with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/wear-state.yaml"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/work-output.md"
    condition: "stage == 3"
```

**Worked example.** A long-running summarization campaign lowers context breadth after repeated compaction debt, then restores it only after two clean low-debt cycles.

### Failure Modes

Wear is inferred from output quality by the same agent whose quality is in question, or the setpoint changes every sample and becomes another oscillator. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Kept as an approximation because the iteration supplied only one strong domain witness. A second independent witness is required before core promotion. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Hutchinson's Warning:** layering — wear moves the target; damped feedback controls movement toward it.
