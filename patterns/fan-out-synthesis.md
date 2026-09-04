---
name: Fan-out + Synthesis
scale: foundational
status: working
forces:
- Information Asymmetry
- Finite Resources
generators:
- Contract at Interfaces
problem: Work that could be parallelized is done sequentially, or parallel outputs remain fragmented without meaningful integration.
signals:
- problem decomposes into independent sub-problems
- sub-problems can be worked simultaneously
- diverse perspectives must be integrated, not concatenated
stages:
- name: prepare
  sheets: 1
  instrument_guidance: claude-code or codex-cli — matched to decomposition difficulty; a cheap instrument suffices for simple scoping
  fallback_friendly: true
  purpose: Define scope and shared context.
  artifacts: []
- name: analyze
  sheets: fan_out(6)
  instrument_guidance: claude-code or codex-cli — capability must match analysis grain; diverse instruments only if independence is the goal (else interchangeable)
  fallback_friendly: true
  purpose: Work independent facets in parallel.
  artifacts: []
- name: synthesize
  sheets: 1
  instrument_guidance: claude-code or codex-cli — stronger than the producers — integration is higher-order work; a cheap fallback risks concatenation
  fallback_friendly: false
  purpose: Integrate parallel outputs, addressing cross-cutting themes.
  artifacts: []
dependencies:
  analyze:
  - prepare
  synthesize:
  - analyze
composes_with:
- pattern: Join-Semilattice Merge
  how: substitution — replaces the judge-synthesis with an algebraic join when facts are additive
- pattern: Attested Merge Gate
  how: substitution — replaces trust-the-merge with contracted, attested, swept merging
- pattern: Skeptical Oracle
  how: substitution — replaces trust-the-findings with deterministic reconstruction
- pattern: Proof-Carrying Artifact
  how: layering — wraps the fan-out so synthesis consumes only admitted evidence
- pattern: The Dropped Axiom
  how: the typing clause — every merge declares its aggregation rule and dropped axioms
- pattern: The Declared Window
  how: the window clause — synthesis over bounded lookback emits a window manifest
type: orchestration-pattern
---

## Fan-out + Synthesis (Foundational Primitive)


**Status:** Working. **Source:** ubiquitous; iterations 1–4, confirmed iteration 5 (all six expeditions were forbidden from returning it; the ban is the confirmation — every voice had to position its discoveries against this move, and all six reported the territory around it as saturated); re-confirmed iteration 6. Prior art: MapReduce.

**Core Dynamic.** Split work into parallel independent streams, merge in a synthesis stage. The boundary condition the corpus earned in iteration 5 stands: fan-out answers *who does what in what order* — and the perpendicular questions (who is authorized, what evidence traveled, who owns failure, when to stop) are not answerable inside it. Every communication and adaptation pattern in this corpus is a wrapper around this move, not a replacement for it.

**When to use:** the problem decomposes into independent sub-problems with a meaningful merge, and the merge can be trusted or made trustworthy.

**When NOT to use:** sub-problems share mutable state (isolated writers + a merge authority); synthesis is trivial concatenation (a pure join, no judge); fan-out width of 1 suffices; or the outputs must *agree* rather than integrate.

**Marianne Score Structure**

```yaml
movements:
  1: { name: prepare }
  2: { name: analyze }
  3: { name: synthesize }

sheet:
  total_items: 3
  fan_out: { 2: 6 }
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Define scope. Write {{ workspace }}/scope.md and stop.
    {% elif stage == 2 %}
    Analyze module {{ instance }}. Write {{ workspace }}/analysis-{{ instance }}.md and stop.
    {% elif stage == 3 %}
    Read all analysis files. Produce a unified review addressing cross-cutting concerns.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/scope.md"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/analysis-{instance}.md"
    condition: "stage == 2"
  - type: command_succeeds
    # Quorum floor 4-of-6 is a DECLARED degradation decision: two dead analysts
    # must not kill the synthesis, but the synthesis must know what it is missing.
    command: 'test $(ls {workspace}/analysis-*.md | wc -l) -ge 4'
    condition: "stage == 3"
```

**Near-miss:** six analysts all reading each other's outputs "for coherence" — independence destroyed before the merge; you paid for a fan-out and got one committee with six names.

**Example.** Six-region market analysis: one sheet per region, one synthesis, wrapped in Proof-Carrying Artifact sidecars so the synthesis consumes only admitted evidence.

---
# Communication Patterns

*v4 had one pattern at this scale — the declared critical deficit. Six enter v5.1. The group's discovery: shared files as a medium for **permission and phase** (who may act, on what, valid until when, superseded by whom), where v4's Stigmergic Workspace used them as a medium for content. Acknowledgement that lives in a prompt is vibes; acknowledgement that lives in a workspace file with a timestamp is a receipt.*

### Review Integration

Iteration 5 reclassified this from a score-level peer pattern to a foundational primitive. The revision names its boundary: it allocates parallel work, but evidence, authority, custody, and termination require wrappers. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.

Iteration 6: the v6 draft re-promoted this to a counted core pattern; Reviews 1 and 2 reversed the re-promotion unanimously ("a primitive, not a differentiated corpus pattern" / "keep it as syntax and remove it from the pattern count") — it remains a foundational primitive, uncounted. The two iteration-6 clauses survive as named contracts attached at the merge, not as reasons to re-count it: the **typing clause** (The Dropped Axiom's `{aggregation_rule, axioms_dropped, declared_authority}` header on every merge) and the **window clause** (The Declared Window's manifest on bounded-lookback synthesis). Both are recorded in `composes_with`.
