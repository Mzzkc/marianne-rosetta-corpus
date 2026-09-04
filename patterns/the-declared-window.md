---
name: "The Declared Window"
scale: communication
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Synthesis sheets read bounded lookback over large runs and then make global claims their window cannot support."
signals:
  - "streak/trend/consensus language in late sheets ('consistently', 'across the run', 'no objections')"
  - "a truncation whose consumers quote 'the' upstream output"
  - "an honest approximation available but a silent exact-looking guess chosen instead"
config_features:
  - "cross_sheet"
  - "instrument: cli"
stages:
  - name: work
    sheets: "fan_out(4)"
    instrument_guidance: "any — writes instance-tagged artifacts"
    fallback_friendly: true
    purpose: "Produce the artifacts the window will bound."
    artifacts: ["work-{{ instance }}.md"]
  - name: window-manifest
    sheets: 1
    instrument_guidance: "instrument: cli — writes the manifest from the run's ACTUAL cross_sheet config and artifacts"
    fallback_friendly: false
    purpose: "Emit {window_span, exact_in_window, total_items_seen, window: full|partial}."
    artifacts: ["window-manifest.yaml"]
  - name: bounded-synthesis
    sheets: 1
    instrument_guidance: "strong reasoner — every claim tagged, structured ledger emitted"
    fallback_friendly: false
    purpose: "Synthesize with a structured claim ledger joinable to the manifest."
    artifacts: ["synthesis.md", "claims.jsonl"]
  - name: join-gate
    sheets: 1
    instrument_guidance: "instrument: cli — ledger arithmetic and span join"
    fallback_friendly: false
    purpose: "exact_in_window + refused = claims_emitted; every global claim has a row."
    artifacts: []
dependencies:
  window-manifest: ["work"]
  bounded-synthesis: ["work", "window-manifest"]
  join-gate: ["bounded-synthesis"]
composes_with:
  - pattern: "The Black-Box Ledger"
    how: "bounded capture is the window; the manifest is the claim contract over that bound"
  - pattern: "Hutchinson's Warning"
    how: "complement — density control vs claim honesty: the two halves of bounded context"
---

## The Declared Window (Bounded-Context Honesty)

`Status: Working` · **Source:** iteration 6 (Expedition 4 — sliding-window stream algorithms). **Scale:** communication. **Force:** Information Asymmetry.

### Core Dynamic

`lookback_sheets` and `max_output_chars` are not hygiene; they are a sliding window over an unbounded artifact stream, and every downstream sheet consuming bounded context stands where the streaming engineers stood — except the engineers knew it. The epistemic rule: from a window you may make **windowed claims** (exact within the window, or approximated with a declared ε) and **counted-total claims** (I saw K items, I read W), but not **global claims** — "all prior findings agree," "no earlier stage contradicts this" — because the window's boundary is also the boundary of your knowledge.

The contract is a **structured claim ledger**: the synthesizer emits `claims.jsonl` rows `{claim_id, text, class ∈ {in-window, total-seen, refused}, window_id}`; a CLI movement writes the window manifest from the run's *actual* `cross_sheet` configuration and prior artifacts (a delivery fact, not a belief); the join gate asserts the arithmetic (`exact_in_window + refused = claims_emitted`) and that every global-quantifier sentence in the prose has a ledger row with an honest class. An honest (1±ε) answer with ε in the output is a *stronger* artifact than a silent exact-looking guess.

The corpus honesty rule (promoted from Cluster Lead's archive): a coordination artifact whose inputs are incomplete publishes the incompleteness — "coverage unknown," "prior weeks unqueried" — never a manufactured success.

Engine fact baked in: `lookback_sheets: 0` means **all** completed sheets, not none — context austerity uses a small positive bound, and the manifest states which.

### When to Use / When NOT to Use

Use: long self-chains and concerts where synthesis sheets read bounded lookback over large runs; any truncation whose consumers quote "the" upstream output; streak/trend/consensus language in later sheets.

Not: short scores where the window provably contains the whole history (declare `window: full`); claims intrinsically local to this file or diff; the whole stream retained and queryable on disk (query it and drop the approximation clause honestly).

### Marianne Score Structure

```yaml
cross_sheet:
  lookback_sheets: 5
  max_output_chars: 4000
movements:
  1: { name: work, voices: 4 }
  2: { name: window-manifest, instrument: cli, instrument_fallbacks: [] }
  3: { name: bounded-synthesis }
  4: { name: join-gate, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 4                # expansion: work 1-4, manifest 5, synthesis 6, gate 7
  fan_out: { 1: 4 }
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  per_sheet_fallbacks: { 5: [], 6: [], 7: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Work your slice. Write {{ workspace }}/work-{{ instance }}.md.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/window.sh" manifest --lookback 5 --workspace "{{ workspace }}" \
      --emit "{{ workspace }}/window-manifest.yaml"
    {% elif stage == 3 %}
    Synthesize from the visible window. Write {{ workspace }}/synthesis.md AND
    {{ workspace }}/claims.jsonl — one row per claim with class in-window|total-seen|refused.
    {% else %}
    bash "{score_dir}/scripts/claims.sh" join --manifest "{{ workspace }}/window-manifest.yaml" \
      --claims "{{ workspace }}/claims.jsonl" --prose "{{ workspace }}/synthesis.md"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/claims.sh join --manifest {workspace}/window-manifest.yaml --claims {workspace}/claims.jsonl --prose {workspace}/synthesis.md'
    condition: "stage == 4"
```

### Example

A season-long advisory concert synthesizes weekly scouting reports; by week 20 the synthesis sheet sees only the last 5 sheets. When it writes "pest pressure has been consistently low," the ledger forces the sentence to carry its own boundary — "consistently low across the visible five weeks; prior weeks unqueried" — and the extension service publishes a claim it can actually defend.

### Review Integration

Iteration 6: Reviews 1 and 2 killed the draft's prose word-ban ("all"/"never" greps) as easy to evade and false-positive-prone. Replaced by the structured claim ledger + manifest-as-delivery-fact + arithmetic join gate. Review 3's cut of Cluster Lead promoted its honesty clause into this pattern's rule.
