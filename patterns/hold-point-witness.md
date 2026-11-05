---
name: "The Hold-Point Witness"
scale: concert-level
status: approximation
forces: [Partial Failure, Progressive Commitment]
generators: [Threshold-Triggered Switch]
problem: "Some seams must STOP — not fail, not retry — until an authority outside the score signs, and the score must not be able to manufacture that signature for itself."
signals:
  - "deployment gates, publication gates, destructive-test authorization, privacy-affecting sends"
  - "the authority to proceed is a human or external system the score cannot impersonate"
  - "a paused job with no notification is a deadlock wearing a safety vest"
stages:
  - name: prepare-hold
    sheets: 1
    instrument_guidance: "strong reasoner + a notification CLI step (Slack/webhook/console) — the package must be honest, complete, and NOTICED"
    fallback_friendly: false
    purpose: "Assemble the typed witness package (what was done, evidence digests, the specific question) and notify the authority that the hold exists."
  - name: hold
    sheets: 1
    instrument_guidance: "engine machinery — on_success trigger pause: true (flow.py:100-102); the job parks durably; nothing retries, nothing times out into proceeding"
    fallback_friendly: false
    purpose: "The designed stop."
  - name: witness-signature
    sheets: 0
    instrument_guidance: "out of band — the human/external witness writes disposition.json (typed: disposition ∈ {proceed, reject, proceed-with-conditions}, conditions, authority_id, timestamp, pause_event_id, package_digest)"
    fallback_friendly: false
    purpose: "The key is manufactured outside the score, by construction."
  - name: resume-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — first sheet after mzt resume; validates disposition.json's schema, authority_id against the declared roster, package_digest binding, AND freshness: the disposition must name the CURRENT pause event (pause_event_id) and be newer than it"
    fallback_friendly: false
    purpose: "The door checks the key itself; writes unlock.json only on full validation."
  - name: execute-post-hold
    sheets: 1
    instrument_guidance: "the work; skip_when is the refusal predicate (skip when unlock.json absent or invalid)"
    fallback_friendly: true
    purpose: "Proceed under a fully validated unlock."
dependencies:
  hold: [prepare-hold]
  resume-check: [hold]
  execute-post-hold: [resume-check]
composes_with:
  - pattern: "Transfer of Command at the Seam"
    how: "owns the briefing content; this owns the signature protocol and the pause mechanics"
  - pattern: "The Graded Ladder"
    how: "the ladder climbs, the hold point stops — escalate/pause actions feed this seam"
  - pattern: "The Change-Order Ledger"
    how: "a proceed-with-conditions disposition writes an entry before post-hold runs"
  - pattern: "The Watchman's Gate"
    how: "same placement law, different scale"
type: orchestration-pattern
---

## The Hold-Point Witness

**Status:** approximation — pause mechanics are source-cited (`pause: true` flow.py:100-102; `pause_before_chain` orchestration.py:316-323, PAUSED_AT_CHAIN) but the end-to-end seam has zero proof executions (the Skeptic: source citations are not an end-to-end proof); the prove queue's #2 item. The Practitioner confirmed it composable in ten minutes with the notify step added; the Skeptic demanded the trust model, and it is now stated.

**Core Dynamic.** In the inspection test plan, certain joints are *hold points*: the condition exists, the process STOPS until the authorized witness signs, and the signature unlocks exactly the next phase — nothing more. What pass 1 lacked and this adds: the witness signature is a typed artifact with a named authority bound to the package digest, and **resumption without a signature-shaped file is itself a validation failure.** The hold point is not "we paused"; it is "the only key that opens the door is a signed disposition from the named authority — and the door checks the key itself."

**Trust model (the Newcomer's demand, stated once):** `authority_id` is not a cryptographic signature; the trust boundary is **authority-by-file-permission** — the roster and disposition live in workspace paths writable only by the human witness's account, the same doctrine CDL's `margins.yaml` and the pulse keeper rely on. This is honest for workspace-local concerts and must be replaced by real signing for adversarial settings — say so, don't imply it. **Stale-disposition handling (the Skeptic's):** the disposition carries `pause_event_id` and a timestamp; resume-check rejects a disposition naming a different or older pause than the current one — a yesterday's proceed cannot unlock today's hold.

**Negative controls.** A: a disposition from an authority NOT on the roster fails — no unlock, receipt naming the impostor id. B: a digest-mismatched disposition (the package changed after signature — the classic substitution attack) fails. C (the seam itself): resume WITHOUT any disposition.json → the failure receipt names resume-check, NOT execute-post-hold's skip (which merely skips) — proving the refusal lives in the right place even though `skip_when` is fail-open. The exact V1 discipline, demonstrated at the corpus's named unowned seam.

**Example.** Model-release concert: training score completes → hold with the evaluation witness package → data-governance reviewer signs (proceed with condition: EU-market flag off) → resume-check validates id, digest, and pause event → the release score executes with the condition visible in its opening context (a change-order ledger entry, naturally).

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
