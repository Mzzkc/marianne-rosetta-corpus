---
name: "Red Team / Blue Team"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Partial Failure"
generators:
  - "Exploit Failure as Signal"
problem: "Artifacts tested by known adversaries pass trivially; unknown adversaries reveal real flaws."
signals:
  - "testing is too predictable when defenders know the attacks"
  - "need to find vulnerabilities that prepared defense would miss"
  - "want realistic stress-testing where defenders work blind"
stages:
  - name: red-attack
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — needs reasoning capability to devise effective attacks; stronger instrument produces more sophisticated attacks"
    fallback_friendly: true
    purpose: "Devise and execute attacks against the artifact, recording both methods and effects."
    artifacts: ["red-workspace/effects.md", "red-workspace/methods.md"]
  - name: relay
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — shell command to copy effect descriptions without revealing method details"
    fallback_friendly: true
    purpose: "Copy attack effects from red's workspace to blue's briefing, redacting methods."
    artifacts: ["blue-briefing/effects.md"]
  - name: blue-defend
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must have reasoning capability to devise defenses against unknown attacks; stronger instrument produces more robust defenses"
    fallback_friendly: true
    purpose: "Read attack effects and devise defenses without knowing attack methods."
    artifacts: ["blue-response.md"]
  - name: purple-debrief
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to analyze attack-defense interactions and extract lessons; claude-code or codex-cli (gpt-5.5) recommended"
    fallback_friendly: false
    purpose: "Analyze all attack and defense data to generate attack-defense matrix and lessons."
    artifacts: ["debrief.md"]
dependencies: {}
composes_with:
  - pattern: "After-Action Review"
    how: "Purple debrief IS an after-action review, documenting attack-defense interactions and extracting patterns."
  - pattern: "Immune Cascade"
    how: "Red Team / Blue Team stress-tests each tier of Immune Cascade's repairs to validate robustness across difficulty levels."
---

## Red Team / Blue Team

`Status: Working` · **Source:** Military adversarial exercises. **Forces:** Information Asymmetry + Partial Failure.

### Core Dynamic

Information asymmetry via redaction: Red writes *effects* but not *methods*. Blue sees effects, must defend blind. Purple debrief gets full access. **Enforcement:** Separate workspace subdirectories (`red-workspace/` vs `blue-briefing/`). A relay stage copies only effect descriptions. Blue's `capture_files` is restricted to `blue-briefing/` only.

### When to Use / When NOT to Use

Use when the artifact needs adversarial stress-testing and the defender should not know attack methods. Not when the team is collaborative or the artifact is too simple for adversarial testing.

### Marianne Score Structure

```yaml
sheets:
  - name: red-attack
    prompt: "Attack the artifact. Write effects to red-workspace/effects.md and methods to red-workspace/methods.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/red-workspace/effects.md"
  - name: relay
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cp {{ workspace }}/red-workspace/effects.md {{ workspace }}/blue-briefing/effects.md"
  - name: blue-defend
    prompt: "Read blue-briefing/effects.md. Defend. Write blue-response.md."
    capture_files: ["blue-briefing/effects.md"]
  - name: purple-debrief
    prompt: "Read ALL files. Write debrief with attack-defense matrix."
    capture_files: ["red-workspace/**", "blue-briefing/**", "blue-response.md"]
```

### Failure Mode

Red produces weak attacks, Blue passes trivially. Validate Red output contains specific attack categories. If relay leaks methods, Blue's defense is tainted.

### Composes With

After-Action Review (purple debrief IS AAR), Immune Cascade
