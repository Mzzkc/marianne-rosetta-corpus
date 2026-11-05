---
name: "Dead Letter Quarantine"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "dead-letter-quarantine.yaml"
forces:
  - "Partial Failure"
  - "Information Asymmetry"
  - "Finite Resources"
generators:
  - "Exploit Failure as Signal"
  - "Accumulate Knowledge"
problem: "Batch processing repeatedly fails on the same items because no systematic analysis identifies root causes or adapts strategy."
signals:
  - "some items consistently fail across retries"
  - "batch processing has persistent partial failures"
  - "retry loops waste resources on unfixable items"
  - "no visibility into why certain items fail while others succeed"
  - "failures seem random but may have underlying patterns"
fan_out:
  process: 10
config_features:
  - fan_out
stages:
  - name: process
    sheets: "fan_out(10)"
    instrument_guidance: "score-author's choice — initial batch processing; proof score demonstrates opencode for cost efficiency, but any capable instrument works"
    fallback_friendly: true
    purpose: "Process batch items in parallel, writing success results to workspace files."
    artifacts: ["result-*.md"]
  - name: collect
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — failure detection and categorization; needs judgment to classify error types and extract symptoms from missing/malformed outputs"
    fallback_friendly: true
    purpose: "Identify failed items from missing or invalid outputs and create structured quarantine manifest."
    artifacts: ["quarantine.yaml"]
  - name: analyze-quarantine
    sheets: 1
    instrument_guidance: "capable instrument required — cross-failure pattern analysis is the core Dead Letter Quarantine dynamic; identifies systematic causes not visible in individual failures; proof score recommends claude-code"
    fallback_friendly: false
    purpose: "Analyze quarantined items to identify common failure patterns and design adapted reprocessing strategies."
    artifacts: ["quarantine-analysis.md"]
  - name: reprocess
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — applies adapted strategies from analysis; needs sufficient capability for the underlying task (code generation, data transformation, etc.)"
    fallback_friendly: true
    purpose: "Reprocess quarantined items using adapted strategies that address identified root causes."
    artifacts: ["reprocess-results.yaml"]
dependencies: {}
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate's BLACK-category items (reject/quarantine) feed directly into Dead Letter Quarantine's collection stage for batch pattern analysis."
  - pattern: "Screening Cascade"
    how: "Screening Cascade's rejected items route to Dead Letter Quarantine, where accumulated rejections reveal systematic criteria gaps in the screening filters."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker halts processing and routes tripped failures to Dead Letter Quarantine for root cause analysis before resuming."
  - pattern: "Immune Cascade"
    how: "Dead Letter Quarantine handles items that fail Immune Cascade's successive verification stages, analyzing what defects survived earlier tiers."
  - pattern: "After-Action Review"
    how: "After-Action Review can analyze Dead Letter Quarantine's pattern-finding process itself, extracting doctrine about what kinds of failures cluster."
---

## Dead Letter Quarantine

`Status: Working` · **Source:** RabbitMQ/Kafka dead letter queues, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

After N retries, STOP RETRYING AND QUARANTINE. Move failed items to a separate processing path with different handling: different instruments, different prompts, different strategy. The quarantine is an ARTIFACT that persists, accumulates, and can be ANALYZED. "Why did these 7 items fail?" often reveals a systematic issue that fixing once clears the entire quarantine.

### When to Use / When NOT to Use

Use for any batch processing where some items are expected to fail, self-chaining scores where iteration N should not re-attempt items from N-1, or concert-level routing of failures to a different score. Not when every item MUST succeed, failures are truly random, or the quarantine grows to dwarf successful items (the pipeline itself is broken).

### Marianne Score Structure

```yaml
sheets:
  - name: process
    instances: 10
    prompt: "Process item {{ instance_id }}. Write result-{{ instance_id }}.md on success."
  - name: collect
    prompt: >
      Identify failures (missing or empty result files). Write quarantine.yaml listing
      failed items with {item_id, error_symptom, attempted_strategy}.
    capture_files: ["result-*.md"]
  - name: analyze-quarantine
    prompt: >
      Read quarantine.yaml. Identify common failure patterns.
      Write quarantine-analysis.md with: {pattern, affected_items, suggested_strategy}.
    capture_files: ["quarantine.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/quarantine-analysis.md"
  - name: reprocess
    prompt: >
      Read quarantine-analysis.md. For each failure pattern, apply the suggested strategy.
      Write reprocess-results.yaml: [{item_id, outcome: success|permanent_quarantine, detail}].
    capture_files: ["quarantine.yaml", "quarantine-analysis.md"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; r=yaml.safe_load(open('{{ workspace }}/reprocess-results.yaml')); success=[e for e in r if e['outcome']=='success']; print(f'{len(success)}/{len(r)} reprocessed successfully')\""
```

### Failure Mode

Quarantine analysis finds no patterns — items failed for unrelated reasons. The reprocess stage still runs but the "adapted strategy" has nothing to adapt from. In this case, escalate to a more capable instrument (Opus) rather than repeating the same strategy. If the quarantine grows across self-chain iterations, the pipeline itself needs debugging, not the items.

### Composes With

Triage Gate (BLACK category feeds quarantine), Screening Cascade (rejected items go to quarantine for pattern analysis), Circuit Breaker (circuit-tripped failures enter quarantine)

### Discover Pass 1, Cycle 7 — The Automatic Curriculum Fold

This pass folded the draft's **Automatic Curriculum** into this pattern (Reviews 1 and 2: "substantially re-proves Dead Letter Quarantine — failure → analyze/carry evidence → adapted regeneration → revalidate; transport is not a new control structure"; "literally a one-line YAML key"). DLQ already proves batch quarantine, cross-failure analysis, adapted reprocessing, and final verification; the fold adds what the draft got right:

**Conductor-mediated failure transport.** A `sheet.loops` generate→validate pair where the generate sheet's wrapped prompt carries `failure_history` — the conductor injects it; no human copies anything. The moment a human must move the lesson from log to prompt, the loop leaks. This is DLQ's evidence-carrying stage with the transport made automatic. Honest relation to Back-Slopping: same shape, but Back-Slopping is *curated* seed transfer; this is conductor-mediated and therefore cannot be forgotten.

**Failure direction is the test.** Iteration N+1's output must differ from iteration N *in the direction the feedback pointed* — the corrected control (Review 2: stochastic generation owes direction, not byte-identical recurrence): assert the *omission of the cited violation*, never the reproduction of the exact prior failure string. Negative control: the same score under `raw` prompt mode (which omits `failure_history`) must reproduce the *class* of failure — the sentinel asserts the round-1 violation's signature reappears — while the wrapped mode's round-2 output passes the violation-absence check.

**Context budget and the zero trap.** Bound history with a small positive `lookback_sheets` — **0 means ALL completed sheets, not none** (workspace.py:346, per the v6 archive) — and record the failure *class*, not the incident, so transient noise doesn't teach superstition.
