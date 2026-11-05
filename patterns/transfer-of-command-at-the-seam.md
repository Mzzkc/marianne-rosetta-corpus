---
name: "Transfer of Command at the Seam"
scale: adaptation
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Information Asymmetry"
generators:
  - "Contract at Interfaces"
problem: "When work escalates from machine to human, the pause is the trivial half — what's missing is the briefing artifact that lets the receiving commander act without archaeology."
signals:
  - "every pause/escalate trigger and human-in-the-loop approval gate"
  - "every resume-after-overnight"
  - "AI-reviewer handoffs: an adjudicator receiving escalated work needs the same briefing shape"
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — the sheet whose failure trips the seam"
    fallback_friendly: true
    purpose: "Normal work; on terminal failure the seam fires."
    artifacts: []
  - name: briefing
    sheets: 1
    instrument_guidance: "strong reasoner — inputs pinned to job state, validation output, and file facts so its output is verifiable"
    fallback_friendly: false
    purpose: "Compose the five-element briefing BEFORE the hold: situation, resources, objectives, organization, safety."
    artifacts: ["briefing.md"]
  - name: hold
    sheets: 0
    instrument_guidance: "trigger: escalate/pause — nothing runs"
    fallback_friendly: false
    purpose: "The seam itself."
    artifacts: []
  - name: disposition
    sheets: 1
    instrument_guidance: "instrument: cli — atomic temp-and-rename append to the command log, fired by the resume action"
    fallback_friendly: false
    purpose: "Record who resolved, what, effective time — a separate ACCEPTANCE event, never an AI's clock."
    artifacts: ["command-log.jsonl.append"]
  - name: resumed
    sheets: 1
    instrument_guidance: "the work instrument, continuation"
    fallback_friendly: true
    purpose: "Continuation whose prompt includes the disposition verbatim."
    artifacts: []
dependencies:
  briefing: ["work"]
  disposition: ["briefing"]
  resumed: ["disposition"]
composes_with:
  - pattern: "Transfer of Command"
    how: "that pattern owns planned succession between operators; this owns the machine→human seam specifically"
  - pattern: "The Write-Time Record"
    how: "the briefing is a write-time record for the escalation moment — no end-of-run archaeology"
  - pattern: "The Black-Box Ledger"
    how: "the briefing is assembled from the ledger's continuous record, never from the failing sheet's self-report"
config_features:
  - "escalate/pause triggers (UNPROVEN in proof scores)"
  - "instrument: cli"
  - "capture_files"
---

## Transfer of Command at the Seam

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 3 (ICS Transfer of Command, FEMA: five-element briefing + announced effective time). **Force:** Information Asymmetry.

### Core Dynamic

The canonical ICS failure is an incident with two people both believing they hold command, or neither; command is never transferred by silence. The briefing artifact: **situation** (what the job was doing when it stopped), **resources** (which artifacts exist, which instruments ran, what they cost), **objectives** (what "resumed" means, stated as validations), **organization** (which sheets remain, which were skipped, what the skip means), **safety** (what must NOT be resumed and why).

Two prohibitions carry the pattern: the briefing is assembled **from conductor state and workspace facts, never from the failing sheet's self-report** (self-authored review paths are counterfeit), and the effective-time record is not ceremony — but a machine timestamp cannot establish when a human *accepted* command. The **disposition is a separate acceptance event**, fired mechanically by the resume action's first hook.

Ordering (review-corrected): the briefing is assembled and validated **before** the pause trigger — if the hold halted the job first, the briefing sheet might never run.

### Marianne Score Structure

```yaml
  - name: work
    on_fail:
      - run_job: briefing-score.yaml        # emits briefing.md BEFORE the hold
  - name: briefing
    prompt: "Assemble briefing.md with sections SITUATION, RESOURCES, OBJECTIVES, ORGANIZATION, SAFETY from job-state.json, validation-output.txt, and workspace file facts. Do NOT ask the failing sheet."
    validations:
      - type: content_contains
        pattern: "SITUATION:"
      - type: content_contains
        pattern: "RESOURCES:"
      - type: content_contains
        pattern: "OBJECTIVES:"
      - type: content_contains
        pattern: "ORGANIZATION:"
      - type: content_contains
        pattern: "SAFETY:"
  - name: disposition
    instrument: cli
    command: "printf '%s | resolved-by: resume-action | decision: %s\\n' \"$(date -Is)\" \"$MARIANNE_RESUME_DECISION\" > /tmp/cl && mv /tmp/cl command-log.jsonl.append"
  - name: resumed
    capture_files: ["briefing.md", "command-log.jsonl.append"]
    prompt: "Continue. Your first input is the disposition record; the briefing is your situation report."
    dependencies: { file_exists: "command-log.jsonl.append" }
```

Five separate `content_contains` checks — one per section — because a single-phrase luck-pass is exactly what killed rev-1 proofs.

**Negative controls:** escalation fires with briefing assembly removed → the resumed stage cannot start (dependency unmet); a clean run must produce *no* briefing — the gate fails both ways or it's a receipt.

### When to Use

Every `pause`/`escalate` trigger, every human-in-the-loop approval gate, every resume-after-overnight, and AI-reviewer handoffs (the adjudicator needs the same briefing shape or its review is unanchored).

### When NOT to Use

Self-assembled briefings (the failure mode); pauses too short to warrant a document; briefings written but never consumed — the resumed sheet must demonstrably read the disposition record, or it's theater.

### Composes With

Transfer of Command (planned succession), The Write-Time Record, The Black-Box Ledger, The Graded Ladder (this is the SAFETY rung's protocol)
