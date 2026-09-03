---
name: Continuity Ledger
scale: communication
type: orchestration-pattern
status: working
forces:
- Producer-Consumer Mismatch
- Accumulated Signal
generators:
- Accumulate Knowledge
problem: Parallel authors silently contradict shared world facts because prose canon has no typed, serialized assertion boundary.
signals:
- many writers depend on persistent facts
- facts have different types and update rules
- contradictions appear only during late synthesis
stages:
- name: propose-facts
  sheets: 1
  instrument_guidance: codex-cli — extracts typed assertions and provenance from each contribution
  fallback_friendly: true
  purpose: Write proposed fact records without mutating canon.
  artifacts:
  - fact-proposals/
- name: serialize
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — validates type-specific invariants and appends accepted facts
  fallback_friendly: false
  purpose: Maintain one canonical fact ledger.
  artifacts:
  - continuity-ledger.jsonl
- name: consume
  sheets: 1
  instrument_guidance: claude-code — reads the canonical projection as required context
  fallback_friendly: true
  purpose: Create against admitted facts only.
  artifacts:
  - continuation.md
dependencies:
  serialize:
  - propose-facts
  consume:
  - serialize
composes_with:
- pattern: Join-Semilattice Merge
  how: substitution — joins additive fact types algebraically while serialized authority handles non-monotone facts
- pattern: The Errata Ledger
  how: layering — corrects facts without erasing their history
---

## Continuity Ledger

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Parallel authors silently contradict shared world facts because prose canon has no typed, serialized assertion boundary. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Represent shared facts as typed assertions with identity, value, authority, and supersession rules. One deterministic writer rejects contradictory non-monotone updates and joins additive types safely.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: propose-facts }
  2: { name: serialize }
  3: { name: consume }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce fact-proposals/ with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/fact-proposals/"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/continuation.md"
    condition: "stage == 3"
```

**Worked example.** A story campaign stores character status as exclusive state but discovered locations as a grow-only set. The ledger applies different merge laws rather than flattening both into prose.

### Failure Modes

All facts use last-writer-wins, or authors bypass the ledger by treating a narrative summary as canon. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a domain-specific substrate. Its explicit seam with Join-Semilattice Merge prevents the serialized writer from needlessly owning monotone facts. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Join-Semilattice Merge:** substitution — joins additive fact types algebraically while serialized authority handles non-monotone facts.
- **The Errata Ledger:** layering — corrects facts without erasing their history.
