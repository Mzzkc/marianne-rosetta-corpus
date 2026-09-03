---
name: Is-Line-Clear
scale: communication
type: orchestration-pattern
status: working
forces:
- Partial Failure
- Progressive Commitment
generators:
- Gate on Environmental Readiness
problem: A sender infers that a shared medium is free and transmits into an unobserved conflicting operation.
signals:
- two parties share a scarce mutable channel
- only the counterparty can attest readiness
- silence is ambiguous rather than permission
stages:
- name: request-clearance
  sheets: 1
  instrument_guidance: codex-cli — writes the requested operation, channel, and expiry
  fallback_friendly: true
  purpose: Ask the counterparty for bounded permission.
  artifacts:
  - clearance-request.json
- name: answer-and-admit
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — validates a positive answer before use
  fallback_friendly: false
  purpose: Move SAFE to GO only on matching unexpired clearance; otherwise move to DANGER.
  artifacts:
  - line-state.json
dependencies:
  answer-and-admit:
  - request-clearance
composes_with:
- pattern: Standby–GO
  how: prerequisite — supplies counterparty readiness before the arm/fire transition
---

## Is-Line-Clear

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A sender infers that a shared medium is free and transmits into an unobserved conflicting operation. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Admission is counterparty-answered, identity-bound, and expiring. No answer, duplicate answer, mismatch, or timeout changes the line to DANGER; it never silently returns to clear.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: request-clearance }
  2: { name: answer-and-admit }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce clearance-request.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/clearance-request.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/line-state.json"
    condition: "stage == 2"
```

**Worked example.** Two release scores share a publication endpoint. One requests a ten-minute slot; only the endpoint custodian's matching signed answer admits publication.

### Failure Modes

Treating absence of a lock file as consent. That observes local state, not the counterparty's readiness. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived because it is a narrow shared-medium protocol. It remains distinct from Dormancy Gate: dormancy waits on observable state; this pattern requires an answer from another authority. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Standby–GO:** prerequisite — supplies counterparty readiness before the arm/fire transition.
