---
name: Globally-Typed Choreography
scale: score-level
type: orchestration-pattern
status: working
forces:
- Producer-Consumer Mismatch
- Exponential Defect Cost
generators:
- Contract at Interfaces
problem: Every local handoff looks plausible while the rendered score graph contains an unmet need, type mismatch, or dependency deadlock.
signals:
- many stages exchange typed artifacts
- local validation passes but integration stalls
- the rendered DAG is available before execution
stages:
- name: render
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — renders JobConfig and emits the expanded DAG
  fallback_friendly: false
  purpose: Materialize every producer, consumer, and dependency.
  artifacts:
  - rendered-graph.json
- name: typecheck
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — performs offer/need unification and cycle checks
  fallback_friendly: false
  purpose: Reject unmet needs, incompatible offers, and deadlocks before dispatch.
  artifacts:
  - choreography-verdict.json
- name: execute
  sheets: 1
  instrument_guidance: codex-cli — runs only the admitted graph
  fallback_friendly: true
  purpose: Perform the typed choreography.
  artifacts:
  - execution-output.md
dependencies:
  typecheck:
  - render
  execute:
  - typecheck
composes_with:
- pattern: Proof-Carrying Artifact
  how: layering — evidence sidecars become declared offer types
- pattern: Behavioral Pre-Mortem
  how: prerequisite — supplies the typed graph its counterexample search consumes
---

## Globally-Typed Choreography

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Every local handoff looks plausible while the rendered score graph contains an unmet need, type mismatch, or dependency deadlock. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Render first, then typecheck the whole graph: each need must have one reachable compatible offer, ordering must respect production, and no wait cycle may remain. Deadlock is a validation error, not a runtime mystery.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: render }
  2: { name: typecheck }
  3: { name: execute }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce rendered-graph.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/rendered-graph.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/execution-output.md"
    condition: "stage == 3"
```

**Worked example.** A synthesis needs admitted-claims/v2, but producers offer raw-claims/v1. The global check rejects before any analyst runs.

### Failure Modes

Types are free-form labels with no compatibility rules, or the checker inspects source YAML rather than the expanded graph. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a strong core candidate. It already composes with two core patterns; promotion requires a reusable graph-export and typecheck proof. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Proof-Carrying Artifact:** layering — evidence sidecars become declared offer types.
- **Behavioral Pre-Mortem:** prerequisite — supplies the typed graph its counterexample search consumes.
