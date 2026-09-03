---
name: Custody Transfer with Seals
scale: communication
type: orchestration-pattern
status: working
forces:
- Information Asymmetry
- Partial Failure
generators:
- Contract at Interfaces
problem: A receiver acknowledges custody without proving that the bytes received are the bytes the sender released.
signals:
- artifact crosses a process, score, or human boundary
- transport may truncate or replace files
- point-in-time transfer integrity matters more than full history
stages:
- name: seal
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — hashes the exact transfer set and signs the manifest
  fallback_friendly: false
  purpose: Create a point seal before release.
  artifacts:
  - transfer-manifest.json
- name: receive-and-check
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — re-hashes before writing acceptance
  fallback_friendly: false
  purpose: Accept custody only when manifest and bytes agree.
  artifacts:
  - receipt.json
dependencies:
  receive-and-check:
  - seal
composes_with:
- pattern: Positive Transfer
  how: layering — adds byte identity to the offer/accept/release dialogue
- pattern: Fork-Evident History
  how: substitution — point seals prove one transfer; history chains prove prefix continuity
---

## Custody Transfer with Seals

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A receiver acknowledges custody without proving that the bytes received are the bytes the sender released. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Sender and receiver independently hash the named set. Acceptance binds both digests and the handoff identity; mismatch leaves ownership with the sender and emits quarantine evidence.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: seal }
  2: { name: receive-and-check }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce transfer-manifest.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/transfer-manifest.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/receipt.json"
    condition: "stage == 2"
```

**Worked example.** A score hands a model package to deployment. The receiver checks every file and only then writes acceptance; a truncated weight shard prevents release.

### Failure Modes

The seal covers a directory name but not its membership, or the receiver trusts the sender's digest without recomputing it. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived with the point-seal versus history-chain seam explicit: it does not replace Fork-Evident History. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Positive Transfer:** layering — adds byte identity to the offer/accept/release dialogue.
- **Fork-Evident History:** substitution — point seals prove one transfer; history chains prove prefix continuity.
