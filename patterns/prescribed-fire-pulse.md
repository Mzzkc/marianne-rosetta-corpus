---
name: Prescribed-Fire Pulse
scale: iteration
type: orchestration-pattern
status: working
forces:
- Accumulated Signal
- Finite Resources
generators:
- Threshold-Triggered Switch
problem: Low-grade workspace fuel accumulates until cleanup becomes a disruptive emergency instead of a bounded maintenance action.
signals:
- temporary artifacts and stale branches grow predictably
- small maintenance bursts are cheaper than periodic reclamation
- cleanup safety can be checked deterministically
stages:
- name: measure-fuel
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — inventories only declared disposable classes
  fallback_friendly: false
  purpose: Measure fuel without deleting it.
  artifacts:
  - fuel-report.json
- name: bounded-burn
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — acts only under a lease and explicit manifest
  fallback_friendly: false
  purpose: Remove or archive the admitted bounded set.
  artifacts:
  - burn-receipt.json
- name: verify
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — proves protected paths and active work survived
  fallback_friendly: false
  purpose: Close the maintenance pulse.
  artifacts:
  - post-burn-verdict.json
dependencies:
  bounded-burn:
  - measure-fuel
  verify:
  - bounded-burn
composes_with:
- pattern: Stigmergic Workspace
  how: layering — keeps the coordination surface legible without erasing live signals
---

## Prescribed-Fire Pulse

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Low-grade workspace fuel accumulates until cleanup becomes a disruptive emergency instead of a bounded maintenance action. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

On an ordinary leased schedule, measure declared fuel classes, select a small bounded set, archive before destructive action where practical, and verify protected state after the pulse.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: measure-fuel }
  2: { name: bounded-burn }
  3: { name: verify }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce fuel-report.json with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/fuel-report.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/post-burn-verdict.json"
    condition: "stage == 3"
```

**Worked example.** A weekly maintenance score archives stale generated reports older than 30 days while refusing any path named by active job manifests.

### Failure Modes

Cleanup is broad, path predicates are unresolved, or the burn runs without a lease and races active writers. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived rather than core because it is a concrete workspace-hygiene composition of schedule, manifests, and deterministic checks. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Stigmergic Workspace:** layering — keeps the coordination surface legible without erasing live signals.
