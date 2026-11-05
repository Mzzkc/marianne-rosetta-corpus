---
name: "Keystone-First Sequencing"
scale: score-level
status: working
forces: [Exponential Defect Cost, Instrument-Task Fit]
generators: [Gate on Environmental Readiness]
problem: "Construction intuition builds big-to-small (biomass ordering), so the artifacts that parameterize the most downstream prompts are built late and every earlier sheet worked under wrong conditions."
signals:
  - "a small upstream artifact (schema, rubric, lexicon) changes the prompts of many downstream sheets"
  - "merge stages reconcile hundreds of small inconsistencies a different order would have prevented"
  - "the expensive instrument's output would amortize across the whole cheap cascade if it ran first"
stages:
  - name: keystone-identification
    sheets: 1
    instrument_guidance: "short analysis sheet; names the leverage set (schema + rubric + lexicon) with a stated reason per item, schema-typed output — its reasoning is recorded, not trusted"
    fallback_friendly: true
    purpose: "Identify which outputs parameterize the most downstream prompts."
  - name: keystone
    sheets: 1
    instrument_guidance: "the strongest reasoner available — keystones are exactly where expensive judgment compounds"
    fallback_friendly: false
    purpose: "Build the leverage set first, alone, with its own quality gate."
  - name: cascade
    sheets: fan_out(N)
    instrument_guidance: "cheap bulk instruments (ollama / cheapest alias) — downstream work is abundant, lower-stakes"
    fallback_friendly: true
    purpose: "Main fan-out, every prompt CARRYING the keystone content via prelude — following in DAG order is not enough."
dependencies:
  keystone: [keystone-identification]
  cascade: [keystone]
composes_with:
  - pattern: "Cathedral Construction"
    how: "keystone-first is the decision rule for what Cathedral builds first; Cathedral owns iterative construction toward a target"
  - pattern: "Prefabrication"
    how: "keystone-first decides which contract Prefabrication freezes first; Prefabrication owns the producer-producer interface"
  - pattern: "The Attested Merge Gate"
    how: "version echoes feed it"
  - pattern: "The Priced Verification Ladder"
    how: "keystones enter at tier 3; cascade artifacts at their own risk class"
  - pattern: "Firing the Pass"
    how: "the keystone is the mise en place the expeditor gates on (kinship edge, permanent-corpus side)"
type: orchestration-pattern
---

## Keystone-First Sequencing

**Status:** working · primitives-proven (dependencies, prelude injection, validations — prime prove-path material). Kept over the Skeptic's fold objection: the Practitioner ranked it among the six strongest, and two reviews beat one. The differentiation the Skeptic demanded is now in-entry (see composes_with): Cathedral Construction owns *iterative construction toward a known target*; Prefabrication owns *interface contracts between producers*; Keystone-First owns *ordering by leverage* — and that selection rule applies to scores with no iteration and no contracts. Where they overlap, keystone-first is the decision rule for what the others build first.

**Core Dynamic.** Ecosystems build *leverage-first*: the component whose presence rewrites the conditions every other component depends on goes in first — even if tiny, even if peripheral. The wolf is a small fraction of the biomass but the prerequisite for the riparian story; willows planted without wolves are elk food. In a DAG, a small set of sheets' outputs *change the prompts of many downstream sheets* — style guides, ground-truth lexicons, schemas, evaluation rubrics. Install them first and gate everything on completion; install them late and rework propagates. This is also *why* mixed-instrument pricing works: the expensive instrument's output amortizes across the whole cheap cascade — the economic argument for instrument mixture in one pattern.

**Sentinel.** A run with the keystone sheet deliberately skipped must fail the version-echo validation across the cascade — cascade work done keyless is the elk-food outcome, caught.

**Example.** Multi-service API documentation score: the OpenAPI spec and terminology lexicon are the wolves; writing endpoint docs before those exist means every doc sheet works under drifting vocabulary and the merge stage reconciles a thousand small inconsistencies a keystone-first order would have prevented.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
