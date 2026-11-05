---
name: "Immune Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
proof_score: "rosetta-proof-immune-cascade.yaml"
forces:
  - "Finite Resources"
  - "Exponential Defect Cost"
generators:
  - "Graduate & Filter"
problem: "Expensive instruments waste resources on broad scanning when cheap preliminary work could narrow scope first."
signals:
  - "broad scanning is expensive but most issues are benign"
  - "don't know which findings warrant expensive investigation"
  - "need to narrow findings before expensive deep analysis"
stages:
  - name: broad-sweep
    sheets: "fan_out(8)"
    instrument_guidance: "opencode — fast, cheap scanning across partitions; capability sufficient for breadth-first issue discovery"
    fallback_friendly: true
    purpose: "Parallelize broad scanning to identify findings efficiently at low cost."
    artifacts: ["sweep-{{ instance_id }}.md"]
  - name: triage-handoff
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — requires judgment to triage findings and prioritize targets; stronger instruments produce better targeting"
    fallback_friendly: false
    purpose: "Deduplicate broad findings and create prioritized targeting brief for expensive investigation."
    artifacts: ["targeting-brief.md"]
  - name: deep-investigation
    sheets: 1
    instrument_guidance: "claude-code — deep code analysis and remediation requiring full reasoning capability; critical for thorough investigation"
    fallback_friendly: false
    purpose: "Deep-dive on prioritized targets with thorough analysis and remediation design."
    artifacts: []
  - name: learning
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — documents methodology and learnings; can use cheaper instrument"
    fallback_friendly: true
    purpose: "Document methodology and learnings for future audit iterations."
    artifacts: ["doctrine.md"]
dependencies: {}
composes_with:
  - pattern: "Triage Gate"
    how: "The triage-handoff stage implements Triage Gate logic, filtering broad findings to identify investigation targets."
  - pattern: "After-Action Review"
    how: "After-Action Review processes Immune Cascade's findings and learning stage outputs to extract methodology improvements."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses the high-volume broad-sweep outputs before triage-handoff, preventing context overflow when parallel scans produce results."
fan_out:
  broad-sweep: 8
config_features:
  - "fan_out"
  - "capture_files"
---

## Immune Cascade

`Status: Working` · **Source:** Immunology (innate/adaptive response). Absorbs Kill Chain F2T2EA. **Forces:** Finite Resources + Exponential Defect Cost.

### Core Dynamic

Escalating tiers: fast/cheap/broad first for intelligence, slow/expensive/precise targeting what tier 1 found, then learning persistence. Three structural moves: graduated response, intelligence forwarding, learning persistence. **Strict Sequential Variant (from Kill Chain):** When the problem is pure narrowing, collapse to a linear pipeline where `command_succeeds verifying count decreased` validates each gate.

### When to Use / When NOT to Use

Use when the problem requires broad search before targeted work and cheap scanning methods exist. Not when the problem is narrow enough for direct attack.

### Marianne Score Structure

```yaml
sheets:
  - name: broad-sweep
    instances: 8
    instrument: haiku
    prompt: "Scan {{ partition }} for issues. Write raw findings."
    validations:
      - type: file_exists
        path: "{{ workspace }}/sweep-{{ instance_id }}.md"
  - name: triage-handoff
    prompt: "Read all sweep files. Deduplicate. Prioritize. Write targeting-brief.md."
    capture_files: ["sweep-*.md"]
  - name: deep-investigation
    instrument: opus
    prompt: "Deep-dive on prioritized targets. Write remediation."
    capture_files: ["targeting-brief.md"]
  - name: learning
    prompt: "Write doctrine.md: what scanning missed, what triage misjudged, rules for next run."
    validations:
      - type: content_regex
        pattern: "RULE:\\s+.+"
```

### Failure Mode

The learning stage is useless if it doesn't write persistent, structured output. Specify the artifact: `doctrine.md` with `RULE:` entries that the next iteration's broad sweep reads via prelude.

### Composes With

Triage Gate (handoff IS triage), After-Action Review (coda), Relay Zone (relay between tiers)

### Discover Pass 1, Cycle 7 — The Priced Variant (Graded Net Fold)

This pass folded the draft's **Graded Net** into this pattern as its priced variant (Review 3: the draft's claimed invariant — "each artifact passes through tiers in strict cost order, and each tier's only job is to decide whether the artifact is worth the next tier's price" — is Immune Cascade's header word for word; "the honest differentiators are real — but they are strengthenings of Immune Cascade, and the draft neither names it nor composes with it"). The fold adds:

**1. The committed price table.** `tiers.yaml` — validator, instrument, per-artifact cost per tier — digest-pinned at authorship, with authored first-run values (Review 3: the table must have an author and first-run numbers, not vibes). Each tier's only job is to decide whether the artifact is worth the next tier's price; no tier verifies "quality" in the abstract.

**2. The collapse rule.** Live when the tier cost ratio is ≥10×; otherwise collapse to two tiers. A free top tier means everything gets it and nothing gets *deep* review — the rigger who inspects everything inspects nothing.

**3. Promotion by declared risk, not habit.** Tier 3 (adversarial red/blue over contested artifacts only) admits by declared evidence of risk from tier-2 verdicts, and uses two different instrument *families* — correlated error is the enemy at the top (compose Condorcet's Premise).

**4. Tier isolation of prose.** Each tier writes `verdicts/t{n}/{artifact}.json`; the next tier receives only paths — a tier never sees the tier below's prose, so reviewers cannot be anchored.

**5. The Pre-Load face** (rigging economics, DOE-STD-1090): the same curve at destructive-work scale — sling check (all units) → probe lift (sample) → critical pick (few): a *shrinking fan-out, the cost curve made visible*.

**Proof debt carried:** `immune-cascade.yaml` is one of the six historical proof files that fail `mzt validate` (folded-command checks). Repair before extending; the priced variant's first proof extends this file rather than adding a new domain showcase. Negative control for the variant: one seeded artifact known to fail tier 1, asserted *absent* from the tier-2 manifest — if the seed survives, the net has a hole and the validation fails. Overlap note: Echelon Repair tiers the *response to failure that already happened*; this variant prices *what you buy, and in what order, once you're spending*.
