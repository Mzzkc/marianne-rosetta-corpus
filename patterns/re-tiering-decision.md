---
name: Re-Tiering Decision
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
- Finite Resources
- Accumulated Signal
generators:
- Threshold-Triggered Switch
problem: A population's risk tier changes item by item, leaving structurally similar items under inconsistent controls after systemic evidence appears.
signals:
- flag rate crosses a declared hold threshold
- one cause affects a broad dependent population
- classification authority must be separate from artifact existence
stages:
- name: measure-and-scope
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — computes flag rate and dependency-bearing blast radius
  fallback_friendly: false
  purpose: Write the candidate population and trigger evidence.
  artifacts:
  - retiering-candidate.json
- name: authorize
  sheets: 1
  instrument_guidance: claude-code or codex-cli — separate authority reviews the systemic case
  fallback_friendly: false
  purpose: Approve or reject the mass class transition.
  artifacts:
  - retiering-decision.yaml
- name: apply
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — rewrites classifications without changing artifact existence
  fallback_friendly: false
  purpose: Apply the authorized bijective reclassification.
  artifacts:
  - tier-ledger.jsonl
dependencies:
  authorize:
  - measure-and-scope
  apply:
  - authorize
composes_with:
- pattern: Negative-Treatment Watch
  how: prerequisite — its flag-rate hold triggers the decision
- pattern: Screening Cascade
  how: layering — changes which instrument echelon receives the affected population
---

## Re-Tiering Decision

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A population's risk tier changes item by item, leaving structurally similar items under inconsistent controls after systemic evidence appears. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

When accumulated evidence crosses a threshold, pause individual routing, define the dependency-closed population, obtain separate authority, and change tier labels in one recorded transition. Reclassification never deletes evidence.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: measure-and-scope }
  2: { name: authorize }
  3: { name: apply }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce retiering-candidate.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/retiering-candidate.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/tier-ledger.jsonl"
    condition: "stage == 3"
```

**Worked example.** Source decay exceeds 15% for one provider family, so all dependent claims move from admitted to recheck-required pending an authorized sweep.

### Failure Modes

The detector also authorizes the tier change, or mass retiering is used as a hidden deletion mechanism. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived because it is a specialized policy response to Negative-Treatment Watch, not a general replacement for Screening Cascade. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Negative-Treatment Watch:** prerequisite — its flag-rate hold triggers the decision.
- **Screening Cascade:** layering — changes which instrument echelon receives the affected population.
