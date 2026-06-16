<!-- markdownlint-disable-file -->
# Implementation Details: Repository Restructure to Reduce Guide Duplication

## Context Reference

Sources: .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md (selected Scenario A); .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (duplication evidence with line numbers); .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md (persona mapping); .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md (section catalog).

Finding-number scheme: This plan uses the MAIN research document numbering (.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md, "Duplication Findings"): Finding 1 = AI baseline, Finding 2 = CI/CD fundamentals, Finding 3 = testing taxonomy, Findings 4/5 = branching + merge-gate, Finding 10 = OpenTelemetry, Finding 11 = AI threat list. The subagent `duplication-research.md` numbers AI baseline/CI-CD in the reverse order; ignore its numbering and use this scheme throughout.

## Implementation Phase 1: Persona Entry Layer

<!-- parallelizable: true -->

### Step 1.1: Create start-here landing page

Create a concise landing page that explains how to use the playbook and routes each persona to its reading path. Link to the existing canonical entry artifacts (checklist, first week). No guidance is duplicated — only orientation and links.

Files:
* docs/start-here/README.md - New "How to use this playbook" page with three persona links plus links to engineering-fundamentals-checklist.md and the-first-week-of-an-ise-project.md.

Discrepancy references:
* Addresses research Navigation Pain Points 1-2 (no persona entry points, no per-persona start-here).

Success criteria:
* Page lists the three personas with one-line descriptions and links to for-engineers.md, for-leads.md, for-data-scientists.md.
* Page links to engineering-fundamentals-checklist.md and the-first-week-of-an-ise-project.md.
* Contains no copied guidance text (links only).

Context references:
* .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md (Scenario A Part 1) - persona page intent.

Dependencies:
* None.

### Step 1.2: Create for-engineers reading path

Curated ordered link list into the engineer-primary sections; no content copied.

Files:
* docs/start-here/for-engineers.md - Ordered path: source-control → code-reviews → automated-testing → CI-CD → security → design → observability → developer-experience, plus ai-assisted-engineering as shared baseline.

Discrepancy references:
* Addresses Pain Point 3 (scattered related guides) for the engineer persona.

Success criteria:
* Links resolve to existing section README index pages.
* Order matches the engineer path in the research persona mapping.
* Links only; no duplicated guidance.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md (Persona summaries: Software Engineer).

Dependencies:
* Step 1.1 (consistent page shape), can proceed in parallel.

### Step 1.3: Create for-leads reading path

Curated ordered link list for the PM / Engineering Lead persona.

Files:
* docs/start-here/for-leads.md - Ordered path: agile-development → the-first-week-of-an-ise-project → engineering-fundamentals-checklist → engineering-feedback → documentation, plus process/governance facets of code-reviews, security, design, and ml-and-ai-projects/tpm-considerations-for-ml-projects.md.

Discrepancy references:
* Addresses Pain Point 3 (PM content split across 4+ top-level peers).

Success criteria:
* Links resolve to existing pages including the embedded TPM guide.
* Order matches the PM/Lead path in the research persona mapping.
* Links only; no duplicated guidance.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md (Persona summaries: Project Manager / Eng Lead).

Dependencies:
* Step 1.1, can proceed in parallel.

### Step 1.4: Create for-data-scientists reading path

Curated ordered link list for the Data Scientist / ML Engineer persona, layering ML content on shared fundamentals.

Files:
* docs/start-here/for-data-scientists.md - Ordered path: ml-and-ai-projects (envisioning → data-exploration → model-experimentation → responsible-ai → testing-data-science-and-mlops-code → generative-ai-and-agentic-systems) → ai-assisted-engineering, plus shared fundamentals (source-control, automated-testing, CI-CD/MLOps, security, observability/ml-observability.md).

Discrepancy references:
* Addresses Pain Point 3 (AI/ML guidance split across ai-assisted-engineering, ml-and-ai-projects, and AI subsections).

Success criteria:
* Links resolve to existing ML and shared-fundamental pages.
* Order matches the Data Scientist path in the research persona mapping.
* Links only; no duplicated guidance.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md (Persona summaries: Data Scientist / ML Engineer).

