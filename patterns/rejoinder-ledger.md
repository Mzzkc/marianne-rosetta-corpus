---
name: Rejoinder Ledger
scale: communication
type: orchestration-pattern
status: working
forces:
- Structured Disagreement
- Information Asymmetry
generators:
- Verify through Diverse Observers
problem: A response claims to address review findings while omitting, duplicating, or answering a different finding under similar prose.
signals:
- large review sets require formal response
- closure depends on every finding receiving one disposition
- rewording makes manual matching unreliable
stages:
- name: freeze-findings
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — assigns stable IDs and digests to the review set
  fallback_friendly: false
  purpose: Create the immutable side of the bijection.
  artifacts:
  - findings.json
- name: respond
  sheets: 1
  instrument_guidance: codex-cli — writes one typed rejoinder per finding ID
  fallback_friendly: true
  purpose: Explain accept, reject, defer, or supersede with evidence.
  artifacts:
  - rejoinders.json
- name: bijection-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — rejects missing, duplicate, and foreign IDs
  fallback_friendly: false
  purpose: Prove exact response coverage.
  artifacts:
  - rejoinder-verdict.json
dependencies:
  respond:
  - freeze-findings
  bijection-gate:
  - respond
composes_with:
- pattern: The Skeptical Oracle
  how: layering — binds every proposed finding to exactly one tested disposition
---

## Rejoinder Ledger

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A response claims to address review findings while omitting, duplicating, or answering a different finding under similar prose. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Freeze the finding identities, then require a one-to-one response map. Semantic argument remains judgment; coverage, identity, and evidence pointers are deterministic.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: freeze-findings }
  2: { name: respond }
  3: { name: bijection-gate }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce findings.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/findings.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/rejoinder-verdict.json"
    condition: "stage == 3"
```

**Worked example.** An adversarial review emits 43 findings. The response has 43 unique IDs; one typo referencing F034 twice fails even though the prose claims full closure.

### Failure Modes

The gate counts responses instead of joining IDs, or accepted fixes lack a reproduction pointer proving closure. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a narrow but reusable response-discipline layer over the Skeptical Oracle. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **The Skeptical Oracle:** layering — binds every proposed finding to exactly one tested disposition.
