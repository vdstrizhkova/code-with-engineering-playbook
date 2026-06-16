<!-- markdownlint-disable-file -->
# RPI Validation — Tone-of-Voice Alignment, Phase 4 (Light Touch — Tier B)

**Plan**: .copilot-tracking/plans/2026-06-16/tone-of-voice-alignment-plan.instructions.md
**Details**: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Phase 4 = lines 110-136)
**Changes Log**: .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md
**Research / Rubric**: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md
**Validated**: 2026-06-16
**Status**: Partial (Pass-with-minor) — edits correct; 2 "already-passes" claims overstated.

## Scope

Phase 4 covers Tier B "light touch" pages. The phase intentionally edited only the two divergent pages and reviewed seven others as already-compliant. This validation:

1. Confirms the 2 edited files implement the changes as described, meet the rubric, and preserve links.
2. Confirms the 7 "unchanged" files have no working-tree diff and spot-checks each against the rubric to justify the "left unchanged" decision.

## Rubric (from research)

* Person: first-person plural "we" / direct "you".
* Rationale-first: state the *why* before the *what*; framing sentence before directive lists.
* Enumerations: 2–4 items (max ~4); Phase 4 hard bar = **no 6+ item comma stack**.
* No unframed bare-imperative section.
* Tone only — no recommendation, heading, link, or anchor may change.

## Step 1 — Plan Items vs Changes (edited files)

### docs/code-reviews/README.md — PASS

