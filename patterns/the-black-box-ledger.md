---
name: The Black-Box Ledger
scale: adaptation
status: working
forces:
- Partial Failure
- Accumulated Signal
generators:
- Exploit Failure as Signal
- Verify through Diverse Observers
problem: After the executor dies, what happened is knowable only from survivor testimony — reconstructed memory — unless a channel that does not share the executor's fate recorded it continuously.
signals:
- any long orchestration whose post-failure value depends on knowing what actually happened
- production incidents, adversarial review concerts, audit trails
- failure analysis must be grounded rather than narrated
stages:
- name: continuous-record
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the work movements themselves — wired with auto_capture_stdout and named capture_files
  fallback_friendly: true
  purpose: Write all along, to media that survive the crash.
  artifacts: []
- name: correlated-readout
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — reads the BUNDLED packet, never one channel
  fallback_friendly: true
  purpose: Interpret evidence read as a bundle, because evidence read alone lies.
  artifacts: []
dependencies:
  correlated-readout:
  - continuous-record
composes_with:
- pattern: Flight Rules
  how: prerequisite — the packet's failure signature feeds the rule matcher
- pattern: The MIST Card
  how: layering — the card rides the packet
- pattern: Positive Transfer
  how: prerequisite — unaccepted offers feed the failure packet
type: orchestration-pattern
---

## The Black-Box Ledger


**Status:** Working. **Source:** ICAO Annex 13 recorder custody; incident scribe channels; WAL/journaling filesystems.

**Core Dynamic.** After the executor dies, there are exactly two ways to know what happened: reconstruction from survivor testimony, or playback of a record written continuously by a channel that does not share the executor's fate. Every serious safety domain chose the second, in a specific shape: the recorder is not triggered by the crash — it writes all along, to crash-protected media, on power independent of what crashes; **survival is structural, not reactive** (Review 2's fate-separation demand, stated as a requirement: a log buffer inside the dying process shares fate and is a diary, not a recorder).

**Fate separation, concretely:** the conductor outlives the sheets and is the independent power bus; workspace state is the crash-protected medium; workspace archival is the secondary recorder. The authorable half is the capture wiring and the correlated-readout discipline; the packet assembly is engine-supplied by the durable `on_failure` hook (Review 3's honesty: a score author benefits from it, they do not build it).

**The correlation rule is the deep one:** evidence travels in bundles, and the bundle composition is mandated, because evidence read alone lies (flight-data readout without the cockpit-voice channel misleads, and voice without data misleads differently). And settlement must not launder the failure: **the original error travels verbatim.**

This is the fifth failure class — terminal custody — completing the table:

| Class | v4 pattern | What it owns | What it cannot answer |
|---|---|---|---|
| Task repair | Andon Cord | The moment of detection | Who holds the work while the human is en route |
| Batch quarantine | Dead Letter Quarantine | The poisoned item | What happens downstream of the hole |
| Infrastructure failover | Circuit Breaker | The route | What happens when there is no alternate path |
| Side-effect compensation | Saga Compensation Chain | The undo | The evidence of what happened before the undo |
| **Terminal custody** | **Black-Box Ledger (this)** | **The job itself, after the executor is gone** | — |

**When to use:** any long orchestration whose post-failure value depends on knowing what actually happened.

**When NOT to use:** the logger shares fate with the thing logging. The record is reconstructed afterward from memory — that is testimony, and testimony is what the recorder exists to replace. Volume drowns signal (bounded overwrite is a design feature — tune `max_output_chars`/`lookback_sheets`). Evidence is editable after the fact — a mutable black box is a diary.

**Marianne Score Structure**

```yaml
cross_sheet:
  auto_capture_stdout: true            # continuous write — every sheet, all along
  max_output_chars: 4000               # bounded overwrite is a FEATURE
  lookback_sheets: 5
  capture_files: ["*-report.json", "*.jsonl"]

movements:
  1: { name: the-work }
  2: { name: correlated-readout }

sheet:
  total_items: 2
  dependencies: { 2: [1] }

# on terminal failure, the durable on_failure hook assembles ONE evidence packet:
# job identity, chain depth, per-sheet artifacts so far, cost spent, and the ORIGINAL
# error verbatim — engine-supplied custody; the score's job is to have recorded.

prompt:
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/*-report.json as you go — the recorder is
    your ordinary output discipline, not an extra channel you remember at the end.
    {% elif stage == 2 %}
    Read the failure packet as a BUNDLE: logs + artifacts + config hash + instrument
    identities. No channel alone. Ground every claim in the packet's bytes and cite
    the packet path per claim.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/failure-packet/manifest.json"
    condition: "stage == 2"
  - type: command_succeeds
    # the original error string is present UNMODIFIED — settlement does not launder failure
    command: 'bash {score_dir}/scripts/packet-integrity.sh "{workspace}/failure-packet" --verbatim-error'
    condition: "stage == 2"
```

**Near-miss:** stderr tee'd to a log file in the same process — the recorder shares fate with the crash, surviving nothing.

**Example.** A nightly data-pipeline concert dies at 03:00 when an API credential expires mid-sheet. The on-duty engineer does not interview the half-finished agents — they open the packet: which sheets completed, what each wrote, the exact 401s in order, the config hash that was live. The evidence was assembled before anyone woke up.

### Review Integration

Review 2 required recorder and executor to have different fates. Review 3 separated engine-supplied terminal packet assembly from score-authored continuous capture and later readout. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
