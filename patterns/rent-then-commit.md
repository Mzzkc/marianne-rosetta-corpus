---
name: "Rent-Then-Commit"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
generators:
  - "Threshold-Triggered Switch"
problem: "A repeated per-use cost and a one-time commitment cost face an unknown horizon, and no rule says when committing becomes provably defensible."
signals:
  - "cheap retries that might go on forever vs one expensive settlement"
  - "recompute-every-run vs freeze-a-contract decisions"
  - "spot vs reserved capacity across a chain of unknown length"
config_features:
  - "concert"
  - "on_success"
  - "skip_when"
  - "capture_files"
stages:
  - name: ledger-probe
    sheets: 1
    instrument_guidance: "instrument: cli — reads the persisted spend ledger; nothing else touches it"
    fallback_friendly: false
    purpose: "Emit ladder-state.yaml: cumulative rent vs declared B."
    artifacts: ["ladder-state.yaml"]
  - name: ladder-decide
    sheets: 1
    instrument_guidance: "instrument: cli — pure arithmetic, exit-coded"
    fallback_friendly: false
    purpose: "Emit decision.yaml: {lane: rent|buy, rent_paid, B, ratio_bound: 2}."
    artifacts: ["decision.yaml"]
  - name: rent-lane
    sheets: "fan_out(2)"
    instrument_guidance: "cheap instrument (opencode GLM-5.3-flash); skip_when per expanded sheet when lane != rent"
    fallback_friendly: true
    purpose: "Cheap partial work while the ledger is below B."
    artifacts: []
  - name: buy-lane
    sheets: 1
    instrument_guidance: "strong reasoner; skip_when when lane != buy"
    fallback_friendly: false
    purpose: "Settle the whole remainder now; the horizon ended."
    artifacts: []
  - name: settle
    sheets: 1
    instrument_guidance: "instrument: cli — appends spend; the self-chain carries the ledger"
    fallback_friendly: false
    purpose: "Persist the ledger for the next cycle."
    artifacts: ["spend-ledger.jsonl"]
dependencies:
  ladder-decide: ["ledger-probe"]
  rent-lane: ["ladder-decide"]
  buy-lane: ["ladder-decide"]
  settle: ["rent-lane", "buy-lane"]
composes_with:
  - pattern: "Circuit Breaker"
    how: "layering — availability state machine composed with the cost ladder"
  - pattern: "Speculative Hedge"
    how: "substitution — the hedge IS the parallel purchase; the ladder prices when parallelism pays"
  - pattern: "The Economic Injury Line"
    how: "contrast — known damage model (EIL) vs unknown horizon (this); never confuse them"
---

## Rent-Then-Commit (Break-Even Escalation)

`Status: Working` · **Source:** iteration 6 (Expedition 4 — ski-rental / rent-versus-buy online algorithms). **Scale:** adaptation. **Force:** Finite Resources.

### Core Dynamic

A repeated per-use cost and a one-time commitment cost face an adversary who knows the horizon and you who do not. The classical result is exactly this strong and exactly this cheap: **keep renting while cumulative rent is below the commitment price B; commit the moment it reaches B; and no adversary can make you pay more than twice what a clairvoyant scheduler would have paid.** The factor of 2 is a proven worst-case bound, and the entire decision policy is arithmetic over a ledger. In an orchestra: cheap retried attempts are rent; the serialized authority, the expensive reasoner, the frozen contract, the precomputed index is the purchase.

The routing, in the real dialect: there is no dynamic instrument reassignment — `fan_out` and instruments resolve at parse time. The lanes are **sheets gated by `skip_when` commands keyed on expanded sheet numbers**: the rent lane's sheets skip when `decision.lane != "rent"`, the buy lane's sheet skips when `!= "buy"`. The decision travels by `capture_files` into whichever lane runs, and the executor cites the ladder position in its output header. The self-chain is the real `concert` + `on_success: run_job` form; `cost_limits` is the auditor of last resort, the ladder is the arithmetic that decides. The randomized 1.582-competitive variant is archive-color (its draw distribution and seed assumptions must be stated); the deterministic 2-bound is the version the corpus carries.

### When to Use / When NOT to Use

Use: self-chaining scores where each iteration cheaply retries work an expensive instrument could settle; repeated per-run recomputation versus freezing a derived contract; spot versus reserved capacity across a concert chain — anywhere the horizon is genuinely unknown and both cost paths are real.

Not: the rent has no marginal cost (a free local model — the ladder degenerates); the commitment price is unknown or negotiable; failure, not spend, is the trigger (that is Circuit Breaker's state machine); the horizon is actually known (a scheduled one-off never needs a competitive bound). Known damage model → Economic Injury Line. Unknown horizon → this.

### Marianne Score Structure

```yaml
instruments:
  cheap: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
concert:
  enabled: true
  max_chain_depth: 12
  inherit_workspace: true
on_success:
  - type: run_job
    job_path: "{score_dir}/rent-then-commit.yaml"
movements:
  1: { name: ledger-probe, instrument: cli, instrument_fallbacks: [] }
  2: { name: ladder-decide, instrument: cli, instrument_fallbacks: [] }
  3: { name: rent-lane, voices: 2 }
  4: { name: buy-lane }
  5: { name: settle, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 5                # expansion: 1,2, rent 3-4, buy 5, settle 6
  fan_out: { 3: 2 }
  dependencies: { 2: [1], 3: [2], 4: [2], 5: [3, 4] }
  skip_when:                    # keys are EXPANDED sheet numbers
    3: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "rent"' }
    4: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "rent"' }
    5: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "buy"' }
  per_sheet_instruments:
    3: cheap
    4: cheap
  per_sheet_fallbacks: { 1: [], 2: [], 6: [] }
cross_sheet:
  capture_files: ["{{ workspace }}/decision.yaml"]
prompt:
  variables: { commitment_price: 6.0 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/ladder.sh" probe --ledger "{{ workspace }}/spend-ledger.jsonl" \
      --commitment {{ commitment_price }} --emit "{{ workspace }}/ladder-state.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/ladder.sh" decide --state "{{ workspace }}/ladder-state.yaml" --emit "{{ workspace }}/decision.yaml"
    {% elif stage == 3 %}
    Renting. Complete your slice on the cheap path. Cite lane and ladder position from decision.yaml.
    {% elif stage == 4 %}
    Committed. Settle the whole remainder now. Cite the ladder position.
    {% else %}
    bash "{score_dir}/scripts/ladder.sh" settle --ledger "{{ workspace }}/spend-ledger.jsonl"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'jq -e "(.ratio_bound == 2) and (.commit == (.rent_paid >= .B))" {workspace}/decision.yaml'
    condition: "stage == 2"
```

Self-test: a ledger with rent ≥ B whose decision did not commit must fail — the proof score's substrate exercises the arithmetic it proves.

### Example

A nonprofit's weekly self-chaining score drafts donor summaries on a cheap model and occasionally needs a strong reasoner for contested numbers. Nobody knows which weeks will be contested. The ladder keeps cheap drafting until cumulative cheap spend equals one strong-instrument takeover, then commits — and the board can be told, arithmetically, that no scheduling hindsight could have done better than twice what was paid.

### Review Integration

Iteration 6: Reviews 1 and 3 found the draft's routing impossible — an invalid overlapping `instrument_map` (`{cheap: [3], strong: [3]}` fails at load on duplicate assignment) and a fabricated `on_success: {action: self}` shape. The lanes are now `skip_when`-gated sheets with expanded-number keys, and the self-chain is the real `concert`/`on_success: run_job` form. Review 2's demand that the randomized variant state its assumptions relegated 1.582 to archive-color.
