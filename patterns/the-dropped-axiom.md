---
name: "The Dropped Axiom"
scale: within-stage
type: orchestration-pattern
status: working
forces:
  - "Structured Disagreement"
generators:
  - "Frame Multiplication"
problem: "Every fan-in embodies an aggregation function constrained by theorems that do not care about intentions, and the synthesis presents its concealed choice as neutrality."
signals:
  - "sheets expressing rankings, priorities, or multi-premise verdicts"
  - "a synthesis that believes it is 'just combining'"
  - "an unlabelled 'consensus' output"
config_features:
  - "instrument: cli"
  - "content_contains"
stages:
  - name: fan-in
    sheets: 1
    instrument_guidance: "any — but the PRODUCER declares input_type on its output; the synthesizer never classifies"
    fallback_friendly: true
    purpose: "Apply the lookup row for each declared input type; emit the typed header."
    artifacts: ["synthesis.md"]
  - name: typecheck
    sheets: 1
    instrument_guidance: "instrument: cli — enforces rule↔axioms bijection per declared type"
    fallback_friendly: false
    purpose: "Reject empty axioms_dropped on rankings; reject dual-pole aggregation; reject unknown input_type."
    artifacts: []
dependencies:
  typecheck: ["fan-in"]
composes_with:
  - pattern: "Typed Force"
    how: "its fan-in form — the typing discipline's merge specialization"
  - pattern: "Fan-out + Synthesis"
    how: "grows this header at every merge — the primitive's typing clause"
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "substitution — editorial authority entered by declaration rather than accident"
---

## The Dropped Axiom (Fan-In Typing)

`Status: Working` · **Source:** iteration 6 (Expedition 4 — Arrow's impossibility theorem, judgment aggregation). **Scale:** within-stage. **Force:** Structured Disagreement.

### Core Dynamic

Every fan-in embodies an aggregation function, and aggregation functions are constrained by theorems that do not care about your intentions. If the sheets express *rankings* over three or more alternatives, Arrow's theorem is already in the room: no rule satisfies unrestricted domain, Pareto, independence of irrelevant alternatives, and non-dictatorship at once — so your "neutral synthesis" is impossible, and whatever it actually does is a concealed choice about which axiom it silently dropped. **Concealment is the defect, not the dropping.** If the sheets express interconnected propositions, majority on each premise can entail a conclusion the majority on the conclusion rejects — and both procedures are "majority rule."

The pattern, as a lookup the producer types: the panel-emitting stage writes `input_type ∈ {binary-verdict, ranking, interconnected-propositions, non-reconstructible-judgment}` on its own output — the synthesizer applies exactly the row for the declared type and never classifies inputs itself. The rows: `binary-verdict` + audited independence → majority (Condorcet's territory); `ranking` → declare the dropped axiom (IIA dropped is positional scoring; non-dictatorship dropped is a named editorial authority; unrestricted-domain dropped is declared single-peaked structure with a median); `interconnected-propositions` → premise-pole or conclusion-pole, exactly one, declared; `non-reconstructible-judgment` → editorial synthesis with dissents. The output field `axioms_dropped` is the pattern's whole teeth: **an empty value on a ranking aggregation is not innocence, it is perjury.**

Kept standalone against the fold motion: it upgrades *every existing merge in every existing score* with one header field — the cheapest broad improvement in the corpus.

### When to Use / When NOT to Use

Use: synthesis sheets fanning in preferences, priorities, ranked options, awards, shortlists, or multi-premise verdicts — anywhere the aggregator believes it is "just combining."

Not: binary facts with deterministic verification (reconstruct them — that is not preference aggregation); single-frame inputs; consumers who genuinely never rely on the dropped axiom's protection (declare and move on); trivially small panels where one declared dictator is honest.

### Marianne Score Structure

```yaml
movements:
  1: { name: fan-in }
  2: { name: typecheck, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks: { 2: [] }
prompt:
  template: |
    {% if stage == 1 %}
    You are aggregating panel outputs, each carrying its declared input_type.
    Apply the typing table per declared type — never re-classify an input.
    Your output header MUST carry {aggregation_rule, axioms_dropped, declared_authority}.
    Write {{ workspace }}/synthesis.md.
    {% else %}
    bash "{score_dir}/scripts/fanin-typecheck.sh" "{{ workspace }}/synthesis.md"
    {% endif %}
validations:
  - type: content_contains
    path: "{workspace}/synthesis.md"
    pattern: "aggregation_rule:"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/fanin-typecheck.sh {workspace}/synthesis.md'
    condition: "stage == 2"
```

The typechecker enforces the bijection per declared type — rule ∈ the shared demotion ladder `{majority, weighted-correlation, editorial-with-dissents, refusal}` ⟺ the matching `axioms_dropped` declaration — and the Arrow table lives as data in the checker, so lens and gate share one source of truth. Self-test: a ranking aggregation with empty `axioms_dropped` must fail.

### Example

A city planning office fans a zoning dispute to five stakeholder panels, each returning ranked preferences over seven land-use options with `input_type: ranking` declared. The synthesis wants to output "the consensus ranking." Arrow says no such neutral object exists; the typed fan-in forces the office to declare — in the published document — that it drops independence of irrelevant alternatives and scores positions, or that the planning director is the named authority. Either is legitimate; an unlabelled "consensus" is neither.

### Review Integration

Iteration 6: Review 1 demanded the input type be explicit and the omnibus table dropped — typing moved to the producer (`input_type` declared on panel outputs). Review 2's motion to fold this into Typed Force lost 2–1 (Reviews 1 and 3 wanted the fan-in rule separate and immediate); the fold is recorded as the losing argument, and the pattern is cross-linked as Typed Force's fan-in form.
