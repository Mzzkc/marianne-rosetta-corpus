---
name: Configuration Control Board
scale: score-level
type: orchestration-pattern
status: working
forces:
- Structured Disagreement
- Progressive Commitment
generators:
- Contract at Interfaces
problem: Configuration changes cross a shared boundary without one serialized authority, so individually reasonable edits combine into an incoherent active configuration.
signals:
- several writers propose changes to one configuration corpus
- a bad change can affect many downstream sheets
- approval and application must be distinguishable
stages:
- name: propose
  sheets: 1
  instrument_guidance: claude-code or codex-cli — drafts a typed change request and impact statement
  fallback_friendly: true
  purpose: Write a proposed delta without mutating canon.
  artifacts:
  - change-request.yaml
- name: decide-and-apply
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — serializes accepted deltas and records the active revision
  fallback_friendly: false
  purpose: Validate, admit, and atomically apply one approved change.
  artifacts:
  - configuration.yaml
  - change-ledger.jsonl
dependencies:
  decide-and-apply:
  - propose
composes_with:
- pattern: Flight Rules
  how: prerequisite — serves as the serialized change board for rule revisions
---

## Configuration Control Board

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Configuration changes cross a shared boundary without one serialized authority, so individually reasonable edits combine into an incoherent active configuration. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Separate proposing a configuration change from authorizing and applying it. Proposals can fan out; canon has one writer. Each decision binds the proposed digest, decision, authority, effective revision, and resulting configuration digest.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: propose }
  2: { name: decide-and-apply }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce change-request.yaml with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/change-request.yaml"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/configuration.yaml"
    condition: "stage == 2"
```

**Worked example.** A recovery team proposes three edits to a flight-rule corpus. The board rejects one schema-breaking delta, admits two non-overlapping deltas in revision order, and publishes one new canonical digest.

### Failure Modes

The board becomes a ceremonial meeting while writers still edit canon directly. Fail closed: a configuration digest not named in the change ledger is not active. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a valid composition rather than promoted to core because Flight Rules already contains a change-board stage. A future promotion should demonstrate independent reuse beyond rule maintenance. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Flight Rules:** prerequisite — serves as the serialized change board for rule revisions.
