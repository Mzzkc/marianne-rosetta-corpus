---
name: The MIST Card
scale: communication
status: approximation
forces:
- Partial Failure
- Accumulated Signal
generators:
- Exploit Failure as Signal
- Verify through Diverse Observers
problem: A retry loop treats an arriving item as fresh and repeats an intervention that already failed, wasting the window or compounding damage.
signals:
- any score-authored retry, recovery chain, or multi-stage escalation
- the next handler must know what previous handlers already tried
- two attempts where one should do is itself a hunt signal
stages:
- name: ledger-writer
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — a wrapper that appends the attempt row; conductor-internal retries CANNOT feed this (no per-attempt hooks exist)
  fallback_friendly: false
  purpose: Append every attempt row mechanically; agents never self-report from memory.
  artifacts: []
- name: recovery
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument; receives the ledger as a required cadenza
  fallback_friendly: true
  purpose: Propose a remedy WITH the treatment history in context.
  artifacts: []
- name: constraint-check
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — fingerprint collision gate
  fallback_friendly: false
  purpose: Reject any remedy whose fingerprint matches a recorded failure.
  artifacts: []
dependencies:
  recovery:
  - ledger-writer
  constraint-check:
  - recovery
composes_with:
- pattern: Black-Box Ledger
  how: layering — the card rides the failure packet
- pattern: Flight Rules
  how: prerequisite — a rule action colliding with a recorded failed remedy is a rule-delta signal
- pattern: Replication Licensing
  how: prerequisite — recovery distinguishes never-started from started-died
type: orchestration-pattern
---

## The MIST Card


**Status:** Approximation — the scope Review 1's engine audit forced. The draft claimed conductor retry hooks feed the ledger mechanically; **no such hooks exist** (the conductor retries internally via checkpoint/resume; nothing appends to a user-visible ledger per attempt). The pattern governs *score-authored* retry and recovery chains, where the retry path is a wrapper the score owns. Full mechanical feeding of conductor-level retries awaits per-attempt hooks (see Awaiting Primitives).

**Core Dynamic.** When work moves through a chain of handlers, the item's **treatment history** must travel with it — and the history is not narrative, it is **constraint**. The next handler is not free to act as if the item were fresh: the failed remedy from two attempts ago must not be re-applied. The card is append-only precisely because a rewrite destroys the constraints. The cardinal failure is "re-triage from scratch."

**The fingerprint function (Reviews 2 and 3 both demanded it defined):**

```
fingerprint = sha256(
  error_class                    # normalized: lowercase, strip vendor prefixes
  | normalize(tool + args)       # sort flag-arguments alphabetically, collapse whitespace,
                                 #   drop volatile tokens (timestamps, temp paths, retry counts)
  | target_path                  # resolved absolute path, workspace-relative prefix stripped
)
```

Normalization is the load-bearing half: it is chosen so "retry with a tweak" — same tool, reordered flags, cosmetic difference — **collides** with the recorded failure, while a genuinely different remedy (different tool, different target) does not.

**When to use:** any score-authored retry loop, recovery chain, or multi-stage escalation where re-trying a failed remedy wastes the window or compounds the damage.

**When NOT to use:** the record travels on a different channel than the item (the card left on the ambulance). Handlers disagree on schema — the fixed form is the point. Nobody is required to read it before acting (enforce with a `required: true` cadenza or do not bother).

**Marianne Score Structure**

```yaml
movements:
  1: { name: attempt, instrument: cli }
  2: { name: recovery }
  3: { name: constraint-check, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }
  cadenzas:
    2:
      - file: "{{ workspace }}/mist-ledger.yaml"
        as: context
        required: true              # no remedy may be proposed without the history

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/attempt-wrapper.sh" "{{ workspace }}/item.json" \
      -- your-command-here          # wrapper appends {item, error_class, remedy_fingerprint,
    {% endif %}                     # timestamp, outcome} to mist-ledger.yaml, THEN execs
    {% if stage == 2 %}             # the command and appends the result row
    Item {{ id }} has failed handlers before you; the ledger above is CONSTRAINT, not
    history. Propose the next remedy. A remedy whose fingerprint appears in the ledger
    as failed WILL be rejected downstream — do not propose it.
    {% elif stage == 3 %}
    python3 "{score_dir}/scripts/fingerprint-collision.py" "{{ workspace }}/mist-ledger.yaml" \
      "{{ workspace }}/proposed-remedy.json" --reject-on-collision
    {% endif %}

validations:
  - type: content_regex
    pattern: "fingerprint: [0-9a-f]{64}"
    path: "{workspace}/mist-ledger.yaml"
    condition: "stage == 1"          # a run that retried without a row is a masked retry
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/fingerprint-collision.py {workspace}/mist-ledger.yaml {workspace}/proposed-remedy.json --check'
    condition: "stage == 3"
```

**Near-miss:** a free-text "lessons learned" section — narrative history does not constrain the next handler; only a keyed, fingerprinted, collision-checked ledger does.

**Example.** A content-migration concert processing 4,000 documents: item #3171 failed twice on an OCR timeout, once on a schema mismatch. When the recovery score reaches it, its MIST row forbids the third OCR retry and routes to the manual-review instrument — without the card, the run burns the batch window on a third identical timeout.

### Review Integration

Review 1 found no conductor per-attempt hook, so this remains an approximation over score-authored retry wrappers. Reviews 2 and 3 required the normalized treatment fingerprint and an explicit collision gate. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
