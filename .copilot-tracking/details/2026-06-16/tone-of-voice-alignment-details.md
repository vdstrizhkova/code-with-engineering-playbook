<!-- markdownlint-disable-file -->
# Implementation Details: Tone-of-Voice Alignment for AI Guidance

## Context Reference

Sources: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (voice rubric, tier classification, before/after samples); hve-core writing-style.instructions.md (canonical voice standard); branch `review-ai-guidance` diff vs `main`.

Voice rubric (acceptance standard for all steps): first-person plural / direct "you"; rationale before directive; bold lead-in + explanatory sentence for bullets; max ~4 comma-separated items per bullet; mentoring and hedged tone; no list-after-list without connective prose. Reference exemplar: docs/agile-development/README.md "AI tooling considerations".

## Implementation Phase 1: Central Guide Rewrite

<!-- parallelizable: true -->

### Step 1.1: Rewrite docs/ai-assisted-engineering/README.md to playbook voice

Rewrite the guide end to end so each section reads as playbook authorship. Convert section intros from impersonal imperative ("Treat AI output as draft material…") to "we"/"you" with a one-sentence rationale. Split every 6+ item comma stack into a short sub-list or a sentence naming the 3-4 most important items plus "and related concerns". Keep every section heading and all "Related Playbook Areas" links intact.

Files:
* docs/ai-assisted-engineering/README.md - Full voice rewrite; preserve structure, headings, links.

Discrepancy references:
* Addresses DR-01 (impersonal register), DR-02 (comma-stack enumerations).

Success criteria:
* No section opens with a bare imperative lacking a framing sentence.
* No bullet exceeds ~4 comma-separated items.
* All headings and "Related Playbook Areas" links byte-identical to the branch version.

Context references:
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (Implementation Patterns rubric table; "Phase 1 — Central guide").

Dependencies:
* Rubric agreed (Phase 0 in research).

## Implementation Phase 2: Tone Seams

<!-- parallelizable: true -->

### Step 2.1-2.4: Revise in-page tone seams

For each file, make the new AI section sound like the same author wrote the surrounding original prose. Add a one-sentence rationale where a section is a bare directive list; convert lead sentences to "we"/"you"; bullets may stay imperative once the framing sentence sets the voice. Preserve all links and anchors.

Files:
* docs/developer-experience/copilots.md - Reframe "Team Operating Model for AI-Assisted Delivery" and "Validating AI-Assisted Work"; add rationale under each lead; convert group lead sentences to "we"/"you"; keep `#team-operating-model-for-ai-assisted-delivery` and other anchors.
* docs/automated-testing/README.md - Convert AI bullets to "we" voice matching "We write our tests early"; keep the `#testing-and-evaluation` link and "treat output as draft" framing.
* docs/non-functional-requirements/privacy/data-handling.md - Lead "AI tool data handling" with a framing sentence; break the 7-item comma stack; soften the four directive bullet openers; keep the shared-guide link before "5 W's".
* docs/documentation/README.md - Lightly re-tone "AI-assisted documentation" intro; rename "Unreviewed AI filler" to a neutral label (for example "Unreviewed generated content") and reframe its sub-bullets as observations.

Discrepancy references:
* Addresses DR-01, DR-02, and DR-03 (judgmental label).

Success criteria:
* No abrupt person/voice shift between original prose and the new AI section on each page.
* "Unreviewed AI filler" label replaced with a neutral label consistent with neighbouring challenge labels.
* All anchors and cross-links preserved.

Context references:
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md ("Phase 2 — Tone seams" with before/after samples).

Dependencies:
* None on Phase 1 (different files); may run in parallel.

## Implementation Phase 3: Dense Enumeration Pages

<!-- parallelizable: true -->

### Step 3.1-3.5: Add connective prose and break long stacks

Keep all content; add connective tissue and split the longest comma stacks so prose breathes. Do not delete checklist items or questions.

