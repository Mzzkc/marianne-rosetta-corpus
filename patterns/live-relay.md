---
name: "Live Relay"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Producer-Consumer Mismatch"
generators:
  - "Contract at Interfaces"
  - "Accumulate Knowledge"
problem: "Sequential creative agents lose artistic continuity or individual authority because handoffs preserve either substrate or voice, but not the living identity of the performance."
signals:
  - "work is a sustained creative performance over time"
  - "different sections benefit from different creative voices"
  - "continuity of identity matters more than continuity of raw substrate"
  - "gaps between agents would be detectable by the audience"
stages:
  - name: tune
    sheets: 1
    instrument_guidance: "claude-code — establishes the performance identity, invariants, open motifs, and handoff packet contract"
    fallback_friendly: false
    purpose: "Write a compact identity score that constrains continuity without scripting later performers."
    artifacts: ["performance-identity.md", "relay-packet-0.yaml"]
  - name: voice-one
    sheets: 1
    instrument_guidance: "claude-code — the opening performer owns one declared section while honoring the shared identity"
    fallback_friendly: false
    purpose: "Create the opening section and leave an exact outgoing packet for the next ordered voice."
    artifacts: ["section-1.md", "relay-packet-1.yaml"]
  - name: voice-two
    sheets: 1
    instrument_guidance: "codex-cli — a distinct capable voice continues rather than restarts the performance"
    fallback_friendly: false
    purpose: "Create the middle section and leave the next playable cue."
    artifacts: ["section-2.md", "relay-packet-2.yaml"]
  - name: voice-three
    sheets: 1
    instrument_guidance: "opencode — a third capable voice closes its section while preserving unresolved motifs for assembly"
    fallback_friendly: false
    purpose: "Create the final authored section and close the relay packet sequence."
    artifacts: ["section-3.md", "relay-packet-3.yaml"]
  - name: continuity-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — checks packet sequence, section presence, motif custody, and zero missing beats"
    fallback_friendly: false
    purpose: "Admit the performance only when every handoff is complete and ordered."
    artifacts: ["continuity-verdict.json"]
  - name: assemble
    sheets: 1
    instrument_guidance: "codex-cli — joins admitted sections without flattening their distinct voices"
    fallback_friendly: false
    purpose: "Produce the audience-facing whole and preserve performer attribution."
    artifacts: ["performance.md"]
dependencies:
  voice-one: [tune]
  voice-two: [voice-one]
  voice-three: [voice-two]
  continuity-gate: [voice-three]
  assemble: [continuity-gate]
composes_with:
  - pattern: "Mission Command"
    how: "layering — the performance identity acts as intent, not a line-by-line prescription"
  - pattern: "Stigmergic Workspace"
    how: "payload/substrate — relay packets and completed sections are the shared coordination surface"
  - pattern: "Succession Pipeline"
    how: "substitution — uses sequential transformation while preserving creative identity rather than only data shape"
  - pattern: "The Tool Chain"
    how: "layering — deterministic packet and continuity checks remain etiquette around the creative work"
---

## Live Relay

`Status: Working` · **Source:** live ensemble handoffs, radio continuity, and serialized collaborative performance. **Scale:** score-level.

### Problem Depth

A sequential creative pipeline can preserve files perfectly and still lose the work's identity. One performer closes a motif another expected to inherit; a new voice restates the premise instead of continuing it; synthesis sands away every local texture to make the whole sound uniform. Ordinary producer-consumer contracts protect shape, not presence. The audience experiences the seam as a gap even when every artifact exists.

Live Relay makes the handoff part of the performance. Each voice receives a compact identity score plus the immediately preceding relay packet, owns its section without committee interference, and leaves the next voice a packet containing unresolved motifs, completed beats, tonal commitments, hazards, and the exact continuation point. The packet is not a summary of the section. It is a playable cue.

### Core Dynamic

Continuity comes from three simultaneous constraints:

1. **Shared identity:** a short stable statement of what the performance is and must not become.
2. **Local authority:** each performer owns a bounded section and may make irreversible artistic choices inside it.
3. **Zero-gap handoff:** every section ends with an outgoing packet whose beat follows the prior packet and names what remains alive.

The voices remain distinct. The assembler joins already admitted sections and may repair mechanical seams, but it cannot rewrite all sections into one house voice. If broad editorial transformation is required, use Sugya Weave rather than calling the result a relay.

### When to Use / When NOT to Use

Use for serial fiction, music criticism, campaign worldbuilding, long-form narrative, or any creative work where changing hands should be perceptible as variation but not rupture. Do not use for additive fact collection, interchangeable batch processing, or work where a deterministic transform fully specifies the handoff. Do not use fan-out alone when the later voice must inherit choices made by the earlier one; those performers are ordered, not independent.

### Marianne Score Structure

```yaml
movements:
  1: { name: tune }
  2: { name: voice-one }
  3: { name: voice-two }
  4: { name: voice-three }
  5: { name: continuity-gate }
  6: { name: assemble }

sheet:
  size: 1
  total_items: 6
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4], 6: [5] }
  per_sheet_fallbacks:
    5: []
  cadenzas:
    2:
      - file: "{{ workspace }}/performance-identity.md"
        as: context
        required: true
    3:
      - file: "{{ workspace }}/relay-packet-1.yaml"
        as: context
        required: true
    4:
      - file: "{{ workspace }}/relay-packet-2.yaml"
        as: context
        required: true

prompt:
  template: |
    {% if stage == 1 %}
    Write performance-identity.md and relay-packet-0.yaml: intent, forbidden breaks,
    open motifs, beat 0, and the first playable cue.
    {% elif stage >= 2 and stage <= 4 %}
    Continue from the incoming packet. Own this section. Preserve identity without
    imitating the previous voice. Write section-{{ stage - 1 }}.md and a packet whose
    beat is exactly one greater than the incoming beat.
    {% elif stage == 5 %}
    python "{score_dir}/scripts/check-relay.py" "{{ workspace }}"
    {% elif stage == 6 %}
    Assemble only admitted sections. Preserve section boundaries and attribution.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'python "{score_dir}/scripts/check-relay.py" "{workspace}"'
    condition: "stage == 5"
  - type: file_exists
    path: "{workspace}/performance.md"
    condition: "stage == 6"
```

### Failure Modes

- **Packet as synopsis:** the next voice learns what happened but not what remains playable.
- **Voice laundering:** the assembler normalizes every section until individual authority vanishes.
- **False fan-out:** supposedly sequential performers run independently and invent incompatible continuities.
- **Identity as script:** the tuning document specifies every creative choice and reduces later voices to transcription.
- **Missing beat:** a section exists without a valid outgoing packet; downstream execution must stop rather than infer the cue.

### Review Integration

The iteration-5 inventory found this as a pre-existing INDEX entry with no split file and no Appendix A frontmatter block. Curation resolves the anomaly by preserving the indexed, score-level pattern and supplying the compiler contract rather than silently dropping a named corpus concept. Both frontmatter and the worked structure use explicit ordered movements because continuity requires sequential inheritance. Deterministic packet checks use an any-wrapped CLI profile with no AI fallback.

The legacy composition name The Tool Chain is retained here as an inbound-link alias to The Etiquette Law; stage 3 can normalize the index/DAG edge while preserving discoverability.

### Composes With

Mission Command, Stigmergic Workspace, Succession Pipeline, The Etiquette Law (formerly The Tool Chain)
