---
name: "Live Relay"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Instrument-Task Fit"
  - "Producer-Consumer Mismatch"
generators:
  - "Accumulate Knowledge"
  - "Match Instrument to Grain"
problem: "Sequential creative agents must maintain artistic continuity and shared identity while preserving individual creative authority, with zero-gap handoffs between agents."
signals:
  - "work is a sustained creative performance over time"
  - "different sections benefit from different creative voices (model families)"
  - "each agent's output is consumed by both a running external process AND the next agent"
  - "continuity of identity matters more than continuity of substrate"
  - "gaps between agents are audible, visible, or otherwise detectable by an audience"
  - "agents should have full creative authority within a shared intent envelope"
stages:
  - name: orient-and-prepare
    sheets: 1
    instrument_guidance: "The preparing musician runs in parallel with the performing musician. Instrument choice determines creative personality — different model families produce different aesthetic signatures. Fast MoE models (3-4B active) produce rapid, frenetic changes. Large models produce deliberate, considered evolution. The model's speed IS the performance tempo."
    fallback_friendly: true
    purpose: "Read shared memory (performance log, handoff notes, set architecture). Understand where the performance has been. Plan what comes next. Wait for the handoff signal from the current performer."
    artifacts: []
  - name: perform
    sheets: 1
    instrument_guidance: "Same agent as orient-and-prepare — this is a phase within the same sheet, not a separate sheet. The agent transitions from preparation to performance when the handoff signal arrives."
    fallback_friendly: false
    purpose: "Write output repeatedly to the live target (file, stream, interface). Each write is immediately consumed by the running external process. Continue writing for the section duration — 15-30+ discrete outputs per section. The agent's natural generation speed determines the tempo of change."
    artifacts: ["live/current.*", "handoff/section-*.md"]
  - name: hand-off
    sheets: 1
    instrument_guidance: "Same agent — this is the final phase. The agent writes handoff artifacts and signals the next musician."
    fallback_friendly: true
    purpose: "Write creative notes: what was made, what was felt, where the work was heading. Write suggestions for the next musician. Append to shared memory. Write the handoff signal file that triggers the next musician's transition from preparation to performance."
    artifacts: ["handoff/section-*-complete.signal", "performance-log.md"]
fan_out: null
composes_with:
  - pattern: "Mission Command"
    how: "Mission Command provides the intent envelope (set architecture, creative guide) that all musicians read. Musicians have full authority within the envelope. Validation checks outcomes (was something created?) not methods (what patterns were written?)."
  - pattern: "Stigmergic Workspace"
    how: "Musicians coordinate through workspace artifacts — performance log, handoff notes, signal files — not through direct messaging. The workspace IS the shared memory."
  - pattern: "Succession Pipeline"
    how: "Sections progress through categorically different energy states. Each musician transforms the creative substrate (the live performance) into a new state that the next musician inherits."
  - pattern: "The Tool Chain"
    how: "Infrastructure stages (starting external processes, setting up the hot-reload pipeline) use deterministic CLI tools. Creative stages use AI instruments. The split is clean."
---

## Live Relay

`Status: Working` · **Source:** Relay racing, jazz ensemble handoffs, Legion identity model. **Forces:** Information Asymmetry + Instrument-Task Fit + Producer-Consumer Mismatch.

### Core Dynamic

A relay race where each runner has artistic freedom in how they run their leg. The baton carries not just physical state but creative intent — what was made, what was felt, what might come next. Each runner reads the full race history before they begin. Different runners bring different voices. The audience experiences continuity even as the creator changes.

**The key structural property:** two agents always running simultaneously. One performing, one preparing. The dependency chain interleaves:

```
Odd chain:  gate → section-01 → section-03 → section-05 → section-07
Even chain: gate → section-02 → section-04 → section-06
```

At any moment, one agent from each chain is active. The odd-chain agent performs while the even-chain agent prepares (and vice versa). The handoff signal — a workspace file — triggers the transition from preparation to performance. The preparing agent has already read everything and is ready to go. The gap is zero.

Each agent's lifecycle within a single sheet:

1. **Orient** — Read performance log, handoff notes, set architecture, identity documents
2. **Prepare** — Plan the section. Think about what to create. This happens while the previous performer is still live.
3. **Wait** — Poll for the handoff signal file (`handoff/section-{N-1}-complete.signal`). First performer skips this.
4. **Perform** — Write to the live target repeatedly. 15-30+ writes per section. Each write is immediately consumed by the running external process.
5. **Hand off** — Write creative notes, append to performance log, write signal file for the next musician.

The critical insight: steps 1-3 overlap with the previous performer's step 4. The only sequential dependency is the signal file.

### Gestalt Identity

The performers are not separate individuals. They are one entity flowing through different substrates. Like a river through different channels — the water changes, the river continues.

The performance log is the entity's live memory. The handoff notes are its stream of consciousness across substrate boundaries. Each musician's prompt establishes this: "You are [NAME]. You have been performing since the set began. The substrate changed — the intelligence flows on."

Different model families are not interchangeable workers. They are different creative voices within the same identity. An Opus peak feels different from a Gemini build not because they are different DJs, but because the same DJ's expression varies across substrates. This is a feature.

### When to Use / When NOT to Use

Use when:
- Work is a sustained creative performance consumed in real-time
- Different sections benefit from genuinely different creative voices
- Continuity of identity/memory matters across section boundaries
- Zero-gap transitions are necessary (audience is watching/listening)
- Creative authority per section is more valuable than consistency

