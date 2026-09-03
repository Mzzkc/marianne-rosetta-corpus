---
name: "Circuit Breaker"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
  - "Finite Resources"
generators:
  - "Threshold-Triggered Switch"
problem: "Long-running jobs fail catastrophically or waste resources when instruments become unavailable mid-execution."
signals:
  - "backend outages cause sudden job failures"
  - "primary instrument becomes unavailable mid-concert"
  - "self-chaining jobs lose progress when instruments fail"
  - "cost overruns from repeated retries on broken instruments"
stages:
  - name: check-circuit
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — system introspection only; reads circuit-state.yaml to determine current breaker status (closed/open/half-open)"
    fallback_friendly: true
    purpose: "Read the persistent circuit state and report the current status."
    artifacts: []
  - name: health-probe
    sheets: 1
    instrument_guidance: "ollama — probes the primary instrument's health; if unavailable, the probe fails and triggers circuit opening"
    fallback_friendly: false
    purpose: "Probe the primary instrument's health; record latency and success/failure to guide circuit state transitions."
    artifacts: ["probe-result.yaml"]
  - name: route-work
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — makes routing decisions between primary and fallback based on circuit state; needs logical capability"
    fallback_friendly: false
    purpose: "Read circuit state and probe results; route work to primary instrument (if closed and healthy) or fallback (if open or failed). Update circuit state with new failure counts and timestamps."
    artifacts: ["circuit-state.yaml"]
  - name: consolidate
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — final assembly of outputs from whichever execution path succeeded; straightforward merging task"
    fallback_friendly: true
    purpose: "Merge results from primary or fallback execution paths into a unified output."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine receives items that fail both primary and fallback execution routes for manual inspection."
  - pattern: "Echelon Repair"
    how: "Circuit Breaker can gate escalation within echelon tiers; if a cheaper tier's primary instrument fails, escalate to the next tier instead of falling back."
  - pattern: "Speculative Hedge"
    how: "Speculative Hedge pre-executes with candidate instruments in parallel; Circuit Breaker routes work to the fastest/most reliable hedge when primary is unavailable."
config_features:
  - "self_chaining"
  - "inherit_workspace"
---

## Circuit Breaker

`Status: Working` · **Source:** Nygard's "Release It!" (2007), Netflix Hystrix, Expedition 5. **Scale:** adaptation. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

After N instrument failures, STOP TRYING. Three states: Closed (normal — route to primary instrument), Open (all requests use fallback immediately — zero cost on broken instrument), Half-Open (one probe request — if it succeeds, close; if it fails, reopen). The critical distinction: instrument failure vs. task failure. A circuit breaker on "agent produced bad output" would shut down the pipeline. This is for infrastructure failures — backends crashing, APIs timing out, models OOM-ing.

**Stateful implementation:** The circuit state persists in `circuit-state.yaml` across self-chain iterations. Each execution reads the state, makes routing decisions, and updates the state. The self-chain carries the state forward via `inherit_workspace`.

### When to Use / When NOT to Use

Use for scores using unreliable instruments (external APIs, local models), long-running concerts where backends may degrade mid-execution, or self-chaining scores where instruments become unavailable. Not when failure is in the TASK (not the instrument), when only one instrument is available, or for short scores where manual intervention is faster.

### Marianne Score Structure

```yaml
sheets:
  - name: check-circuit
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml,os; s=yaml.safe_load(open('{{ workspace }}/circuit-state.yaml')) if os.path.exists('{{ workspace }}/circuit-state.yaml') else {'state':'closed','failures':0}; print(f'Circuit: {s[\"state\"]}, failures: {s[\"failures\"]}')\""
  - name: health-probe
    instrument: ollama
    prompt: "Health check. Write probe-result.yaml: {status: ok|fail, latency_ms, error}."
    validations:
      - type: file_exists
        path: "{{ workspace }}/probe-result.yaml"
  - name: route-work
    prompt: >
      Read circuit-state.yaml and probe-result.yaml.
      If circuit CLOSED and probe OK: execute with primary instrument (ollama). Write to primary-output/.
      If circuit OPEN or probe FAIL: execute with fallback instrument (claude). Write to fallback-output/.
      Update circuit-state.yaml: {state, failures, last_check, last_transition}.
    capture_files: ["circuit-state.yaml", "probe-result.yaml"]
  - name: consolidate
    prompt: "Merge results from whichever path completed."
    capture_files: ["primary-output/**", "fallback-output/**"]
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 20
```

### Failure Mode

Circuit opens permanently because the health probe itself is too sensitive (marks transient failures as outages). Use a failure count threshold (e.g., 3 consecutive failures) before opening. If the fallback instrument also fails, the circuit breaker can't help — escalate to Dead Letter Quarantine.

### Composes With

Dead Letter Quarantine (circuit-tripped items go to quarantine), Echelon Repair (circuit breaker per echelon), Speculative Hedge (backup instrument IS the hedge)