Dependencies:
* Step 1.1, can proceed in parallel.

### Step 1.5: Create start-here .pages ordering file

Order the persona pages within the Start Here section so the landing README is first.

Files:
* docs/start-here/.pages - awesome-pages ordering: README, For Engineers, For Project Managers, For Data Scientists.

Success criteria:
* Section renders with the landing page first, then the three persona pages in a stable order.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md (awesome-pages `.pages` mechanics).

Dependencies:
* Steps 1.1-1.4 (files must exist to be ordered).

## Implementation Phase 2: Navigation and Landing Updates

<!-- parallelizable: false -->

### Step 2.1: Update docs/.pages

Add the Start Here group at the top and replace the alphabetical `...` auto-fill with an explicit topic order matching the Engineering Fundamentals Checklist taxonomy. Current file (docs/.pages) has the nav block with `- ...` between CI/CD and UI/UX.

Files:
* docs/.pages - Insert `Start Here: start-here` after README and before the checklist entry; replace `- ...` with explicit, checklist-ordered section entries (Source Control, Code Reviews, Automated Testing, CI/CD, AI-Assisted Engineering, Security, Observability, Agile Development, Design, Developer Experience, Documentation, Engineering Feedback, Non-Functional Requirements, ML & AI Projects, UI/UX); keep `resources` out of the explicit list (Step 4.3).

Discrepancy references:
* Addresses Pain Points 1 (persona entry points) and 7 (nav not aligned to checklist).
* DD-01: design decision (not a deviation) — Start Here is placed above the checklist landing, matching the research illustrative ordering.

Success criteria:
* Start Here appears at the top of the nav.
* All existing sections still appear (none dropped) except empty `resources`.
* `mkdocs build --strict` produces the expected nav with no missing-page warnings.

Context references:
* docs/.pages (current nav block lines 1-9).
* .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md (illustrative `.pages` YAML).

Dependencies:
* Phase 1 complete (start-here/ exists).

### Step 2.2: Add Start Here pointer to docs/README.md

Add a short pointer near the top of the landing page directing readers to the persona pages, without duplicating their content.

Files:
* docs/README.md - Add a brief "New here? Start with the Start Here guide for your role" line linking to start-here/README.md.

Success criteria:
* Link resolves to docs/start-here/README.md.
* No persona reading-path content is copied into README.md.

Context references:
* docs/README.md (current landing page).

Dependencies:
* Step 1.1 (start-here/README.md exists).

## Implementation Phase 3: Canonical Hub-and-Spoke Deduplication

<!-- parallelizable: false -->

### Step 3.1: Deduplicate AI-assisted baseline (Finding 1)

Keep docs/ai-assisted-engineering/README.md as the canonical hub. In each spoke, replace the restated principles/threat list with a one-to-two sentence summary plus a deep link to the relevant hub anchor. Replicate the proven thin-stub pattern from docs/documentation/guidance/pull-requests.md.

Files:
* docs/developer-experience/copilots.md - Lines ~104-160: replace restated "treat output as untrusted / named human owner / attribution" blocks with summary + link to ai-assisted-engineering/README.md anchors.
* docs/automated-testing/README.md - Lines ~18-30: keep the testing-specific angle, link the shared baseline.
* docs/security/README.md - Lines ~13-25: keep security-specific framing, link the shared baseline and threat list.
* docs/source-control/README.md - Lines ~13-20: keep traceability point, link the shared baseline.
* docs/code-reviews/README.md - Lines ~13-25: keep review-specific framing, link the shared baseline.

Discrepancy references:
* Addresses DR/Finding 1 (most pervasive overlap).
* DD-06: the 8-item AI threat list has a single canonical home in docs/security/threat-modelling.md (see Step 3.6); the AI hub references it rather than owning the enumerated list.

Success criteria:
* The principles text (untrusted draft, named human owner, no secrets in prompts) lives canonically in ai-assisted-engineering/README.md; spokes link to it.
* The verbatim 8-item AI threat list exists in only one canonical location (docs/security/threat-modelling.md), referenced elsewhere (including the AI hub) by link.
* Each spoke retains its domain-specific sentence(s) and links to the hub.
* No new broken links.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (AI-assisted baseline evidence; listed file/line references).

