---
name: "The Hotwash Dispatch (Lesson Routing)"
scale: iteration
status: approximation
forces: [Information Asymmetry, Convergence Imperative]
generators: [Exploit Failure as Signal]
problem: "Failure evidence accumulates in run records but no downstream sheet has committed to change behavior on it, so lessons dispatch into the void as context noise."
signals:
  - "self-improvement loops where iteration N+1 should learn from iteration N's actual validation failures"
  - "failure logs grow while prompts stay identical"
  - "evidence without a named consumer is being carried forward anyway"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "work instrument; wrapped prompt receives prior failures via the loop's failure transport"
    fallback_friendly: true
    purpose: "The work; its validation failures are the raw material."
  - name: validate
    sheets: 1
    instrument_guidance: "real validations — the failures land in the engine's record"
    fallback_friendly: false
    purpose: "Honest failure surface; no paraphrase."
  - name: classify
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — maps validation codes through the digest-pinned dispatch-table.yaml to consuming sheets and failure classes; writes curriculum/{class}.json"
    fallback_friendly: false
    purpose: "Deterministic routing; unmapped codes land in curriculum/unclaimed/ and are COUNTED — the honesty meter."
dependencies:
  validate: [attempt]
  classify: [validate]
composes_with:
  - pattern: "After-Action Review"
    how: "AAR owns reflection and capture; Hotwash owns routing the evidence to a pre-committed consumer — the neighbor this pattern must never duplicate (the Newcomer's catch)"
  - pattern: "The Paid Question"
    how: "same demand-register logic, transposed from questions to lessons"
  - pattern: "Serial Troponin"
    how: "the loop spine — unproven together, proven together"
  - pattern: "The Spent Lesson Checkout"
    how: "the other half of the lifecycle, now independently provable (the split)"
type: orchestration-pattern
---

## The Hotwash Dispatch (Lesson Routing)

**Status:** approximation — the failure-transport surface (`failure_history` for the retry-local case, and any cross-iteration carrier) is native-unproven; the classification and routing machinery itself is ordinary files + CLI and composes today against an explicit failure-report file if the engine transport never lands. **The split (the Practitioner's):** the draft fused dispatch and checkout into one seven-stage monolith riding two unproven surfaces at once; each half now stands alone with its own debt named.

**Core Dynamic.** On the failure-evidence channel: a failure enters the curriculum only if a *named downstream sheet in the next iteration has pre-registered that it will change behavior on that failure class* — otherwise it dies as a logged non-event in `unclaimed/`, counted. Evidence without an owner is noise; the consumer pays for the lesson by pre-committing to consume it. The dispatch table is digest-pinned; a renamed consumer dispatches into the void — which the count catches.

**Validations.** Every `curriculum/{class}.json` names a consuming sheet that exists in the score; the next attempt's output cites the curriculum files it consumed (line-anchored `content_regex`). **Sentinel:** a synthetic failure code planted in the table with no consumer → `test $(ls curriculum/unclaimed/ | wc -l) -ge 1` — the run FAILS if unclaimed failures silently dispatched anyway.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
