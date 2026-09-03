---
name: Join-Semilattice Merge
scale: score-level
status: working
forces:
- Structured Disagreement
- Finite Resources
generators:
- Contract at Interfaces
problem: 'The fan-in point is both a bottleneck and a trust point: merging concurrent writers requires arbitration that can destroy concurrent work.'
signals:
- 'genuinely additive facts: findings keyed by ID, coverage observations, disjoint-segment translations'
- isolated writers appending disjoint records
- concurrent updates delivered in any order, possibly duplicated
stages:
- name: writers
  sheets: fan_out(5)
  instrument_guidance: claude-code or codex-cli — any instruments; each emits records into an append-only, instance-tagged ID namespace
  fallback_friendly: true
  purpose: Append disjoint records — the instance tag makes concurrent numbering collision-free by construction.
  artifacts: []
- name: join
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — jq -s union by ID, dedupe by content digest; no LLM participates in merging
  fallback_friendly: false
  purpose: Converge the lattice deterministically.
  artifacts: []
- name: synthesize
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — tension/emergence work over the joined lattice, never a summary
  fallback_friendly: true
  purpose: Interpret the lattice; do not re-merge it.
  artifacts: []
dependencies:
  join:
  - writers
  synthesize:
  - join
composes_with:
- pattern: Fan-out + Synthesis
  how: substitution — the trust-free fan-in
- pattern: Attested Merge Gate
  how: substitution — when a contract, not algebra, is what you have
type: orchestration-pattern
---

## Join-Semilattice Merge


**Status:** Working. **Source:** CRDTs; the CALM theorem. **Isolation claim corrected per Review 1:** per-sheet worktrees do not exist; the instance-tagged namespace (`findings/{instance}-{n}.json`) is what makes concurrent numbering collision-free by construction — and it renders per-sheet isolation mostly unnecessary.

**Core Dynamic.** Convergence by *data-type construction*, not arbitration. When every writer's output is an append into an ID-keyed, monotone namespace and the merge function is a semilattice join (commutative, associative, idempotent), "conflict" is not suppressed or adjudicated — it is *undefined*. Any interleaving of concurrent updates, delivered in any order, possibly duplicated, converges to the same state without coordination. The fan-in stops being a bottleneck and a trust point simultaneously.

**When to use:** genuinely additive facts — findings keyed by ID, coverage observations, translations of disjoint segments, tagged excerpts, sensor readings.

**When NOT to use:** non-monotone semantics — veto, rejection, move operations, "take the latest prose" (last-writer-wins silently destroys concurrent work; it is amnesia, not convergence). Interacting facts (this finding contradicts that one) — a join can only collect both; adjudication needs the Skeptical Oracle. Deletion (needs tombstones; forward-only supersession avoids them).

**Marianne Score Structure**

```yaml
movements:
  1: { name: writers }
  2: { name: join, instrument: cli }
  3: { name: synthesize }

sheet:
  total_items: 3
  fan_out: { 1: 5 }
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Transcribe your disjoint source set. Append each observation as
    {{ workspace }}/findings/{{ instance }}-<n>.json — instance-tagged, ID-keyed,
    append-only. Never touch another instance's namespace.
    {% elif stage == 2 %}
    jq -s 'sort_by(.id) | group_by(.id) | map(.[0])' {{ workspace }}/findings/*.json \
      > {{ workspace }}/joined.jsonl
    {% elif stage == 3 %}
    Read {{ workspace }}/joined.jsonl. Find tensions and emergent themes. Do NOT summarize —
    the join already merged; you interpret.
    {% endif %}

validations:
  - type: command_succeeds
    # THE idempotence probe: run the join twice into scratch; diff must be empty.
    # merge ∘ merge = merge, mechanically checked — a property check, not a process check.
    command: 'bash {score_dir}/scripts/idempotence-probe.sh {workspace}/findings'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'test "$(cat {workspace}/findings/*.json | wc -l)" -ge 5'
    condition: "stage == 1"
```

**Near-miss:** "merge with last-writer-wins" — amnesia marketed as convergence.

**Example.** Five analysts each transcribe a disjoint source set into a shared observation lattice over a weekend, working offline in isolated checkouts; Monday's join converges all five branches with no coordination meeting, no merge conflicts, and no analyst blocked on another's schedule.

### Review Integration

Review 1 replaced per-sheet isolation with instance-tagged namespaces and required the algebraic laws—especially idempotence—to be executed as property probes rather than asserted in prose. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
