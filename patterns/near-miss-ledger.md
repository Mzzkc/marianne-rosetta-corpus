---
name: "The Near-Miss Ledger"
scale: adaptation
type: orchestration-pattern
status: aspirational
iteration_added: "discover pass 1, cycle 7"
blocked_on: "documented conductor status export (retry counts, durations, validation margins) as a score-readable artifact or stable API"
forces:
  - "Accumulated Signal"
generators:
  - "Exploit Failure as Signal"
problem: "Validation near-passes — the retry that succeeded on attempt 2, the check that passed by luck, the sheet that finished at 95% of its timeout — are silent holes in the defenses, and no pattern consumes them."
signals:
  - "repeated runs of the same score (trends across runs are the signal)"
  - "luck-dependent validations"
  - "capacity planning: duration-near-limit is tomorrow's outage"
stages:
  - name: execution
    sheets: 1
    instrument_guidance: "the normal score, with per-sheet attempt/duration events written to the workspace by on_fail/on_success post-steps (the buildable today-half)"
    fallback_friendly: true
    purpose: "Emit the events the harvester will read."
    artifacts: ["events/"]
  - name: harvest
    sheets: 1
    instrument_guidance: "instrument: cli — external next-run collector over attempt/duration events; deterministic extraction, never an LLM summarizer"
    fallback_friendly: false
    purpose: "Write ledger/near-miss.md: class labels (recovered-failure, duration-near-limit, margin-narrow)."
    artifacts: ["ledger/near-miss.md"]
  - name: adapt
    sheets: 1
    instrument_guidance: "strong reasoner — routes each class to a decision"
    fallback_friendly: false
    purpose: "Strengthen-the-gate, pin-the-flake, or accept-with-receipt; decisions append to the same ledger."
    artifacts: []
dependencies:
  harvest: ["execution"]
  adapt: ["harvest"]
composes_with:
  - pattern: "After-Action Review"
    how: "AAR learns from failures; this learns from non-failures — the optimistic twin"
  - pattern: "The Unprimed Falsifier"
    how: "the luck-pass detector is its standing ally"
config_features:
  - "instrument: cli"
  - "on_fail/on_success post-steps"
---

## The Near-Miss Ledger

`Status: Aspirational` — blocked on a documented conductor status export. **Source:** discover pass 1, cycle 7 — Expedition 6 (HRO theory — ASRS's 48-year near-miss corpus; Cooke 2006). **Force:** Accumulated Signal.

### Core Dynamic

HRO theory's core claim: near-misses are *more informative than failures per unit of damage* — they expose latent weaknesses while the system is still alive to fix them. The signals already exist in conductor state (retry counts, durations); the gap is that no pattern *consumes* them. Harvest, aggregate, route into adaptation: which validations to strengthen, which dependencies to pin, where the next run's verification budget goes.

**Why aspirational:** the desired signals are not shown to be available as score-readable data — retry counts and durations may exist in conductor state, but "narrow-margin validations" do not unless validators emit margins, and an in-run harvester cannot necessarily observe terminal status for the whole run. Until a documented status API or export exists, this is observability requirements disguised as a score. The buildable **today-half** ships inside: working sheets emit their own attempt/duration events via post-steps, margin-capable validators emit margins, and the harvester is a next-run collector over those events. When the export lands, the pattern upgrades to `working` unchanged in shape.

### Marianne Score Structure (today-half)

```yaml
  - name: harvest
    instrument: cli
    command: "python3 scripts/harvest_near_miss.py events/*.json --epsilon 0.1 --out ledger/near-miss.md"
    validations:
      - type: file_exists
        path: "ledger/near-miss.md"
```

**Negative control:** a seeded run with one forced-then-recovered failure — the harvester output must contain that sheet with class `recovered-failure`. **Sentinel:** harvester removed → no ledger, and the strengthened validation the adapt stage would have produced is confirmed never applied.

### When to Use

Repeated runs of the same score; luck-dependent validations; capacity planning.

### When NOT to Use

Definitions so broad everything qualifies (the epsilon must be defended); a ledger that routes to no decision — surveillance without response is voyeurism, not reliability; retries so cheap and constant that retry_count is noise about the instrument, not the system.

### Composes With

After-Action Review (non-failure learning), The Unprimed Falsifier (luck-pass detection)
