<!-- markdownlint-disable-file -->
# Planning Log: Tone Review Rework Fixes

## Discrepancy Log

Gaps and decisions identified while planning the rework of the tone-of-voice review findings.

### Unaddressed Research Items

* DR-01: Minor findings MIN-02 through MIN-06 from the review are not all addressed in this plan
  * Source: .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md (Findings detail)
  * Reason: They are rubric-advisory, mostly in unedited Tier B files or term-of-art enumerations where splitting risks changing meaning; only the cheapest (MIN-01) is included as optional Phase 2.
  * Impact: low

* DR-02: The out-of-scope `.gitattributes` working-tree change (OOS-01) is not handled by this plan
  * Source: review log Missing Work and Deviations / OOS-01
  * Reason: Unrelated to tone work; requires a user keep/commit/revert decision, not a code fix.
  * Impact: low (flagged for user, not blocking)

### Plan Deviations from Research

* DD-01: Whether to keep "groundedness" in the CI-CD evaluation-gate item
  * Research/original recommends: original enumeration was "prompt, model, retrieval, agent, safety, and regression behavior" (no groundedness).
  * Plan implements: restore all original gate types and remove "groundedness" by default, but allow keeping it if the user confirms it is an intended improvement (groundedness is a legitimate eval dimension referenced elsewhere in the AI guidance).
  * Rationale: the task constraint is to preserve the original recommendation; adding a dimension is a content change that should be an explicit choice, not a silent side effect of a tone edit.

<!-- Entries below added by Plan Validator (2026-06-16) -->

* DD-02: Privacy intro line-number cross-reference is off by one (Minor)
  * Research/source recommends: the review cites the privacy intro stack at docs/non-functional-requirements/privacy/README.md#L10, and the live file confirms the "Generative AI and agentic systems can move private data through..." sentence is on line 10.
  * Plan implements: plan Context Summary and details Step 1.2 Files both cite "Line 9".
  * Rationale: low impact because the edit is text-anchored to the "AI Privacy Review Prompts" intro sentence (will still target the correct line), but the documented pointer is inaccurate and should read Line 10.

* DD-03: Plan-to-details line-range cross-references are misaligned with the actual detail step blocks (Minor)
  * Research/source recommends: plan checklist steps should point to the exact detail block for each step.
  * Plan implements: actual detail headers are Step 1.1 = L12-37, Step 1.2 = L38-62, Step 2.1 = L73-91, Step 3.1 = L102-119; the plan points Step 1.1->"12-44" (overruns into Step 1.2), Step 1.2->"46-72" (starts 8 lines after the real Step 1.2 header at L38 and bleeds into Step 1.3), Step 2.1->"74-96", and Step 3.1->"98-124" (L98 is the Phase 3 header, not Step 3.1 at L102).
  * Rationale: navigation/traceability only; no impact on edit correctness, but ranges should be tightened to match each detail block.

* DD-04: Restored CI-CD Item 1 wording yields a 5-item comma stack, marginally above the ~4-item rubric guidance (Minor/low)
  * Research/source recommends: rubric advises max ~4 comma items per bullet; review MAJ-01 also requires restoring the original "or release record" location and "tool-permission" precision.
  * Plan implements: details Step 1.1 restores "Prompt, model, retrieval, safety, and tool-permission changes have evaluation evidence in the PR or release record" (5 comma items), and the step's own success criterion only guards against a 6+ item stack.
  * Rationale: accepted as a faithful restoration of the original recommendation (preserve-every-recommendation outranks the soft ~4 guidance here); flagged so the rubric tension is explicit and an optional re-grouping can be considered.

## Implementation Paths Considered

### Selected: Targeted two-file rework with optional minor polish

* Approach: fix only the two Major findings (MAJ-01, MAJ-02) as parallel edits, offer MIN-01 as optional polish, then sync tracking artifacts.
* Rationale: smallest change that clears the merge-blocking findings while honoring the tone-only/preserve-recommendation constraint.
* Evidence: .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md Follow-Up Recommendations (items 1-2 before merge; items 4-5 optional).

### IP-01: Address all 6 Minor findings as well

* Approach: also split the reviewer-guidance.md, test-planning.md, UI-UX, data-handling stacks and align the reviewer-guidance opener.
* Trade-offs: fuller rubric compliance, but several involve term-of-art enumerations where splitting changes meaning, and touch previously-validated Tier B files, widening risk and re-validation surface.
* Rejection rationale: out of proportion to the merge-blocking issues; better deferred as explicit follow-on if desired.

### IP-02: Revert the original tone edits on the two files and re-tone from scratch

* Approach: discard the Phase 3.5 / Phase 4 outcomes on these files and redo.
* Trade-offs: cleaner provenance but discards good voice work that is otherwise correct.
* Rejection rationale: wasteful; the defects are localized and patchable in place.

## Suggested Follow-On Work

* WI-01: Decide and apply the `.gitattributes` change (OOS-01) — keep, commit separately, or revert (medium)
  * Source: review OOS-01
  * Dependency: user decision
* WI-02: Sweep remaining Minor comma stacks in Tier B pages (MIN-02..06) if full rubric compliance is desired (low)
  * Source: review Findings detail
  * Dependency: none
* WI-03: Carry-over from original planning — WI nav labels, CONTRIBUTING voice note, deeper generative-ai pass (low)
  * Source: original tone-of-voice planning log
  * Dependency: none
