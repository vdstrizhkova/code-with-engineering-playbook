<!-- markdownlint-disable-file -->
# Release Changes: Tone-of-Voice Alignment for AI Guidance

**Related Plan**: tone-of-voice-alignment-plan.instructions.md
**Implementation Date**: 2026-06-16

## Summary

Revise the AI-guidance prose added on the `review-ai-guidance` branch so it matches the playbook's established conversational, first-person-plural mentoring voice, without changing technical meaning or links.

## Changes

### Added

* (none yet)

### Modified

* docs/ai-assisted-engineering/README.md — Rewrote the central guide to the playbook's first-person-plural mentoring voice: converted impersonal-imperative section intros to rationale-first "we"/"you" framing and split every 6+ item comma stack into <=4-item runs (the 11-item observability capture bullet became a grouped sub-list); all section headings, "Related Playbook Areas" links, and the `#ai-systems-threat-modeling-considerations` anchor preserved (Phase 1.1).
* docs/developer-experience/copilots.md — Reframed the "Team Operating Model for AI-Assisted Delivery" and "Validating AI-Assisted Work" group lead sentences to first-person-plural "we"/"you" voice so the new sections read as the same author as the surrounding "Considerations" prose; headings, anchors, links, and bullets unchanged (Phase 2.1).
* docs/automated-testing/README.md — Converted the "Testing AI-assisted and AI-enabled changes" bullets to the page's "we" voice matching "We write our tests early"; kept the `#testing-and-evaluation` link and the "treat output as draft" framing (Phase 2.2).
* docs/non-functional-requirements/privacy/data-handling.md — Led "AI tool data handling" with a page-voice framing sentence, broke the 7-item comma stack into a short grouped list, and softened the four directive bullet openers to "we" voice; kept the shared-guide link (Phase 2.3).
* docs/documentation/README.md — Lightly re-toned the "AI-assisted documentation" intro to the page's register and renamed the "Unreviewed AI filler" challenge label to the neutral "Unreviewed generated content", reframing its two sub-bullets as observations (Phase 2.4).
* docs/code-reviews/README.md — Reframed the bare-imperative "Reviewing AI-assisted changes" opener ("Review AI-generated code as untrusted code:") to first-person-plural "We review AI-generated code as untrusted code, confirming…"; bullets, headings, and the AI-Assisted Engineering link unchanged (Phase 4.1).
* docs/engineering-feedback/README.md — Broke the 8-item comma stack in the "AI Tooling Feedback" closing sentence into grouped clauses with direct "you" voice ("When you submit AI tooling feedback, include…"); preserved all submission details and the AI-Assisted Engineering link (Phase 4.1).
* docs/security/threat-modelling.md — Gave each of the three lists in "AI Systems Threat Modeling Considerations" a voiced "we" lead-in and split the 13-item closing "Common controls include…" run-on into a four-theme grouped list (input/output handling, least privilege, operational safety, recovery); every risk item and the `#ai-systems-threat-modeling-considerations` anchor preserved (Phase 3.1).
* docs/ml-and-ai-projects/responsible-ai.md — Added one "we"-voiced framing sentence under each of the five question-list subsections explaining when the team asks them; kept the question format and all four cross-links (Phase 3.2).
* docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md — Varied the repetitive "Use [X] to…" openers in "Review the System Across Disciplines" (Lean on / Turn to / Let / Run / Plan with / Treat / Reach for / Check / Revisit / Bring in); checklists and the `#review-the-system-across-disciplines` heading/anchor and all links unchanged (Phase 3.3).
* docs/observability/README.md — Split the 11-item "AI observability" capture mega-bullet into three grouped bullets (request context, operational signals, safety signals), each <=4 items; kept the other bullets and the shared-guide link (Phase 3.4).
* docs/CI-CD/README.md — Led the AI artifact paragraph with the principle as a sentence then listed the six artifacts as a three-item sub-list, and tightened the two added checklist items to match existing checkbox brevity; preserved the AI-Assisted Engineering and `#review-the-system-across-disciplines` deep links (Phase 3.5).

