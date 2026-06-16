<!-- markdownlint-disable-file -->
# Task Research: Tone-of-Voice Alignment for AI Guidance (`review-ai-guidance` branch)

The `review-ai-guidance` branch adds a new AI-Assisted Engineering guide and inserts AI-related sections into ~30 existing playbook pages. The added prose is factually strong and well cross-linked, but much of it is written in an impersonal, policy/compliance register that does not match the playbook's established conversational, mentoring voice. This document is the remediation plan to bring the new content into the playbook's tone of voice.

## Task Implementation Requests

* Define the canonical "playbook voice" the repo already uses, as an explicit, checkable rubric.
* Identify every branch-added passage whose tone diverges from that voice, ranked by severity.
* Provide a phased, file-by-file plan to revise divergent passages without changing their technical meaning or links.
* Preserve content that already matches the voice and use it as the reference pattern.

## Scope and Success Criteria

* Scope (in): prose tone, voice, person, and rhythm of branch-added Markdown content under `docs/`.
* Scope (out): technical accuracy of the guidance, link correctness, file moves/restructure, `.pages` navigation, and the `.copilot-tracking/` research artifacts themselves. No changes to code or non-prose.
* Assumptions:
  * The comparison baseline is `main` (016770e); the branch is `review-ai-guidance`, two commits ahead.
  * The repo's canonical voice standard is the hve-core `writing-style.instructions.md` (applyTo `**/*.md`) plus the de-facto voice of existing `docs/**` pages on `main`.
  * Revisions must not change technical meaning, recommendations, or cross-links — tone only.
* Success Criteria:
  * A documented voice rubric exists with concrete do/don't examples drawn from this repo.
  * Every added AI passage is classified into Tier A (rewrite), Tier B (light touch), or Tier C (keep).
  * Each Tier A/B file has a specific revision instruction and a before/after sample.
  * The plan can be executed page-by-page and verified against the rubric.

## Outline

1. Canonical playbook voice rubric (target state).
2. The divergent "AI policy" voice (current state) with verbatim evidence.
3. File inventory classified into Tier A / B / C.
4. Phased remediation plan with per-file instructions and samples.
5. Verification checklist.

## Potential Next Research

* Confirm full contents of `docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md` (new, 89 lines) for Tier A rewrite scope.
  * Reasoning: only partially sampled; likely the densest enumeration page.
  * Reference: git diff main...HEAD -- docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md
* Confirm whether `mkdocs.yml`/`.pages` nav labels need tone alignment too.
  * Reasoning: navigation titles are user-facing prose.
  * Reference: docs/.pages, docs/start-here/.pages

## Research Executed

### File Analysis

* docs/ai-assisted-engineering/README.md (new, 123 lines)
  * Entire file in impersonal imperative register; no first-person plural. Example lead: "Treat AI output as draft material until a responsible person reviews, tests, and accepts it."
  * Pervasive long comma-separated enumerations, e.g. "injection, authorization, authentication, cryptography, dependency, logging, and error-handling issues".
* docs/developer-experience/copilots.md (+67 lines)
  * New sections "Team Operating Model for AI-Assisted Delivery" and "Validating AI-Assisted Work" use directive bullets; sit directly beside original warmer prose ("it can be beneficial…", "You can read more about…"). Visible tone seam in one file.
* docs/automated-testing/README.md (+10 lines)
  * AI bullets ("Add regression tests…", "Track evaluation failures as defects…") follow original "We consider code to be incomplete…", "We write unit tests…". Person shift seam.
* docs/observability/README.md (+12 lines)
  * "AI observability" is one long capture enumeration (model/provider/version, prompt template version, retrieval source IDs, tool calls, latency, token/cost, refusal rates, error rates, fallback paths, safety outcomes, escalation rates).
* docs/non-functional-requirements/privacy/data-handling.md (+11 lines)
  * Terse imperative "AI tool data handling" directly above conversational "5 W's of Data Handling" ("Who – gets access… with whom will we share…").
* docs/security/threat-modelling.md (+38 lines)
  * "AI Systems Threat Modeling Considerations": multiple back-to-back bare bullet lists (risk categories, assets, prompts) with little connective prose; closes with a single very long run-on "Common controls include…" sentence.
