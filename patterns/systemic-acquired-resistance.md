---
name: "Systemic Acquired Resistance"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
generators:
  - "Threshold-Triggered Switch"
problem: "Failures encountered in one score don't inform subsequent scores in a concert, causing repeated failures across the campaign."
signals:
  - "scores in a concert face similar threats"
  - "first-encounter failure cost is high"
  - "failures repeat across scores in a concert"
  - "no mechanism to share failure recovery"
config_features:
  - capture_files
  - on_success
  - inherit_workspace
stages:
  - name: work
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must handle failure recovery and write structured primers; stronger instruments produce more effective countermeasures"
    fallback_friendly: false
    purpose: "Execute the primary task while reading relevant defense primers and writing new primers when recovering from failures."
    artifacts: ["output.md", "priming/*.yaml"]
dependencies: {}
composes_with:
  - pattern: "After-Action Review"
    how: "Primers are structured AAR output — AAR extracts lessons, SAR broadcasts them as actionable defenses."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) provides the mechanism for culture inheritance; SAR structures that culture as threat-specific primers."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker generates a failure signal; SAR captures that signal as a primer to adjust future behavior."
---

## Systemic Acquired Resistance

`Status: Working` · **Source:** Plant immune priming (SAR/ISR), Expedition 2. **Scale:** concert-level. **Iteration:** 4. **Force:** Accumulated Signal.

### Core Dynamic

When a score recovers from a failure, it broadcasts failure-derived defenses to all subsequent scores via structured `priming/` directory. Primed scores CHANGE BEHAVIOR — adjusting prompts, validation thresholds, or monitoring. The priming is specific: a rate-limit encounter primes for rate-limit handling, not general defensiveness.

**Primer schema:** Each primer file in `priming/` follows: `{threat_type: string, trigger_signature: string, countermeasure: string, confidence: float, timestamp: string}`. Downstream scores read primers matching their threat surface and incorporate countermeasures into their prompts.

### When to Use / When NOT to Use

Use for concert campaigns where scores face related threat landscapes, when failure in one score should make the entire campaign more resilient, or when first-encounter failure cost is high. Not when scores face unrelated threats, the priming signal is too vague, or defense overhead degrades unaffected scores (autoimmune response — primers that are too broad cause unnecessary caution).

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: |
      Before starting, read priming/ for defense primers matching your work type.
      For each relevant primer, incorporate the countermeasure into your approach.

      Execute the primary task. Write output to output.md.

      If you encounter and recover from a failure, write a primer to priming/:
      File: priming/{threat_type}.yaml
      Schema: {threat_type, trigger_signature, countermeasure, confidence, timestamp}.
    capture_files: ["priming/*.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/output.md"
```

### Failure Mode

Primers too broad cause autoimmune response — every score wastes tokens on irrelevant defenses. Primers too narrow never match. The `trigger_signature` field is the key: specific enough to match real threats, broad enough to generalize. If primers accumulate without pruning, the priming directory becomes noise. Include a `confidence` field and prune low-confidence primers after N uses without trigger.

### Composes With

After-Action Review (primers are structured AAR output), Back-Slopping (Learning Inheritance) (priming IS culture inheritance across scores), Circuit Breaker (primer from circuit-tripped instrument)

---

# Communication Patterns
