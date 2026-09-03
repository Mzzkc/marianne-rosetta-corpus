---
name: "Andon Cord"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Exploit Failure as Signal"
problem: "Validation failures are retried blindly without diagnosing root cause, wasting resources on repeated errors."
signals:
  - "validation failures repeat the same error across retries"
  - "failure output is informative but gets ignored"
  - "retry costs are high (~$1+ per attempt)"
  - "agent needs corrective guidance, not just another attempt"
stages:
  - name: generate
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must be capable enough for the implementation task; pattern focuses on failure handling workflow rather than generation instrument selection"
    fallback_friendly: true
    purpose: "Generate the initial implementation."
    artifacts: ["test-output.log"]
  - name: diagnose
    sheets: 1
    instrument_guidance: "capable instrument (codex-cli (gpt-5.5) or claude-code recommended) — diagnostic reasoning is load-bearing; failure mode explicitly mentions claude-code for triage to ensure accurate root cause analysis"
    fallback_friendly: false
    purpose: "Analyze failure output and identify root cause with concrete fix plan."
    artifacts: ["andon-diagnosis.md"]
  - name: regenerate
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — same capability tier as generate stage; applies the identified fix rather than performing full regeneration"
    fallback_friendly: true
    purpose: "Apply the diagnosis to fix the identified issue without rewriting from scratch."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker monitors instrument-level failures across tasks; Andon Cord diagnoses task-level validation failures within a single workflow, operating at different failure scopes."
  - pattern: "Quorum Trigger"
    how: "Quorum Trigger activates Andon Cord when multiple validation failures reach threshold, preventing single-failure noise from triggering expensive diagnosis stages."
  - pattern: "Commissioning Cascade"
    how: "Commissioning Cascade verifies outputs at multiple quality gates; Andon Cord provides the diagnostic-and-fix mechanism when any commissioning tier fails validation."
---

## Andon Cord

`Status: Working` · **Source:** Toyota Production System stop-the-line, Expedition 1. **Scale:** adaptation. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

Replaces blind retry with diagnostic intervention. On validation failure: detect → stop (don't retry blindly) → diagnose (dedicated diagnostic sheet reads failure output) → fix (inject diagnosis as cadenza) → resume (re-run with new context). Transforms failure response from stochastic retry to deterministic diagnosis.

**Relationship to self-healing:** Marianne's conductor-level self-healing feature implements a similar detect-diagnose-fix loop. Andon Cord is the score-level pattern — you compose it explicitly in your YAML. Self-healing is the conductor-level implementation that applies automatically. Both exist at different abstraction levels.

### When to Use / When NOT to Use

Use when failures are diagnostic (agent misunderstood the task, missed a constraint), when failure output contains enough information to diagnose root cause, or when retry cost justifies a diagnostic stage (~$1+ per attempt). Not when failures are stochastic (network timeouts — just retry), failure output is empty, or diagnosis cost exceeds a few blind retries.

### Marianne Score Structure

```yaml
sheets:
  - name: generate
    prompt: "Generate the REST API implementation."
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && pytest -x 2>&1 | tee {{ workspace }}/test-output.log; exit ${PIPESTATUS[0]}"
  - name: diagnose
    prompt: |
      The previous stage failed validation. Read the failed output and test results.
      Write andon-diagnosis.md with:
      ROOT CAUSE: (what specifically went wrong)
      FIX PLAN: (concrete steps to fix)
    capture_files: ["**/*.py", "test-output.log"]
    validations:
      - type: content_contains
        content: "ROOT CAUSE:"
      - type: content_contains
        content: "FIX PLAN:"
  - name: regenerate
    prompt: "Read andon-diagnosis.md. Fix the identified issue. Do not rewrite from scratch."
    capture_files: ["andon-diagnosis.md", "**/*.py"]
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && pytest -x"
```

### Failure Mode

Diagnosis is wrong — the root cause analysis misidentifies the problem, and the fix introduces new failures. Validate that the regenerated output passes the SAME validation that the original failed. If diagnosis consistently fails, fall back to a more capable instrument for the diagnostic sheet (Opus for triage, per CEGAR Loop strategy).

### Composes With

Circuit Breaker (andon for task failure, circuit breaker for instrument failure), Quorum Trigger (quorum triggers andon), Commissioning Cascade (andon at each commissioning tier)