Files:
* docs/security/threat-modelling.md - Add a one-line lead-in before each of the three lists (risk categories, assets/trust boundaries, identification prompts); split the closing "Common controls include…" run-on into a short grouped list or two sentences; keep `#ai-systems-threat-modeling-considerations` anchor and every risk item.
* docs/ml-and-ai-projects/responsible-ai.md - Keep the question format; add one "we"-voiced framing sentence under each of the five subsection headings; preserve all four cross-links.
* docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md - Keep checklists; ensure each has its one-line framing sentence; vary the repetitive "Use [X] to…" openers in "Review the System Across Disciplines". Lowest-risk Tier A page.
* docs/observability/README.md - Split the 11-item capture mega-bullet into 3 grouped bullets (model/version context; operational signals; safety signals); keep surrounding bullets and the shared-guide link.
* docs/CI-CD/README.md - Lead the artifact paragraph with the principle, then list artifacts as a short sub-list or trimmed set; tighten the two added checklist items; preserve both deep links.

Discrepancy references:
* Addresses DR-02 (comma stacks), DR-04 (list-after-list without connective prose).

Success criteria:
* No section presents 2+ bare lists back-to-back without a lead-in sentence.
* The observability capture bullet is grouped into <=3 bullets, each <=4 items.
* All anchors, deep links, risk items, questions, and checklist items preserved.

Context references:
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md ("Phase 3 — Dense enumeration pages").

Dependencies:
* None on Phases 1-2 (different files); may run in parallel.

## Implementation Phase 4: Light Touch (Tier B)

<!-- parallelizable: true -->

### Step 4.1: Review and lightly revise Tier B pages

Review each Tier B page; edit only where it diverges from the rubric (impersonal opener or one overlong stack). Several may already pass — do not over-rewrite. branching-and-cicd.md is mostly de-duplication/link redirection; verify wording reads in the page voice, no tone rewrite.

Files:
* docs/code-reviews/README.md - Optional light "we review…" opener for "Reviewing AI-assisted changes".
* docs/code-reviews/process-guidance/reviewer-guidance.md - Add one framing sentence per checklist sub-block; keep checks intact.
* docs/source-control/README.md and docs/source-control/git-guidance/README.md - Check bullet openers read consistently; minimal change.
* docs/UI-UX/README.md - Light trim of long numbered items; verify ordered-list rendering.
* docs/engineering-feedback/README.md - Trim the longest comma stack if heavy.
* docs/non-functional-requirements/privacy/README.md - Add one framing sentence; leave questions.
* docs/automated-testing/test-planning.md - Trim only if a pattern item runs too long.
* docs/agile-development/branching-and-cicd.md - Verify rewritten sentences read in page voice; no tone rewrite.

Discrepancy references:
* Addresses DR-01, DR-02 where still present in Tier B.

Success criteria:
* No Tier B page retains an unframed bare-imperative section or a 6+ item comma stack.
* Pages that already pass are left unchanged.

Context references:
* .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md ("Phase 4 — Light touch").

Dependencies:
* None on Phases 1-3 (different files); may run in parallel.

## Implementation Phase 5: Validation

<!-- parallelizable: false -->

### Step 5.1: Run full validation

Run the project's markdown lint and link check over all edited files, then re-read each against the rubric.

Validation commands:
* markdownlint over edited docs/** files - style/format.
* lychee (lychee.toml) link check - confirm no broken links introduced.

### Step 5.2: Confirm meaning and links unchanged

Run `git diff main...HEAD -- <edited files>` and confirm no recommendation, heading, anchor, or link target changed — only prose voice.

### Step 5.3: Confirm Tier C pages untouched

Verify docs/agile-development/README.md, docs/developer-experience/README.md, docs/start-here/**, and docs/non-functional-requirements/README.md show no new changes versus the pre-edit branch state.

## Dependencies

* git, markdownlint, lychee.

## Success Criteria

* All Tier A/B pages pass the rubric; Tier C untouched; links and meaning preserved.
