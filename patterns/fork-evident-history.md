---
name: Fork-Evident History
scale: communication
status: working
forces:
- Structured Disagreement
- Accumulated Signal
generators:
- Verify through Diverse Observers
- Accumulate Knowledge
problem: A retroactively edited history is undetectable, so downstream consumers cannot know they saw the same claims as everyone else.
signals:
- self-chaining scores where iteration N+1 must not silently weaken iteration N
- long concerts whose claims are consumed by multiple downstream parties
- corrections-heavy domains where the honest correction cites what it supersedes
stages:
- name: link
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — its evidence compiler appends one journal record per sheet
  fallback_friendly: true
  purpose: Append {sheet, inputs, outputs, prev_digest} to the workspace journal.
  artifacts: []
- name: chain-and-verify
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — journal-keeper/recompute; or use git outright
  fallback_friendly: false
  purpose: Compute the running digest; verify prefix property and append-only length.
  artifacts: []
dependencies:
  chain-and-verify:
  - link
composes_with:
- pattern: The Errata Ledger
  how: payload/substrate — corrections are payloads over this chain (the chain verifies; the ledger corrects)
- pattern: Proof-Carrying Artifact
  how: payload/substrate — sidecars are the per-entry links
- pattern: Self-Stabilizing Custody
  how: prerequisite — legitimacy predicates read the journal
type: orchestration-pattern
---

## Fork-Evident History


**Status:** Working. **Source:** Lamport/Pease signed messages; Raft log-matching; Certificate Transparency; in-toto. **Reframed per Reviews 2 and 3:** this is the *substrate* layer — fork-evidence is what corrections and proof sidecars ride on, not a sibling of them.

**Core Dynamic.** Signatures and digest chains convert equivocation from undetectable to detectable: a liar must now tell the *same* lie to everyone, and any two observers can mechanically compare notes. A hash chain fixes history — each entry commits to its predecessor's digest — so a retroactive edit breaks the chain at exactly the edit point, and prefix checks expose forks. Corrections enter as *supersession* entries citing the digest of what they replace; a shrinking journal is a rewritten journal. **The simplest robust form is `git` itself:** the commit DAG is already fork-evident and verifiable by any clone — when your workspace is a git repo, `git log --oneline` + `git diff` is the journal-keeper, and this pattern costs one disciplined habit (commit at every sheet boundary, never rewrite history) rather than a script.

**When to use:** self-chaining scores; multi-consumer concerts; corrections-heavy domains.

**When NOT to use:** short single-shot runs with no re-consumption. Histories that must be legitimately rewritten — deletion rights require envelope-key shredding, not history edits. Anywhere nobody will ever verify: unwatched chains are ceremony.

**Marianne Score Structure**

```yaml
movements:
  1: { name: work }
  2: { name: journal-verify, instrument: cli }

sheet:
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks: { 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Do the work. Then append one record to {{ workspace }}/journal.jsonl:
    {sheet, inputs, outputs, prev_digest} where prev_digest is the sha256 of the last line.
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/journal-verify.py" "{{ workspace }}/journal.jsonl" \
      --recompute --assert-append-only --require-supersedes-on-corrections
    {% endif %}

validations:
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/journal-verify.py {workspace}/journal.jsonl --check'
    condition: "stage == 2"
  - type: content_regex
    pattern: "supersedes: [0-9a-f]{64}"      # every correction entry cites its victim
    path: "{workspace}/journal.jsonl"
    condition: "stage == 2"
```

**Near-miss:** timestamps and an append promise — chronological ordering without digest commitment detects nothing; the edit is still invisible.

**Example.** A multi-day competitive-analysis concert: day-3 correction of a day-1 market-size figure enters as a supersession citing the original entry's digest; the client's auditor later proves no day-1 claim was quietly altered to flatter the narrative.

### Review Integration

Reviews 2 and 3 reclassified this as communication substrate and named Git as the canonical simple implementation. Errata and proof sidecars are payloads on the history chain, not competing histories. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