* docs/ml-and-ai-projects/responsible-ai.md (+46 lines)
  * Five subsections that are each pure question lists; consistent but checklist-heavy and impersonal relative to the page's existing "we start to complete…" voice.
* docs/CI-CD/README.md (+8 lines)
  * Added artifact paragraph and checklist items in dense noun-stacked style ("prompts, evaluation datasets, model configuration, grounding indexes, safety policies, and tool permission manifests").
* docs/documentation/README.md (+17 lines)
  * New "AI-assisted documentation" section plus added challenge bullets including the label "Unreviewed AI filler" — heavier, more pejorative register than surrounding challenge list.
* docs/start-here/for-engineers.md (new), docs/non-functional-requirements/README.md (new)
  * These match the playbook voice well ("A curated reading path…", "Use these pages to identify, capture, and validate…"). Reference exemplars, not problems.

### Code Search Results

* `^## .*AI` across docs/**
  * AI sections added to: copilots.md (3), engineering-fundamentals-checklist.md, agile-development/README.md, privacy/data-handling.md, privacy/README.md, UI-UX/README.md, developer-experience/README.md, plus the new guide.
* `ai-assisted-engineering/README.md` link references
  * ~20 pages now point to the shared guide (good structural consistency; tone is the only gap).

### External Research

* git diff main...HEAD --stat
  * 62 files changed, 2721 insertions(+), 30 deletions(-). Confirms scope is additive prose plus restructure/persona pages.

### Project Conventions

* Standards referenced: hve-core `writing-style.instructions.md` (voice/tone for all Markdown), `markdown.instructions.md` (formatting).
* Instructions followed: tone-only edits; preserve links and meaning; no new tracking docs beyond this research file.

## Key Discoveries

### Project Structure

The branch's structural work (persona `start-here/` pages, `non-functional-requirements/README.md`, `.pages` nav, link de-duplication) largely matches the playbook voice and is not the problem. The tone gap is concentrated in the **AI policy passages** added across domain pages and the new central guide.

### Implementation Patterns

**Target voice (the playbook's existing register), distilled into a rubric:**

| Dimension | Playbook voice (target) | AI-policy voice (to fix) |
|-----------|-------------------------|--------------------------|
| Person | First-person plural and direct "you": "We write our tests early"; "build your application with testing in mind" | Impersonal imperative, no agent: "Treat AI output as draft material" |
| Rationale | States the *why* before the *what* | Lists directives with little reasoning |
| Bullet shape | Bold lead-in + explanatory sentence: "**Parameterize everything.** Rather than hard-code any variables…" | Bare imperative fragment |
| Enumerations | 2–4 concrete items, or prose | 6–11 comma-stacked nouns in one bullet |
| Tone | Mentoring, pragmatic, hedged ("patterns, not prescriptions") | Compliance/policy, absolute |
| Rhythm | Mixed sentence lengths, connective tissue between lists | List-after-list with run-on closers |

**Reference exemplar already in the branch** (keep, and pattern others after it) —
docs/agile-development/README.md "AI tooling considerations": "Consider these principles as you tailor your process… These are patterns, not prescriptions — adapt them to fit your engagement and stakeholder needs."

### Complete Examples

Before / after illustrating the target transformation (meaning unchanged):

```text
BEFORE (docs/automated-testing/README.md):
- Add regression tests for generated code paths and edge cases the AI may have missed.
- Track evaluation failures as defects with reproducible prompts, context, model or version, and expected behavior.

AFTER (playbook voice):
- We add regression tests for any code an AI tool generates, covering the edge cases it is most likely to miss.
- When an AI evaluation fails, we track it like any other defect: capture the prompt, context, model version, and the behavior we expected so it can be reproduced.
```

```text
BEFORE (docs/non-functional-requirements/privacy/data-handling.md):
Treat prompts, context files, embeddings, transcripts, generated outputs, screenshots, and evaluation
datasets as project data.

AFTER (playbook voice):
Anything we feed to or get back from an AI tool — prompts, context files, embeddings, transcripts,
generated output, screenshots, and evaluation datasets — is project data, and we handle it with the
same care as the rest of the engagement's data.
```

### Configuration Examples

Not applicable — this is a prose/editorial task.

## Technical Scenarios

### Scenario: Voice-align the AI guidance to the playbook register

The team wants the new AI content to read as if it were written by the same authors as the rest of the playbook, without losing any guidance or links.

**Requirements:**

* Preserve every recommendation, warning, and cross-link.
* Convert impersonal imperatives to the playbook's "we"/"you" mentoring voice.
* Break up 6+ item comma stacks into prose or short, scannable sub-lists.
* Add a one-line rationale where a section is a bare directive list.
* Keep edits page-scoped and independently reviewable.

**Preferred Approach:**

Phase the work by tone severity, not by file order, so the highest-impact pages (the central guide and the seams where new text sits beside original prose) are fixed first. Use the agile-development section as the gold reference. Make edits page-by-page with `multi_replace_string_in_file`, verifying each against the rubric table above. This keeps each change small, reviewable, and reversible, and avoids touching technical meaning.

```text
docs/
  ai-assisted-engineering/README.md        (Tier A — full voice rewrite)
  developer-experience/copilots.md          (Tier A — new sections)
  security/threat-modelling.md              (Tier A — AI section)
  ml-and-ai-projects/
    responsible-ai.md                       (Tier A — prompt lists)
    generative-ai-and-agentic-systems.md    (Tier A — confirm + rewrite)
  observability/README.md                   (Tier A — capture enumeration)
  non-functional-requirements/privacy/data-handling.md (Tier A)
  automated-testing/README.md               (Tier A)
  CI-CD/README.md                           (Tier A — artifact para + checklist)
  documentation/README.md                   (Tier A — section + "AI filler")
  code-reviews/** , source-control/** , UI-UX/README.md ,
  design/README.md , engineering-feedback/README.md , privacy/README.md ,
  agile-development/branching-and-cicd.md , */test-planning.md (Tier B — light touch)
  agile-development/README.md , developer-experience/README.md ,
  start-here/** , non-functional-requirements/README.md (Tier C — keep as model)
```

**Implementation Details — phased plan:**

**Phase 0 — Establish the rubric (no doc edits).**
Adopt the rubric table above as the acceptance standard. Confirm it against hve-core `writing-style.instructions.md`. Pick docs/agile-development/README.md "AI tooling considerations" as the canonical example.

**Phase 1 — Central guide.** Rewrite docs/ai-assisted-engineering/README.md end to end:
* Convert section intros from imperative to "we"/"you" with a one-sentence rationale each.
* Split every 6+ item comma stack into either a short sub-list or a sentence naming the 3–4 most important items plus "and related concerns".
* Keep all section headings and the "Related Playbook Areas" links intact.

**Phase 2 — Tone seams (new text beside original prose). Highest reader impact.**

These pages are first priority because a reader moving from the page's original prose into the new AI section feels an abrupt change in person and rhythm within a single screen. Goal: make the new section sound like the same author wrote it, without losing any directive.

* docs/developer-experience/copilots.md (Tier A; +67 lines)
  * Problem: the new "Team Operating Model for AI-Assisted Delivery" and "Validating AI-Assisted Work" sections are stacks of bare imperatives ("Use the lightest tool that fits the task", "Give the assistant enough context…", "Set tool and execution boundaries…"). They sit directly below the original "## Considerations" prose, which uses warm direct address ("If you make use of AI tools, it is important to understand…", "You can read more about how GitHub Copilot handles your data…").
  * Instruction: keep the section structure and all links, but (a) add a one-sentence rationale under each `###`/bold lead that connects the list to *why* the team does it; (b) convert at least the lead sentence of each bullet group to "we"/"you"; (c) keep the bullets themselves scannable — bullets may stay imperative once the framing sentence sets the voice, mirroring the existing "Build for Testing" pattern elsewhere in the playbook.
  * Before / after sample:
    ```text
    BEFORE:
    Give the assistant enough context to make a reviewable change:
    - Problem statement and user impact
    - Acceptance criteria and expected behavior

    AFTER:
    We give the assistant the same context we would give a new teammate, so the
    change it proposes is reviewable rather than a guess:
    - Problem statement and user impact
    - Acceptance criteria and expected behavior
    ```

* docs/automated-testing/README.md (Tier A; +10 lines)
  * Problem: the AI bullets ("Add regression tests…", "Review generated tests…", "Track evaluation failures as defects…") follow the page's strongly first-person opening ("We consider code to be incomplete if it is not accompanied by tests", "We write our tests early").
  * Instruction: convert the bullets to the page's "we" voice and keep them short. Preserve the `#testing-and-evaluation` deep link and the "treat output as draft" framing sentence (which is already well-toned).
  * Before / after sample:
    ```text
    BEFORE:
    - Add regression tests for generated code paths and edge cases the AI may have missed.
    AFTER:
    - We add regression tests for any AI-generated code, covering the edge cases the tool is most likely to miss.
    ```

* docs/non-functional-requirements/privacy/data-handling.md (Tier A; +11 lines)
  * Problem: "## AI tool data handling" opens with a bare imperative ("Treat prompts, context files, embeddings, transcripts, generated outputs, screenshots, and evaluation datasets as project data") directly above the conversational "## 5 W's of Data Handling" ("Who – gets access… with whom will we share…").
  * Instruction: lead with a single framing sentence in the page's voice that names the idea, then break the 7-item comma stack into a short illustrative list or trim to the 3–4 highest-risk items plus "and other AI inputs and outputs". Keep the four directive bullets but soften the openers ("Do not send…", "Use de-identified…") to match.
  * Before / after sample:
    ```text
    BEFORE:
    Treat prompts, context files, embeddings, transcripts, generated outputs, screenshots,
    and evaluation datasets as project data.
    AFTER:
    Anything we feed to or get back from an AI tool is project data, and we handle it with
    the same care as the rest of the engagement's data — prompts, context files, embeddings,
    transcripts, generated output, screenshots, and evaluation sets included.
    ```

* docs/documentation/README.md (Tier A; +17 lines)
  * Problem: the new "## AI-assisted documentation" section is acceptable, but the added challenge bullets introduce the pejorative label "Unreviewed AI filler", which is sharper and more judgmental than the neighbouring challenge labels ("Inaccurate", "Obsolete", "Afterthought").
  * Instruction: keep the section, but rename "Unreviewed AI filler" to a label consistent with the existing list voice (for example, "Unreviewed generated content") and reframe its two sub-bullets as observations rather than accusations. Lightly convert the section intro to match the page's "we typically encounter…" register.

**Phase 3 — Dense enumeration pages. Reduce list-after-list and noun stacks.**

These pages are technically strong but read as reference checklists. The fix is not to delete content — it is to add connective tissue and break the longest comma stacks so the prose breathes like the rest of the playbook.

* docs/security/threat-modelling.md (Tier A; +38 lines)
  * Problem: "## AI Systems Threat Modeling Considerations" runs three bare lists back-to-back (risk categories, assets/trust boundaries, identification prompts) with almost no connective prose, then closes with one very long run-on: "Common controls include prompt and tool schema review, strict input and output validation, least-privilege tools, … and retesting after red-team findings are fixed."
  * Instruction: add a one-line lead-in before each of the three lists explaining what the list is for; split the closing "Common controls include…" sentence into a short bulleted list or two sentences grouped by theme (input/output handling, least privilege, operational safety). Keep every risk item and the `#ai-systems-threat-modeling-considerations` anchor intact.

* docs/ml-and-ai-projects/responsible-ai.md (Tier A; +46 lines)
  * Problem: five subsections ("Grounding and generated content", "Prompt, retrieval, and tool abuse", "Agent actions and human oversight", "Memory, logs, and retention", "Production monitoring and review cadence") are each pure question lists, more impersonal than the page's existing "The process begins as soon as we start a prospective project… We start to complete…" voice.
  * Instruction: keep the question format (it is genuinely useful), but add a single "we"-voiced framing sentence under each subsection heading explaining when the team asks these questions. The existing intro paragraph already does this well and is the model. Preserve all four cross-links.

* docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md (Tier A; new, 89 lines)
  * Problem: largely well-written and even has good rationale openers ("Prefer the simplest design that can satisfy the user need…", "A generative AI or agentic feature is not ready because it responds convincingly in a demo"). The weak spots are the three long `- [ ]` checklists (Workload Readiness, RAG and Grounding, Agentic Systems) and the "Review the System Across Disciplines" list where every bullet is "Use [X] to …".
  * Instruction: lighter than the others — keep the checklists (their format suits a readiness gate) but ensure each checklist has its existing one-line framing sentence (most already do). In "Review the System Across Disciplines", vary the repetitive "Use [X] to…" openers so the list does not read mechanically. This is the lowest-risk Tier A page.

* docs/observability/README.md (Tier A; +12 lines)
  * Problem: the "## AI observability" section's first bullet is an 11-item capture mega-list ("model, provider, and version, prompt template version, retrieval source IDs, tool calls, latency, token or cost signals, refusal rates, error rates, fallback paths, safety outcomes, and escalation rates").
  * Instruction: split that single bullet into 3 short grouped bullets — model/version context, operational signals (latency, tokens, cost, errors, fallback), and safety signals (refusal rates, safety outcomes, escalation). Keep the surrounding bullets and the shared-guide link.

* docs/CI-CD/README.md (Tier A; +8 lines)
  * Problem: the added artifact paragraph stacks nouns ("Treat prompts, evaluation datasets, model configuration, grounding indexes, safety policies, and tool permission manifests as deployable artifacts…") and two new checklist items are dense.
  * Instruction: keep the paragraph but lead with the principle in a sentence, then list the artifacts as a short sub-list or trimmed set. Tighten the two added checklist items so they match the brevity of the existing checkbox lines. Preserve both deep links.

**Phase 4 — Light touch (Tier B). Single-sentence or near-passing additions.**

These pages received small, mostly well-toned additions. They need only targeted fixes to impersonal openers or one overlong stack; several may already pass the rubric and require no change. Review each, edit only where it diverges, and do not over-rewrite.

* docs/code-reviews/README.md — new "## Reviewing AI-assisted changes" opens "Review AI-generated code as untrusted code…". Consider a light "we review…" opener to match the page's collaborative framing; bullets are short and can stay.
* docs/code-reviews/process-guidance/reviewer-guidance.md (+25 lines) — "## AI-Assisted and Agent-Authored Changes" is a large checklist block. Add one framing sentence per sub-list ("During review, check that:" / "also review evaluation evidence:") and confirm it matches the surrounding reviewer-guidance voice; otherwise leave the checks intact.
* docs/source-control/README.md and docs/source-control/git-guidance/README.md — additions are mostly prose and already reasonable; check the two bullet openers ("Require AI agent branches…", "Do not commit prompts…") read consistently with the page; minimal change expected.
* docs/UI-UX/README.md — "## AI-assisted UI and UX work" intro is well-toned; the numbered list mixes long items. Light trim only; verify the `1.`-repeated ordered list renders as intended.
* docs/engineering-feedback/README.md — "## AI Tooling Feedback" list and the closing context sentence are dense; trim the longest comma stack ("Privacy, data handling, policy, retention, or customer-data friction…") if it reads heavy.
* docs/non-functional-requirements/privacy/README.md — "## AI Privacy Review Prompts" is a question list like responsible-ai; add one framing sentence (the intro paragraph already mostly does this) and leave the questions.
* docs/automated-testing/test-planning.md — "### AI Evaluation Planning" is mostly good prose with one long pattern list; trim only if an item runs too long.
* docs/agile-development/branching-and-cicd.md — changes here are largely de-duplication/link redirection (removing restated policy), which is structurally good; verify the rewritten sentences read in the page's voice, no tone rewrite needed.

After Phase 4, re-scan with the rubric to confirm no Tier B page still has an unframed bare-imperative section or a 6+ item comma stack.

**Phase 5 — Verify.** Re-read each edited page against the rubric; confirm links and meaning unchanged with `git diff`; ensure no Tier C page was altered.

#### Considered Alternatives

* **Global find/replace of imperative openers** — rejected: tone is contextual; mechanical substitution would produce awkward or incorrect sentences and risks changing meaning.
* **Rewrite only the central guide, leave domain pages** — rejected: the most jarring experience is the in-page seams (Phase 2), so domain pages must be included.
* **Defer all edits and only document findings** — rejected: the user explicitly asked for a plan to fix the tone, so the plan must be executable file-by-file.
* **Soften by adding "we recommend" prefixes everywhere** — rejected: produces repetitive padding; the rubric calls for varied, rationale-first prose, not a uniform prefix.

## Verification Checklist (per edited page)

* [ ] Uses first-person plural / direct "you" consistent with the page's existing prose.
* [ ] No bullet stacks more than ~4 comma-separated items without being broken up.
* [ ] Each directive list has at least one sentence of rationale or framing.
* [ ] All original links and section headings preserved.
* [ ] Technical meaning and recommendations unchanged (confirm via `git diff`).
* [ ] Tier C reference pages untouched.
