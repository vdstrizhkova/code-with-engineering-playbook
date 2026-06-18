<!-- markdownlint-disable-file -->
# RPI Validation: Repository Restructure Phase 002

## Metadata

* Plan: `.copilot-tracking/plans/2026-06-16/repo-restructure-dedup-plan.instructions.md`
* Changes log: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md`
* Research: `.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md`
* Phase: 002 - Navigation and Landing Updates
* Validation date: 2026-06-17
* Additional context: staged follow-up on branch `review-ai-guidance` makes `docs/start-here/README.md` the front door, nests Project Kickoff Checklist and Engineering Fundamentals Checklist under `docs/start-here/.pages`, removes those entries from top-level `docs/.pages`, updates README/docs links, and retains `docs/the-first-week-of-an-ise-project.md` as a compatibility page.

## Validation Status

**Status: Resolved with Known External Validation Blocker**

## Follow-Up Resolution

2026-06-18 update: the old first-week page now preserves the historical section headings as link stubs into the new Project Kickoff Checklist, so page-level and section-anchor compatibility are both retained. The changes log also records the staged follow-up and compatibility strategy.

The staged follow-up preserves the main Phase 2 navigation intent: `Start Here` remains surfaced immediately after the docs landing page, topic sections remain in checklist-like order, `resources/` remains omitted from rendered nav, and `docs/README.md` points readers into the Start Here role path. The follow-up also improves the front-door experience by placing the kickoff checklist and engineering fundamentals checklist under the Start Here nav group.

The no published URL churn objective is now preserved for the first-week page path and its historical section anchors. External links to `/the-first-week-of-an-ise-project/#day-1`, `/the-first-week-of-an-ise-project/#day-2`, and related section anchors land on compatibility headings that link to the equivalent sections in the new checklist.

## Phase 2 Plan Requirements

| Plan item | Requirement | Evidence | Validation |
|---|---|---|---|
| Step 2.1 | Add `Start Here: start-here` after README in top-level nav. | Plan lines 30 and details lines 118-140; staged `docs/.pages` line 3. | Passed |
| Step 2.1 | Replace `- ...` auto-fill with explicit checklist-ordered section entries. | Changes log line 24; staged `docs/.pages` lines 3-19. | Passed |
| Step 2.1 | Keep all existing sections visible except empty `resources`. | Staged `docs/.pages` lines 5-19 include Source Control through UI/UX; no `resources` entry. | Passed |
| Step 2.1 | Preserve existing topic-section URLs and avoid URL churn. | Plan line 21 and line 142; research lines 20 and 177. | Passed for this follow-up; page path and old first-week section anchors are preserved. |
| Step 2.2 | Add a brief Start Here pointer to `docs/README.md`. | Changes log line 25; staged `docs/README.md` line 12. | Passed |
| Step 2.2 | Do not copy persona reading-path content into `docs/README.md`. | Staged `docs/README.md` lines 12 and 22 are short pointers only. | Passed |

## Changes Log Comparison

### Matched Claims

* The changes log claims `docs/.pages` inserted `Start Here: start-here` after README and omitted `resources` from rendered nav. Verified in `docs/.pages` lines 1-19.
* The changes log claims `docs/README.md` added a brief role pointer to Start Here. Verified in `docs/README.md` line 12.
* The staged follow-up adds `docs/start-here/project-kickoff-checklist.md` and includes it in `docs/start-here/.pages` line 6.
* The staged follow-up nests `Engineering Fundamentals Checklist` under `docs/start-here/.pages` line 7, aligning with the user-provided additional context.
* The staged follow-up retains `docs/the-first-week-of-an-ise-project.md` as a compatibility page with a link to `start-here/project-kickoff-checklist.md` and original section anchors preserved as link stubs.

### Gaps or Unlogged Follow-Up

* Resolved: the changes log now describes the staged follow-up that adds `docs/start-here/project-kickoff-checklist.md`, removes the checklist and first-week entries from top-level `docs/.pages`, and converts `docs/the-first-week-of-an-ise-project.md` into a compatibility page with preserved anchors.

## Findings

### Resolved: First-week compatibility page preserves previously published section anchors

