---
name: "The Acknowledged False Alarm"
scale: adaptation
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Finite Resources"
  - "Partial Failure"
generators:
  - "Threshold-Triggered Switch"
problem: "Suppression lists rot: entries accumulate silently until the suppressed set includes the code that meant the roof was on fire."
signals:
  - "a score run repeatedly over shifting inputs where some codes are known-benign for named reasons"
  - "brownfield pipelines where zero-warning is a multi-month project and you must ship now with honest debt"
  - "an ignore list that has never been reviewed since it was written"
stages:
  - name: acknowledge
    sheets: 1
    instrument_guidance: "strong reasoner — the one place one belongs: writing a mechanism-level benignity argument"
    fallback_friendly: false
    purpose: "PROPOSE a suppression: {code, mechanism_of_benignity, owner, evidence pointer, expiry}. Cannot edit the enacted list."
    artifacts: ["proposed/"]
  - name: enact
    sheets: 1
    instrument_guidance: "instrument: cli — rebuilds the list file from accepted proposals, stamps digest, decrements countdowns"
    fallback_friendly: false
    purpose: "Expired entries drop and their codes revert to failing. The enacted list is digest-pinned."
    artifacts: ["suppress-list.yaml", "suppress-list.sha"]
  - name: run
    sheets: 1
    instrument_guidance: "the working sheets — their VALIDATION SCRIPTS read the list file"
    fallback_friendly: true
    purpose: "Work under the suppressions; unknown codes still fail."
    artifacts: []
dependencies:
  enact: ["acknowledge"]
  run: ["enact"]
composes_with:
  - pattern: "Configuration Control Board"
    how: "enactment is a one-seat CCB — propose and apply are distinguishable acts"
  - pattern: "The Validity Window"
    how: "the countdown is a per-entry TTL; expiry changes behavior, it does not merely log"
  - pattern: "The Graded Ladder"
    how: "the suppress list is the pre-declared CONCERN class"
config_features:
  - "instrument: cli (validation scripts read a workspace list file)"
  - "file_sha256"
engine_note: "validate_suppress is a static score-YAML list today — a runtime sheet cannot alter it. The honest mechanism is scripts reading a list file; validate_suppress is this pattern's DESTINATION when the engine grows dynamic suppression loading."
---

## The Acknowledged False Alarm

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 5 (alert-fatigue economics — 50–80% false-positive rates in SOC triage; medicine's documented acknowledgement of known-benign findings). **Forces:** Finite Resources + Partial Failure.

### Core Dynamic

The naive reading of suppression is "an ignore list," and that reading is how alert fatigue kills regimes. The invariant: **every suppression is a named, reasoned, expiring, reviewable decision — never a permanent silence.** The hidden cost of noise is not the wasted triage; it's the real threat dismissed amid fatigue. Suppressions rot; expiry is the pattern.

Engine honesty: the mechanism is **validation scripts that read a workspace list file** (`scripts/lint.py --ack-file suppress-list.yaml`) — not the engine's static `validate_suppress` key, which a runtime sheet cannot modify. What `validate_suppress` still contributes today is the boundary discipline: ERROR-class codes are never suppressible — the primitive itself forbids it, and the pattern inherits that spine.

A real reason-linter, not a cosmetic one: a proposal must carry **code existence, severity eligibility (WARN-only), owner, expiry, and an evidence pointer** — enact rejects entries lacking any field, mechanically.

### Marianne Score Structure

```yaml
  - name: acknowledge
    prompt: "Propose suppressions for WARN codes proven benign. Each entry: {code, mechanism, owner, evidence, expiry_runs}. Mechanism must name WHY it is benign (e.g., 'partner pads exports with BOM; parser handles'), never 'known issue'."
    response_format: { type: json_object }
  - name: enact
    instrument: cli
    command: "python3 scripts/enact_suppressions.py proposed/ --out suppress-list.yaml --min-fields 5 && sha256sum suppress-list.yaml > suppress-list.sha"
    validations:
      - type: command_succeeds
      - type: file_sha256
  - name: run
    instrument: cli
    command: "python3 scripts/lint.py exports/ --ack-file suppress-list.yaml"
    validations:
      - type: command_succeeds
```

**Negative controls:** (a) a proposal missing the evidence field must be *rejected* by enact (field-count check); (b) an entry whose countdown reaches zero must drop and its code must **fail again** — the control that proves expiry re-arms the alarm; (c) an unknown code must fail the run even with a non-empty list.

### When to Use

Repeated runs over shifting inputs with documented benign codes; brownfield pipelines shipping with honest debt.

### When NOT to Use

Suppressions without expiry (dead even if the YAML is valid); ERROR-class codes (never suppressible); copy-pasted reasons ("known issue" is not a mechanism).

### Composes With

Configuration Control Board (one-seat enactment), The Validity Window (entry TTLs), The Graded Ladder (CONCERN class)
