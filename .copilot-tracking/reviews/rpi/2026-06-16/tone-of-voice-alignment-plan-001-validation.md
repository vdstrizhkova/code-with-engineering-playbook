<!-- markdownlint-disable-file -->
# RPI Validation: Tone-of-Voice Alignment — Phase 1 (Central Guide Rewrite)

**Validation Date**: 2026-06-16
**Phase**: 1 — Central Guide Rewrite
**Status**: Pass-with-minor

## Inputs

* Plan: .copilot-tracking/plans/2026-06-16/tone-of-voice-alignment-plan.instructions.md
* Details (Phase 1): .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Lines 12-44)
* Changes Log: .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md
* Research (rubric/acceptance standard): .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md
* Planning Log: .copilot-tracking/plans/logs/2026-06-16/tone-of-voice-alignment-log.md
* File under review: docs/ai-assisted-engineering/README.md (127 lines, uncommitted working-tree edits via `git diff HEAD`)

## Acceptance Standard (Voice Rubric)

From the research file Implementation Patterns table — first-person plural "we" / direct "you"; rationale before directive; framing sentence before bullet lists; max ~4 comma-separated items per bullet; mentoring / hedged tone; tone-only with no meaning, heading, link, or anchor change.

## Step 1: Plan Items vs Changes

| Plan item (Phase 1) | Changes Log claim | Verified evidence | Status |
|---|---|---|---|
| Step 1.1 Rewrite docs/ai-assisted-engineering/README.md to playbook voice | "Rewrote the central guide … rationale-first we/you framing and split every 6+ item comma stack" | `git diff HEAD` shows every section intro re-toned to we/you; all 11 section bodies edited | Complete |
| 1.1 — convert imperative intros to we/you + rationale | claimed | Every `##` section intro now opens with a rationale clause + we/you (see Step 2 evidence) | Complete |
| 1.1 — split every 6+ item comma stack | claimed (observability 11-item bullet → grouped sub-list) | Observability mega-bullet split into 4 grouped sub-bullets, each ≤4 items (lines 78-82) | Complete |
| 1.1 — keep headings + "Related Playbook Areas" links intact | claimed | 12 headings unchanged; Related Playbook Areas block (lines 118-127) absent from diff = untouched | Complete |
| Step 1.2 Validate (lint + link check, headings/links unchanged) | "get_errors clean; link checker zero broken" | `get_errors` returns "No errors found"; no heading/link/anchor line appears with +/- in diff | Complete |

## Step 2: File Evidence Verification

### Headings preserved (no +/- in diff; all 12 present)

* docs/ai-assisted-engineering/README.md:1 `# AI-Assisted Engineering`
* docs/ai-assisted-engineering/README.md:7 `## When to Use AI Assistance`
* docs/ai-assisted-engineering/README.md:25 `## Human Oversight`
* docs/ai-assisted-engineering/README.md:35 `## Data and Context Hygiene`
* docs/ai-assisted-engineering/README.md:46 `## Prompt and Repository Hygiene`
* docs/ai-assisted-engineering/README.md:56 `## Security`
* docs/ai-assisted-engineering/README.md:66 `## Testing and Evaluation`
* docs/ai-assisted-engineering/README.md:76 `## Observability`
* docs/ai-assisted-engineering/README.md:89 `## Authorship and Traceability`
* docs/ai-assisted-engineering/README.md:99 `## Accessibility and Inclusion`
* docs/ai-assisted-engineering/README.md:108 `## Governance`
* docs/ai-assisted-engineering/README.md:118 `## Related Playbook Areas`

### Links and anchor preserved

* docs/ai-assisted-engineering/README.md:5 — intro cross-link sentence (7 domain-guide links) is a context line in the diff = unchanged.
* docs/ai-assisted-engineering/README.md:63 — `#ai-systems-threat-modeling-considerations` anchor present and unchanged (context line).
* docs/ai-assisted-engineering/README.md:118-127 — "Related Playbook Areas" list (8 links) is entirely absent from `git diff HEAD`, confirming byte-identical preservation.