Dependencies:
* None (canonical hub already exists).

### Step 3.2: Deduplicate CI/CD fundamentals (Finding 2)

Keep docs/CI-CD/README.md lines 26-32 as canonical. In docs/agile-development/branching-and-cicd.md lines 60-66, remove the near-verbatim five bullets and defer to the existing cross-reference (line 59).

Files:
* docs/agile-development/branching-and-cicd.md - Replace lines 60-66 duplicate bullets with a one-line "see CI/CD fundamentals" link (the cross-reference at line 59 already exists).

Discrepancy references:
* Addresses Finding 2 (HIGH, near-verbatim DUP).

Success criteria:
* The five CI/CD fundamentals bullets appear only in CI-CD/README.md.
* branching-and-cicd.md keeps its branching-specific content and links out for the shared fundamentals.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (CI/CD fundamentals evidence).

Dependencies:
* None.

### Step 3.3: Deduplicate testing taxonomy (Finding 3)

Keep docs/automated-testing/README.md lines 8-14 as canonical. In the spokes, retain a one-line summary that links to the canonical taxonomy rather than re-explaining unit/integration/e2e/performance.

Files:
* docs/CI-CD/continuous-integration.md - Lines ~190-246: trim the in-depth E2E re-explanation to a summary + link to automated-testing/e2e-testing/.
* docs/agile-development/team-agreements/definition-of-done.md - Keep checklist items, link taxonomy.
* docs/non-functional-requirements/maintainability.md - Keep the NFR angle, link taxonomy.

Discrepancy references:
* Addresses Finding 3 (MEDIUM-HIGH, PARTIAL).

Success criteria:
* Detailed unit/integration/e2e/performance explanation lives only in automated-testing; spokes summarize and link.
* Checklists remain valid (still summarize requirements).

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 3 evidence).

Dependencies:
* None.

### Step 3.4: Deduplicate branching/merge-gate (Findings 4, 5)

Designate docs/source-control/ (git-guidance/README.md + README.md) as the canonical branching/merge workflow owner and docs/code-reviews/pull-requests.md as the canonical PR-policy owner. Other pages summarize and link.

Files:
* docs/agile-development/branching-and-cicd.md - Lines ~7-22, 36-41: keep the short policy intent; link source-control for workflow and code-reviews/pull-requests.md for the merge-gate checklist.
* docs/CI-CD/continuous-integration.md - Lines ~222-235: keep CI-specific branch-policy enforcement, link the canonical workflow.

Discrepancy references:
* Addresses Findings 4 and 5 (MEDIUM, PARTIAL).

Success criteria:
* Branch-protection / required-reviewer / required-CI gate described in full in one canonical place; other pages link.
* github_conf/branch_protection_rules.json remains the machine config (unchanged).

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Findings 4, 5 evidence).

Dependencies:
* None.

### Step 3.5: Deduplicate OpenTelemetry blurb (Finding 10)

Keep docs/observability/tools/OpenTelemetry.md as canonical. Replace the verbatim recommendation sentence in the other three files with a link.

Files:
* docs/observability/correlation-id.md - Line ~30: replace verbatim blurb with link to tools/OpenTelemetry.md.
* docs/observability/pillars/tracing.md - Line ~22: replace verbatim blurb with link.
* docs/observability/microservices.md - Line ~55: replace verbatim blurb with link.

Discrepancy references:
* Addresses Finding 10 (LOW, localized DUP).

Success criteria:
* The OpenTelemetry recommendation sentence appears verbatim in only the canonical tool page.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 10 evidence).

Dependencies:
* None.

### Step 3.6: Deduplicate AI threat-modeling list (Findings 1, 11)

Designate docs/security/threat-modelling.md as the single canonical home for the enumerated AI threat list (DD-06). Replace duplicated lists in security/README.md and ai-assisted-engineering/README.md with a link to the canonical anchor.

Files:
* docs/security/README.md - Line ~15: link to threat-modelling.md AI section instead of restating.
* docs/ai-assisted-engineering/README.md - Line ~67: keep one reference; link to security/threat-modelling.md for the enumerated list.

