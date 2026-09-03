---
name: Firing the Pass
scale: score-level
type: orchestration-pattern
status: working
forces:
- Finite Resources
- Progressive Commitment
generators:
- Gate on Environmental Readiness
problem: Forward scheduling discovers too late that prerequisite work cannot fit before a fixed release instant.
signals:
- the terminal date is fixed
- stage durations have credible upper bounds
- late work has explicit cut or degrade options
stages:
- name: backward-plan
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — computes latest-start times from the fixed hard date
  fallback_friendly: false
  purpose: Write the reverse schedule and slack for every stage.
  artifacts:
  - backward-plan.yaml
- name: fire-and-monitor
  sheets: 1
  instrument_guidance: codex-cli — executes due work while checking current slack
  fallback_friendly: true
  purpose: Start at latest-safe cues and surface negative slack immediately.
  artifacts:
  - schedule-state.jsonl
dependencies:
  fire-and-monitor:
  - backward-plan
composes_with:
- pattern: Graceful Retreat
  how: layering — negative slack selects a predeclared lower-completeness tier
- pattern: Standby–GO
  how: prerequisite — the calculated cue feeds the arm/fire boundary
---

## Firing the Pass

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Forward scheduling discovers too late that prerequisite work cannot fit before a fixed release instant. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Anchor the terminal event, subtract worst-case durations and handoff margins backward, then execute against latest-start cues. The schedule never invents offset-from-artifact runtime support; a deterministic planner writes ordinary dated inputs for score execution.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: backward-plan }
  2: { name: fire-and-monitor }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce backward-plan.yaml with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/backward-plan.yaml"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/schedule-state.jsonl"
    condition: "stage == 2"
```

**Worked example.** A report must publish Friday 17:00. Validation needs two hours and synthesis four; the plan fires synthesis by 11:00 and cuts optional appendices when slack turns negative.

### Failure Modes

Durations are optimistic point estimates or the controller tries to catch up by compressing every later gate. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

This archived form resurrects The Aboyeur under a clearer name. It is buildable as deadline-first planning, not as a missing start-time scheduler primitive. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Graceful Retreat:** layering — negative slack selects a predeclared lower-completeness tier.
- **Standby–GO:** prerequisite — the calculated cue feeds the arm/fire boundary.
