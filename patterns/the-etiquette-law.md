---
name: The Etiquette Law
scale: foundational
status: working
forces:
- Instrument-Task Fit
- Accumulated Signal
generators:
- Verify through Diverse Observers
problem: Deterministic protocol checks are given to LLM instruments that can hallucinate them, making the coordination layer no more reliable than the performers it coordinates.
signals:
- any check whose result could be a shell exit code
- a gate described in prose inside a prompt
- a fallback from a deterministic instrument to an LLM
stages:
- name: etiquette-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — deterministic by construction; this stage must never think
  fallback_friendly: false
  purpose: Own the protocol decision (admit/reject) as a command with an empty fallback chain.
  artifacts: []
- name: performance
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument matched to the work's grain
  fallback_friendly: true
  purpose: Do the judgment work the gate admitted.
  artifacts: []
dependencies:
  performance:
  - etiquette-gate
composes_with:
- pattern: Every core pattern
  how: prerequisite — every gate in this corpus is an Etiquette Law stage
type: orchestration-pattern
---

## The Etiquette Law (formerly The Tool Chain)


**Status:** Working. **Source:** v4 iterations 2–4; confirmed iteration 5 — 74 independent empty-fallback-chain attestations across the six expeditions; prior art CI/CD.

**Core Dynamic.** The deterministic part is always the etiquette, never the music. The protocol layer — cues, gates, ledgers, meters — goes to non-LLM instruments with empty fallback chains, not because AI instruments are unreliable, but because the etiquette must be *more reliable than the performers*, and the cheapest way to make something reliable is to make it not need to think. Three different things are routinely conflated and must not be: *tool use inside an LLM sheet*, *a deterministic validation command*, and *a non-LLM instrument that owns execution* (`instrument: cli`). The etiquette always belongs to the third. The de Bruijn criterion names the audit condition: the checker must be small enough to audit by reading.

**When to use:** always — this is the substrate of every other pattern. The moment a check can be a command, it must be a command.

**When NOT to use:** the work itself is judgment (do not "optimize" tone into a linter). A deterministic stage given a fallback to an LLM is the anti-pattern this law exists to name — a fallback for a clock is a second clock, and two clocks are the desynchronization you built the law to prevent.

**Marianne Score Structure**

```yaml
movements:
  1: { name: gate, instrument: cli }
  2: { name: ai-review }

sheet:
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    1: []                      # the etiquette does not degrade

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/run-gates.sh" "{{ workspace }}" --lint --schema --tests
    {% elif stage == 2 %}
    Review only what the gate admitted. Cite gate outputs by path.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/gate-report.json"'
    condition: "stage == 1"
  - type: content_regex
    pattern: "gate-report.json"
    path: "{workspace}/review.md"
    condition: "stage == 2"
```

**Near-miss:** an `agentai` sheet asked "run the linter and report whether it passed" — tool *use* inside a thinking instrument; the exit code became a sentence, and sentences hallucinate.

**Example.** A documentation pipeline: markdown lint, link check, and schema validation as `instrument: cli` movements with empty fallback chains; the AI reviewer consumes only the typed gate report — its judgment is spent on meaning, not on re-deriving what a script already decided.

### Review Integration

Iteration 5 promoted the former Tool Chain from an instrument-strategy pattern to a foundational law. The split keeps the former name as an inbound-link alias while making deterministic ownership and empty fallbacks constitutive. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
