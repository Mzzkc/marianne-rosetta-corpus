---
name: "Delphi Convergence"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Information Asymmetry"
generators:
  - "Measure Convergence Character"
problem: "Multiple independent agents must converge without anchoring on early opinions."
signals:
  - "expert opinions vary widely and need to converge"
  - "agents anchor on initial assessments and won't update"
  - "single-round synthesis isn't achieving consensus"
fan_out:
  assess: 3
script_dependencies:
  - "check_convergence.py"
config_features:
  - "fan_out"
  - "self_chaining"
  - "command_succeeds"
stages:
  - name: assess
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — needs strong reasoning capability for expert assessment; codex-cli (gpt-5.5) or claude-code recommended"
    fallback_friendly: false
    purpose: "Each assessor independently evaluates the problem and documents their position, reading prior-round assessments if available."
    artifacts: []
  - name: check-convergence
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — convergence validation via user-supplied script that analyzes assessment variance"
    fallback_friendly: true
    purpose: "Run the convergence check script to determine if assessments have sufficiently converged."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Source Triangulation"
    how: "Source Triangulation verifies consistency across one-pass multi-perspective views; Delphi Convergence extends to iterative rounds where perspectives update toward consensus."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate captures multiple conflicting perspectives; Delphi Convergence iterates those perspectives toward measurable convergence."
---

## Delphi Convergence

`Status: Working` · **Source:** Delphi method (RAND Corporation). **Forces:** Convergence Imperative + Information Asymmetry.

### Core Dynamic

Multiple agents independently assess, then converge through structured rounds. Different from Fan-out + Synthesis (one round). Delphi iterates until convergence — each round shares anonymized prior assessments, allowing agents to update positions.

### When to Use / When NOT to Use

Use when independent expert judgment needs convergence. Not when a single assessment suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: assess
    instances: 3
    prompt: "Read prior round results if they exist. Write your independent assessment."
    capture_files: ["round-*/**"]
  - name: check-convergence
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/check_convergence.py --threshold 0.8"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Agents anchor on first-round assessments and never genuinely update. Validate that positions actually change between rounds.

### Composes With

Source Triangulation, Rashomon Gate

### Discover Pass 1, Cycle 7 — The Anonymous Rounds Fold

This pass folded the draft's **Anonymous Rounds** into this pattern (a collision the reviews did not flag; repaired under the standard Review 3 set at the Graded Net). Delphi already owns the structure — independent rounds, aggregate feedback, convergence detection; the fold adds four sections:

**1. Mechanically computed aggregates as the ONLY between-round feedback.** Each round's panelists see per-item median + interquartile range + an anonymized outlier-reason digest, computed by a CLI stats sub-step — never a sibling's prose. The aggregate IS the metered tap: panelists drink from the median, not the firehose.

**2. The anonymity gate, honestly scoped.** Disjoint output paths in one shared workspace are convention, not access control — the anonymity wall requires path-scoped visibility or per-sheet workspaces for the claim to hold. Within what the engine gives, enforce mechanically: a `content_regex` validation that no aggregate (or panelist output) contains a sibling sheet id — quote a sibling and it trips.

**3. The honest stopping rule.** Stop when the IQR stabilizes across rounds (round-over-round delta below a declared threshold), and **stability itself is the published finding** — a panel that never converges has told you something true about the question. Non-convergence is published, never hidden, and never manufactured away by pressure.

**4. The round cap is load-bearing.** 3–4 rounds; unbounded rounds is deliberation drift.

Boundary paragraph (the newcomer's question, answered): **frames differ → Rashomon Gate; same question over rounds → this pattern; parallel measurements with a declarable additive tolerance → The Misclosure Ledger.** Identical correlated inputs yielding IQR 0 tests the statistic only — the anonymity negative control must instead plant an identifiable sibling answer and assert the aggregate cannot quote it.