### Removed

* (none planned)

## Additional or Deviating Changes

* DD-02: Phase 3.1 threat-modelling controls — the closing run-on contained 13 distinct controls; honoring the <=4-item rule required FOUR themed groups (input/output handling, least privilege, operational safety, recovery/follow-up) rather than the three named illustratively in the research. No control was dropped.
* DD-03: Phase 3.5 CI-CD — to meet the "tighten" instruction, one added checklist item's enumeration ("prompt, model, retrieval, agent, safety, and regression behavior") was condensed to "safety, groundedness, and regression behavior". This was flagged in review as MAJ-01 (a substantive narrowing beyond tone scope) and **corrected in the follow-up rework** (.copilot-tracking/changes/2026-06-16/tone-rework-review-fixes-changes.md): full gate-type coverage restored and "groundedness" removed.
* OUT OF SCOPE (not made by this task): `.gitattributes` has an uncommitted working-tree change adding `\.github/workflows/*.lock.yml linguist-generated=true merge=ours`. This is unrelated to tone-of-voice work and was present in the working tree; it was left untouched rather than discarded. Flag for user review.
* Phase 4 (Tier B light touch) — reviewed and intentionally left UNCHANGED because they already pass the rubric: docs/code-reviews/process-guidance/reviewer-guidance.md (both checklist sub-blocks already framed with "During review, check that:" and "…also review evaluation evidence:"; all `#team-operating-model-for-ai-assisted-delivery`, `#ai-evaluation-planning`, `#ai-systems-threat-modeling-considerations` links intact); docs/source-control/README.md and docs/source-control/git-guidance/README.md (bullet openers read consistently after well-toned framing prose); docs/UI-UX/README.md (intro well-toned, ordered list renders correctly, no 6+ item comma stack — max 5); docs/non-functional-requirements/privacy/README.md (CORRECTED: this justification was overstated — the intro carried a 7-item comma stack; flagged as review MAJ-02 and fixed in the follow-up rework, see .copilot-tracking/changes/2026-06-16/tone-rework-review-fixes-changes.md); docs/automated-testing/test-planning.md (good prose; the pattern bullets enumerate distinct test types where trimming would change meaning, so left intact); docs/agile-development/branching-and-cicd.md (de-duplication/link-redirection changes verified to read in the page voice — no tone rewrite needed).

## Release Summary

Tone-only alignment of the branch's AI guidance to the playbook's first-person-plural mentoring voice. 12 documentation files modified (0 added, 0 removed). Tier A central guide fully re-toned; four in-page tone seams removed; five dense enumeration pages given connective prose and split comma stacks; two Tier B pages lightly revised and seven verified as already compliant. Tier C reference exemplars (docs/agile-development/README.md, docs/developer-experience/README.md, docs/start-here/**, docs/non-functional-requirements/README.md) confirmed untouched.

Validation: `get_errors` clean on all 12 files; repo internal-link checker reports zero broken links/anchors in any edited file (pre-existing link errors elsewhere in the repo are unrelated and untouched); `git diff` confirms only prose/structure lines changed — no heading, link, or anchor target altered. No recommendation or technical meaning changed.

Files modified: docs/ai-assisted-engineering/README.md, docs/developer-experience/copilots.md, docs/automated-testing/README.md, docs/non-functional-requirements/privacy/data-handling.md, docs/documentation/README.md, docs/code-reviews/README.md, docs/engineering-feedback/README.md, docs/security/threat-modelling.md, docs/ml-and-ai-projects/responsible-ai.md, docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md, docs/observability/README.md, docs/CI-CD/README.md.

No dependency or infrastructure changes. No deployment impact (documentation only).

Out-of-scope note: an unrelated uncommitted `.gitattributes` change exists in the working tree and was deliberately left for user review.