Discrepancy references:
* Addresses Finding 11 (and the threat-list portion of Finding 1).
* DD-06: canonical owner of the enumerated AI threat list = docs/security/threat-modelling.md (coordinated with Step 3.1).

Success criteria:
* The enumerated AI threat list exists in one canonical location, referenced elsewhere by link.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 11 evidence).

Dependencies:
* Step 3.1 (decide single canonical home for the threat list).

## Implementation Phase 4: Structural Cleanups

<!-- parallelizable: true -->

### Step 4.1: Add NFR section README

Create a short section index for non-functional-requirements so it has a landing page like other sections (it currently has none, only privacy/README.md).

Files:
* docs/non-functional-requirements/README.md - New index listing the quality-attribute pages; brief intro; link to design/design-patterns/non-functional-requirements-capture-guide.md as the capture guide.

Discrepancy references:
* Addresses Pain Point 7 (NFR has no section README) and Finding 4-catalog overlap note (NFR-capture guide lives in design/).

Success criteria:
* NFR section renders an index page; `navigation.indexes` picks it up.
* Links to the existing attribute pages resolve.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md (NFR section: no root README).

Dependencies:
* None.

### Step 4.2: Normalize design/readme.md casing

Rename docs/design/readme.md to docs/design/README.md for consistency with all other sections and `navigation.indexes`.

Files:
* docs/design/readme.md → docs/design/README.md - Rename via `git mv` to preserve history; update any internal references that point to `readme.md` explicitly.

Discrepancy references:
* Addresses Pain Point 4 (inconsistent casing).
* DD-02: this rename can change the file's published URL fragment casing on case-sensitive hosts; verify the section URL is unchanged (folder URL `design/` typically resolves via index, so impact is expected to be nil).

Success criteria:
* Section index renders from README.md; no broken links to the old `readme.md`.

Context references:
* .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md (design/readme.md lowercase note).

Dependencies:
* None.

### Step 4.3: Remove empty resources/ from nav

`docs/resources/` contains only `ms_icon.png` and renders as an empty nav entry. Exclude it from the rendered navigation while keeping the asset (referenced by mkdocs.yml logo/favicon).

Files:
* docs/.pages - Ensure `resources` is excluded from the explicit nav list (handled in Step 2.1); optionally add `docs/resources/.pages` with `hide: true` if awesome-pages requires it.

Discrepancy references:
* Addresses Pain Point 7 (resources renders empty).

Success criteria:
* `resources` no longer appears as a nav item; the logo/favicon asset still loads.

Context references:
* mkdocs.yml (logo/favicon reference resources/ms_icon.png).

Dependencies:
* Step 2.1 (explicit nav list).

## Implementation Phase N: Validation

<!-- parallelizable: false -->

### Step N.1: Build the site

Execute documentation validation:
* pip install -r requirements-docs.txt (if environment not already prepared)
* mkdocs build --strict
* lychee ./docs (MANDATORY anchor/fragment-aware link check per lychee.toml; mkdocs --strict does not validate intra-page #anchors that the dedup stubs rely on)

### Step N.2: Fix minor validation issues

Iterate on broken internal links introduced by dedup stubs, the design README rename, and nav reordering. Apply fixes directly when straightforward and isolated.

### Step N.3: Report blocking issues

When validation failures require changes beyond minor fixes:
* Document the issues and affected files.
* Provide the user with next steps.
* Recommend additional research/planning (e.g., URL-changing folder renames + redirects) rather than inline fixes.

## Dependencies

* MkDocs + Material, awesome-pages, git-revision-date-localized (requirements-docs.txt / mkdocs.yml).
* Python environment for `mkdocs build --strict`.
* Required: lychee link checker for anchor/fragment validation.

## Success Criteria

* Persona entry layer exists and is the top nav group; topic sections unchanged in location.
* All HIGH/MEDIUM duplication findings resolved to a single canonical owner with link stubs.
* Structural cleanups applied (NFR README, design README casing, resources hidden, nav reordered).
* `mkdocs build --strict` passes with no broken internal links, and `lychee ./docs` passes with no broken `#anchor` fragments; no URL changes to existing topic sections.
