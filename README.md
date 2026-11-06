# Marianne Rosetta Corpus

A curated collection of 148 orchestration patterns for composing Marianne scores. Each pattern encodes a structural move — how to decompose work, route it to agents, validate outcomes, and recover from failure.

## Structure

| Path | Contents |
|------|----------|
| `patterns/` | 148 pattern files with YAML frontmatter (forces, stages, compositions) |
| `INDEX.md` | Problem-oriented pattern index grouped by scale |
| `forces.md` | 10 generative forces + 11 generators (recognition vocabulary) |
| `selection-guide.md` | Problem-type to pattern mapping for end users |
| `composition-dag.yaml` | Machine-readable pattern composition graph |
| `the-rosetta-score.yaml` | Pattern discovery engine (self-chaining, 6-domain fan-out) |
| `rosetta-prove.yaml` | Pattern proof engine (composes demonstration scores) |
| `rosetta-cycle.yaml` | Discover and prove in one score: each path a bounded loop (`sheet.loops`, `count`), the two running side by side; the hand-off is the corpus on disk |
| `proof-scores/` | 25 demonstration scores, including six small offline long-tail proofs; see `examples/rosetta/README.md` in the parent repository for the indexed copies and corpus-only entries |
| `archive/` | Original monolith corpus (preserved for reference) |

## Using the Corpus

**For agents composing scores:** Read `INDEX.md` first to find patterns by problem type. Read individual patterns in `patterns/` for force profiles, stage structures, and composition relationships. Use `selection-guide.md` for problem-to-pattern mapping.

**For discovering new patterns:** Run `the-rosetta-score.yaml` via `mzt run`.

**For checking proof coverage:** Run `python3 -I tools/unproven.py .` from this directory.
The ledger counts explicit `PRIMARY PATTERN:` headers; six historical proofs still use legacy `Pattern:` headers.
Pattern frontmatter's `proof_score:` points to a file under `proof-scores/`, including those historical proofs.
A pointer is an executable example to inspect, not evidence that a paid run passed.

**For auditing usage citations:** Run `python3 -I tools/unproven.py . --usage --json`.
The default scans the repository's `scores/` tree, excluding this corpus's `proof-scores/`.
Pass `--usage /path/to/compositions` for a different tree (explicit trees include proofs if present).
Counts are YAML files citing the canonical pattern name, case-insensitively, once per pattern per file.
They measure citations, not observed execution or successful adoption. Patterns with no citations remain visible at zero.

**For small offline demonstrations:** The six new proofs are `talmudic-page.yaml`,
`sugya-weave-editorial-synthesis.yaml`, `forward-observer.yaml`, `stigmergic-workspace.yaml`,
`after-action-review.yaml`, and `screening-cascade.yaml` under `proof-scores/`.
Run any with `mzt run proof-scores/<name>.yaml`; they need a configured role-class instrument chain,
Python 3 and the sibling `tools/long_tail_proof.py`, but no data downloads or publication credentials.
Each bootstraps deterministic fixtures in an auto-managed workspace, then executes the pattern with agents.
Their gates check source joins, visible links, routing conservation, byte compression and learning consumption;
they do not judge semantic quality, enforce agent filesystem isolation, or measure token billing.
The AAR demo performs two task executions within one score; it does not mutate the corpus or a person's memory.

**For proving patterns:** Run `rosetta-prove.yaml` via `mzt run`. Proof scores land in `proof-scores/`.

**For a bounded cycle of both:** Run `rosetta-cycle.yaml` via `mzt run`. Each path repeats its authored pass count (`prompt.variables.discover_passes` / `prove_passes`, mirrored by `sheet.loops.*.count`); pass artifacts land in `discover-pass-N/` and `prove-pass-N/` in the workspace. Requires Marianne ≥ 6717158d (V105 accepts loop indices in validation paths).

## Pattern Format

Each pattern file has structured YAML frontmatter:

```yaml
---
name: "Pattern Name"
scale: within-stage | score-level | concert-level | communication | adaptation | instrument-strategy | iteration
type: orchestration-pattern
status: working | aspirational
proof_score: "<filename>.yaml"  # optional; relative to proof-scores/
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
