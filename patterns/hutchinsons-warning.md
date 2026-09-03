---
name: Hutchinson's Warning
scale: adaptation
status: working
forces:
- Finite Resources
- Producer-Consumer Mismatch
generators:
- Match Instrument to Grain
problem: 'Negative feedback with lag oscillates: a controller fed by lagged telemetry throttles hard, bursts through, and throttles hard forever.'
signals:
- a large multi-movement score with a genuinely shared budget — money, wall-clock, or context
- spend telemetry arrives with lag (batched billing, periodic usage polls) — which is everywhere
- 'feeding work into anything with a real capacity curve: paid APIs, human review, CI pools'
stages:
- name: trend-probe
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — computes the spend-rate EMA from the ledger
  fallback_friendly: false
  purpose: Emit capacity-state.yaml {ema, ceiling, rung} — the WRITTEN state the router and prompts cite.
  artifacts: []
- name: router
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — chooses the rung; down-cross immediate, up-cross after M windows
  fallback_friendly: false
  purpose: Translate the damped trend into a declared degradation rung.
  artifacts: []
- name: work
  sheets: 1
  instrument_guidance: 'claude-code or codex-cli — rung-dependent: rung 0 full instruments; rung 1 instrument_map routes half the movements cheap; rung 2 scope reduction; rung 3 deferral'
  fallback_friendly: true
  purpose: Execute under the chosen rung, DECLARED in the state file the prompt cites.
  artifacts: []
- name: settle
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — appends actuals; the EMA is the only thing the next iteration reads
  fallback_friendly: false
  purpose: Close the loop on measured trend, never instantaneous reading.
  artifacts: []
dependencies:
  router:
  - trend-probe
  work:
  - router
  settle:
  - work
composes_with:
- pattern: The Etiquette Law
  how: layering — the rungs are instrument tiers on the chain
- pattern: Standby–GO
  how: substitution — the hold is degradation rung zero
type: orchestration-pattern
---

## Hutchinson's Warning (Damped Load-Shedding)


**Status:** Working. **Source:** Nicholson's 1954 blowfly cultures; the Hutchinson delay-logistic. **Narrowed per Review 2** to its structural identity: *damped delayed-feedback control with asymmetric shed/restore*. The Metered Merge absorption is **reversed** — its ALINEA equation lives in the archive as its own entry (same damping law, applied to admission flow instead of budget), and the seam is stated here and there.

**Core Dynamic.** The deep result of density dependence is not "who gets cut when the food runs out" — that is triage, and v4 owns triage. The deep result is that **negative feedback with delay oscillates**, and the design problem is *damping*: feedback lag longer than the system's natural period generates oscillation (Nicholson's violent ~35-day cycles). Translated: under a hard budget ceiling, sheets are not killed in priority order by a judge stage — they degrade along a ladder each experiences locally, and the controller must measure spend as a **damped trend (EMA)**, never an instantaneous reading. The asymmetry is load-bearing: **shed fast (one measurement window), restore slow (several)** — a controller that restores as eagerly as it sheds is Nicholson's culture in YAML. And the most LLM-specific instance: **context is a habitat** — `lookback_sheets` and `max_output_chars` bound the population of artifacts competing for each consumer's attention, and when density exceeds capacity the failure is quiet: no sheet starves, every sheet gets measurably worse.

**Control wiring, corrected per Review 1:** `circuit_breaker` accepts **sheet-failure counts only** — it is wired for exactly that. Spend ceilings live in `cost_limits`, which *pauses the job* — a different, correct, observable. The rung ladder is neither: it is score-level routing that reads the written `capacity-state.yaml`; the rung is declared in that file — which the prompt cites — so degradation is *declared*, not experienced as mysterious constraint.

**When to use:** large multi-movement scores with a genuine shared budget; lagged telemetry; feeding anything with a real capacity curve.

**When NOT to use:** the resource is not actually shared (sheet-local budget counters have no density dependence; a controller there is ceremony). The shed ladder is symmetric (the failure mode restated). The consumer's capacity is constant and known (a static rate or plain stagger is the same thing with less machinery). No honest sensor — feedback on a lied-about occupancy is worse than open loop.

**Marianne Score Structure**

```yaml
cost_limits: { max_cost_usd: 40 }      # the ceiling — pauses the job when hit (its own observable)

movements:
  1: { name: trend-probe, instrument: cli }
  2: { name: router, instrument: cli }
  3: { name: work }
  4: { name: settle, instrument: cli }

sheet:
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks: { 1: [], 2: [], 4: [] }

instruments:
  cheap: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_map:
  opus: [3]                             # rung 1 would rewrite this map to route half
  cheap: [3]                            # the movements cheap — routing by WRITTEN state

prompt:
  variables: { ceiling: 40, restore_windows: 3 }
  template: |
    {% if stage == 1 %}
    python3 "{score_dir}/scripts/ema-probe.py" "{{ workspace }}/spend-ledger.jsonl" \
      --alpha 0.3 --ceiling {{ ceiling }} --emit "{{ workspace }}/capacity-state.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/rung-router.sh" "{{ workspace }}/capacity-state.yaml" \
      --shed-immediate --restore-after {{ restore_windows }} --emit-rung
    {% elif stage == 3 %}
    You are running at rung {{ rung }} (see {{ workspace }}/capacity-state.yaml — read it):
    0 full instruments, 1 cheap instrument for half the movements, 2 narrower scope,
    3 deferral. The rung is DECLARED state, not a suggestion.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/settle.sh" "{{ workspace }}/spend-ledger.jsonl" \
      --append-actuals --assert-under-ceiling
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/capacity-state.yaml"
    condition: "stage == 2"            # the router cannot run on unwritten state
  - type: command_succeeds
    # THE validation that makes the damping real: down-cross immediate, up-cross after M windows
    command: 'bash {score_dir}/scripts/rung-router.sh {workspace}/capacity-state.yaml --assert-asymmetry'
    condition: "stage == 4"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/settle.sh {workspace}/spend-ledger.jsonl --check-only'
    condition: "stage == 4"
```

**Worked example with real numbers (Review 3's demand):** a 40-sheet documentation migration under `$40`. The ledger records actual spend per sheet; the EMA (α = 0.3) over the last 5 entries reads $0.82/sheet at sheet 20 — 0.82 × 40 = $32.8 projected, under the $34 shed threshold (0.85 × ceiling): rung 0. At sheet 25, lagged billing catches up: EMA jumps to $0.94/sheet → $37.6 projected → cross → rung 1 **immediately**: sheets 26+ route to the cheap instrument and a reduced `capture_files` list, declared in `capacity-state.yaml`. Occupancy falls; the EMA declines $0.94 → $0.88 → $0.81 over three windows; only when EMA < $28 (0.7 × ceiling) for **three consecutive windows** does the router restore rung 0. No sheet is executed against a wall; the habitat gets honestly poorer, then honestly richer — and the post-hoc assertion `total spend ≤ $40` is checked mechanically at settle.

**Near-miss:** sheet-local budget counter checks against instantaneous spend — the lagged-telemetry oscillator with extra steps.

### Review Integration

Review 2 narrowed the identity to damped delayed feedback with asymmetric shed and restore. Review 1 corrected failure-count circuit breaking versus job-level cost limits and required written rung state; Review 3 required the numerical example. Metered Merge remains separate because it controls flow, not budget. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
