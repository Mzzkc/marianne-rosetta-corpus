---
name: Negative-Treatment Watch
scale: concert-level
status: working
forces:
- Accumulated Signal
- Progressive Commitment
generators:
- Accumulate Knowledge
problem: Admitted claims silently rot as their external sources move, and derived work keeps building on stale truth.
signals:
- long-lived corpora whose truth depends on mutable externals
- legal research, scientific claim bases, compliance baselines, dependency manifests, docs with code anchors
- a missed audit cycle must be visible, not silent
stages:
- name: sweep
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — deterministic fetch/hash of every anchored source, hard-bounded per cycle
  fallback_friendly: false
  purpose: Detect source drift; count flag rate.
  artifacts: []
- name: adjudicate
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — reviews ONLY flagged claims (few, cheap)
  fallback_friendly: true
  purpose: Does the negative treatment touch the issue our claim relies on?
  artifacts: []
- name: quarantine
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — moves flagged claims; enumerates dependents from the claim graph
  fallback_friendly: false
  purpose: Quarantine + blast-radius enumeration; hold auto-quarantine when flag rate exceeds threshold.
  artifacts: []
dependencies:
  adjudicate:
  - sweep
  quarantine:
  - adjudicate
composes_with:
- pattern: The Errata Ledger
  how: prerequisite — decay detection feeds corrections
- pattern: Flight Rules
  how: substitution — effectivity pinning is the same lease applied to configuration
- pattern: Proof-Carrying Artifact
  how: prerequisite — the anchors it audits are PCA claim-form bundles
type: orchestration-pattern
---

## Negative-Treatment Watch


**Status:** Working. **Source:** Shepard's/KeyCite citators; PubMed linked errata; CVE feeds. Runs on a leased `schedule`.

**Core Dynamic.** Admission is not permanence. The brief is filed, the magazine printed, the claim enters canon — and the world keeps moving: courts overrule, journals retract, dependencies patch. The citator's move turns the citation graph into a *decay detector*: every admitted claim holds a **validity lease**, renewed by a recurring audit against the current state of its sources. Staleness is made loud instead of impossible — the flag, not the silence, is the product. Because citators demonstrably disagree (two independent authorities agreed on negative treatment in only 53 of the relationships each identified), the watch cross-checks rather than trusts one probe.

**The claim graph (Review 2's requirement):** the ledger is not a flat list. Every claim carries `{id, source_anchor: {path, digest}, dependents: [claim-ids...]}` — source anchors so drift is mechanically detectable, dependent edges so blast radius is enumerable. Without dependent edges, quarantine is detection without consequence.

**Mass invalidation is a different event from fifty independent ones:** when the flag rate exceeds threshold, the sweep script **holds auto-quarantine** and escalates to a re-tiering decision — mass invalidation means the premise changed, not fifty claims. (This hold is enforced by the deterministic sweep script comparing counts — Review 1's correction: `circuit_breaker` accepts sheet-failure counts only, and is wired for exactly that.)

**When to use:** long-lived corpora whose truth depends on mutable externals.

**When NOT to use:** sources are immutable or self-contained (nothing to watch). The schedule runs without a durable lease — a missed cycle must be *visible*, or staleness returns silently through the gap. Alert fatigue: if every cycle flags half the corpus, readers stop reading. One probe trusted alone.

**Marianne Score Structure**

```yaml
schedule:
  interval: 7d
  timezone: "Europe/Amsterdam"
  overlap: skip
  misfire: skip

movements:
  1: { name: sweep, instrument: cli }
  2: { name: adjudicate }
  3: { name: quarantine, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/source-sweep.sh" "{{ workspace }}/claim-ledger.json" \
      --refetch --rehash --flag-drift --flag-rate-hold-threshold 0.10 \
      --max-wall 600
    {% elif stage == 2 %}
    Adjudicate ONLY the claims flagged in {{ workspace }}/flagged.json (they are few).
    For each: does the negative treatment touch the issue our claim relies on?
    Verdict QUARANTINE or RETAIN, with the touched issue named.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/quarantine.sh" "{{ workspace }}/claim-ledger.json" \
      "{{ workspace }}/adjudications.json" --enumerate-dependents
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/sweep-report.json"'
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/lease-record.json"
    condition: "stage == 1"            # a cycle that ran without touching leases is a fabrication
  - type: content_regex
    pattern: "dependent(s)?: \\[.+\\]|no dependents"
    path: "{workspace}/quarantine-report.md"
    condition: "stage == 3"            # every quarantined claim appears WITH its blast radius or its absence
```

**Near-miss:** a nightly "sources changed" digest email — detection without dependent enumeration or quarantine is weather reporting.

**Example.** An internal API-docs corpus where every code sample anchors to a repository path and commit SHA: the weekly watch detects upstream API changes, quarantines samples whose anchors broke, and enumerates every tutorial page that embeds them.

### Review Integration

Review 2 required a dependency-bearing claim graph for blast radius. Review 1 moved flag-rate control out of the sheet-failure circuit breaker and into a deterministic count gate. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
