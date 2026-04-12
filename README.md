# Marianne Rosetta Corpus

A curated collection of 56 orchestration patterns for composing Marianne scores. Each pattern encodes a structural move — how to decompose work, route it to agents, validate outcomes, and recover from failure.

## Structure

| Path | Contents |
|------|----------|
| `patterns/` | 56 pattern files with YAML frontmatter (forces, stages, compositions) |
| `INDEX.md` | Problem-oriented pattern index grouped by scale |
| `forces.md` | 10 generative forces + 11 generators (recognition vocabulary) |
| `selection-guide.md` | Problem-type to pattern mapping for end users |
| `composition-dag.yaml` | Machine-readable pattern composition graph |
| `the-rosetta-score.yaml` | Pattern discovery engine (self-chaining, 6-domain fan-out) |
| `rosetta-prove.yaml` | Pattern proof engine (composes demonstration scores) |
| `proof-scores/` | 6 production-grade demonstration scores from research iterations |
| `archive/` | Original monolith corpus (preserved for reference) |

## Using the Corpus

**For agents composing scores:** Read `INDEX.md` first to find patterns by problem type. Read individual patterns in `patterns/` for force profiles, stage structures, and composition relationships. Use `selection-guide.md` for problem-to-pattern mapping.

**For discovering new patterns:** Run `the-rosetta-score.yaml` via `mzt run`.

**For proving patterns:** Run `rosetta-prove.yaml` via `mzt run`. Proof scores land in `proof-scores/`.

## Pattern Format

Each pattern file has structured YAML frontmatter:

```yaml
---
name: "Pattern Name"
scale: within-stage | score-level | concert-level | communication | adaptation | instrument-strategy | iteration
type: orchestration-pattern
status: working | aspirational
forces: [list of forces from forces.md]
generators: [structural generators]
problem: "One-line problem statement"
signals: [when to reach for this pattern]
stages: [stage definitions with instrument guidance]
composes_with: [composition relationships]
---
```

Followed by prose documentation: core dynamic, when to use, Marianne score structure example, failure modes, and composition notes.

## Provenance

Patterns discovered through cross-domain research (construction, biology, music, military strategy, storytelling, distributed systems) across 4 iterations with adversarial review. See `review-integration.md` for the full review history.
