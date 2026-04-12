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
    instrument_guidance: "score-author's choice — initial batch processing; proof score demonstrates haiku for cost efficiency, but any capable instrument works"
    fallback_friendly: true
    purpose: "Process batch items in parallel, writing success results to workspace files."
    artifacts: ["result-*.md"]
  - name: collect
    sheets: 1
    instrument_guidance: "score-author's choice — failure detection and categorization; needs judgment to classify error types and extract symptoms from missing/malformed outputs"
    fallback_friendly: true
    purpose: "Identify failed items from missing or invalid outputs and create structured quarantine manifest."
    artifacts: ["quarantine.yaml"]
  - name: analyze-quarantine
    sheets: 1
    instrument_guidance: "capable instrument required — cross-failure pattern analysis is the core Dead Letter Quarantine dynamic; identifies systematic causes not visible in individual failures; proof score recommends opus"
    fallback_friendly: false
    purpose: "Analyze quarantined items to identify common failure patterns and design adapted reprocessing strategies."
    artifacts: ["quarantine-analysis.md"]
  - name: reprocess
    sheets: 1
    instrument_guidance: "score-author's choice — applies adapted strategies from analysis; needs sufficient capability for the underlying task (code generation, data transformation, etc.)"
    fallback_friendly: true
    purpose: "Reprocess quarantined items using adapted strategies that address identified root causes."
    artifacts: ["reprocess-results.yaml"]
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
