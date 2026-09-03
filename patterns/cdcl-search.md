---
name: "CDCL Search"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
  - "Exploit Failure as Signal"
problem: "Iterative processes repeat the same failures because no mechanism captures and propagates failure patterns as constraints."
signals:
  - "same failures occur across retry attempts"
  - "retries don't help because nothing is learned"
  - "failures contain diagnostic information that could prevent recurrence"
  - "need to avoid known bad paths in subsequent iterations"
config_features:
  - "self_chaining"
  - "inherit_workspace"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — instrument capability must match the task being attempted; learned clauses guide behavior but don't reduce the task's inherent capability requirements"
    fallback_friendly: false
    purpose: "Attempt the task while avoiding failure patterns documented in learned-clauses.yaml from previous iterations."
    artifacts: []
  - name: analyze-failure
    sheets: 1
    instrument_guidance: "codex-cli (gpt-5.5) or claude-code recommended — requires strong reasoning to extract generalizable failure patterns; weak instruments produce clauses that are too specific (don't generalize) or too broad (over-constrain)"
    fallback_friendly: false
    purpose: "Extract the root cause of failure and append it as a constraint to learned-clauses.yaml to guide future attempts."
    artifacts: ["learned-clauses.yaml"]
dependencies: {}
composes_with:
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) provides the learning inheritance mechanism; CDCL Search uses it to accumulate and forward learned failure clauses across self-chaining iterations."
  - pattern: "After-Action Review"
    how: "After-Action Review extracts lessons post-execution for human learning; CDCL Search's analyze-failure stage performs similar extraction inline for machine learning between iterations."
  - pattern: "CEGAR Loop"
    how: "Both are iterative constraint refinement patterns — CEGAR Loop refines abstractions when verification fails, CDCL Search refines the search space by adding failure-derived clauses; compose by using CDCL for failure learning within CEGAR's refinement loop."
---

## CDCL Search

`Status: Working` · **Source:** Conflict-driven clause learning (SAT solving). **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

When a branch fails, extract WHY it failed and add the failure reason as a new constraint. The constraint prevents the same failure pattern in subsequent iterations. Learning from failure, not just retrying.

### When to Use / When NOT to Use

Use when failures are informative and recurring patterns are likely. Not when failures are random.

### Marianne Score Structure

```yaml
sheets:
  - name: attempt
    prompt: "Read learned-clauses.yaml. Attempt the task avoiding known failure patterns."
    capture_files: ["learned-clauses.yaml"]
  - name: analyze-failure
    prompt: "If attempt failed, extract failure reason. Append to learned-clauses.yaml."
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; c=yaml.safe_load(open('{{ workspace }}/learned-clauses.yaml')); print(f'{len(c)} clauses learned')\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Learned clauses are too specific (don't generalize) or too broad (over-constrain). Validate clause quality.

### Composes With

Back-Slopping (Learning Inheritance), After-Action Review, CEGAR Loop
