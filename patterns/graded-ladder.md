---
name: "The Graded Ladder"
scale: adaptation
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Accumulated Signal"
  - "Partial Failure"
generators:
  - "Threshold-Triggered Switch"
problem: "Untyped escalation forces every interruption to be maximally expensive (always human) or maximally cheap (always auto) — both wrong at scale."
signals:
  - "every mixed AI/human score"
  - "retries that could silently absorb a real problem"
  - "WARN/INFO codes exist and someone must decide if they're benign"
stages:
  - name: work-with-typed-raise
    sheets: 1
    instrument_guidance: "score-author's choice — emits escalations as a typed enum field, never prose"
    fallback_friendly: true
    purpose: "Do the work; raises carry escalation_type: CONCERN | UNCOMFORTABLE | SAFETY."
    artifacts: ["raises.json"]
  - name: concern-review
    sheets: 1
    instrument_guidance: "cheap instrument — auto-resolve WITH a receipt"
    fallback_friendly: true
    purpose: "Disposition CONCERN raises; append to the receipt ledger."
    artifacts: ["ledger/escalations.md"]
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" == 'SAFETY' -o \"$(jq -r .escalation_type raises.json)\" == 'UNCOMFORTABLE'"
  - name: adjudicate
    sheets: 1
    instrument_guidance: "strong reasoner — must rule before work continues"
    fallback_friendly: false
    purpose: "Disposition UNCOMFORTABLE raises with a written ruling."
    artifacts: []
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" == 'CONCERN' -o \"$(jq -r .escalation_type raises.json)\" == 'SAFETY'"
  - name: safety-pause
    sheets: 1
    instrument_guidance: "instrument: cli — fires the escalate/pause trigger; humans enter here"
    fallback_friendly: false
    purpose: "SAFETY reaches the human seam (hand off to Transfer of Command at the Seam)."
    artifacts: []
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" != 'SAFETY'"
  - name: ledger-gate
    sheets: 1
    instrument_guidance: "instrument: cli — final gate; continuation requires the receipt ledger's unresolved-set to be empty"
    fallback_friendly: false
    purpose: "A gate, not a hope: no disposition, no continuation."
    artifacts: []
dependencies:
  concern-review: ["work-with-typed-raise"]
  adjudicate: ["work-with-typed-raise"]
  safety-pause: ["work-with-typed-raise"]
  ledger-gate: ["concern-review", "adjudicate", "safety-pause"]
composes_with:
  - pattern: "Transfer of Command at the Seam"
    how: "this pattern is the state machine; that one is the handoff protocol at the SAFETY seam"
  - pattern: "The Acknowledged False Alarm"
    how: "the suppress list is the pre-declared CONCERN class"
  - pattern: "Rejoinder Ledger"
    how: "every disposition is a rejoinder — one per raise, none omitted"
config_features:
  - "skip_when (real command syntax, not template control flow)"
  - "instrument: cli"
  - "escalate/pause triggers (UNPROVEN in proof scores)"
---

## The Graded Ladder

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 3 (TeamSTEPPS CUS — Concerned/Uncomfortable/Safety — and the two-challenge rule; aviation CRM). Owns typed escalation, named unowned for three iterations. **Forces:** Accumulated Signal + Partial Failure.

### Core Dynamic

"Escalation" is one word for three different acts. Type the ladder the way CUS types it: **CONCERN** — a WARN or soft signal; auto-resolve *with a receipt*. **UNCOMFORTABLE** — a failed validation or ambiguous judgment; an explicit adjudicator sheet must rule before work continues. **SAFETY** — declared by the raiser in structured output, or reached by the **two-challenge rule**: the same validation failing twice auto-raises one level — the counterweight that keeps auto-resolve from becoming a rubber stamp. The type lives in a typed field, never prose — prose is where expectation bias hides.

Routing is **predeclared branch sheets gated by `skip_when` on the typed artifact** — no template control flow rewriting stages at runtime. The challenge counter's identity key: the **same validation id against the same artifact digest** — generic retry counts never escalate unrelated transients. Buildable counter today: a CLI pre-step counting the sheet's own retry attempts from validation receipts written by `on_fail` post-steps (engine-native); a conductor-state export would be nicer but is unverified (see corpus Open Questions).

### Marianne Score Structure

```yaml
  - name: ledger-gate
    instrument: cli
    command: "test -f ledger/escalations.md && ! grep -q 'DISPOSITION: none' ledger/escalations.md"
    validations:
      - type: command_succeeds
```

**Negative controls:** (a) an item raised twice (same validation id + digest) must land one level up — remove the counter and it auto-resolves forever; (b) a SAFETY raise with the pause trigger removed must still fail the final ledger-gate via the unresolved-set check. **Sentinel:** `field_match` that a CONCERN never reaches the safety-pause path (routing asserted mechanically).

### When to Use

Every mixed AI/human score; every score where retries could silently absorb a real problem; anywhere WARN/INFO codes exist and someone must decide if they're benign.

### When NOT to Use

Vocabulary drift ("this seems maybe bad" is not a type); the human tier reached for anything routine — the ladder exists so SAFETY stays rare and *meaningful*; auto-resolve dispositions unrecorded (an un-receipted auto-resolve is a silent pass-through wearing a badge).

### Composes With

Transfer of Command at the Seam (SAFETY handoff), The Acknowledged False Alarm (suppressions as CONCERN class), Rejoinder Ledger (one disposition per raise)
