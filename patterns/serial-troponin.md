---
name: "The Serial Troponin"
scale: score-level
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Finite Resources"
  - "Progressive Commitment"
generators:
  - "Graduate & Filter"
problem: "Verification regimes test-to-complete — run every check, await every result, then decide — when most artifacts can be conclusively cleared cheaply but not conclusively convicted cheaply."
signals:
  - "logs, generated configs, dependency trees, translation drafts: one grep can clear, no grep can convict"
  - "the negative case is common and the expensive cascade should be rare, priced, pre-declared"
  - "re-test at interval is natural (the delta between measurements is signal)"
stages:
  - name: declare
    sheets: 1
    instrument_guidance: "instrument: cli — checks listed cheapest-first with PRE-DECLARED exit thresholds, committed and digest-pinned"
    fallback_friendly: false
    purpose: "Write pathway.yaml: per-tier check, exit threshold, retest interval."
    artifacts: ["pathway.yaml"]
  - name: test
    sheets: 1
    instrument_guidance: "instrument: cli — looped sheet; reads state.yaml, runs CURRENT tier's check, advances tier only on indeterminate, writes the typed next state"
    fallback_friendly: false
    purpose: "One typed carrier: state.yaml {status: ruled_out | indeterminate | escalate, current_tier}."
    artifacts: ["state.yaml"]
  - name: legal-transition-gate
    sheets: 1
    instrument_guidance: "instrument: cli — recomputes, never trusts, that every ruled_out satisfied its tier's threshold"
    fallback_friendly: false
    purpose: "The state machine's own audit."
    artifacts: []
  - name: cascade
    sheets: 1
    instrument_guidance: "strong reasoner — the expensive conviction stage, OUTSIDE the loop"
    fallback_friendly: false
    purpose: "Runs only for escalations — rare by design, priced like it's rare."
    artifacts: ["verdict.json"]
dependencies:
  test: ["declare"]
  legal-transition-gate: ["test"]
  cascade: ["legal-transition-gate"]
composes_with:
  - pattern: "Immune Cascade"
    how: "the priced variant's price table feeds this pathway's tier list; the Net prices the menu, the Troponin times the meal"
  - pattern: "Circuit Breaker"
    how: "the loop bound is a breaker against unbounded serial testing"
  - pattern: "Sign-Off Chain Against the Hard Date"
    how: "the cascade's verdict joins the sign-off record"
config_features:
  - "sheet.loops + until (native, UNPROVEN in proof scores)"
  - "instrument: cli"
---

## The Serial Troponin

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 5 (emergency medicine's 0/1-hour high-sensitivity troponin rule-out pathways). **Forces:** Finite Resources + Progressive Commitment.

### Core Dynamic

The pathway's entire economic contribution is **early negative exit** — most cases are ruled out cheaply at step one or two. Two structural commitments make it work where "check things in order" doesn't: the negative-exit threshold is **declared before the first test** (post-hoc thresholds are how motivated reasoning enters), and **ambiguity does not exit** — intermediate results route to *repeat at interval*, not to the decision; the delta between measurements is the signal.

State and failure are separate fields: the loop body's command succeeds (observation executed) while `status: indeterminate` keeps it looping — that is the normal condition, not an error. Tier ordering is **monotone by construction** (schema → cross-check → semantic), and the retest interval is input-version-keyed so repeats measure new evidence, never reroll the same input.

### Marianne Score Structure

```yaml
  - name: test
    instrument: cli
    loops:
      count: 3
      until: "workspace:state.yaml:status == 'ruled_out' || workspace:state.yaml:status == 'escalate'"
    command: "python3 scripts/pathway_step.py pathway.yaml state.yaml --input feed.xml"
    validations:
      - type: command_succeeds
  - name: legal-transition-gate
    instrument: cli
    command: "python3 scripts/check_transitions.py pathway.yaml state.yaml"
    validations:
      - type: command_succeeds
  - name: cascade
    skip_when: "test \"$(jq -r .status state.yaml)\" != 'escalate'"
    prompt: "The pathway escalated at tier N. Perform the full adversarial conviction review. Write verdict.json."
```

**Negative controls, both required:** a seeded dirty input must drive the loop to `escalate` within `count`, never to `ruled_out`; a seeded clean input must exit at tier 1. Early exit on dirty and full-course runs on clean are the two ways this pattern fails.

### When to Use

Validation of things that can be conclusively cleared cheaply but not conclusively convicted cheaply; the negative case common, the cascade rare, priced, pre-declared.

### When NOT to Use

Low negative predictive value in the first check (discharging a high-risk patient on one troponin); no natural re-test interval (repeats become re-rolls); surveillance rather than rule-out — when you need positive conviction every run, this is the wrong pattern.

### Composes With

Immune Cascade (menu pricing), Circuit Breaker (loop bound), Sign-Off Chain Against the Hard Date (verdict in the record)
