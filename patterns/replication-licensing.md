---
name: Replication Licensing
scale: iteration
status: working
forces:
- Progressive Commitment
- Exponential Defect Cost
generators:
- Incremental Exposure
- Exploit Failure as Signal
problem: A cycle counter cannot prevent a side-effectful cycle from happening twice, and naive retries duplicate deployments.
signals:
- any self-chaining or recurring score whose work stage has side effects that must be exactly-once per cycle
- deploys, sends, publishes, billing events, state migrations
- a conductor crash mid-stage would otherwise leave 'did the deploy happen?' answerable only by archaeology
stages:
- name: restriction-point
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — verify inputs, prior completion, and NO unconsumed license; then issue
  fallback_friendly: false
  purpose: Issue licenses/cycle-{n}.json naming exactly what it authorizes, by hash.
  artifacts: []
- name: work
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument; its FIRST action is the mv that consumes the license
  fallback_friendly: true
  purpose: Consume the license by moving it; possession of the moved file is the proof of authorization.
  artifacts: []
- name: mitosis
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — verification-only gate on the products
  fallback_friendly: false
  purpose: Check products complete and grounded; arm the next restriction point.
  artifacts: []
dependencies:
  work:
  - restriction-point
  mitosis:
  - work
composes_with:
- pattern: The Fencing Token
  how: 'substitution — same family (physical authority), different primitive: exactly-once consumption vs ordering defense (seam stated in both)'
- pattern: Canon of Phases
  how: layering — the packet boundary carries license state
type: orchestration-pattern
---

## Replication Licensing


**Status:** Working. **Source:** MCM2-7 licensing; geminin's steric blockade; the G1 restriction point. Ranked strongest pattern in the corpus by Review 1: fully expressible today, its atomic `mv`-as-consumption is a real mechanism with a real validation, and it covers a failure class (exactly-once under crash) nothing else owns.

**Core Dynamic.** `max_chain_depth` counts cycles; it cannot prevent a cycle from *happening twice*. The cell solved duplication safety the way orchestration should: the right to do expensive, side-effectful work is a **single-use artifact** that (a) carries provenance — the license names exactly what it authorizes, by hash; (b) is atomically consumed by the act of beginning — the `mv` across a filesystem boundary is the firing; and (c) cannot be re-issued until a checkpoint has verified the products of the last cycle. The anti-relicensing guard is constitutive: refusal is the default state, and permission is the temporary, supervised exception. Crash between start and finish leaves a consumed license and no products — recovery can therefore *tell the difference* between "never started" and "started, died," which is precisely the ambiguity that makes naive retries duplicate deployments.

**When to use:** any self-chaining or recurring score whose work stage has side effects that must be exactly-once per cycle.

**When NOT to use:** purely idempotent work (regenerating a derived file that overwrites in place; a `file_modified` check suffices). License issuance and consumption not *atomically* ordered: issue-then-consume with any gap invites a second consumer to read a still-valid license — the consumption must be the `mv` the work stage itself performs as its first act.

**Marianne Score Structure**

```yaml
schedule:
  interval: 1d
  timezone: "Europe/Amsterdam"
  overlap: skip
  misfire: skip

movements:
  1: { name: restriction-point, instrument: cli }
  2: { name: work }
  3: { name: mitosis, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/license-issue.sh" "{{ workspace }}" \
      --verify-inputs --verify-prior-complete --refuse-if-unconsumed \
      --emit licenses/cycle-{n}.json     # {cycle, input_sha256 map, issued_utc, consumer, expires_at}
    {% elif stage == 2 %}
    Your FIRST action: mv {{ workspace }}/licenses/cycle-*.json {{ workspace }}/consumed/
    Then do the expensive work, writing outputs that reference the license's input hashes.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/mitosis.sh" "{{ workspace }}" \
      --verify-products-grounded --emit-completion-marker
    {% endif %}

validations:
  - type: command_succeeds
    # the atomic move, asserted BOTH ways: consumed present AND licenses/ empty of it
    command: 'test -n "$(ls {workspace}/consumed/cycle-*.json 2>/dev/null)" && test -z "$(ls {workspace}/licenses/cycle-*.json 2>/dev/null)"'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/mitosis.sh {workspace} --check-only'
    condition: "stage == 3"
```

**Failure wiring:** `mzt recover` finding a consumed license with no products enters resume-or-compensate, never re-license — the "no unconsumed license" check is constitutive and cannot be skipped by configuration.

**Near-miss:** a `deployed.flag` file checked at start — presence-of-marker without atomic consumption re-licenses on every retry; the flag can be read by two consumers at once.

**Example.** A nightly publishing pipeline: build → deploy → notify. The conductor crashes after deploy, before notify. Naive retry redeploys. Under licensing: the license was consumed by deploy; recovery finds consumed-license-without-completion-marker and resumes at notify — the restriction point physically cannot re-issue for cycle n until mitosis verified cycle n's products, and the next license carries n+1's input hashes, which the deploy target will not match if the content did not change.

### Review Integration

Review 3 made the seam with Fencing Token explicit: this pattern grants single-use exactly-once authority, while a fence rejects stale ordering. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