### Voice rubric — rationale-first we/you intros (sampled, all 11 sections converted)

* docs/ai-assisted-engineering/README.md:27 — "AI can produce confident-looking work that is subtly wrong, so we treat its output as draft material…" (was bare imperative "Treat AI output as draft material…").
* docs/ai-assisted-engineering/README.md:37 — "Every prompt is a place data can leak, so we give AI tools only the minimum context…" (was "AI tools should receive the minimum context…").
* docs/ai-assisted-engineering/README.md:58 — "A model has no stake in our security, so we treat its output as untrusted input…" (was "Treat model output as untrusted input.").
* docs/ai-assisted-engineering/README.md:78 — "AI-enabled systems can drift in ways traditional ones do not, so we capture enough telemetry…".
* docs/ai-assisted-engineering/README.md:110 — "No single policy fits every engagement, so we adapt this guidance…".

### Comma-stack rule (max ~4 per bullet) — observability mega-bullet split

* docs/ai-assisted-engineering/README.md:78-82 — former 11-item capture bullet replaced by framing line + 4 grouped sub-bullets ("Versions in play" 3, "What the system did" 3, "Cost and performance" 2, "Outcomes" 4). All runs ≤4.

### Comma-stack scan across all bullets (no 6+ runs remaining)

Every directive bullet was checked. The longest comma runs are split with em-dashes / "along with" / "plus" into segments of ≤4 items, e.g.:

* docs/ai-assisted-engineering/README.md:60 — "injection, authorization, and authentication — and for cryptography, dependency, logging, and error-handling issues" (3 + 4).
* docs/ai-assisted-engineering/README.md:42 — "access tokens, connection strings, and personal data — along with customer identifiers and confidential business details — from any prompts, screenshots, logs, or attachments" (3 + 2 + 4).
* docs/ai-assisted-engineering/README.md:71-72 — testing evals split into "prompts, retrieval, models, or agents — or on generated content, ranking, summarization, or recommendations" (4 + 4) and "quality, groundedness, safety, and bias, along with robustness, tool-call correctness, regression behavior, and fallback behavior" (4 + 4).
* docs/ai-assisted-engineering/README.md:114 — governance reviews "Responsible AI assessment, privacy review, and security review, plus design, accessibility, and legal or compliance review" (3 + 3).

No bullet retains a 6+ item comma stack.

## Step 3: Coverage and Findings

### Coverage

Phase 1 is fully covered. Both plan steps (1.1 rewrite, 1.2 validate) are implemented and evidenced. The single in-scope file received an end-to-end voice rewrite; structure, headings, links, and the threat-modeling anchor are intact; the one 6+ comma stack flagged in research (observability) is split; lint/error check is clean. No out-of-scope file was touched by this phase (the unrelated `.gitattributes` working-tree change is correctly logged as OOS-01 and untouched).

### Findings

#### Critical

* None.

#### Major

* None.

#### Minor

* M-1 — docs/ai-assisted-engineering/README.md:3 — Intro prose sentence "AI tools help us explore ideas, draft code, write tests, summarize context, and improve documentation." carries 5 comma-separated verb phrases. The "~4" rule targets bullets, not flowing prose, and this 5-item run pre-existed the rewrite (only "teams" → "us" changed), so it is within tolerance — noted for awareness only, no action required for tone-only scope.
* M-2 — Terminology drift between artifacts and file: the Details Step 1.1 success criterion references "'Related Playbook Areas' links" while the intro cross-link sentence (line 5) is the primary divergent link cluster. Both the intro links (line 5) and the actual "Related Playbook Areas" section (lines 118-127) are preserved, so meaning is intact; the note is purely about wording precision in the planning artifacts.

### Areas needing no further investigation

* Meaning preservation: confirmed — no recommendation removed; every directive in the original appears in the rewrite (verified line-by-line in the diff).
* Tier C exemplars: out of Phase 1 scope (covered by Phase 5).

## Clarifying Questions

* None. All Phase 1 requirements were resolvable from the provided artifacts and the working-tree diff.
