---
name: "The Validity Window"
scale: foundational
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Accumulated Signal"
generators:
  - "Threshold-Triggered Switch"
problem: "Pipelines hold expirable state — tokens, permits, freshness-bound context, generated datasets — and silently reuse it after it expires."
signals:
  - "state whose safety or truth depends on when it was created"
  - "a TTL, freshness bound, or maturity threshold mentioned only in prose"
  - "retry or resume paths that re-present old artifacts"
config_features:
  - "instrument: cli"
  - "per_sheet_fallbacks"
stages:
  - name: stamp
    sheets: 1
    instrument_guidance: "instrument: cli — the creation event writes the clock; nothing else may"
    fallback_friendly: false
    purpose: "Write {window_id, subject_digest, issued_at, expires_at, handler} atomically."
    artifacts: ["window.json"]
  - name: probe
    sheets: 1
    instrument_guidance: "instrument: cli — measures monotone accumulation when readiness is not wall-clock"
    fallback_friendly: false
    purpose: "Append measured maturity units to the accumulation ledger."
    artifacts: ["maturity.jsonl"]
  - name: gate
    sheets: 1
    instrument_guidance: "instrument: cli — two-sided window arithmetic in one transaction, adjacent to the consumer"
    fallback_friendly: false
    purpose: "Decide valid | expired→regenerate | degraded."
    artifacts: ["window-report.jsonl"]
  - name: consume
    sheets: 1
    instrument_guidance: "any — works under the window the gate admitted"
    fallback_friendly: true
    purpose: "Consume the artifact, citing the window id in the output header."
    artifacts: ["output.md"]
dependencies:
  probe: ["stamp"]
  gate: ["stamp", "probe"]
  consume: ["gate"]
composes_with:
  - pattern: "The Gas-Free Certificate"
    how: "the destructive-boundary specialization — independence and digest binding added"
  - pattern: "The Declared Window"
    how: "the epistemic specialization — the window bounds claims, not safety"
  - pattern: "Effectivity Blocks"
    how: "generalizes it — config validity is one carrier of the window arithmetic"
---

## The Validity Window

`Status: Working` · **Source:** iteration 6, minted from convergence C9's carriers (Builder, Reasoner, Commander, Gardener). **Scale:** foundational law. **Forces:** Information Asymmetry, Accumulated Signal.

### Core Dynamic

A validity interval measured from a creation event, whose crossing forces regeneration or degradation — never silent reuse. A creation event stamps a clock; crossing the clock is an *event with a defined handler*; the handler regenerates or degrades. The transition table:

| State | Entry condition | Handler |
|---|---|---|
| `stamped` | creation event wrote the window record | artifact usable only via `valid` |
| `valid` | now ∈ [issued_at + min_age, expires_at) AND maturity ≥ floor | consumer admitted; consumer must cite `window_id` |
| `expired` | now ≥ expires_at, or maturity probe red under min-age backstop | **fail forward to regeneration**: a NEW window id, never re-presentation of the same bytes |
| `regenerated` | gate re-stamped within its own transaction | old id lands on a revocation list; any input containing it fails the join |
| `degraded` | handler declares degradation instead | tier label written to the window report; run proceeds at declared lower force |

Precedence: minimum age gates entry, expiry gates exit, accumulated maturity is a parallel readiness channel measured by monotone accumulation (not every day is a day) with the minimum-age backstop surviving a green probe. Adjacency: the gate movement runs immediately before the consumer, and the consumer cites the window id — a stale id in any consumer input is a join failure.

### When to Use / When NOT to Use

Use: any pipeline state whose validity is bounded — tokens, credentials, permits, freshness-bound context, generated datasets, plans with effective periods.

Not: artifacts are timeless (source at a pinned SHA has no expiry — windows on it are ritual); readiness cannot be probed deterministically (a window you argue about is a mood); regeneration costs more than the work it gates.

### Marianne Score Structure

```yaml
movements:
  1: { name: stamp, instrument: cli, instrument_fallbacks: [] }
  2: { name: probe, instrument: cli, instrument_fallbacks: [] }
  3: { name: gate, instrument: cli, instrument_fallbacks: [] }
  4: { name: consume }
sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  per_sheet_fallbacks: { 1: [], 2: [], 3: [] }
prompt:
  variables: { ttl_minutes: 90, min_age_seconds: 30 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/window.sh" stamp --subject "{{ workspace }}/artifact.bin" \
      --ttl-minutes {{ ttl_minutes }} --min-age {{ min_age_seconds }} --emit "{{ workspace }}/window.json"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/window.sh" probe --maturity-ledger "{{ workspace }}/maturity.jsonl" --append
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/window.sh" gate "{{ workspace }}/window.json" \
      --maturity "{{ workspace }}/maturity.jsonl" --regenerate-on-expiry
    {% else %}
    Consume the artifact. Cite window_id from {{ workspace }}/window.json in your header.
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/window.sh --self-test'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/window.sh gate {workspace}/window.json --check-only'
    condition: "stage == 4"
```

Negative controls in `--self-test`: a stale window must fail and produce a new id; a green probe under minimum age must fail.

### Example

A long migration pipeline using 60-minute cloud tokens: each stage batch-refreshes and stamps; the probe authenticates a synthetic request; the gate passes only inside the window. When a stage overruns, the gate routes to re-batch instead of letting the next stage discover a 401 mid-flight.

### Composes With

Layering over every carrier pattern (Gas-Free at destructive boundaries, Declared Window at epistemic ones); substitution for Effectivity Blocks' lease semantics.

### Review Integration

Iteration 6: survived all three reviews; the transition table and the gate-adjacency rule were added on Reviews 1 and 2's finding that the draft conflated elapsed TTL, minimum age, and accumulated maturity without precedence, and validated the window after rather than before consumption.
