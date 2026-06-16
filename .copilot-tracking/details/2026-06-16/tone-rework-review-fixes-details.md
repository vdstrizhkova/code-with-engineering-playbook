<!-- markdownlint-disable-file -->
# Implementation Details: Tone Review Rework Fixes

## Context Reference

Sources: .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md (MAJ-01, MAJ-02, MIN-01); .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (voice rubric); docs/CI-CD/README.md and docs/non-functional-requirements/privacy/README.md (current state read during planning).

## Implementation Phase 1: Major Finding Fixes

<!-- parallelizable: true -->

### Step 1.1: Restore CI-CD evaluation-gate coverage (MAJ-01)

The tone edit narrowed the second checklist item from "evaluation gates for prompt, model, retrieval, agent, safety, and regression behavior where applicable" to "evaluation gates for safety, groundedness, and regression behavior", dropping four gate types and adding "groundedness". Restore the full gate-type coverage while keeping the item readable. Because the original enumeration is six items, express it as two grouped clauses rather than one flat 6-item stack (rubric: max ~4 comma items per bullet).

Suggested target wording (confirm during implementation):
* Item 1 (evaluation evidence): keep the restored "or release record" location reference if it was meaningful — "Prompt, model, retrieval, safety, and tool-permission changes have evaluation evidence in the PR or release record". Decide whether the shorter "tool" vs original "tool-permission" matters; prefer restoring "tool-permission" for precision.
* Item 2 (evaluation gates): "AI-enabled systems include evaluation gates for prompt, model, retrieval, and agent behavior, plus safety and regression checks, where applicable." This restores all original gate types, keeps each clause <=4 items, and drops the unrequested "groundedness" addition (or retain groundedness only if the user confirms it is an intended addition — see Planning Log DD-01).

Files:
* docs/CI-CD/README.md - Lines 86-87 (the two checklist items under "Guardrails and checklist").

Discrepancy references:
* Addresses MAJ-01 / reverses the substantive part of DD-03 in the original changes log.

Success criteria:
* Both original gate-type enumerations (prompt, model, retrieval, agent) are present again.
* No single checklist item contains a 6+ item comma stack.
* "groundedness" is removed unless the user confirms keeping it.
* No checkbox added or removed; surrounding items unchanged.

Context references:
* .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md - MAJ-01 evidence and recommendation.

Dependencies:
* None (independent file).

### Step 1.2: Resolve privacy intro comma stack and justification (MAJ-02)

The "AI Privacy Review Prompts" intro sentence carries a 7-item comma stack ("prompts, retrieved content, model providers, tool calls, telemetry, memory, and generated summaries"). Apply the same light touch used on sibling pages: keep meaning, break the stack into <=4-item groups, and add a brief connective framing if natural.

Suggested target wording (confirm during implementation): "Generative AI and agentic systems can move private data through many surfaces — user-facing inputs like prompts and retrieved content, the systems that process them such as model providers and tool calls, and what the system retains afterward in telemetry, memory, and generated summaries." (Three grouped clauses, each <=3 items, all seven surfaces preserved.)

After editing, correct the original changes log so its Tier B "unchanged" justification no longer claims privacy/README.md already passes the rubric (handled in Step 3.1).

Files:
* docs/non-functional-requirements/privacy/README.md - Line 10 intro paragraph under "## AI Privacy Review Prompts".

Discrepancy references:
* Addresses MAJ-02 (review F-001).

Success criteria:
* No comma stack above ~4 items in the intro.
* All seven data surfaces still named; the two cross-links (Responsible AI, generative AI and agentic systems) unchanged.
* Heading and the eight question bullets unchanged.

Context references:
* .copilot-tracking/reviews/rpi/2026-06-16/tone-of-voice-alignment-plan-004-validation.md - F-001 detail.

Dependencies:
* None (independent file).

### Step 1.3: Validate phase changes

Validation commands:
* get_errors on docs/CI-CD/README.md and docs/non-functional-requirements/privacy/README.md - expect no errors.
* python .copilot-tracking/scripts/check_internal_links.py (filter to the two files) - expect no broken links/anchors.

## Implementation Phase 2: Optional Minor Polish

<!-- parallelizable: true -->

### Step 2.1: Split the automated-testing 6-item comma stack (MIN-01)

Line 25 retains a 6-item stack ("prompt injection, malformed input, sensitive data, refusal, fallback, and human-escalation scenarios") inside a passage already re-toned in Phase 2. Break it into two grouped clauses (e.g. adversarial inputs vs response/escalation behavior) without changing which scenarios are listed. This step is optional polish; skip if the user declines.

Files:
* docs/automated-testing/README.md - Line 25.

Discrepancy references:
* Addresses MIN-01 (optional).

Success criteria:
* All six scenarios preserved; no 6+ item comma stack remains in that bullet; `#testing-and-evaluation` link unchanged.

Context references:
* .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md - MIN-01.

Dependencies:
* None.

### Step 2.2: Validate phase changes

Validation commands:
* get_errors on docs/automated-testing/README.md.
* python .copilot-tracking/scripts/check_internal_links.py (filter to the file).

## Implementation Phase 3: Tracking and Validation

<!-- parallelizable: false -->

### Step 3.1: Update changes log and review status

Update the existing changes log and review log to reflect the rework:
* In .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md: amend the DD-03 entry to note MAJ-01 was corrected (coverage restored), and correct the Tier B "unchanged" list so it no longer claims privacy/README.md already passes (it was edited in this rework).
* In .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md: mark MAJ-01 and MAJ-02 resolved and update Overall Status.
* Record the rework itself in a new changes log at .copilot-tracking/changes/2026-06-16/tone-rework-review-fixes-changes.md (created during implementation per the plan frontmatter).

Files:
* .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md
* .copilot-tracking/reviews/2026-06-16/tone-of-voice-alignment-plan-review.md
* .copilot-tracking/changes/2026-06-16/tone-rework-review-fixes-changes.md (new)

Success criteria:
* Tracking artifacts accurately reflect the resolved Major findings.

Dependencies:
* Phase 1 (and Phase 2 if run) complete.

### Step 3.2: Run full validation

Execute:
* get_errors on all changed files.
* python .copilot-tracking/scripts/check_internal_links.py (filter to changed files).
* git diff HEAD on changed docs files - confirm only prose/coverage changed; no heading, link, or anchor target altered.

### Step 3.3: Report residual items

Confirm MAJ-01 and MAJ-02 resolved. Note remaining deferred Minor items (MIN-02..06) and the still-open out-of-scope `.gitattributes` decision (OOS-01). Recommend next steps rather than expanding scope.

## Dependencies

* .copilot-tracking/scripts/check_internal_links.py
* Existing review and changes-log artifacts.

## Success Criteria

* MAJ-01 and MAJ-02 resolved with tone-only/coverage-restoring edits; all validation clean.
