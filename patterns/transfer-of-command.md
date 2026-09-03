---
name: Transfer of Command
scale: concert-level
type: orchestration-pattern
status: working
forces:
- Partial Failure
- Information Asymmetry
generators:
- Contract at Interfaces
problem: Planned succession changes the named operator but leaves tacit state, pending decisions, and incident context behind.
signals:
- ownership changes at a known time
- work spans shifts or deployments
- the successor must act immediately without re-discovery
stages:
- name: prepare-command-state
  sheets: 1
  instrument_guidance: codex-cli — compiles open work, authorities, decisions, and hazards
  fallback_friendly: true
  purpose: Write the mandated command-state document before the transfer minute.
  artifacts:
  - command-state.yaml
- name: transfer-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — checks completeness, seal, and declared time
  fallback_friendly: false
  purpose: Atomically change active command only with a valid state document.
  artifacts:
  - command-transfer.json
- name: assume
  sheets: 1
  instrument_guidance: claude-code — successor reads the sealed state and acknowledges priorities
  fallback_friendly: false
  purpose: Accept command and continue from the declared state.
  artifacts:
  - assumption-receipt.md
dependencies:
  transfer-gate:
  - prepare-command-state
  assume:
  - transfer-gate
composes_with:
- pattern: The Black-Box Ledger
  how: prerequisite — supplies incident and execution evidence to the command-state document
- pattern: Positive Transfer
  how: layering — makes the planned ownership handoff explicit
---

## Transfer of Command

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Planned succession changes the named operator but leaves tacit state, pending decisions, and incident context behind. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Before the declared minute, the outgoing authority writes and seals a typed state document. At the minute, a deterministic gate changes the active authority only if the successor acknowledges the exact digest.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: prepare-command-state }
  2: { name: transfer-gate }
  3: { name: assume }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce command-state.yaml with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/command-state.yaml"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/assumption-receipt.md"
    condition: "stage == 3"
```

**Worked example.** A multi-day release concert transfers from one operator to another with open hooks, current rung, unresolved waivers, and next safe action attached.

### Failure Modes

The transfer document is written after authority changes, or it lists artifacts without decisions and hazards. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived because it is planned succession, distinct from crash recovery. The Black-Box Ledger remains the evidence substrate when no planned handoff is possible. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **The Black-Box Ledger:** prerequisite — supplies incident and execution evidence to the command-state document.
- **Positive Transfer:** layering — makes the planned ownership handoff explicit.
