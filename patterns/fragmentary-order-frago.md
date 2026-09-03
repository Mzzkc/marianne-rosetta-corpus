---
name: "Fragmentary Order (FRAGO)"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
generators: []
problem: "Plans become stale mid-execution when discovered conditions diverge from expectations but no mechanism exists for targeted correction without full replanning."
signals:
  - "earlier stages produced results that invalidate downstream assumptions"
  - "the plan is partially wrong but not wrong enough to discard"
  - "downstream agents need adjusted guidance, not a completely new plan"
  - "conditions discovered mid-execution were not anticipated by the original plan"
stages:
  - name: assess
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — needs enough reasoning to compare actual outputs against the plan and identify meaningful deviations; instrument depends on domain complexity"
    fallback_friendly: true
    purpose: "Read outputs so far, identify deviations from the execution plan, and write frago.md with targeted corrections if needed."
    artifacts: ["frago.md"]
  - name: continue
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must be capable enough for the underlying task; the FRAGO adjustment doesn't change instrument requirements"
    fallback_friendly: true
    purpose: "Read frago.md if it exists and adjust execution approach per the corrections while continuing the original plan."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Read-and-React"
    how: "Read-and-React provides the workspace-driven adaptation mechanism that the continue stage uses to detect and respond to the FRAGO correction document."
  - pattern: "Lines of Effort"
    how: "FRAGO provides mid-execution course corrections to individual lines of effort when they diverge from the convergence plan."
  - pattern: "Mission Command"
    how: "Mission Command defines the original intent envelope; FRAGO adjusts tactical guidance when execution conditions diverge from the original brief without overriding the mission's purpose or end state."
---
## Fragmentary Order (FRAGO)

`Status: Working` · **Source:** Military fragmentary orders. **Forces:** Partial Failure.

### Core Dynamic

Mid-execution course correction via cadenza injection. When earlier stages produce unexpected results, a FRAGO sheet writes a correction document that downstream stages read. Not replanning — targeted adjustments to the existing plan.

### When to Use / When NOT to Use

Use when plans need mid-execution adjustment based on discovered conditions. Not when the plan is too broken for incremental fixes.

### Marianne Score Structure

```yaml
sheets:
  - name: assess
    prompt: "Read outputs so far. Identify deviations from plan. Write frago.md if corrections needed."
    capture_files: ["execution-plan.md", "progress/**"]
  - name: continue
    prompt: "Read frago.md if it exists. Adjust approach per corrections."
    capture_files: ["frago.md", "execution-plan.md"]
```

### Failure Mode

FRAGO contradicts the original plan too severely. Downstream agents can't reconcile. Keep corrections incremental.

### Composes With

Read-and-React, Lines of Effort, Mission Command
