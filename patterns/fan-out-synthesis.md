---
name: "Fan-out + Synthesis"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Work that could be parallelized is done sequentially, wasting time, or parallel outputs remain fragmented without meaningful integration."
signals:
  - "problem decomposes into independent sub-problems"
  - "sub-problems can be worked on simultaneously"
  - "need to integrate diverse perspectives or findings"
  - "synthesis must address cross-cutting themes, not just concatenate"
fan_out:
  analyze: 6
stages:
  - name: prepare
    sheets: 1
    instrument_guidance: "score-author's choice — sonnet or opus for complex problem decomposition requiring clear scope definition; haiku may suffice for simple scoping tasks"
    fallback_friendly: true
    purpose: "Define scope and shared context for parallel analysis."
    artifacts: ["scope.md"]
  - name: analyze
    sheets: "fan_out(6)"
    instrument_guidance: "score-author's choice — instrument capability must match the analysis complexity; sonnet recommended for code review or detailed analysis; haiku suffices for simple classification or data extraction"
    fallback_friendly: true
    purpose: "Analyze independent facets in parallel, each producing separate findings."
    artifacts: ["analysis-{{ instance_id }}.md"]
  - name: synthesize
    sheets: 1
    instrument_guidance: "sonnet or opus — synthesis requires finding cross-cutting themes and integrating diverse perspectives, higher-order reasoning beyond what produced individual analyses; fallback to cheaper instruments risks mere concatenation"
    fallback_friendly: false
    purpose: "Read all parallel outputs and produce unified result addressing cross-cutting concerns."
    artifacts: []
composes_with:
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before fan-out, preventing output format drift across parallel instances."
  - pattern: "Shipyard Sequence"
    how: "Shipyard Sequence validates the prepare stage's scope before expensive fan-out begins, preventing cascading rework."
  - pattern: "After-Action Review"
    how: "After-Action Review provides a coda on the synthesis stage, extracting lessons from the integration process."
  - pattern: "Triage Gate"
    how: "Triage Gate classifies parallel outputs by quality before synthesis, allowing the synthesis stage to handle different quality tiers differently."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses verbose parallel outputs before synthesis, reducing synthesis complexity when fan-out produces high-volume results."
---

## Fan-out + Synthesis

`Status: Working` · **Source:** Ubiquitous — confirmed across all expeditions. Prior art: MapReduce (Dean & Ghemawat, 2004).

### Core Dynamic

Split work into parallel independent streams, merge in a synthesis stage. N agents work simultaneously on different facets. A final agent reads all outputs and produces a unified result. Most score-level patterns in this corpus build on, modify, or explicitly reject this structure. It is the default move when information asymmetry meets finite resources.

### When to Use / When NOT to Use

Use when the problem decomposes into independent sub-problems with a meaningful merge. Not when sub-problems share mutable state, synthesis is trivial concatenation, or fan-out width of 1 suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: prepare
    prompt: "Define scope and shared context for the analysis."
    validations:
      - type: file_exists
        path: "{{ workspace }}/scope.md"
  - name: analyze
    instances: 6
    prompt: "Analyze module {{ instance_id }}. Write findings to analysis-{{ instance_id }}.md."
    capture_files: ["scope.md"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/analysis-{{ instance_id }}.md"
  - name: synthesize
    prompt: "Read all analysis files. Produce a unified review addressing cross-cutting concerns."
    capture_files: ["analysis-*.md"]
    validations:
      - type: command_succeeds
        command: "test $(ls {{ workspace }}/analysis-*.md | wc -l) -ge 4"
```

### Failure Mode

Synthesis produces concatenation rather than integration. Validate with `command_succeeds` checking the synthesis references cross-cutting themes, not just individual reports. If fan-out agents share state, outputs will converge — use Prefabrication with interface contracts instead.

### Composes With

Barn Raising (conventions govern fan-out), Shipyard Sequence (validate before fanning out), After-Action Review (coda on synthesis), Triage Gate (classify outputs before synthesis), Relay Zone (compress before synthesis)

---

# Within-Stage Patterns

*Prompt techniques — these structure a single sheet's prompt, not sheet arrangement.*
