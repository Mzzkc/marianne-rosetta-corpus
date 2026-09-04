---
name: "The Freeze"
scale: foundational
type: orchestration-pattern
status: working
forces:
  - "Exponential Defect Cost"
  - "Producer-Consumer Mismatch"
generators:
  - "Contract at Interfaces"
problem: "Downstream work starts against upstream structure that is still moving, so finishers build on a version that stops existing."
signals:
  - "parallel specialists blocked on a structure still under negotiation"
  - "re-deciding structure later costs multiples of deciding it now"
  - "post-freeze edits arriving silently instead of as visible amendments"
config_features:
  - "cadenzas"
  - "fan_out"
  - "command_succeeds"
stages:
  - name: propose
    sheets: "fan_out(3)"
    instrument_guidance: "any — pitches complete structures with stable element ids"
    fallback_friendly: true
    purpose: "Propose complete candidate structures with stable BEAT-xx identifiers."
    artifacts: ["pitch-{{ instance }}.yaml"]
  - name: lock
    sheets: 1
    instrument_guidance: "instrument: cli — the appointed convergence authority's decision, executed deterministically"
    fallback_friendly: false
    purpose: "Write frozen structure + digest; one hash becomes the interface."
    artifacts: ["frozen/structure.yaml", "frozen.sha256"]
  - name: specialize
    sheets: "fan_out(3)"
    instrument_guidance: "any — each receives the frozen artifact by required cadenza"
    fallback_friendly: true
    purpose: "Draft against the frozen structure, citing its digest."
    artifacts: ["draft-{{ instance }}.md"]
  - name: join-gate
    sheets: 1
    instrument_guidance: "instrument: cli — sha256sum -c plus citation join"
    fallback_friendly: false
    purpose: "Reject any successor built on a different hash."
    artifacts: []
dependencies:
  lock: ["propose"]
  specialize: ["lock"]
  join-gate: ["specialize"]
composes_with:
  - pattern: "Fork-Evident History"
    how: "payload/substrate — the lock's digest is the chain's head"
  - pattern: "Prefabrication"
    how: "contrast — authored-in-advance contract with no discovery room; the Freeze has discovery then authority-declared termination"
  - pattern: "The Unprimed Falsifier"
    how: "the falsifier's evidence loop terminates in this lock, not in convergence"
---

## The Freeze (Lock-as-Interface)

`Status: Working` · **Source:** iteration 6 (convergence: iteration terminates by authority declaration, not convergence). **Scale:** foundational law. **Forces:** Exponential Defect Cost, Producer-Consumer Mismatch.

### Core Dynamic

An artifact under negotiation becomes, by declaration, an **interface** — digest-named, delivered by required cadenza, consumed by parallel successors whose validity is a join against the digest. Transition rules: iteration terminates by *authority declaration* (an appointed convergence authority, not an elected one); the frozen thing is the spec that parallel specialization obeys; post-freeze change travels as visible amendment — a new digest that supersedes, never a silent edit of the frozen bytes. Structure decided at the beat stage costs 10× less than at the prose stage, so the lock is where iteration *should* stop.

The pin is expressible: `file_sha256` cannot verify a runtime-discovered digest (it requires a literal at authorship), so the lock movement writes `frozen.sha256` and every consumer-side check is `sha256sum -c` inside `command_succeeds`. Delivery is physical: each specialist's **required cadenna** (keyed to its expanded sheet number) injects exactly the frozen artifact — absent file, failed sheet.

Distinct from Prefabrication (no discovery room), Fork-Evident History (the substrate the digest rides), Attested Merge Gate (contract compliance at merge, not structure termination). The scoped-delta form (add-only over the frozen spine, gate proves structure delta zero and prose delta positive) re-enters through a new lock.

### When to Use / When NOT to Use

Use: artifact families where downstream work is expensive enough that it must not start until upstream is truly frozen — documentation suites keyed to a locked section order, finishing disciplines against a locked cut, precedent-bound campaigns.

Not: structure already known (use Prefabrication); no convergence authority worth trusting (the lock becomes a bottleneck or a farce); parts truly independent (run plain fan-out); the frozen structure cannot be machine-extracted (the join gate is prose — a politely worded prayer).

### Marianne Score Structure

```yaml
movements:
  1: { name: propose, voices: 3 }
  2: { name: lock, instrument: cli, instrument_fallbacks: [] }
  3: { name: specialize, voices: 3 }
  4: { name: join-gate, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 4                # expansion: propose 1-3, lock 4, specialize 5-7, join 8
  fan_out: { 1: 3, 3: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    5:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
    7:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
  per_sheet_fallbacks: { 4: [], 8: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Propose a complete structure with stable BEAT-xx identifiers. Write {{ workspace }}/pitch-{{ instance }}.yaml.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/lock.sh" --pitches "{{ workspace }}/pitch-*.yaml" \
      --emit "{{ workspace }}/frozen/structure.yaml" --digest "{{ workspace }}/frozen.sha256"
    {% elif stage == 3 %}
    Draft against the frozen structure you received. Cite its digest in your header.
    {% else %}
    bash "{score_dir}/scripts/freeze-join.sh" "{{ workspace }}/draft-*.md" --against "{{ workspace }}/frozen.sha256"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'cd {workspace} && sha256sum -c frozen.sha256'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/freeze-join.sh {workspace}/draft-1.md {workspace}/draft-2.md {workspace}/draft-3.md --against {workspace}/frozen.sha256'
    condition: "stage == 4"
```

### Example

A six-chapter onboarding guide: three pitching sheets propose incompatible orderings; the lock freezes one beat shape; three drafting sheets write against it, each receiving it by cadenza; the gate rejects any chapter whose headings drift. A readability pass lands as an amendment with a new digest, visibly superseding.

### Review Integration

Iteration 6: survived review with the pin made expressible (`sha256sum -c`, per Review 3's finding that `file_sha256` requires an authorship-time digest) and delivery made physical (required cadenzas per Reviews 1 and 2's finding that the draft's spec-dir routing never delivered the runtime-locked artifact). Narrowed to the lock primitive; absorbed The Break and The Punch-Up Pass with seams stated.
