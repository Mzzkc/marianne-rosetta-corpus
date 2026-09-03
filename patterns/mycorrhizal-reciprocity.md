---
name: Mycorrhizal Reciprocity
scale: concert-level
type: orchestration-pattern
status: approximation
forces:
- Finite Resources
- Producer-Consumer Mismatch
generators:
- Accumulate Knowledge
problem: Participants consume shared quality improvements without returning evidence or maintenance, so the shared substrate degrades.
signals:
- several scores reuse one shared corpus
- contributions and consumption are measurable
- scarce review capacity can be allocated conditionally
stages:
- name: account
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — records consumed and contributed value by stable identity
  fallback_friendly: false
  purpose: Maintain the reciprocal ledger.
  artifacts:
  - reciprocity-ledger.jsonl
- name: allocate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — applies graduated sanctions and restoration rules
  fallback_friendly: false
  purpose: Allocate scarce review or execution capacity from the ledger.
  artifacts:
  - allocation.yaml
- name: contribute
  sheets: 1
  instrument_guidance: codex-cli — repairs or enriches the shared substrate
  fallback_friendly: true
  purpose: Return value before unrestricted future consumption.
  artifacts:
  - contribution.md
dependencies:
  allocate:
  - account
  contribute:
  - allocate
composes_with:
- pattern: Season Bible
  how: layering — attaches maintenance obligations to shared campaign memory
---

## Mycorrhizal Reciprocity

`Status: Approximation` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Participants consume shared quality improvements without returning evidence or maintenance, so the shared substrate degrades. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Measure both withdrawal and return to a shared substrate. Mild imbalance narrows access, continued imbalance requires contribution-first admission, and repaired reciprocity restores capacity gradually.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: account }
  2: { name: allocate }
  3: { name: contribute }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce reciprocity-ledger.jsonl with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/reciprocity-ledger.jsonl"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/contribution.md"
    condition: "stage == 3"
```

**Worked example.** Teams drawing from a shared research corpus earn future deep-review slots by contributing verified corrections and source refreshes.

### Failure Modes

The ledger becomes a social score with no allocatable scarcity, or contribution volume substitutes for contribution quality. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as an approximation because current scores have budgets and learning records but no general exchange market. The pattern must not imply a nonexistent scheduler allocation primitive. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Season Bible:** layering — attaches maintenance obligations to shared campaign memory.
