---
name: "Season Bible"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
generators:
  - "Contract at Interfaces"
problem: "Multi-score campaigns lose continuity because agents lack shared memory of prior decisions and evolving constraints."
signals:
  - "scores make decisions inconsistent with earlier work"
  - "agents repeat mistakes or ignore prior learnings"
  - "no central record of evolving state across campaign"
  - "continuity errors accumulate as work progresses"
stages:
  - name: read-bible
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — needs reading comprehension to extract relevant constraints from the bible; any capable instrument"
    fallback_friendly: true
    purpose: "Read season-bible.md to understand current state and constraints before beginning work."
    artifacts: []
  - name: work
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — instrument depends entirely on the nature of the work being performed; bible reading is context, not the task"
    fallback_friendly: false
    purpose: "Execute the actual work while respecting constraints documented in the bible."
    artifacts: []
  - name: update-bible
    sheets: 1
    instrument_guidance: "score-author's choice — needs to write coherent documentation updates; codex-cli (gpt-5.5) or opencode sufficient for most continuity recording"
    fallback_friendly: true
    purpose: "Update season-bible.md with new decisions, state changes, and continuity constraints discovered during work."
    artifacts: ["season-bible.md"]
dependencies: {}
composes_with:
  - pattern: "Lines of Effort"
    how: "Multiple parallel effort lines all read and update the shared bible, maintaining cross-stream continuity."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses accumulated outputs to prevent context overflow; Season Bible preserves canonical state that survives compression, ensuring continuity decisions persist across relayed handoffs."
  - pattern: "Cathedral Construction"
    how: "Long-running iterative construction where the bible accumulates architectural decisions and constraints across iterations."
---

## Season Bible

`Status: Working` · **Source:** Television production (show bible). **Forces:** Producer-Consumer Mismatch.

### Core Dynamic

A mutable reference document that evolves as the campaign progresses. Different from Barn Raising conventions (which are static). The bible records decisions, character evolutions, and continuity constraints. Scores read it before starting and update it after completing.

### When to Use / When NOT to Use

Use for multi-score campaigns needing continuity. Not for single-score work.

### Marianne Score Structure

```yaml
sheets:
  - name: read-bible
    prompt: "Read season-bible.md. Note current state and constraints."
    capture_files: ["season-bible.md"]
  - name: work
    prompt: "Execute work respecting bible constraints."
  - name: update-bible
    prompt: "Update season-bible.md with new decisions and state changes."
    validations:
      - type: content_contains
        path: "{{ workspace }}/season-bible.md"
        content: "Updated:"
```

### Failure Mode

Bible grows stale — scores read it but don't update. Validate update stage actually modifies the bible.

### Composes With

Lines of Effort, Relay Zone, Cathedral Construction
