<!-- markdownlint-disable-file -->
# Planning Log: Tone-of-Voice Alignment for AI Guidance

## Discrepancy Log

Gaps and differences identified between research findings and the implementation plan.

### Unaddressed Research Items

* DR-01: Impersonal imperative register (no "we") across AI sections
  * Source: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md ("Implementation Patterns" rubric)
  * Reason: Addressed in Phases 1-4; listed here for traceability.
  * Impact: high (primary tone mismatch)
* DR-02: 6-11 item comma-stacked enumerations in single bullets
  * Source: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (File Analysis: observability, threat-modelling, CI-CD)
  * Reason: Addressed in Phases 1, 3, 4.
  * Impact: medium
* DR-03: Judgmental label "Unreviewed AI filler"
  * Source: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (File Analysis: documentation/README.md)
  * Reason: Addressed in Phase 2 (Step 2.4).
  * Impact: low
* DR-04: List-after-list with no connective prose
  * Source: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (File Analysis: threat-modelling, responsible-ai)
  * Reason: Addressed in Phase 3.
  * Impact: medium

### Plan Deviations from Research

* DD-01: Research lists generative-ai-and-agentic-systems.md as Tier A, but the plan treats it as the lowest-risk Tier A page (mostly framing/variation, not rewrite)
  * Research recommends: same treatment as other Tier A pages
  * Plan implements: lighter treatment because the page already has good rationale openers and checklist framing
  * Rationale: avoids over-engineering; the page largely passes the rubric already.
  * Resolved during implementation: confirmed checklists already had framing sentences; only varied the repetitive "Use [X] to…" openers. (Phase 3.3)

* DD-02: threat-modelling.md controls split into FOUR groups, not three
  * Plan/research named three illustrative control themes; the closing run-on held 13 distinct controls.
  * Implementation used four themed groups (input/output handling, least privilege, operational safety, recovery/follow-up) to honor the <=4-item rule without dropping any control.
  * Rationale: meaning preservation + rubric compliance. Impact: low.

* DD-03: CI-CD checklist item condensed
  * One added checklist item's enumeration ("prompt, model, retrieval, agent, safety, and regression behavior") was tightened to "safety, groundedness, and regression behavior" per the "tighten checklist items" instruction.
  * Slight reduction in enumerated specificity; recommendation unchanged. Impact: low.

### Out-of-Scope Observations

* OOS-01: `.gitattributes` has an uncommitted working-tree change adding `\.github/workflows/*.lock.yml linguist-generated=true merge=ours`. Not produced by this task; unrelated to tone work. Left untouched (not discarded) per operational safety. Flagged for user review.

### Environment Note

* The canonical hve-core writing-style/markdown instruction files live on a host path (`/Users/vstrizhkova/.vscode/extensions/...`) not mounted in the dev container, so subagents could not read them directly. They relied on the equivalent rubric captured verbatim in the research file, which encodes the same standard. No impact on output quality.

## Implementation Paths Considered

### Selected: Phase-by-tone-severity, page-scoped edits

* Approach: Group edits into Tier A (rewrite), seams, dense pages, and Tier B light touch; edit page-by-page; verify against rubric.
* Rationale: Highest-impact, in-page tone seams fixed first; each change small, reviewable, reversible; preserves meaning.
* Evidence: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md ("Preferred Approach").

### IP-01: Global mechanical find/replace of imperative openers

* Approach: Scripted substitution of common imperative starts with "we"/"you" phrasing.
* Trade-offs: Fast, but tone is contextual; produces awkward or incorrect sentences and risks changing meaning.
* Rejection rationale: Unsafe for meaning preservation; rejected in research.

### IP-02: Rewrite only the central guide, leave domain pages

* Approach: Fix docs/ai-assisted-engineering/README.md only.
* Trade-offs: Less work, but leaves the most jarring in-page seams unaddressed.
* Rejection rationale: The seams (Phase 2) are the highest reader-impact issue.

### IP-03: Document findings only, no edits

* Approach: Stop at the review.
* Trade-offs: No remediation delivered.
* Rejection rationale: User asked for an executable fix plan.

## Suggested Follow-On Work

Items identified during planning that fall outside current scope.

* WI-01: Tone-align navigation labels — review docs/.pages and docs/start-here/.pages titles for voice consistency (low)
  * Source: research "Potential Next Research"
  * Dependency: none
* WI-02: Add a short voice/tone note to CONTRIBUTING.md or a docs style guide so future AI content matches the playbook by default (medium)
  * Source: planning inference
  * Dependency: completion of this plan (use the rubric as the source)
* WI-03: Confirm full contents of generative-ai-and-agentic-systems.md against rubric during implementation in case deeper rewrite is warranted (low)
  * Source: DD-01
  * Dependency: Phase 3 execution
