---
name: Sign-Off Chain Against the Hard Date
scale: score-level
type: orchestration-pattern
status: working
forces:
- Finite Resources
- Exponential Defect Cost
generators:
- Graduate & Filter
problem: A hard deadline collapses independent review obligations into one vague approval, hiding which failure class was knowingly waived.
signals:
- release date cannot move
- several reviewers own disjoint risk classes
- some defects may be waived but must remain attributable
stages:
- name: independent-signoffs
  sheets: 1
  instrument_guidance: claude-code, codex-cli, and opencode — independent reviewers each own one declared failure class
  fallback_friendly: true
  purpose: Produce signed verdicts without sharing responsibility.
  artifacts:
  - signoffs/
- name: deadline-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — joins verdicts and explicit waivers bijectively
  fallback_friendly: false
  purpose: Admit only a complete sign-off or waiver set.
  artifacts:
  - release-attestation.json
dependencies:
  deadline-gate:
  - independent-signoffs
composes_with:
- pattern: The Attested Merge Gate
  how: layering — supplies disjoint pre-merge sign-offs and explicit waivers
---

## Sign-Off Chain Against the Hard Date

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A hard deadline collapses independent review obligations into one vague approval, hiding which failure class was knowingly waived. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Partition failure classes before review. Every class has exactly one accountable sign-off; every non-accept verdict requires a waiver naming authority, expiry, and compensating control. The hard date changes disposition, never evidence.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: independent-signoffs }
  2: { name: deadline-gate }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce signoffs/ with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/signoffs/"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/release-attestation.json"
    condition: "stage == 2"
```

**Worked example.** Security, data integrity, and documentation each sign independently. Documentation receives a dated waiver; an absent security verdict cannot be converted into an implicit waiver by the release sheet.

### Failure Modes

One reviewer signs for all classes, or a deadline turns missing evidence into approval. The deterministic join must reject duplicate ownership and uncovered classes. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Retained in the archive because its deadline-and-waiver discipline is useful but narrower than the Attested Merge Gate it decorates. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **The Attested Merge Gate:** layering — supplies disjoint pre-merge sign-offs and explicit waivers.
