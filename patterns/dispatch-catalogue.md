---
name: "The Dispatch Catalogue (MEL)"
scale: adaptation
status: working
forces: [Partial Failure, Finite Resources]
generators: [Threshold-Triggered Switch]
problem: "'Skip it this run' is decided ad hoc under pressure; degraded operation needs ex-ante authorization with compensation and expiry, not runtime judgment."
signals:
  - "instruments, credentials, feeds, or environments have known partial-failure modes worth tolerating for one run but not forever"
  - "the same degradation decision is being remade every run by whoever is tired"
  - "authorization to run degraded should expire, not persist silently"
stages:
  - name: mel-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — reads the AUTHORING-TIME mel.yaml (a versioned input, never generated at runtime) and the defect census defects.jsonl; left-join; emits dispatch-permit.json per matched row with expiry stamped; fails closed on any defect with no row"
    fallback_friendly: false
    purpose: "Deterministic admission: an item with no row is undispatchable, full stop."
  - name: compensate
    sheets: fan_out(K)
    instrument_guidance: "cheap instruments — executing a written procedure is mechanical; K is a PRE-DECLARED roster with per-defect skip_when guards, never a dynamic fan-out"
    fallback_friendly: true
    purpose: "Execute the matched row's compensating conditions; write comp-{item}.receipt.json."
  - name: expiry-audit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — at score end and on resume; expired permits revoke dispatch rights"
    fallback_friendly: false
    purpose: "A revoked item with a dependent stage routes to on_fail: escalate, never silently skipped."
dependencies:
  compensate: [mel-gate]
  expiry-audit: [compensate]
composes_with:
  - pattern: "Capability Census"
    how: "census measures, catalogue authorizes — the two artifacts must never merge, different authorities"
  - pattern: "The Validity Window"
    how: "the permit's expiry is a window with a compensation payload — the composition the corpus lacked"
  - pattern: "Dispatch with Declared Penalty"
    how: "MEL compensates procedurally; CDL prices quantitatively — siblings"
  - pattern: "The Graded Ladder"
    how: "a revoked permit's escalation route"
type: orchestration-pattern
---

## The Dispatch Catalogue (MEL)

**Status:** working · primitives-proven (core); the fleet-membership face carries the `fleet` flag (zero proof executions). Ranked #3 by the collision; the Newcomer named it the strongest entry and its legal e-discovery example "the one I'd show a new user first."

**Core Dynamic.** The corpus's failure clause was `RUNNING → (failure) → DEGRADED → RETREAT/ESCALATE`, armed at runtime by judgment. The MEL is a **different state machine entirely**: `AUTHORIZE (pre-run, static, negotiated) → DISPATCH(degraded ∧ compensated) → WINDOW(expiring) → RESTORE`. The `RUNNING → DEGRADED` transition never happens — the system is *born* dispatched-degraded-and-compensated. Three properties: **ex-ante** — the compensating procedure is written when nobody is tired and nobody is scored on completing this run; **the unit of truth is the exemption catalogue, not the incident** — a typed table, one row per dispatchable failure (item, compensating conditions, repair-interval class A/B/C/D, expiry), and *an item with no row is undispatchable, full stop* (C2 — the closed vocabulary is the safety mechanism); **authorization carries an expiry clock** — a Category C deferral self-revokes in 10 days; authorization is a function of state ∧ time. Three authorities, none producible by the others: the composer authors the catalogue; a deterministic gate consults it; no sheet in the run ever gets a judgment seat over its own admission.

**The repair both flagging reviews demanded (the Practitioner's and the Skeptic's, converged from opposite sides):** the draft's Stage 1 was an LLM sheet generating `mel.yaml` *at runtime* — an ad-hoc judgment wearing the catalogue's clothes, contradicting the pattern's own ex-ante story. The catalogue is now an **authoring-time static asset**, versioned with the score, changed by review, never by the run it governs; the strong reasoner's one judgment seat is discharged at composition time. The compensation stage is a **pre-declared fixed roster** whose per-defect `skip_when` guards consult the permit file — the static DAG cannot spawn sheets from a runtime census, and the pattern no longer pretends otherwise.

**Sentinel (unchanged — it was already right):** a defect with no MEL row must abort dispatch — gate exits nonzero, `dispatch-permit.json` **absent**, failure naming the unmatched item. Not "reviewers notice." Novel failures have no row and the answer is "no dispatch" — correct and unsatisfying, and the pattern says so in When NOT to Use.

**Example.** Legal e-discovery: OCR down for 3 of 40,000 documents. The catalogue row: `ocr-unavailable-for-subset` dispatchable iff affected documents are flagged; compensation = mandatory attorney-review queue; interval C. The gate emits the permit; the compensate roster creates the review queue before any run stage sees a document; the permit expires in 10 days, after which the pipeline refuses to run until OCR is fixed or the catalogue is re-authored.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
