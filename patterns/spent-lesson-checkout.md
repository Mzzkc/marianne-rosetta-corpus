---
name: "The Spent Lesson Checkout"
scale: iteration
status: approximation
forces: [Convergence Imperative, Finite Resources]
generators: [Measure Convergence Character]
problem: "An automatic failure channel with no checkout is a context-debt machine: iteration 30's prompt carries iterations 1–29's failures, most long remediated, each training the current attempt to dodge a ghost."
signals:
  - "long self-chains or shared workspaces where per-iteration context cost is measurable and growing"
  - "prompts carry failures no current sheet has failed for many iterations"
  - "lessons leave the curriculum by silence, not by receipt"
stages:
  - name: track
    sheets: 1
    instrument_guidance: "any-wrapped CLI — appends each iteration's failure classes to curriculum-history.csv (class, iteration, present/absent, signature)"
    fallback_friendly: false
    purpose: "The claim ledger: presence/absence history per class."
  - name: checkout
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — finds classes absent N consecutive iterations (N authored, default 2), verifies against the ENGINE'S OWN RECORD, not the CSV; moves them to archive/ with a receipt row"
    fallback_friendly: false
    purpose: "Supervised, receipted retirement: the CSV is the claim, the engine record is the evidence."
  - name: re-enter
    sheets: 1
    instrument_guidance: "CLI — an archived class re-fails → back to active, recurrence_count incremented; at an authored threshold, promoted to escalation instead of curriculum"
    fallback_friendly: false
    purpose: "The loop confesses it cannot fix this."
dependencies:
  checkout: [track]
  re-enter: [checkout]
composes_with:
  - pattern: "The Hotwash Dispatch"
    how: "the other half of the lifecycle — dispatch arms lessons, checkout retires them; composed end-to-end only after each is proven alone (the Skeptic's sequencing)"
  - pattern: "The Validity Window"
    how: "per-class TTLs — the automatic checkout for classes too stale to track"
  - pattern: "Watch Rollover"
    how: "handover hygiene for the curriculum itself — what carries forward is chosen, not defaulted"
  - pattern: "After-Action Review"
    how: "AAR captures; checkout decides what may be forgotten"
type: orchestration-pattern
---

## The Spent Lesson Checkout

**Status:** approximation — same transport debt as the dispatch half (the engine's own record needs a documented, stable path and schema, which the Skeptic demanded and the engine has not yet exposed; until then the record is an explicit engine-written failure log, if and when it exists). The retirement arithmetic composes today.

**Core Dynamic.** A resource does not leave the incident because the fire is out; it leaves when the demobilization unit confirms its business is complete (ICS-221). Applied to lessons: **ending things is a supervised, receipted act.** A lesson leaves the curriculum only through a verified checkout — a run whose evidence demonstrates the failure class is closed — and the checkout is checked against the *engine's own record*, because a CSV can be forged by absence. Cyclical failures take the re-entry path: a released class that re-fails returns with its recurrence count, and recurrence is itself curriculum — at threshold, the class is promoted to escalation (the loop admits it cannot fix this).

**Sentinel (the draft's best paranoia, preserved):** a never-remediated class planted with a *forged* two-iteration absence in the CSV but a live failure in the engine record → `grep -c "planted-class" archive/*` exits 1 — the run FAILS if checkout trusted the ledger over the evidence.

**Example.** Documentation-generation loop: iteration 1 fails `content_contains` on three required safety warnings; the classifier maps the code to the writer's curriculum; iteration 2's writer sees the actual failure evidence — the three missing strings, not a paraphrase — and the citation check proves it acted on them. Month-long variant: week 1's broken image paths are fixed in week 2 and check out in week 3 with receipts; week 6's prompts carry week 5's *live* problems only — not a museum of solved ones.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
