---
applyTo: '.copilot-tracking/changes/2026-06-16/tone-rework-review-fixes-changes.md'
---
<!-- markdownlint-disable-file -->
# Implementation Plan: Tone Review Rework Fixes

## Overview

Resolve the two Major findings from the tone-of-voice alignment review by restoring the CI-CD evaluation-gate recommendation coverage and removing the rubric-breaching comma stack in the privacy fundamentals intro, then re-validate.

## Objectives

### User Requirements

* Address the review findings produced for the tone-of-voice alignment work — Source: conversation (task-review handoff, then task-plan invocation on the review log).

### Derived Objectives

* Restore the full evaluation-gate coverage that the tone edit narrowed (MAJ-01) without reintroducing a 6+ item comma stack — Derived from: review finding MAJ-01 and the original task constraint "preserve every recommendation".
* Bring docs/non-functional-requirements/privacy/README.md into rubric compliance and make the changes-log justification accurate (MAJ-02) — Derived from: review finding MAJ-02.
* Optionally clear the two cheapest Minor findings in already-edited passages (MIN-01) — Derived from: review Follow-Up "optional polish".
* Keep all edits tone/structure only — no heading, link, or anchor target changes — Derived from: original task constraint carried into rework.

## Context Summary

### Project Files

* docs/CI-CD/README.md - Lines 84-90 hold the two altered checklist items; the second dropped prompt/model/retrieval/agent gate types and introduced "groundedness" (MAJ-01).
* docs/non-functional-requirements/privacy/README.md - Line 10 intro has a 7-item comma stack ("prompts, retrieved content, model providers, tool calls, telemetry, memory, and generated summaries") left unchanged with an inaccurate "already passes" justification (MAJ-02).
* docs/automated-testing/README.md - Line 25 retains a 6-item comma stack inside an already-edited passage (MIN-01, optional).
* .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md - Existing changes log; DD-03 entry and the Tier B "unchanged" justification need correcting after these fixes.

### References

* .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md - Review log with MAJ-01, MAJ-02, MIN-01 evidence and recommended remediation.
* .copilot-tracking/reviews/rpi/2026-06-16/tone-of-voice-alignment-plan-003-validation.md - Phase 3 detail behind MAJ-01 (DD-03).
* .copilot-tracking/reviews/rpi/2026-06-16/tone-of-voice-alignment-plan-004-validation.md - Phase 4 detail behind MAJ-02 (F-001).
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md - Voice rubric (acceptance standard): "we"/"you", rationale-first, framing before lists, max ~4 comma items per bullet.

### Standards References

* .github/instructions writing-style and markdown instructions apply to **/*.md — voice, tone, and markdown conventions for all edits.

## Implementation Checklist

### [x] Implementation Phase 1: Major Finding Fixes

<!-- parallelizable: true -->

* [x] Step 1.1: Restore CI-CD evaluation-gate coverage (MAJ-01)
  * Details: .copilot-tracking/details/2026-06-16/tone-rework-review-fixes-details.md (Lines 12-37)
* [x] Step 1.2: Resolve privacy intro comma stack and justification (MAJ-02)
  * Details: .copilot-tracking/details/2026-06-16/tone-rework-review-fixes-details.md (Lines 38-62)
* [x] Step 1.3: Validate phase changes
  * Run get_errors on the two edited files
  * Run .copilot-tracking/scripts/check_internal_links.py filtered to the edited files

### [x] Implementation Phase 2: Optional Minor Polish

<!-- parallelizable: true -->

* [x] Step 2.1: Split the automated-testing 6-item comma stack (MIN-01)
  * Details: .copilot-tracking/details/2026-06-16/tone-rework-review-fixes-details.md (Lines 73-91)
* [x] Step 2.2: Validate phase changes
  * Run get_errors and the link checker on docs/automated-testing/README.md

### [x] Implementation Phase 3: Tracking and Validation

<!-- parallelizable: false -->

* [x] Step 3.1: Update changes log and review status
  * Details: .copilot-tracking/details/2026-06-16/tone-rework-review-fixes-details.md (Lines 102-119)
* [x] Step 3.2: Run full validation
  * get_errors on all changed files; link checker; `git diff HEAD` confirms tone/coverage only, no anchor or link target changed
* [x] Step 3.3: Report residual items
  * Confirm MAJ-01 and MAJ-02 resolved; note any remaining Minor items deferred and the still-open `.gitattributes` decision (OOS-01)

## Planning Log

See .copilot-tracking/plans/logs/2026-06-16/tone-rework-review-fixes-log.md for discrepancy tracking, implementation paths considered, and suggested follow-on work.

## Dependencies

* Existing review log and RPI validation files (inputs).
* .copilot-tracking/scripts/check_internal_links.py (internal link/anchor checker).
* VS Code diagnostics via get_errors (markdownlint/lychee not installed locally).

## Success Criteria

* CI-CD checklist again recommends evaluation gates covering prompt, model, retrieval, agent, safety, and regression behavior, expressed without a 6+ item comma stack — Traces to: MAJ-01.
* docs/non-functional-requirements/privacy/README.md intro carries no comma stack above ~4 items and the changes-log justification matches reality — Traces to: MAJ-02.
* All edited files pass get_errors and the internal-link checker; `git diff HEAD` shows no heading, link, or anchor target changes — Traces to: tone-only constraint.
* Review log Overall Status updated to reflect resolved Major findings — Traces to: review handoff.
