<!-- markdownlint-disable-file -->
# RPI Validation: Tone-of-Voice Alignment — Phase 2 (Tone Seams)

**Plan**: .copilot-tracking/plans/2026-06-16/tone-of-voice-alignment-plan.instructions.md
**Details**: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Phase 2, lines 46-74)
**Changes Log**: .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md
**Research / Rubric**: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md (lines 186-235)
**Phase**: 2 — Tone Seams
**Validation date**: 2026-06-16
**Status**: Pass-with-minor

## Acceptance Standard (Voice Rubric)

First-person-plural "we" / direct "you"; rationale before directive; framing sentence before lists; max ~4 comma-separated items per bullet; mentoring/hedged tone; no list-after-list without connective prose. Constraint: TONE ONLY — no recommendation, heading text, link target, or anchor may change.

## Step 1: Plan Items vs Changes Log

| Plan Step | File | Changes Log Entry | Status |
| --- | --- | --- | --- |
| 2.1 | docs/developer-experience/copilots.md | "Reframed … group lead sentences to first-person-plural 'we'/'you'" | Implemented |
| 2.2 | docs/automated-testing/README.md | "Converted … bullets to the page's 'we' voice … kept the `#testing-and-evaluation` link" | Implemented |
| 2.3 | docs/non-functional-requirements/privacy/data-handling.md | "Led with a page-voice framing sentence, broke the 7-item comma stack … softened the four directive bullet openers" | Implemented |
| 2.4 | docs/documentation/README.md | "renamed 'Unreviewed AI filler' … to 'Unreviewed generated content', reframing its two sub-bullets" | Implemented |
| 2.5 | (validation) | "`get_errors` clean … link checker zero broken links" | Claimed, not independently re-run here |

All four content steps have corresponding, accurate changes-log entries that match the working-tree diff.

## Step 2: File Evidence

### docs/developer-experience/copilots.md

- Heading "## Team Operating Model for AI-Assisted Delivery" unchanged at [copilots.md](docs/developer-experience/copilots.md#L67) → anchor `#team-operating-model-for-ai-assisted-delivery` PRESERVED.
- Six group-lead sentences converted to "we"/"you" with rationale clauses (e.g. "so the workflow stays proportional to the risk of the change", "because anything we paste into a tool can leave the approved environment"). Rationale-before-directive satisfied.
- Bullets left imperative — explicitly permitted by Phase 2 instruction ("bullets may stay imperative once the framing sentence sets the voice").
- All deep links (`generative-ai-and-agentic-systems.md`, `test-planning.md#ai-evaluation-planning`, code-reviews, source-control) sit on unchanged lines → PRESERVED.
- Lead-sentence comma runs are all 4 items (e.g. "production code, customer data, infrastructure, or security-sensitive changes"). Within rubric.

### docs/automated-testing/README.md

- `#testing-and-evaluation` deep link intact on unchanged context line [automated-testing/README.md](docs/automated-testing/README.md#L20) → PRESERVED.
- "treat output as draft" framing sentence retained.
- Five bullets converted to "we" voice matching "We write our tests early".
- FINDING: bullet at [automated-testing/README.md](docs/automated-testing/README.md#L25) retains a 6-item comma stack ("prompt injection, malformed input, sensitive data, refusal, fallback, and human-escalation scenarios"). See Findings.

### docs/non-functional-requirements/privacy/data-handling.md

- Heading "## AI tool data handling" unchanged; shared-guide link `../../ai-assisted-engineering/README.md` on unchanged line → PRESERVED.
- Opening bare-imperative replaced with a framing sentence in page voice; the original 7-item comma stack broken into a 3-item illustrative sub-list. Framing-before-list satisfied.
- Four directive bullets softened to "we" voice.
- FINDING: bullet at [data-handling.md](docs/non-functional-requirements/privacy/data-handling.md#L33) carries a 5-item stack ("retention, logging, access, deletion, and export"). Marginally over ~4. See Findings.

### docs/documentation/README.md

- "## AI-assisted documentation" heading unchanged; intro converted to "AI tools can help us draft … but we validate generated documentation". Voice aligned.
- Judgmental label "Unreviewed AI filler" renamed to neutral "Unreviewed generated content" at [documentation/README.md](docs/documentation/README.md#L56), matching neighbour labels (Inaccurate, Obsolete, Afterthought). Two sub-bullets reframed as observations ("fill space without a clear reader need", "drifts from the original technical meaning"). DR-03 satisfied.
- No links in the edited region.

## Step 3: Coverage & Findings

### Coverage Assessment

All four Phase 2 files implemented as described. Voice rubric substantially met on every file; in-page tone seams removed (lead sentences now match surrounding prose). All four protected anchors/links verified intact. Both specifically-named targets confirmed: `#team-operating-model-for-ai-assisted-delivery` and `#testing-and-evaluation`. No heading text, link target, or recommendation altered — tone-only constraint honored.

### Findings

#### Critical

- None.

#### Major

- None.

#### Minor

- **M-1 — 6-item comma stack remains in an edited bullet.** [automated-testing/README.md](docs/automated-testing/README.md#L25): "We include prompt injection, malformed input, sensitive data, refusal, fallback, and human-escalation scenarios where they apply." Six comma-separated items exceeds the rubric's max ~4. The Phase 2 step for this file scoped only voice conversion (not stack-splitting), and the items are six distinct test scenarios, so meaning is intact — but the edited line still breaches the global success criterion "No edited bullet contains more than ~4 comma-separated items." Directly answers the user's "any 6+ stacks remaining?" question: yes, one.
- **M-2 — 5-item comma stack in an edited bullet.** [data-handling.md](docs/non-functional-requirements/privacy/data-handling.md#L33): "the retention, logging, access, deletion, and export expectations". Five items, marginally over ~4 (was 5 pre-edit; the softening edit touched the line but did not split it). Low impact.

### Severity Summary

| Severity | Count |
| --- | --- |
| Critical | 0 |
| Major | 0 |
| Minor | 2 |

## Clarifying Questions

1. Is the ~4-item rule a hard gate for *edited* lines, or advisory when the items are atomic/distinct (as in the test-scenario list M-1)? If hard, M-1 should be split into two bullets or a framed sub-list.

## Recommended Next Validations (not performed this session)

- [ ] Independently re-run markdownlint and the repo internal-link checker on the four Phase 2 files (Step 2.5 results were taken from the changes log, not re-executed here).
- [ ] Validate Phase 1 (docs/ai-assisted-engineering/README.md central rewrite).
- [ ] Validate Phase 3 (dense enumeration pages; note DD-02 four-theme deviation and DD-03 CI-CD condensation).
- [ ] Validate Phase 4 (Tier B light touch + the seven "verified unchanged" pages).
- [ ] Confirm Phase 5 Tier C exemplars remain untouched.
- [ ] Confirm the out-of-scope `.gitattributes` working-tree change is addressed separately.
