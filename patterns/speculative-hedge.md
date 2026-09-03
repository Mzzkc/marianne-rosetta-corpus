---
name: "Speculative Hedge"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Choosing one approach that fails requires expensive restart from scratch, wasting the initial attempt's cost."
signals:
  - "uncertain which approach will work for this problem"
  - "starting over after failed approach costs more than running both"
  - "need guaranteed progress despite approach uncertainty"
  - "multiple valid strategies exist but success is unpredictable"
stages:
  - name: analyze
    sheets: 1
    instrument_guidance: "codex-cli (gpt-5.5) or claude-code — requires strategic analysis to define competing approaches and robust evaluation criteria"
    fallback_friendly: false
    purpose: "Analyze the problem and define two competing approaches with evaluation criteria."
    artifacts: ["hedge-plan.yaml"]
  - name: approach-a
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — instrument must match the task complexity; mechanical transformations may use cheaper instruments than clean-room rewrites"
    fallback_friendly: true
    purpose: "Execute approach A using mechanical transformation strategy."
    artifacts: ["approach-a-result/**"]
  - name: approach-b
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — clean-room rewrites typically need stronger reasoning than mechanical transforms; choose based on actual task complexity"
    fallback_friendly: false
    purpose: "Execute approach B using clean-room rewrite strategy."
    artifacts: ["approach-b-result/**"]
  - name: evaluate
    sheets: 1
    instrument_guidance: "codex-cli (gpt-5.5) or claude-code — must run tests, evaluate results, and make justified winner selection with rationale"
    fallback_friendly: false
    purpose: "Run tests against both approaches and select winner with rationale."
    artifacts: ["hedge-decision.yaml"]
dependencies: {}
composes_with:
  - pattern: "Canary Probe"
    how: "Canary Probe validates each approach on a small subset before Speculative Hedge commits full resources to parallel execution."
config_features:
  - "capture_files"
  - "command_succeeds"
---

## Speculative Hedge

`Status: Working` · **Source:** CPU branch prediction, military COA analysis, financial hedging, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Run DIFFERENT strategies on the SAME problem and commit to whichever succeeds. Not fan-out (same task, different data) — this runs different APPROACHES on the same data. The cost analysis: if retry-from-scratch costs more than running both, hedge.

**Execution note:** In current Marianne, approaches run sequentially (sheets execute in order). This means the delivery time is the SUM of both approaches, not the MAX. The value proposition is not time savings but elimination of the "wrong approach, start over" scenario — you always get at least one valid result. For true parallel hedging, use two separate scores in a concert.

### When to Use / When NOT to Use

Use for migration tasks with unknown edge cases, research with multiple search strategies, any task where "wrong approach, retry" costs more than "both approaches, discard one." Not when both approaches are equally expensive and success rate is high, when budget is hard-capped, or when approaches interfere.

### Marianne Score Structure

```yaml
sheets:
  - name: analyze
    prompt: "Analyze the problem. Define two approaches and evaluation criteria. Write hedge-plan.yaml."
  - name: approach-a
    prompt: "Execute approach A: mechanical transformation. Write all output to approach-a-result/."
  - name: approach-b
    prompt: "Execute approach B: clean-room rewrite guided by tests. Write all output to approach-b-result/."
    capture_files: ["hedge-plan.yaml"]
  - name: evaluate
    prompt: "Run tests against both. Write hedge-decision.yaml: {winner, rationale, test_results}."
    capture_files: ["approach-a-result/**", "approach-b-result/**"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; d=yaml.safe_load(open('{{ workspace }}/hedge-decision.yaml')); assert 'winner' in d\""
```

### Failure Mode

Both approaches fail — the hedge didn't reduce risk, it doubled cost. Mitigate with a Canary Probe on each approach before full execution. If approaches write to the same files (no subdirectory isolation), they clobber each other's output — always use separate output directories.

### Composes With

Canary Probe (canary each approach before full hedge)
