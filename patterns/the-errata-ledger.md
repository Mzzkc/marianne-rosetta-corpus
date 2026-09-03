---
name: The Errata Ledger
scale: communication
status: working
forces:
- Accumulated Signal
- Producer-Consumer Mismatch
generators:
- Accumulate Knowledge
problem: A correction that silently rewrites the text lies about its own history, and a correction notice nobody consumes leaves derived copies wrong.
signals:
- a canonical document with derived translations, summaries, or extracts
- syndicated anything
- a downstream copy that would otherwise drift from corrected truth
stages:
- name: intake
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — assembles {claim_id, error, new_text, authority}
  fallback_friendly: true
  purpose: Stage the correction for atomic commit.
  artifacts: []
- name: atomic-commit
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — THE single serialized writer; writes corrected canon AND ledger row in one movement
  fallback_friendly: false
  purpose: Commit the pair together; the hash-join makes divergence impossible.
  artifacts: []
- name: propagate
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument or CLI regenerator — consumes entries newer than its watermark
  fallback_friendly: true
  purpose: Update derived copies; advance the watermark.
  artifacts: []
dependencies:
  atomic-commit:
  - intake
  propagate:
  - atomic-commit
composes_with:
- pattern: Fork-Evident History
  how: payload/substrate — chaining beneath the published corrections
- pattern: Negative-Treatment Watch
  how: prerequisite — decay detection feeds corrections
- pattern: Proof-Carrying Artifact
  how: substitution — the hash-join is a deterministic source check applied to the pair
type: orchestration-pattern
---

## The Errata Ledger


**Status:** Working. **Source:** NYT/NPR/AP corrections practice; NLM citable errata. **Kept per Review 2's condition:** the atomic pair commit and the propagation watermark are now stated as *the* load-bearing mechanism (without them this is Fork-Evident History plus a correction payload). **Serialization wired per Review 3:** one deterministic writer movement owns the commit — not an assertion.

**Core Dynamic.** A correction must be two things at once — a change to the living text and a durable record of the change. Only the first is the silent rewrite; only the second is the errata nobody reads while the text stays wrong. The pattern is the *atomic pair*: fix and notice commit together, and the notice — not the fix — is what propagates downstream, because derived copies hold state the fix cannot reach directly.

**When to use:** multi-consumer corpora: canonical documents with derived translations, summaries, extracts; syndicated anything.

**When NOT to use:** consumers ignore the ledger — an advisory watermark is a seam, not a mechanism (this needs acknowledged-handoff grammar or a deterministic join). Corrections so frequent they flood the ledger (batch per release, not per typo). Adversarial environments where notices get scrubbed — there the ledger needs digest chaining beneath it.

**Marianne Score Structure**

```yaml
movements:
  1: { name: intake }
  2: { name: atomic-commit, instrument: cli }
  3: { name: propagate }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }      # the serialized writer never degrades

prompt:
  template: |
    {% if stage == 1 %}
    Stage the correction to {{ workspace }}/pending-correction.json:
    {claim_id, error, new_text, authority}. Do NOT touch the canon.
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/errata-commit.py" "{{ workspace }}" \
      --canon spec.md --ledger ledger/corrections.jsonl
      # writes BOTH in one movement: corrected canon file AND appends
      # {id, claim_id, prior_hash, new_hash, date, note}; exits nonzero if either half fails
    {% elif stage == 3 %}
    Consume {{ workspace }}/ledger/corrections.jsonl entries newer than your watermark
    in watermark.json. Regenerate affected derived copies. Advance the watermark.
    {% endif %}

validations:
  - type: command_succeeds
    # the deterministic hash-join: the entry's new_hash MUST equal sha256 of the corrected file
    command: 'python3 {score_dir}/scripts/errata-commit.py --verify-join "{workspace}"'
    condition: "stage == 2"
  - type: file_exists
    path: "{workspace}/watermark.json"
    condition: "stage == 3"           # a consumer that ran without a watermark is a fabrication
```

**Failure wiring:** a cycle ending ledger-written-but-canon-unwritten is a failed state — `on_failure` custody holds the half-committed pair for repair rather than retry-blind (the commit script's nonzero exit is what makes the half-state visible).

**Near-miss:** a CHANGELOG.md nobody's build consumes — the notice without the propagation watermark is a diary, not a mechanism.

**Example.** A product's canonical spec sheet with generated PDF, web page, and partner-portal extracts: a dimensional error corrected once in canon, and the ledger entry drives regeneration of every extract whose watermark predates it — no extract silently retains the wrong number.

### Review Integration

Review 2 made the canon-and-ledger pair commit and propagation watermark constitutive. Review 3 required one serialized deterministic writer and a hash join between correction and canonical text. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
