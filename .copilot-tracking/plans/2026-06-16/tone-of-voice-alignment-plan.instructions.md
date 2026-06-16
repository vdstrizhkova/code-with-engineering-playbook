---
applyTo: '.copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md'
---
<!-- markdownlint-disable-file -->
# Implementation Plan: Tone-of-Voice Alignment for AI Guidance

## Overview

Revise the AI-guidance prose added on the `review-ai-guidance` branch so it matches the playbook's established conversational, first-person-plural mentoring voice without changing technical meaning or links.

## Objectives

### User Requirements

* Align the tone of voice of the branch's AI content with `main` — Source: conversation ("Create a plan for fixing the tone of voice of the repo").
* Elaborate the remediation work into actionable phases — Source: conversation ("elaborate on phase 2 3 and 4").
* Produce a plan from the existing research — Source: task-plan prompt invocation.

### Derived Objectives

* Preserve every recommendation, warning, heading, and cross-link while editing — Derived from: research scope constraint "tone only, no meaning change".
* Leave already-aligned pages (Tier C) untouched and use them as reference exemplars — Derived from: research finding that structure/persona pages already match the voice.
* Verify each edit against an explicit voice rubric — Derived from: need for objective, repeatable acceptance criteria.

## Context Summary

### Project Files

* docs/ai-assisted-engineering/README.md - New central guide; most divergent (Tier A, full rewrite).
* docs/developer-experience/copilots.md - New AI sections create an in-page tone seam (Tier A).
* docs/automated-testing/README.md - AI bullets clash with "We write our tests early" (Tier A).
* docs/non-functional-requirements/privacy/data-handling.md - Imperative section above conversational "5 W's" (Tier A).
* docs/documentation/README.md - "Unreviewed AI filler" label too judgmental (Tier A).
* docs/security/threat-modelling.md - Back-to-back bare lists + run-on closer (Tier A).
* docs/ml-and-ai-projects/responsible-ai.md - Five pure question lists (Tier A).
* docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md - Repetitive "Use [X] to…" list (Tier A, low risk).
* docs/observability/README.md - 11-item capture mega-bullet (Tier A).
* docs/CI-CD/README.md - Noun-stacked artifact paragraph (Tier A).
* docs/code-reviews/README.md, docs/code-reviews/process-guidance/reviewer-guidance.md, docs/source-control/README.md, docs/source-control/git-guidance/README.md, docs/UI-UX/README.md, docs/engineering-feedback/README.md, docs/non-functional-requirements/privacy/README.md, docs/automated-testing/test-planning.md, docs/agile-development/branching-and-cicd.md - Tier B light touch.
* docs/agile-development/README.md, docs/developer-experience/README.md, docs/start-here/**, docs/non-functional-requirements/README.md - Tier C reference exemplars (do not edit).

### References

* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md - Voice rubric, tier classification, per-file before/after instructions.

### Standards References

* /Users/vstrizhkova/.vscode/extensions/ise-hve-essentials.hve-core-all-3.2.2/.github/instructions/hve-core/writing-style.instructions.md — Canonical voice/tone standard for all Markdown.
* /Users/vstrizhkova/.vscode/extensions/ise-hve-essentials.hve-core-all-3.2.2/.github/instructions/hve-core/markdown.instructions.md — Markdown formatting standard.

## Implementation Checklist

### [x] Implementation Phase 1: Central Guide Rewrite

<!-- parallelizable: true -->

* [x] Step 1.1: Rewrite docs/ai-assisted-engineering/README.md to playbook voice
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 12-44)
* [x] Step 1.2: Validate phase changes
  * Run markdown lint and link check on the edited file
  * Confirm all headings and "Related Playbook Areas" links unchanged

### [x] Implementation Phase 2: Tone Seams

<!-- parallelizable: true -->

* [x] Step 2.1: Revise docs/developer-experience/copilots.md AI sections
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 46-74)
* [x] Step 2.2: Revise docs/automated-testing/README.md AI bullets
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 46-74)
* [x] Step 2.3: Revise docs/non-functional-requirements/privacy/data-handling.md AI section
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 46-74)
* [x] Step 2.4: Re-tone docs/documentation/README.md AI section and challenge label
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 46-74)
* [x] Step 2.5: Validate phase changes
  * Run markdown lint and link check on the four edited files

### [x] Implementation Phase 3: Dense Enumeration Pages

<!-- parallelizable: true -->

* [x] Step 3.1: Revise docs/security/threat-modelling.md AI section
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 76-108)
* [x] Step 3.2: Frame docs/ml-and-ai-projects/responsible-ai.md question lists
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 76-108)
* [x] Step 3.3: Vary list openers in docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 76-108)
* [x] Step 3.4: Split docs/observability/README.md capture mega-bullet
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 76-108)
* [x] Step 3.5: Unstack docs/CI-CD/README.md artifact paragraph and checklist
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 76-108)
* [x] Step 3.6: Validate phase changes
  * Run markdown lint and link check on the five edited files

### [x] Implementation Phase 4: Light Touch (Tier B)

<!-- parallelizable: true -->

* [x] Step 4.1: Review and lightly revise Tier B pages
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 110-136)
* [x] Step 4.2: Validate phase changes
  * Run markdown lint and link check on any edited Tier B files

### [x] Implementation Phase 5: Validation

<!-- parallelizable: false -->

* [x] Step 5.1: Run full validation
  * Details: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 138-156)
* [x] Step 5.2: Confirm meaning and links unchanged
  * Run `git diff main...HEAD` on edited files; verify no recommendation, anchor, or link was altered
* [x] Step 5.3: Confirm Tier C pages untouched
  * Verify docs/agile-development/README.md, docs/developer-experience/README.md, docs/start-here/**, docs/non-functional-requirements/README.md have no new changes

## Planning Log

See .copilot-tracking/plans/logs/2026-06-16/tone-of-voice-alignment-log.md for discrepancy tracking, implementation paths considered, and suggested follow-on work.

## Dependencies

* git (diff against `main` for verification)
* markdownlint / lychee link check (project lint tooling)
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (rubric and per-file instructions)

## Success Criteria

* Every Tier A page uses first-person-plural / direct "you" framing consistent with its surrounding prose — Traces to: User Requirement "align tone with main".
* No edited bullet contains more than ~4 comma-separated items without being broken up — Traces to: research rubric.
* Each directive list has at least one sentence of rationale or framing — Traces to: research rubric.
* All original links, anchors, headings, and recommendations are preserved — Traces to: Derived Objective "preserve meaning".
* Tier C reference pages are unmodified — Traces to: Derived Objective "leave aligned pages untouched".
