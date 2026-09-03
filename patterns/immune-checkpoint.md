---
name: Immune Checkpoint
scale: within-stage
status: working
forces:
- Exponential Defect Cost
- Instrument-Task Fit
generators:
- Verify through Diverse Observers
- Incremental Exposure
problem: 'In a system with a powerful reviewer and an automated remediation path, the reviewer is the most dangerous instrument: a false-positive finding triggers rollback or deletion of healthy work.'
signals:
- adversarial review feeding automated remediation — fix-PRs, scanner-gated deploys, takedowns
- reviewer recall tuned high AND a downstream stage treating findings as verdicts rather than leads
- an AI code reviewer opening fix-PRs directly
stages:
- name: adversarial-review
  sheets: 1
  instrument_guidance: claude-code or codex-cli — a strong instrument generating findings in a strict schema
  fallback_friendly: true
  purpose: Produce {id, claim, location, evidence, proposed_remediation, severity} — high recall, no self-restraint required.
  artifacts: []
- name: tolerance-checkpoint
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — deterministic, INSIDE the review boundary, before findings are ever emitted as actionable
  fallback_friendly: false
  purpose: Ground location against actual bytes; compute blast radius; classify load-bearing. Failed/ambiguous → tolerated, never routed.
  artifacts: []
- name: remediation
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — receives ONLY the actionable subset
  fallback_friendly: true
  purpose: Remediate the bijective actionable set — no more.
  artifacts: []
dependencies:
  tolerance-checkpoint:
  - adversarial-review
  remediation:
  - tolerance-checkpoint
composes_with:
- pattern: The Skeptical Oracle
  how: layering — recall-side harvest there; precision-side gate here; the pair covers both directions of reviewer error
- pattern: Andon Cord (v4 archive)
  how: prerequisite — the human summons for ambiguous findings
type: orchestration-pattern
---

## Immune Checkpoint


**Status:** Working. **Source:** regulatory T cells; CTLA-4's higher affinity winning ties. **Plain structural language first (Review 2): this is a precision gate on the critic.** The immunology is illustration, not argument.

**Core Dynamic.** The corpus had adversarial review and gates on the work. It had nothing that gates the **critic** — yet with a powerful reviewer and an automated remediation path, a false-positive finding doesn't waste a cycle, it triggers rollback, churn, or deletion of healthy work. That is autoimmunity, and its prevalence scales with reviewer capability. The checkpoint is an inhibitory gate *inside the review path*: findings cannot trigger destructive remediation until each passes a self-tolerance check — source validation (the cited file:line exists and contains what is claimed), blast-radius computation (the proposed remediation's diff is bounded and touches what the finding names), and load-bearing classification. The constitutive-presence rule is the part worth copying exactly: the checkpoint cannot be configured away, and **on ambiguity it defaults to tolerance** — no action, escalate to a human. The off-signal is designed to win ties. Everything still surfaces — flagged `autoimmune-suspect` rather than `actionable`.

**The recalibration rule, correctly wired (Review 1's fix):** a checkpoint rejecting >80% of findings is itself a finding — the reviewer and the code have diverged and need recalibration, not more rounds. This is enforced by a **deterministic count gate** comparing actionable vs tolerated totals (a script, an exit code), not by `circuit_breaker`, which accepts sheet-failure counts only.

**When to use:** any score where adversarial review feeds automated remediation.

**When NOT to use:** findings are advisory-only and a human reads every one (the checkpoint duplicates the reader). The tolerance check is weaker than the reviewer (a grep that can't see what the finding means will pass plausible nonsense). "Tolerance by default" misread as "review is optional" — the checkpoint suppresses automated *action*, never the finding itself.

**Marianne Score Structure**

```yaml
movements:
  1: { name: adversarial-review }
  2: { name: tolerance-checkpoint, instrument: cli }
  3: { name: remediation }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }        # the checkpoint cannot be degraded away

prompt:
  template: |
    {% if stage == 1 %}
    Generate findings in STRICT schema: {id, claim, location, evidence,
    proposed_remediation, severity}. Tune recall high — the checkpoint downstream
    is your precision; do not self-censor.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/tolerance-checkpoint.sh" "{{ workspace }}/findings.json" \
      --ground-locations --compute-blast-radius --classify-load-bearing \
      --default-to-tolerance --emit "{{ workspace }}/actionable.json" \
      --tolerated "{{ workspace }}/tolerated.jsonl"
    {% elif stage == 3 %}
    Remediate EXACTLY the findings in {{ workspace }}/actionable.json. If you find yourself
    working on something not in that file, stop — the bijection is the contract.
    {% endif %}

validations:
  - type: command_succeeds
    # the bijection is the anti-bypass proof: remediation's input set EQUALS the actionable set
    command: 'bash {score_dir}/scripts/assert-bijection.sh {workspace}/actionable.json {workspace}/remediation-log.json'
    condition: "stage == 3"
  - type: command_succeeds
    # the recalibration gate: a checkpoint rejecting >80% is itself a finding (a count gate,
    # NOT circuit_breaker — the breaker accepts sheet-failure counts only)
    command: 'bash {score_dir}/scripts/recalibration-gate.sh {workspace}/actionable.json {workspace}/tolerated.jsonl --max-rejection-ratio 0.8'
    condition: "stage == 2"
```

**Near-miss:** a second reviewer stage — more judgment layered on judgment; the gate must be a checker, not another critic.

**Example.** An automated PR-review agent for a monorepo, recall tuned high, opening fix-PRs directly. Without a checkpoint, one bad afternoon of plausible hallucinated "bugs" reverts healthy code across a dozen services — and the team's rational response is to turn the agent off entirely. With the checkpoint: every finding resolves to real bytes or is tolerated; ambiguous ones sit in a human queue; the fix-PR stream runs at a precision that keeps the automation alive.

### Review Integration

Review 2 reframed the pattern as a precision gate on the critic. Review 1 moved the high rejection-ratio stop from the sheet-failure circuit breaker to a deterministic ratio gate. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