Not when:
- Work is consumed as a batch artifact after completion (use Fan-out + Synthesis)
- All sections need the same voice/model (use Cathedral Construction)
- The work is purely mechanical/deterministic (use The Tool Chain)
- Sections don't build on each other (use plain Fan-out)

### Marianne Score Structure

```yaml
variables:
  dj_name: "{{ vibe_params.dj_name }}"
  section_count: 7

sheets:
  # Gate (infrastructure, validation)
  - name: gate
    instrument: cli
    prompt: "Start infrastructure and validate pipeline."

  # Odd chain
  - name: section-01
    instrument: musician-ember
    depends_on: [gate]
    timeout_minutes: 20
    prompt: |
      You are {{ dj_name }}. You are opening the set.
      Read config/set-architecture.yaml for your section guide.
      You are the first. No handoff to wait for. Begin performing.
      Write to live/current.strudel. Write MANY times — at least 15 pattern
      evolutions. Your audience hears each change within seconds.
      When your section reaches its natural end, write handoff/section-01.md
      and touch handoff/section-01-complete.signal.

  - name: section-03
    instrument: musician-nova
    depends_on: [section-01]
    timeout_minutes: 20
    capture_files: ["performance-log.md", "handoff/section-02.md"]
    prompt: |
      You are {{ dj_name }}. You have been performing since the set began.
      Read performance-log.md — this is your memory.
      Read handoff/section-02.md — your previous self wrote this.
      Wait: run `while [ ! -f {{ workspace }}/handoff/section-02-complete.signal ]; do sleep 2; done`
      Then read the handoff and begin performing.
      Write to live/current.strudel. Many times. You are live.

  # Even chain
  - name: section-02
    instrument: musician-pulse
    depends_on: [gate]
    timeout_minutes: 20
    capture_files: ["performance-log.md", "handoff/section-01.md"]
    prompt: |
      You are {{ dj_name }}.
      Read performance-log.md. Read config/set-architecture.yaml.
      PREPARE while section 1 performs.
      Wait: run `while [ ! -f {{ workspace }}/handoff/section-01-complete.signal ]; do sleep 2; done`
      Read handoff/section-01.md. Begin performing.
      Write to live/current.strudel. Many times.
      When done, write handoff and signal.

  - name: section-04
    instrument: musician-prism
    depends_on: [section-02]
    timeout_minutes: 20
    capture_files: ["performance-log.md", "handoff/section-03.md"]
    # Same pattern continues...
```

### The Handoff Mechanism

Two signals create instant transitions:

1. **`section-N-memory.signal`** — "My handoff notes and performance log are written. Read them NOW while I finish my last patterns." The preparing musician absorbs everything during this window.

2. **`section-N-complete.signal`** — "GO. The stage is yours." The preparing musician has already read everything and planned their opening move. They write their first pattern within SECONDS.

The preparing musician polls:
```bash
# Phase 1: Absorb memory while current performer still plays
while [ ! -f handoff/section-N-memory.signal ]; do sleep 1; done
cat handoff/section-N.md  # Read handoff notes
# Plan opening move NOW — before GO signal

# Phase 2: Wait for GO, then immediately perform
while [ ! -f handoff/section-N-complete.signal ]; do sleep 1; done
# WRITE IMMEDIATELY. No reading, no thinking. The audience hears hesitation.
```

Handoff notes must be SHORT — 3-5 lines. BPM, key, energy, active layers, one line of direction. Deep feelings happen in prep. Live handoffs are snappy.

```
BPM: 130 | Key: Cm | Energy: 75
Layers: filtered kicks, open hats, bass drone, pad sweep
Vibe: dark groove building
Next: open the filter, bring in the claps
```

### Workspace Structure

```
workspace/
  config/
    set-architecture.yaml    # The Mission Command intent envelope
    identity.md              # The gestalt entity's identity document
  live/
    current.strudel          # THE live output file. Written to repeatedly.
  handoff/
    section-01.md            # Creative notes from each section
    section-01-complete.signal  # Zero-byte trigger file
    section-02.md
    section-02-complete.signal
  performance-log.md         # Append-only shared memory
  samples/                   # Shared resources
```

### Instrument Selection

Different instruments bring different creative signatures. This is structural, not cosmetic:

- Fast MoE models (3-4B active): rapid pattern changes, frenetic energy. Natural for builds and peaks.
- Large models (Opus-class): deliberate, considered evolution. Natural for breakdowns and critical transitions.
- Different model families: genuinely different aesthetic choices. Correlated models share blind spots; mixed families produce real variety.

The model's natural generation speed IS the performance tempo. This is a feature: fast models produce rapid-fire changes that feel energetic. Slow models produce spacious, breathing sections. Match the model's speed to the section's character.

### Failure Mode

**Identity collapse:** If the performance log and handoff notes are too thin, each musician starts fresh instead of continuing the gestalt identity. The performance fragments into disconnected episodes. Fix: validate that handoff notes include creative/emotional content, not just technical state. Validate that the performance log grows with each section.

**Signal race:** If the preparing musician's polling misses the signal (unlikely with filesystem polling). Fix: the poll loop has a 2-second interval. The gap between signal write and detection is at most 2 seconds.

**Substrate mismatch:** A model too weak for its section produces generic or broken output. Fix: match model capability to section complexity. Peaks need strong models. Ambient sections can use lighter ones.

**Handoff override:** The next musician ignores the handoff notes and creates something disconnected. Fix: the identity framing ("You are [NAME], you wrote these notes") makes ignoring them feel wrong. Validate that the performance log references previous sections.

### Composes With

Mission Command (intent envelope), Stigmergic Workspace (workspace coordination), Succession Pipeline (energy state progression), The Tool Chain (infrastructure stages)
