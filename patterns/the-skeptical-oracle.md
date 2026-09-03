---
name: The Skeptical Oracle
scale: score-level
status: working
forces:
- Structured Disagreement
- Information Asymmetry
generators:
- Verify through Diverse Observers
- Contract at Interfaces
problem: Vendor-diverse advisors' findings cannot enter the record without importing their hallucinations.
signals:
- vendor-diverse review fan-outs
- LLM-judge ensembles judging anything mechanically reproducible
- you want the union of different models' coverage without inheriting any model's failures
stages:
- name: propose
  sheets: fan_out(3)
  instrument_guidance: N heterogeneous instruments (claude-code / codex-cli / opencode), each REQUIRED to attach a reproduction pointer to every finding
  fallback_friendly: true
  purpose: Propose findings with reproduction pointers — never conclusions.
  artifacts: []
- name: reconstruct
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — runs every pointer; the test fails or the finding is dropped
  fallback_friendly: false
  purpose: Deterministic reconstruction into a typed verified-findings manifest.
  artifacts: []
- name: interpret
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI family — interprets the VERIFIED manifest only; OPTIONAL consumer, not part of the oracle proper
  fallback_friendly: true
  purpose: Severity, narrative, ordering of verified facts — never generation of them.
  artifacts: []
dependencies:
  reconstruct:
  - propose
  interpret:
  - reconstruct
composes_with:
- pattern: Proof-Carrying Artifact
  how: substitution — the oracle is PCA applied to peer review
- pattern: Immune Checkpoint
  how: layering — recall-side harvest here; precision-side gate there; the pair covers both directions of reviewer error
type: orchestration-pattern
---

## The Skeptical Oracle


**Status:** Working. **Source:** Isabelle/Sledgehammer's untrusted provers. **Scope corrected per Review 2** (the interpretation stage is an optional consumer) **and Review 3** (the oracle must not price out a free-local run).

**Core Dynamic.** N vendor-diverse advisors propose; a deterministic reconstructor disposes. Nothing any advisor says enters the record until it can be *reproduced* — re-derived by a cheap, mechanical process the advisors cannot influence. Heterogeneity is harvested, not trusted: the point of different model families is that they fail differently; the point of reconstruction is that their different failures never become the record's failures. Crucially this is *not* a vote or quorum: voting asks advisors to check each other (peer trust); reconstruction asks a deterministic instrument to check them all (no peer trust at all). Sledgehammer's own numbers set expectations: reconstruction fails about 5% of the time, and those proofs are simply not added.

**The reproduction pointer is a schema, not prose (Review 3):** `{finding_id, kind: failing_test|lint_rule|grep_invariant|reproducer_script, ref: "tests/test_x.py::test_y" | "rule-id" | "pattern + path" | "scripts/repro-N.sh", expected: fail|violation}`. A finding without a pointer is not weakly verified — it is a lead.

**The single-family degraded mode (Review 3):** when only one vendor is available (free-local runs), run N instances of that one family with **disjoint question ownership** — each instance reviews a disjoint slice, so independence of *coverage* is preserved even though independence of *failure* is not. The output is labeled `independence: question-disjoint-single-family` — honest about being the weaker claim. Do not silently relabel it vendor-diverse.

**When to use:** vendor-diverse review fan-outs; ensembles judging anything mechanically reproducible.

**When NOT to use:** claims that are not reconstructible — style judgments, strategy recommendations — where the deterministic reproducer cannot exist, and pretending to have one yields a filter that passes only trivia. Reconstruction as expensive as solving (keep the reconstruction path cheaper than the search). A single advisor (nothing to integrate; verify directly).

**Marianne Score Structure**

```yaml
movements:
  1: { name: propose }
  2: { name: reconstruct, instrument: cli }
  3: { name: interpret }

sheet:
  total_items: 3
  fan_out: { 1: 3 }
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }        # if the deterministic checker is down, the score stops

instruments:
  glm: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_map:
  opus: [1]                              # movement 1 instance routing via instruments +
  codex-cli: [1]                         # fan-out; vendor diversity constructed in config,
  glm: [1]                               # where it is inspectable

prompt:
  template: |
    {% if stage == 1 %}
    Review the subject. EVERY finding must carry a reproduction pointer:
    {finding_id, kind: failing_test|lint_rule|grep_invariant|reproducer_script, ref, expected}.
    Findings without pointers are leads, not findings.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/reproducer-harness.sh" "{{ workspace }}/findings" \
      --run-all-pointers --emit "{{ workspace }}/verified-manifest.json" \
      --quarantine "{{ workspace }}/leads-quarantine.jsonl"
    {% elif stage == 3 %}
    Interpret {{ workspace }}/verified-manifest.json: severity, narrative, ordering.
    You are reading VERIFIED facts. Unverified leads in the quarantine file are
    visible but never confusable with findings.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/reproducer-harness.sh {workspace}/findings --check-only'
    condition: "stage == 2"
  - type: content_regex
    pattern: "repro_id: [A-Za-z0-9_-]+"     # a finding without a reproducer binding is inadmissible
    path: "{workspace}/verified-manifest.json"
    condition: "stage == 2"
```

**Near-miss:** a majority vote across three vendors — peer trust dressed as verification; two coordinated hallucinations outrank one truth.

**Example.** Cross-model code review for a release gate: three families review the diff; only findings that trigger a failing test, a linter rule, or a grep-able invariant violation survive into the report; two other families rank the verified findings for release notes. Unverified hunches sit in a clearly labeled leads file — useful, honest, never confusable with findings.

### Review Integration

Review 2 ended the oracle at proposal, deterministic reconstruction, and quarantine; AI interpretation is only an optional consumer. Review 3 required typed reproduction pointers and an honest degraded mode when only one instrument family is available. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
