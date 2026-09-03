---
name: Behavioral Pre-Mortem
scale: score-level
status: working
forces:
- Exponential Defect Cost
- Partial Failure
generators:
- Incremental Exposure
- Match Instrument to Grain
problem: Mechanism interactions — concurrency windows, skip/fallback interplay, self-chain livelock — are invisible in YAML source and kill in production.
signals:
- 'a DAG where mechanisms interact: concurrency caps meeting shared regions'
- skip_when conditions interacting with fallback chains
- self-chain loop conditions that could livelock; recurring schedules whose leases could double-fire
stages:
- name: render
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — mzt validate renders the DAG; a programmatic JobConfig render dumps the full graph
  fallback_friendly: false
  purpose: Render the execution graph itself — never a hand-written mirror.
  artifacts: []
- name: check
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — typed invariant checker over the rendered graph
  fallback_friendly: false
  purpose: Check safety/liveness invariants; emit counterexample artifacts on violation.
  artifacts: []
- name: explain
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — runs ONLY on violation
  fallback_friendly: true
  purpose: Turn the counterexample trace into a human-readable fix proposal.
  artifacts: []
dependencies:
  check:
  - render
  explain:
  - check
composes_with:
- pattern: Self-Stabilizing Custody
  how: substitution — the kill-injection probe is this pattern's runtime twin
- pattern: The Etiquette Law
  how: prerequisite — 'deterministic stages have empty fallback chains' is itself a checked invariant
type: orchestration-pattern
---

## Behavioral Pre-Mortem


**Status:** Working. **Source:** TLA+/TLC at AWS. **The render is real and named (Review 3):** `mzt validate` performs three validation layers (YAML syntax, Pydantic schema, extended semantics) and renders the DAG visualization; a programmatic JobConfig dry-render is established substrate discipline for auditing concurrency and ancestry before releasing locks.

**Core Dynamic.** The pattern's object is not the work product — it is the orchestration's own *behavior space*. Before anything runs, render the plan and check every reachable behavior against invariants. Safety violations (two writers to one path in overlapping windows; a fallback routing to an occupied executor) surface as counterexample traces — concrete interleavings that break the invariant; liveness violations (a self-chain livelock; a recurring schedule whose lease has no owner; an orphan stage nothing consumes) as fairness-cycle witnesses. The AWS lesson generalized: the bugs that kill are usually *design* bugs, and the cheapest place to find one is where fixing it costs a YAML edit, not a production incident.

**Typed graph schema (Review 2's demand) and mandatory counterexample output:** the checker consumes `{nodes: {id, instrument, fallback_chain[], cadenza_dirs[], skip_when}, edges: {from, to, kind: dependency|fan_out|chain}, windows: {concurrency_cap, shared_regions[]}}`. On violation it MUST emit a counterexample artifact — the offending interleaving as an ordered event list — not a prose complaint. An invariant checker without counterexample output is a lint with ambitions.

**When to use:** any DAG where mechanisms *interact*; any score expensive enough that a wasted run matters.

**When NOT to use:** state explosion — the model must be bounded (finite workers, finite queue depths, bounded loop unrollings). Trivial pipelines with no interaction. Nondeterminism that lives outside the model (external APIs) — those need runtime patterns (fencing, self-stabilization), not pre-mortems.

**Marianne Score Structure**

```yaml
movements:
  1: { name: render, instrument: cli }
  2: { name: check, instrument: cli }
  3: { name: explain }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    mzt validate "{score_dir}/this-score.yaml" --json > {{ workspace }}/graph-render.json
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/invariant-check.py" "{{ workspace }}/graph-render.json" \
      --no-cycles --no-shared-region-two-writers \
      --deterministic-stages-have-empty-fallbacks \
      --ai-stages-have-nonempty-fallbacks \
      --leases-name-an-owner --chains-reach-terminal --emit-counterexamples
    {% elif stage == 3 %}
    The checker found violations ({{ workspace }}/counterexamples.jsonl). For each, turn the
    trace into a concrete YAML fix proposal. Cite the trace line by line.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/graph-render.json"'
    condition: "stage == 1"
  - type: content_regex
    # a render that silently dropped a sheet would otherwise check a phantom
    pattern: "\"stage\""
    path: "{workspace}/graph-render.json"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/invariant-check.py {workspace}/graph-render.json --check-only'
    condition: "stage == 2"
```

**Near-miss:** a design-review meeting over the YAML source — checking a hand-written mirror of the graph, not the rendered graph; the mirror is where the bug isn't.

**Example.** A data-migration concert with parallel loaders and per-loader fallbacks: the pre-mortem finds that under one `skip_when` combination, two fallback paths both route to the same writer in overlapping windows — a two-writer safety violation fixed by one dependency edge, discovered for the cost of a dry run instead of a corrupted staging table.

### Review Integration

Review 3 required the actual mzt validation and JobConfig render. Review 2 required a typed rendered graph and mandatory counterexample artifacts before execution is admitted. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
