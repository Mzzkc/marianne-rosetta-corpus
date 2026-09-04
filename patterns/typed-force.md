---
name: "Typed Force"
scale: foundational
type: orchestration-pattern
status: working
forces:
  - "Structured Disagreement"
  - "Information Asymmetry"
generators:
  - "Contract at Interfaces"
problem: "Authority-carrying and claim-carrying objects flow through pipelines without a type a gate can join on, so binding decisions and persuasive suggestions enforce identically."
signals:
  - "downstream consumers behave differently depending on what kind of thing this is, but the kind is not a field"
  - "a decision record indistinguishable from an observation"
  - "an aggregation presented as neutral"
config_features:
  - "instrument: cli"
  - "content_regex"
stages:
  - name: emit-typed
    sheets: 1
    instrument_guidance: "any — emits objects whose force field is assigned by a NAMED authority"
    fallback_friendly: true
    purpose: "Produce decision/claim objects carrying {force, assigned_by} at creation."
    artifacts: ["decision.jsonl"]
  - name: typecheck
    sheets: 1
    instrument_guidance: "instrument: cli — joins on the type, never judges the type"
    fallback_friendly: false
    purpose: "Enforce type-selects-rule and visible retyping; reject untyped and unassigned rows."
    artifacts: []
dependencies:
  typecheck: ["emit-typed"]
composes_with:
  - pattern: "The Precedent Bench"
    how: "its authority form — binding/persuasive force over decisions"
  - pattern: "The Dropped Axiom"
    how: "its fan-in form — aggregation headers over merges"
  - pattern: "Proof-Carrying Artifact"
    how: "its evidence form — admissibility typing over artifacts"
---

## Typed Force

`Status: Working (narrowed)` · **Source:** iteration 6. **Scale:** foundational law. **Forces:** Structured Disagreement, Information Asymmetry.

### Core Dynamic

Untyped authority is vibes; untyped claims are furniture. The law is four transitions, no more:

1. **Type at creation** — an object carries its force field when emitted, not when disputed.
2. **The type is assigned by a named authority** — `assigned_by` is a provenance field a gate can check; the gate checks syntax and provenance and *never* the truth of the assignment, which belongs to the assigning authority and is contested through that authority's own motion procedure.
3. **The type selects the enforcement rule** — bind/persuade, admit/quarantine, fund-acquisition-only, demote.
4. **Retyping is visible** — supersession or demotion edges, never silent edits.

The draft's umbrella (legal precedent + claim typing + aggregation policy + budget allocation + disposal under one law) is delegated to the pattern forms that earned it: binding/persuasive → The Precedent Bench; fan-in headers → The Dropped Axiom; evidence admissibility → Proof-Carrying Artifact. The law is the shared discipline those patterns specialize. The demotion ladder `{majority, weighted-correlation, editorial-with-dissents, refusal}` is shared with Condorcet's Premise so the typechecker's enum and the demotion path cannot diverge.

### When to Use / When NOT to Use

Use: anywhere authority flows (decisions that bind later scores; dispositions; verdicts over non-reconstructible claims) and anywhere claims flow (embedded assertions; syntheses over rankings; prices that drove allocations).

Not: everything genuinely carries the same force (a uniform corpus needs no typing); the type cannot be assigned mechanically at creation (the binding/persuasive split collapses into "everything binds"); no gate ever joins on the type (schema theater).

### Marianne Score Structure

```yaml
movements:
  1: { name: emit-typed }
  2: { name: typecheck, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks: { 2: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Produce {{ workspace }}/decision.jsonl. Every row MUST carry
    force ∈ {binding, persuasive} and assigned_by: <authority-id>, set at creation.
    Aggregations additionally carry {aggregation_rule, axioms_dropped, declared_authority}.
    {% else %}
    python3 "{score_dir}/scripts/force-typecheck.py" "{{ workspace }}/decision.jsonl"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/force-typecheck.py {workspace}/decision.jsonl'
    condition: "stage == 2"
  - type: content_contains
    path: "{workspace}/decision.jsonl"
    pattern: "assigned_by:"
    condition: "stage == 2"
```

### Example

A refactoring campaign's early scores decided "no new dependencies," "errors at exit 0 are still failing." Typed as holdings, they bind later scores until explicitly overruled; a later score wanting a new dependency files a typed motion — distinguish or overrule — and the citation gate catches an un-overruled contradiction deterministically.

### Review Integration

Iteration 6: Review 1 moved to cut the umbrella law; Review 2 kept it but demanded the syntax/authority split. Narrowed to the four-transition discipline with `assigned_by` provenance, umbrella coverage delegated to the pattern forms. Review 3's enum-mismatch finding fixed by the shared demotion ladder.
