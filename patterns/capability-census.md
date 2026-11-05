---
name: "The Capability Census"
scale: concert-level
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Instrument-Task Fit"
  - "Partial Failure"
generators:
  - "Match Instrument to Grain"
problem: "A fleet roster is a claim; a census is a proof — and the two artifacts must never merge because they are produced by different authorities and fail differently."
signals:
  - "a fleet launch whose members have decaying prerequisites (credentials, data drops, sibling services, disk state)"
  - "surge: know in seconds who can start"
  - "recurring multi-run workloads where instruments drift between authorship and run N+50"
stages:
  - name: roster-declare
    sheets: 1
    instrument_guidance: "instrument: cli — mechanical; one row per member with typed capability claims and probe contracts"
    fallback_friendly: false
    purpose: "Write roster.jsonl — the CLAIM, authored by the composer."
    artifacts: ["roster.jsonl"]
  - name: muster-probe
    sheets: 1
    instrument_guidance: "instrument: cli — deliberately serial; probes are cheap and serial probing is deterministic and rerunnable"
    fallback_friendly: false
    purpose: "Run each declared probe; write census.jsonl {member, probe_exit, evidence}. Probe failure is a STATUS, not a crash."
    artifacts: ["census.jsonl"]
  - name: classify
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic mapping from probe evidence to the closed vocabulary; NO judgment seat"
    fallback_friendly: false
    purpose: "Write readiness.json / capabilities.yaml with stale_after. Broken-by-default; disagreement with the roster is signal."
    artifacts: ["readiness.json", "capabilities.yaml"]
  - name: exceptions
    sheets: 1
    instrument_guidance: "strong reasoner — ONLY the exception rows; cites probe evidence"
    fallback_friendly: false
    purpose: "Adjudicate disagreement rows the deterministic mapping cannot decide; output is a typed disposition, never a fourth state."
    artifacts: []
dependencies:
  muster-probe: ["roster-declare"]
  classify: ["muster-probe"]
  exceptions: ["classify"]
composes_with:
  - pattern: "Concurrent Count"
    how: "roster vs census are independent enumerations that must agree — the bijection is the count"
  - pattern: "Dormancy Gate"
    how: "the census is the gate's evidence source"
  - pattern: "Admission by First Cycle"
    how: "census establishes CAN RUN; first cycle establishes DOES RUN, validated"
config_features:
  - "instrument: cli"
  - "csv_unique_key"
---

## The Capability Census

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 4 (NIMS/ICS resource typing; DoDI 7730.66 possessed-vs-operational; OFRP) + Expedition 1 (subcontractor prequalification) as the instrument-scale Vendor Board face: per-instrument fitness attested by a live prequal probe producing a machine-checkable `capabilities.yaml` with `stale_after` — the bonding letter that launders unfitness as qualification is the named failure both scales share. **Forces:** Instrument-Task Fit + Partial Failure.

### Core Dynamic

The roster answers "who belongs" — registration, mechanical, authored. The census answers "who can *run*, now" — obtained the only way orchestration gets answers: by executing a probe and reading its exit code. Reconciliation is a bijection with a typed third column — ready / dormant / broken, a closed vocabulary, broken-by-default. Disagreement is signal, not noise. An admission granted is not an admission forever: capacity decays, tokens expire, vendors have incidents.

The judgment fence holds because **classification is deterministic** — the classify stage is a CLI mapping probe evidence to vocabulary states by declared rules. A reasoner may never invent a state or overrule a failed probe; it may only adjudicate the residual disagreement rows the mapping cannot decide, citing probe evidence per row — and a hallucinated fourth state fails the closed-vocabulary validation mechanically. A census with judgment in the mapping is an opinion poll.

Admission is **fail-closed**: a `command_succeeds` jq entry gate, never `skip_when` (which is fail-open on timeout — dangerous for admission; that engine behavior is on the corpus's citation-owing list). Visible skips keyed on readiness remain for non-admission decisions.

### Marianne Score Structure

```yaml
  - name: muster-probe
    instrument: cli
    command: "python3 scripts/muster.py roster.jsonl --serial --out census.jsonl"
    validations:
      - type: csv_unique_key
        path: "census.jsonl"
        key: "member"
  - name: classify
    instrument: cli
    command: "python3 scripts/classify.py roster.jsonl census.jsonl --vocabulary ready,dormant,broken --default broken --out readiness.json --stale-after 24h"
  - name: entry-gate                    # fail-closed, in the CONSUMING score
    instrument: cli
    command: "jq -e 'all(.[]; .state == \"ready\")' readiness.json"
    validations:
      - type: command_succeeds
```

**Negative controls:** a member whose probe exits non-zero must classify not-ready — a census that green-lights a failed probe is a receipt (sentinel: `field_match` asserting the injected member's row reads `broken`); remove the census and the first downstream admission gate fails closed.

### When to Use

Before any fleet launch with decaying prerequisites; before surge; recurring multi-run workloads; scores shared across machines with different instrument availability.

### When NOT to Use

Stateless single-file scores (degenerates to "does the YAML parse"); one-shot scores (never amortizes); probes allowed to become judgment calls; a TTL'd roster never re-attested (worse than none).

### Composes With

Concurrent Count (roster/census bijection), Dormancy Gate (evidence source), Admission by First Cycle (can-run vs. does-run)
