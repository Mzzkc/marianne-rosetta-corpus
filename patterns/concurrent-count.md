---
name: Concurrent Count
scale: score-level
type: orchestration-pattern
status: working
forces:
- Structured Disagreement
- Information Asymmetry
generators:
- Verify through Diverse Observers
problem: A single inventory count cannot distinguish a real total from omissions caused by one traversal or observer.
signals:
- completeness matters
- two independent enumerations are affordable
- a count mismatch can be narrowed by partitions
stages:
- name: independent-counts
  sheets: 1
  instrument_guidance: codex-cli and opencode — use independent traversal strategies and isolated outputs
  fallback_friendly: false
  purpose: Produce two keyed tallies without cross-reading.
  artifacts:
  - count-a.json
  - count-b.json
- name: reconcile
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — compares keys and recursively splits mismatching partitions
  fallback_friendly: false
  purpose: Locate omissions until tallies are bijective or quarantined.
  artifacts:
  - count-reconciliation.json
dependencies:
  reconcile:
  - independent-counts
composes_with:
- pattern: The Skeptical Oracle
  how: layering — supplies an independent completeness oracle before reconstruction
---

## Concurrent Count

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A single inventory count cannot distinguish a real total from omissions caused by one traversal or observer. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Count the same population twice through structurally different traversals, compare keyed sets rather than totals alone, and split-search only mismatching regions. Agreement on a number without agreement on identities is not reconciliation.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: independent-counts }
  2: { name: reconcile }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce count-a.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/count-a.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/count-reconciliation.json"
    condition: "stage == 2"
```

**Worked example.** One inventory walks Git's index; the other walks filesystem candidates under declared roots. Equal counts with different paths still fail until the sets agree.

### Failure Modes

Both counters share the same parser or input list, so correlated omission looks like agreement. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a specialized completeness technique; the Skeptical Oracle is the broader reconstruction pattern. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **The Skeptical Oracle:** layering — supplies an independent completeness oracle before reconstruction.