* Plan/research: reframe bare-imperative opener of "Reviewing AI-assisted changes" to a light "we review…".
* Verified diff ([docs/code-reviews/README.md](docs/code-reviews/README.md#L14-L15)): `Review AI-generated code as untrusted code:` → `We review AI-generated code as untrusted code, confirming the change satisfies the work item, avoids unrelated generated code, and meets the same expectations as any other pull request.`
* Rubric: "we" voice ✓; rationale-first ✓; 3-item run (≤4) ✓.
* Links/anchors: bullets unchanged; `[AI-Assisted Engineering](../ai-assisted-engineering/README.md)` preserved at [docs/code-reviews/README.md](docs/code-reviews/README.md#L21). No heading/anchor change. ✓

### docs/engineering-feedback/README.md — PASS

* Plan/research: trim the longest comma stack; the closing sentence was an 8-item stack.
* Verified diff ([docs/engineering-feedback/README.md](docs/engineering-feedback/README.md#L27)): `Include reproducible prompts or scenarios, sanitized context, expected behavior, actual behavior, impact, workaround, tool name, and relevant configuration when submitting…` → `When you submit AI tooling feedback, include a reproducible prompt or scenario with sanitized context, describe the expected and actual behavior, and note the impact, any workaround, and the tool name and configuration.`
* Rubric: "you" voice ✓; 8 comma items regrouped into 3 clauses ✓.
* Meaning: all eight original elements retained (prompt/scenario, sanitized context, expected behavior, actual behavior, impact, workaround, tool name, configuration). ✓
* Links: `[AI-Assisted Engineering](../ai-assisted-engineering/README.md)` preserved at [docs/engineering-feedback/README.md](docs/engineering-feedback/README.md#L27). ✓

## Step 2 — "Unchanged" files: no-diff + rubric spot-check

`git diff HEAD --` returned **empty** for all seven (no working-tree changes). Rubric spot-check results:

| File | Diff | Rubric | Finding |
|------|------|--------|---------|
| code-reviews/process-guidance/reviewer-guidance.md | empty | Framed, but 6-item stacks + inconsistent opener | Minor (F-002) |
| source-control/README.md | empty | Framed prose + short imperative bullets | None |
| source-control/git-guidance/README.md | empty | Framed declarative + ≤3-item bullets | None |
| UI-UX/README.md | empty | Framed; two 5-item stacks (>~4, <6) | Minor (F-003) |
| non-functional-requirements/privacy/README.md | empty | 7-item stack in framing paragraph | Major (F-001) |
| automated-testing/test-planning.md | empty | Framed; two 6-item enumerations | Minor (F-004) |
| agile-development/branching-and-cicd.md | empty | Page voice; no AI-policy stack | None |

## Findings

### F-001 (Major) — privacy/README.md framing paragraph retains a 7-item comma stack

* Evidence: [docs/non-functional-requirements/privacy/README.md](docs/non-functional-requirements/privacy/README.md#L10): "...can move private data through **prompts, retrieved content, model providers, tool calls, telemetry, memory, and generated summaries**." = 7 items.
* Conflict: violates the Phase 4 explicit success criterion "No Tier B page retains … a 6+ item comma stack" and the ~4-item rubric. The changes log asserts this page was left unchanged because the "intro paragraph already frames the question list" — the framing sentence itself is the over-long stack, so the "already passes the rubric" claim is overstated.
* Impact: readability/style only; meaning and links intact, no functional defect. Items are plain prose nouns and could be grouped without meaning loss (e.g. "…through user/model inputs (prompts, retrieved content), the providers and tools that process them, and the data they leave behind (telemetry, memory, generated summaries)").
* Note: the question bullets below are intentionally long question lists (research said keep). Only the framing paragraph is flagged.

### F-002 (Minor) — reviewer-guidance.md: bare-imperative opener inconsistency + 6-item stacks

* Evidence:
  * [docs/code-reviews/process-guidance/reviewer-guidance.md](docs/code-reviews/process-guidance/reviewer-guidance.md#L62): "Review AI-assisted changes as untrusted contribution." — a bare-imperative opener parallel to the code-reviews/README.md opener that *was* reframed to "We review…". Same engagement, two parallel sentences now read in different voices.
  * [docs/code-reviews/process-guidance/reviewer-guidance.md](docs/code-reviews/process-guidance/reviewer-guidance.md#L64): "…or the PR changes AI prompts, model configuration, retrieval behavior, tool permissions, eval datasets, or generated documentation." = 6 items.
  * [docs/code-reviews/process-guidance/reviewer-guidance.md](docs/code-reviews/process-guidance/reviewer-guidance.md#L71): "New dependencies, generated lockfile updates, external actions, model providers, MCP servers, or tool integrations…" = 6 items.
* Context: the checklist sub-blocks *are* framed ("During review, check that:" / "…also review evaluation evidence:" at [L76](docs/code-reviews/process-guidance/reviewer-guidance.md#L76)), so the "unframed bare-imperative" half of the criterion is satisfied. The page is a reviewer checklist whose existing voice is imperative, so leaving the bullets is defensible. The changes-log claim that it "already passes the rubric" is mostly accurate but glosses over the two 6-item stacks and the opener-voice inconsistency.
* Severity rationale: style gap, not a meaning/link defect; downgraded to Minor.

### F-003 (Minor) — UI-UX/README.md: two 5-item comma stacks slightly over the soft target

* Evidence:
  * [docs/UI-UX/README.md](docs/UI-UX/README.md#L17): subjects "personas, content, alt text, captions, and flows" (5) and criteria "accessibility, inclusion, bias, plain language, and cognitive load" (5).
  * [docs/UI-UX/README.md](docs/UI-UX/README.md#L18): "disclosure, user control, fallback, appeal, and human escalation" (5).
* Assessment: above the ~4 soft target but **under** the 6+ hard bar, so the Phase 4 criterion is met. Intro at [L15](docs/UI-UX/README.md#L15) frames the list; ordered list renders fine. The changes-log claim ("no 6+ item comma stack — max 5") is accurate. No action required; logged for completeness.

### F-004 (Minor) — test-planning.md: two 6-item enumerations remain

* Evidence:
  * [docs/automated-testing/test-planning.md](docs/automated-testing/test-planning.md#L52): "retrieval relevance, groundedness, faithfulness to sources, citation quality, security trimming, and source freshness" = 6.
  * [docs/automated-testing/test-planning.md](docs/automated-testing/test-planning.md#L58): "minimum quality scores, no critical safety failures, passing tool-call contract tests, acceptable latency and cost, reviewed red-team findings, and documented follow-up for known limitations" = 6.
* Assessment: each item is a distinct term-of-art (RAG check dimension / release-gate criterion). Section is framed at [L45](docs/automated-testing/test-planning.md#L45). The changes log justifies leaving them because "trimming would change meaning" — correct under the tone-only/no-meaning-change constraint. Flagged only as an optional reformat-to-sub-list readability opportunity; technically these exceed the 6+ bar.

## Coverage Assessment

* Edited files (2/2): fully implemented as described, rubric-compliant, links/anchors/headings preserved. **Pass.**
* Unchanged files (7/7): all confirmed zero-diff. Five (source-control/README.md, source-control/git-guidance/README.md, agile-development/branching-and-cicd.md, plus UI-UX and test-planning under the 6+ hard bar) genuinely justify "left unchanged". Two ("already passes" claims) are overstated: privacy/README.md (Major, 7-item stack) and reviewer-guidance.md (Minor, 6-item stacks + opener inconsistency).
* No recommendation, heading, link, or anchor changed in any Phase 4 file (verified via diffs and link grep). Tone-only constraint upheld.

## Finding Counts

* Critical: 0
* Major: 1 (F-001)
* Minor: 3 (F-002, F-003, F-004)

## Clarifying Questions

* Should the Phase 4 "no 6+ item comma stack" criterion be treated as a hard gate (then privacy/README.md L10 and reviewer-guidance.md L64/L71 require a follow-up edit), or as guidance subordinate to the tone-only/no-meaning-change constraint (then test-planning.md's term-of-art stacks are correctly left as-is)? Resolving this decides whether F-001/F-002 are actionable now or accepted as-is.

## Recommended Next Validations

* [ ] Phase 1 — docs/ai-assisted-engineering/README.md central-guide rewrite.
* [ ] Phase 2 — tone-seam files (copilots.md, automated-testing/README.md, privacy/data-handling.md, documentation/README.md).
* [ ] Phase 3 — dense-enumeration pages (threat-modelling.md, responsible-ai.md, generative-ai-and-agentic-systems.md, observability/README.md, CI-CD/README.md); verify DD-02/DD-03 deviations.
* [ ] Phase 5 — full `git diff main...HEAD` meaning/link audit and Tier C untouched confirmation; review the out-of-scope uncommitted `.gitattributes` change flagged in the changes log.
