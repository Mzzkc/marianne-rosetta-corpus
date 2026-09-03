---
name: "CEGAR Loop (Progressive Refinement)"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
  - "Instrument-Task Fit"
generators:
  - "Incremental Exposure"
  - "Match Instrument to Grain"
problem: "Coarse-grained analysis produces spurious findings requiring expensive verification to distinguish real from false alarms."
signals:
  - "coarse analysis produces too many false alarms"
  - "expensive to verify every finding at fine grain"
  - "most findings disappear when abstraction is refined"
  - "need selective refinement, not full re-analysis"
stages:
  - name: coarse-check
    sheets: 1
    instrument_guidance: "codex-cli (gpt-5.5) — module-level analysis is primarily pattern-matching; codex-cli (gpt-5.5) provides good context for reducing false positives without the cost of claude-code"
    fallback_friendly: true
    purpose: "Analyze code at module level, identifying potential issues without deep reasoning."
    artifacts: ["findings.yaml"]
  - name: triage-findings
    sheets: 1
    instrument_guidance: "claude-code — distinguishing real from spurious findings requires deep code reasoning and domain knowledge; cannot be delegated to cheaper instruments"
    fallback_friendly: false
    purpose: "Verify each finding: determine if it is a real issue or an artifact of coarse abstraction."
    artifacts: ["triage-report.yaml"]
  - name: refine-or-report
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — filtering findings and selecting refinement targets is data-processing logic; any capable instrument suffices"
    fallback_friendly: true
    purpose: "Filter triage results and identify areas requiring finer-grained analysis; report findings confirmed as real."
    artifacts: ["refinement-targets.yaml", "current-report.md"]
  - name: check-termination
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — this stage uses shell-based validation to assert convergence (no LLM needed)"
    fallback_friendly: false
    purpose: "Verify that all refinement targets have been resolved, terminating the loop if convergence is achieved."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Memoization Cache"
    how: "Memoization Cache skips re-analysis of modules whose code has not changed, reducing the cost of CEGAR iterations."
  - pattern: "CDCL Search"
    how: "CDCL Search uses real findings confirmed by CEGAR triage as logical constraints to guide subsequent search."
  - pattern: "Immune Cascade"
    how: "CEGAR instantiates Immune Cascade with abstraction level as the escalation tier: coarse analysis first, then selective refinement on false positives."
config_features:
  - "self_chaining"
---

## CEGAR Loop (Progressive Refinement)

`Status: Working` · **Source:** Counterexample-Guided Abstraction Refinement (Clarke et al., 2000), Expedition 4. **Scale:** iteration. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Iteratively refines ABSTRACTION LEVEL, not output. Start coarse. If a problem is found, check if it's REAL or SPURIOUS (artifact of over-abstraction). If spurious, refine only the specific part that caused the false alarm. You never refine more than necessary. The structural move is minimum-cost verification through progressive abstraction refinement.

The multi-instrument strategy is central: cheap instrument (Sonnet) for the broad coarse pass, expensive instrument (Opus) for the targeted triage. This matches the work's nature — coarse scanning is pattern-matching (cheap), distinguishing real from spurious requires deep reasoning (expensive).

**Termination:** The loop terminates when the CLI validation sheet finds `refinement-targets.yaml` is empty (all findings resolved as REAL or SPURIOUS with no new areas to refine). If `max_chain_depth` is reached before convergence, the loop produces its best current report rather than failing.

### When to Use / When NOT to Use

Use for code review at scale (module-level first, function-level only where coarseness misleads), security audits (dependency scan then exploitability analysis), any verification where thorough analysis is expensive and most of the system is fine. Not when the abstraction hierarchy is shallow, spurious counterexamples are rare, or checking spurious vs. real costs more than full fine-grained analysis.

### Marianne Score Structure

```yaml
sheets:
  - name: coarse-check
    instrument: sonnet
    prompt: "Analyze at module level. Write findings.yaml with [{module, finding, confidence}]."
    validations:
      - type: file_exists
        path: "{{ workspace }}/findings.yaml"
  - name: triage-findings
    instrument: opus
    prompt: >
      For each finding in findings.yaml, determine: REAL or SPURIOUS?
      Write triage-report.yaml: [{module, finding, verdict: REAL|SPURIOUS, evidence}].
    capture_files: ["findings.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/triage-report.yaml"
  - name: refine-or-report
    prompt: >
      Read triage-report.yaml.
      Write refinement-targets.yaml listing modules with SPURIOUS findings needing finer analysis.
      Write current-report.md summarizing all REAL findings confirmed so far.
    capture_files: ["triage-report.yaml"]
  - name: check-termination
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; t=yaml.safe_load(open('{{ workspace }}/refinement-targets.yaml')); assert len(t)==0, f'{len(t)} targets remain'\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Triage consistently marks real findings as spurious — refinement chases ghosts while real issues pass through. Validate by checking that refined areas produce fewer findings (convergence signal). If the loop exhausts `max_chain_depth` without converging, the abstraction hierarchy may be too shallow for this problem — fall back to full fine-grained analysis. The check-termination assertion fails when targets remain, breaking the self-chain — this is intentional, forcing refinement to continue.

### Composes With

Memoization Cache (unchanged modules skip re-analysis), CDCL Search (real findings become constraints), Immune Cascade (CEGAR IS graduated response with abstraction control)
