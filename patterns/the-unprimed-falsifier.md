---
name: "The Unprimed Falsifier"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Structured Disagreement"
  - "Convergence Imperative"
generators:
  - "Verify through Diverse Observers"
  - "Measure Convergence Character"
problem: "Makers cannot perceive their finished artifact — fluency hides the claims it makes — and internal evaluation shares the blind spot."
signals:
  - "anything read by humans whose makers are too close to it"
  - "'we think it's clear' has ever been wrong"
  - "self-evaluation and structural-equality checks both passing while users misread the thing"
config_features:
  - "fan_out"
  - "cadenzas"
  - "concert"
stages:
  - name: assemble
    sheets: 1
    instrument_guidance: "any — builds the current cut from the beat map and drafts"
    fallback_friendly: true
    purpose: "Produce the artifact under evaluation."
    artifacts: ["cut.md"]
  - name: read-cold
    sheets: "fan_out(5)"
    instrument_guidance: "cheap local tier (ollama) — the audience is many, shallow, and genuinely naive; each receives ONLY the artifact by cadenza"
    fallback_friendly: true
    purpose: "Report section-anchored reactions: confusion, dead zones, misreads."
    artifacts: ["cards/card-{{ instance }}.md"]
  - name: note-code
    sheets: 1
    instrument_guidance: "instrument: cli — codes cards into typed, located evidence"
    fallback_friendly: false
    purpose: "Emit evidence.json: per-section density of located reactions."
    artifacts: ["evidence.json"]
  - name: verdict
    sheets: 1
    instrument_guidance: "strong reasoner — evidence-targeted recut or done; NOT the lock authority"
    fallback_friendly: false
    purpose: "Recut ONLY where density crosses threshold; declare done or chain."
    artifacts: ["done.stamp"]
dependencies:
  read-cold: ["assemble"]
  note-code: ["read-cold"]
  verdict: ["note-code"]
composes_with:
  - pattern: "The Freeze"
    how: "termination — the loop ends in authority-declared lock, not convergence (the lock half of the former Test Screening lives there)"
  - pattern: "Rehearsal Spotlight"
    how: "substitution — external falsifier replaces self-evaluation"
  - pattern: "The Declared Window"
    how: "the audience's claims are windowed to what the cut shows them — they are the honest window"
---

## The Unprimed Falsifier

`Status: Working` · **Source:** iteration 6 (Expedition 6 — film test screenings, recruited audiences), split from the draft's "Test Screening to Picture Lock" per Review 2. **Scale:** iteration. **Forces:** Structured Disagreement, Convergence Imperative.

### Core Dynamic

The people who made the film are constitutionally incapable of seeing it. They know what every shot was *meant* to say; the audience, seeing cold, reports what it *says*. The test screening is **falsification by outsiders**: recruited naive readers receive *only the artifact* — never the makers' intent, never the questions the makers are worried about (that would prime them) — and return reaction cards coded into **typed, located evidence**: where readers were confused, where attention died, what they thought happened. Thumbs-up/down is not a location; "bored somewhere in act two" is. The recut is *targeted*: only where evidence density crosses a threshold — a quiet screening is a verdict too, and recutting everything after every screening is churn with a ritual attached.

Unprimedness is structural, not asserted: this score authors **no prelude**; each reader sheet's cadenza injects exactly one file — the cut — `required: true`; reader prompts contain no design-document references; and a priming check runs as a command gate — reader outputs must contain no reference to any intent-document path (grep over the cards returns empty). Readers tier to cheap local instruments — many, shallow, genuinely naive. Termination is authority-declared lock (The Freeze), with the self-chain bounded by `max_chain_depth` as the perfectionism circuit-breaker — infinite test screening is a known pathology.

Distinct from Rehearsal Spotlight (self-evaluation — no audience) and Fixed-Point Iteration (structural equality — no reader): neither can detect that the audience misread the protagonist's motive, because neither has an audience.

### When to Use / When NOT to Use

Use: anything read by humans whose makers are too close to it — documentation, onboarding flows, API references, incident narratives, tutorials. Anywhere downstream finishing work is too expensive to start before the text is truly frozen (with The Freeze).

Not: no naive reader exists or can be honestly simulated (readers sharing context with makers is Rehearsal Spotlight in costume); cards cannot be coded into typed, located evidence; the authority refuses to lock; recuts are not evidence-targeted.

### Marianne Score Structure

```yaml
concert:
  enabled: true
  max_chain_depth: 4             # the perfectionism breaker
  inherit_workspace: true
on_success:
  - type: run_job
    job_path: "{score_dir}/unprimed-falsifier.yaml"
movements:
  1: { name: assemble }
  2: { name: read-cold, voices: 5 }
  3: { name: note-code, instrument: cli, instrument_fallbacks: [] }
  4: { name: verdict }
sheet:
  size: 1
  total_items: 4                # expansion: assemble 1, readers 2-6, code 7, verdict 8
  fan_out: { 2: 5 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  skip_when:                    # EXPANDED sheet keys: all five reader sheets
    2: { command: 'test -f {workspace}/done.stamp' }
    3: { command: 'test -f {workspace}/done.stamp' }
    4: { command: 'test -f {workspace}/done.stamp' }
    5: { command: 'test -f {workspace}/done.stamp' }
    6: { command: 'test -f {workspace}/done.stamp' }
  cadenzas:
    2:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    3:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    4:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    5:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
  per_sheet_instruments:        # cheap local tier on every reader sheet
    2: ollama
    3: ollama
    4: ollama
    5: ollama
    6: ollama
  per_sheet_fallbacks: { 7: [], 8: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Assemble the current cut into {{ workspace }}/cut.md.
    {% elif stage == 2 %}
    You are a naive reader. You receive ONLY the cut. Report section-anchored reactions:
    confusion, dead zones, misreads. Write {{ workspace }}/cards/card-{{ instance }}.md
    with one `section:` anchor per note.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/notes.sh" code --cards "{{ workspace }}/cards/" --density --emit "{{ workspace }}/evidence.json"
    {% else %}
    Read {{ workspace }}/evidence.json. If any section's density crosses 2: recut ONLY
    those sections into a new {{ workspace }}/cut.md. Otherwise write {{ workspace }}/done.stamp.
    {% endif %}
validations:
  - type: content_contains
    path: "{workspace}/cards/card-1.md"
    pattern: "section:"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'test $(grep -lE "design-doc|intent|spec/" {workspace}/cards/*.md | wc -l) -eq 0'
    condition: "stage == 3"
```

The grep gate is the priming check: any card naming an intent-document path fails the run — the falsification property is enforced, not hoped for.

### Example

An API reference read cold by five naive sheets that have never seen the design docs. Cards report: "the auth section assumes a token the reader doesn't have yet," "examples 3–4 read as one example," "the error table lost me." Note-code locates density in the auth section; the verdict recuts exactly that; when a screening runs quiet, the done-stamp lands and The Freeze takes over for the finishing fan-out.

### Review Integration

Iteration 6: Review 2 split the draft's "Test Screening to Picture Lock" into its two stapled patterns — the unprimed falsifier (this file) and the lock (absorbed into The Freeze law). Review 1's strengthening conditions (physical context isolation, structured cards, evidence-density math, executable relock loop) and Review 3's demand for a priming check that actually runs are implemented: no prelude, artifact-only cadenzas, the grep priming gate, and the bounded self-chain.
