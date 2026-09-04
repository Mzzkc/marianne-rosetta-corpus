---
name: "Monitor Mix"
scale: communication
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators:
  - "Contract at Interfaces"
problem: "Many consumers need different slices of one shared accumulating state, and each currently receives either everything or someone else's slice."
signals:
  - "one shared state, many consumers with genuinely different depth needs"
  - "a summarizer drowning in function bodies; an implementer starved of them"
  - "routing decisions made ad hoc per run instead of written down"
config_features:
  - "cadenzas"
  - "fan_out"
  - "instrument: cli"
stages:
  - name: channel-inventory
    sheets: 1
    instrument_guidance: "instrument: cli — enumerate the channels; no opinions"
    fallback_friendly: false
    purpose: "Emit channels.yaml from the actual shared state."
    artifacts: ["channels.yaml"]
  - name: assemble
    sheets: 1
    instrument_guidance: "instrument: cli — applies the versioned mixdown prescription"
    fallback_friendly: false
    purpose: "Project per-consumer mixes under char budgets; refuse union-over-source."
    artifacts: ["mixes/consumer-*.md"]
  - name: line-check
    sheets: 1
    instrument_guidance: "instrument: cli — per-consumer liveness and budget sweep"
    fallback_friendly: false
    purpose: "Every mix has every required channel within budget, before doors."
    artifacts: []
  - name: perform
    sheets: "fan_out(3)"
    instrument_guidance: "per consumer role; each receives ONLY its mix by required cadenza keyed to its expanded sheet"
    fallback_friendly: true
    purpose: "Perform the consumer role from the mix, citing its mix id."
    artifacts: ["consumer-outputs/out-{{ instance }}.md"]
dependencies:
  assemble: ["channel-inventory"]
  line-check: ["assemble"]
  perform: ["line-check"]
composes_with:
  - pattern: "Relay Zone"
    how: "layering — route per consumer first, then compress a mix that would drown its consumer"
  - pattern: "The Declared Window"
    how: "the mix manifest is the delivery receipt the window contract joins against"
---

## Monitor Mix

`Status: Working` · **Source:** iteration 6 (Expedition 3 — monitor engineering and the line check). **Scale:** communication. **Forces:** Information Asymmetry, Finite Resources.

### Core Dynamic

One shared state, many ears, and no ear wants all of it. The drummer's mix is kick, click, and a sliver of bass; the singer's is their own voice loud against a hint of the band. Same channels, different gains, different destinations — and the mixing decisions are *routing* decisions, made once, written down as a versioned prescription, and checked by a deterministic sweep before the run starts. Distinct from Relay Zone (compresses the stream's *size*) and Screening Cascade (filters items by escalation): Monitor Mix changes each consumer's **view**, and the mix is a first-class artifact. The line check — every channel in every mix, before doors — is a per-consumer liveness sweep: a consumer whose mix is dead does not perform.

Delivery is enforced by construction: cadenzas key on the expanded sheet number and the file path carries `{{ instance }}`, so each fan-out voice receives exactly its mix, `required: true`. Consumers never read raw channels. A prescription whose mixes' union exceeds the source is amplification, not mixing — assembly refuses it.

### When to Use / When NOT to Use

Use: many consumers, one accumulating shared state, genuinely different depth needs (a summarizer wants counts and deltas; an implementer wants exact function bodies; a compliance reader wants the custody sequence), and a mix prescription stable enough to write down before the run.

Not: all consumers need the same context (inject it directly); per-consumer mixing requires semantic judgment per item (that is N AI curators — the cost is the whole budget).

### Marianne Score Structure

```yaml
movements:
  1: { name: channel-inventory, instrument: cli, instrument_fallbacks: [] }
  2: { name: assemble, instrument: cli, instrument_fallbacks: [] }
  3: { name: line-check, instrument: cli, instrument_fallbacks: [] }
  4: { name: perform, voices: 3 }
sheet:
  size: 1
  total_items: 4                  # expansion: 1,2,3 then perform = sheets 4,5,6
  fan_out: { 4: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    4:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
    5:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
  per_sheet_fallbacks: { 1: [], 2: [], 3: [] }
prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/mix.sh" channels --from "{{ workspace }}/shared/" --emit "{{ workspace }}/channels.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/mix.sh" assemble --channels "{{ workspace }}/channels.yaml" \
      --prescription "{score_dir}/mixdown.yaml" --out "{{ workspace }}/mixes/"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/mix.sh" line-check --dir "{{ workspace }}/mixes/" --against "{score_dir}/mixdown.yaml"
    {% else %}
    You receive ONLY your mix file. Perform your consumer role from it. Cite mix id and channels in your header.
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/mix.sh line-check --dir {workspace}/mixes --against {score_dir}/mixdown.yaml'
    condition: "stage == 3"
  - type: content_contains
    path: "{workspace}/consumer-outputs/out-1.md"
    pattern: "mix:"
    condition: "stage == 4"
```

Negative control: a mix missing a required channel must fail line-check before any performer runs.

### Example

An incident postmortem: one timeline, three readers. The executive mix: impact counts, deltas, recovery timestamps. The engineer's mix: full command logs and stack traces. Compliance: the custody sequence with seal references. Same channels, three mixes under budget — and the line check guarantees nobody performs without their required channels.

### Review Integration

Iteration 6: Reviews 1 and 2 found the draft's `spec_tags` could not route a distinct mix per fan-out instance and that nothing enforced consumer isolation. Per-instance required cadenzas (`consumer-{{ instance }}.md`) and the output mix-id citation are the fix; the line-check negative control was added per Review 1's reachable-negative-control clause of the Etiquette Law.
