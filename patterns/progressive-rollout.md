---
name: "Progressive Rollout"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Full deployment before validation risks large-scale failure; incremental rollout with monitoring gates progression but requires coordinating batch selection, execution, and go/no-go decisions across phases."
signals:
  - "works on 5 doesn't guarantee works on 500"
  - "need to detect scaling issues before full deployment"
  - "rollback from 100% deployment is expensive"
  - "early validation could prevent large-scale failures"
config_features:
  - "self_chaining"
  - "fan_out"
  - "max_chain_depth"
  - "inherit_workspace"
fan_out:
  execute-batch: 5
stages:
  - name: select-batch
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading YAML state, computing batch sizes, and updating rollout state; algorithmic task suitable for any tier"
    fallback_friendly: true
    purpose: "Select the next batch based on current rollout phase and update state."
    artifacts: ["current-batch.yaml", "rollout-state.yaml"]
  - name: execute-batch
    sheets: "fan_out(5)"
    instrument_guidance: "score-author's choice — instrument depends on the actual work being rolled out (refactoring needs strong code reasoning, data migrations may need specific domain knowledge)"
    fallback_friendly: false
    purpose: "Process items in the current batch with 5 parallel workers."
    artifacts: []
  - name: monitor
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of analyzing results, computing error rates, and making threshold-based go/no-go decisions"
    fallback_friendly: true
    purpose: "Compute health metrics and determine whether to proceed to the next phase."
    artifacts: ["phase-verdict.yaml"]
composes_with:
  - pattern: "Canary Probe"
    how: "Canary Probe provides the initial safety probe that becomes phase 1 of Progressive Rollout's graduated deployment sequence."
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine analyzes failed items from each rollout phase to determine whether failures are systemic or isolated."
---

## Progressive Rollout

`Status: Working` · **Source:** DevOps graduated deployment, feature flags, Expedition 5. **Scale:** concert-level. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Apply a change in PHASES with increasing scope. Each phase's success GATES the next. Each phase's monitoring INFORMS the next's parameters. Different from Canary Probe (probe-then-full). Progressive Rollout is probe → 10% → 25% → 50% → 100%.

**Implementation note:** Marianne's `instances` field is static per score execution. The rollout achieves graduated scaling through the select-batch sheet: each self-chain iteration reads `rollout-state.yaml` to determine which items are in the current batch. The instance count stays fixed (e.g., 5 parallel workers), but the batch selection grows across iterations.

### When to Use / When NOT to Use

Use for large-scale migrations, multi-repository changes, any operation where "works on 5" doesn't guarantee "works on 500." Not when items are not independent or monitoring can't distinguish success from luck.

### Marianne Score Structure

```yaml
sheets:
  - name: select-batch
    prompt: >
      Read rollout-state.yaml (or initialize if first run).
      Select the next batch: phase 1 = 3 items, phase 2 = 20, phase 3 = 80, phase 4 = remainder.
      Write current-batch.yaml and update rollout-state.yaml with phase number and processed items.
    capture_files: ["rollout-state.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/current-batch.yaml"
  - name: execute-batch
    instances: 5
    prompt: "Read current-batch.yaml. Process items assigned to worker {{ instance_id }}."
    capture_files: ["current-batch.yaml"]
  - name: monitor
    prompt: >
      Compute health metrics for this phase. Write phase-verdict.yaml:
      {go: bool, phase: N, confidence, items_processed, items_remaining, error_rate}.
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; v=yaml.safe_load(open('{{ workspace }}/phase-verdict.yaml')); assert v.get('go', False), f'Phase {v.get(\"phase\")} failed: error_rate={v.get(\"error_rate\")}'\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Early phases pass with small samples but later phases fail at scale — sampling bias. If error rate exceeds threshold at any phase, the rollout pauses (self-chain breaks on failed validation) and Dead Letter Quarantine analyzes failures. `max_chain_depth` prevents infinite rollout if the termination condition (`items_remaining == 0`) isn't reached.

### Composes With

Canary Probe (canary IS phase 1), Dead Letter Quarantine (failed items in each phase), Stratification Gate (N consecutive healthy phases before advancing)