The plan and research repeatedly prioritize avoiding published URL churn because the site has external inbound links and no redirects configured. The staged follow-up keeps the old page path by retaining `docs/the-first-week-of-an-ise-project.md`, which prevents a page-level 404. That is good and addresses the largest URL churn risk.

The compatibility page now keeps the original section headings for `Before Starting the Project`, `Day 1`, `Day 2`, `Day 3`, `Day 4`, and `Day 5`. Those headings preserve stable MkDocs anchors such as `#before-starting-the-project`, `#day-1`, `#day-2`, `#day-3`, `#day-4`, and `#day-5`. Each compatibility section links to the equivalent heading in `docs/start-here/project-kickoff-checklist.md`.

Evidence:

* Plan derived objective: avoid URL churn because external inbound links may exist and `mkdocs-redirects` is not configured, `.copilot-tracking/plans/2026-06-16/repo-restructure-dedup-plan.instructions.md` lines 21 and 142.
* Research assumption: published site external inbound links make URL-changing moves costly, `.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md` lines 20 and 177.
* Current compatibility page preserves the old headings, `docs/the-first-week-of-an-ise-project.md` lines 7, 11, 15, 19, 23, and 27.
* New target page owns the old section headings, `docs/start-here/project-kickoff-checklist.md` lines 5, 24, 39, 50, 58, and 67.
* Historical old headings existed at lines 10, 29, 44, 55, 63, and 72 in `HEAD:docs/the-first-week-of-an-ise-project.md`.

Impact:

* External links to the old page still land on a compatibility page.
* External deep links to old section anchors land on equivalent compatibility stubs and direct readers to the moved checklist sections.

Resolution:

* The low-risk compatibility-heading option was implemented.

### Resolved: Changes log does not reflect the staged Phase 2 follow-up

The changes log says the implementation has no content relocation or published URL changes and records only the original Phase 2 updates: adding Start Here to `docs/.pages` and adding a pointer to `docs/README.md`. It does not record the staged follow-up that makes the Start Here section the front door for the kickoff/checklist entries, adds `docs/start-here/project-kickoff-checklist.md`, removes the first-week and checklist entries from top-level `docs/.pages`, or changes `docs/the-first-week-of-an-ise-project.md` into a compatibility page.

Evidence:

* Changes log summary claims no content relocation and no published URL changes, `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` lines 9 and 60.
* Changes log Phase 2 modified entries mention `docs/.pages` and `docs/README.md`, but not the staged follow-up files, `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` lines 24-25.
* Staged files include `docs/start-here/.pages`, `docs/start-here/project-kickoff-checklist.md`, and `docs/the-first-week-of-an-ise-project.md` changes.

Impact:

* Traceability is incomplete for reviewers validating the current staged state against the implementation record.
* The omission makes the URL-churn claim harder to audit because the compatibility-page behavior is not documented in the changes log.

Resolution:

* The changes log now includes the staged follow-up files and explicitly documents the compatibility-page strategy.

## Coverage Assessment

**Coverage: Substantial but not complete.**

Phase 2 navigation and landing requirements are implemented for the main rendered nav and landing-page guidance. The staged follow-up arguably strengthens the front-door experience by grouping the role paths, kickoff checklist, and engineering fundamentals checklist under Start Here. Existing topic sections remain present at top level, so the canonical topic IA is preserved.

The earlier functional gap for old first-week deep links has been fixed. The old page path and old anchor fragments are preserved.

## Clarifying Questions

* Resolved: section-fragment compatibility is preserved.
* Resolved: the changes log is updated as part of this follow-up.

## Recommended Next Validations

* Run the repository's anchor-aware internal link checker against staged files after fixing or accepting the first-week anchor compatibility behavior.
* Run `mkdocs build --strict` once the known docs toolchain issue is resolved, then inspect the rendered navigation to confirm `docs/start-here/.pages` handles the parent reference to `../engineering-fundamentals-checklist.md` as intended.
* Validate that no generated nav item points directly to `docs/the-first-week-of-an-ise-project.md` while the page remains accessible by URL.
* Update and re-check the changes log if the staged follow-up is intended to be part of the same release record.
