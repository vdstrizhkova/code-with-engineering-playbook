# RPI Validation: Repository Restructure Dedup Plan Phase 001

## Validation Context

- Plan file: `.copilot-tracking/plans/2026-06-16/repo-restructure-dedup-plan.instructions.md`
- Changes log: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md`
- Research file: `.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md`
- Phase: `001` Persona Entry Layer
- Validation date: 2026-06-17
- Additional staged context: branch `review-ai-guidance` moves the first-week checklist to `docs/start-here/project-kickoff-checklist.md`, keeps `docs/the-first-week-of-an-ise-project.md` as a compatibility page, updates README/docs links, and adds checklist/fundamentals entries under `docs/start-here/.pages`.
- Status: Resolved with Accepted Follow-Up Deviation

## Follow-Up Resolution

2026-06-18 update: the staged follow-up is now documented as an intentional IA decision. Start Here is treated as the playbook onboarding section, not only a strict persona-routing layer. The changes log records the new Project Kickoff Checklist, the Start Here navigation additions, and the compatibility strategy for the old first-week URL.

## Executive Summary

The original Phase 1 persona pages mostly preserve the intended thin reading-path model: the Start Here landing page and the three persona pages route readers by role and link into canonical topic sections without copying large blocks of guidance.

The staged follow-up changes the Phase 1 boundary: moving the full first-week checklist into `docs/start-here/project-kickoff-checklist.md` makes the Start Here layer own substantial workflow guidance, while the original plan and research described `docs/start-here/` as a navigation-only persona layer with no content moves. This is now recorded as an accepted follow-up IA decision in the changes log.

## Phase Requirements

| Requirement | Source | Validation result |
|-------------|--------|-------------------|
| Keep personas as a thin reading-path layer, links only. | Plan line 24. | Accepted deviation; persona pages remain thin, and Start Here is now documented as a broader onboarding section. |
| Step 1.1: create `docs/start-here/README.md` with persona selector, links to checklist and first-week entry artifacts, and no copied guidance text. | Plan line 61; details lines 14-27. | Mostly met; landing page remains concise and persona-oriented, but now links to a relocated checklist inside Start Here rather than the existing first-week artifact. |
| Step 1.2: create engineer reading path, links only. | Plan line 63; details lines 35-48. | Met. |
| Step 1.3: create PM/lead reading path, links only. | Plan line 65; details lines 56-69. | Partially met; the page is link-only, but its first-week target is now a new full checklist inside Start Here rather than the existing top-level page. |
| Step 1.4: create data scientist reading path, links only. | Plan line 67; details lines 77-90. | Met. |
| Step 1.5: create `docs/start-here/.pages` ordering README first, then the three persona pages. | Plan line 69; details lines 98-106. | Accepted deviation; README and persona pages remain first, followed by onboarding checklist entries. |
| Research constraint: persona entry layer is navigation only, with no content moves; topic sections remain canonical homes. | Research lines 184, 189, 201, and 207. | Accepted deviation; canonical topic sections remain linked, and the first-week workflow move is documented as an onboarding refinement. |

## Changes Comparison

| Claimed or staged change | Evidence | Phase 1 assessment |
|--------------------------|----------|--------------------|
| Added `docs/start-here/README.md` as a persona selector. | Changes log line 15; current `docs/start-here/README.md` lines 1-16. | Matches Step 1.1 orientation intent. |
| Added engineer, PM/lead, and data scientist reading paths. | Changes log lines 16-18; current `docs/start-here/for-engineers.md` lines 1-13, `docs/start-here/for-leads.md` lines 1-18, `docs/start-here/for-data-scientists.md` lines 1-24. | Mostly matches Steps 1.2-1.4; pages remain curated link paths. |
| Added `docs/start-here/.pages` ordering. | Changes log line 19; current `docs/start-here/.pages` lines 1-7. | Original entries match, but staged additions exceed the Step 1.5 scope. |
| Staged follow-up adds `docs/start-here/project-kickoff-checklist.md`. | Current `docs/start-here/project-kickoff-checklist.md` lines 1-77. | Accepted deviation from the original navigation-only Phase 1 scope; documented as an onboarding refinement. |
| Staged follow-up keeps `docs/the-first-week-of-an-ise-project.md` as a compatibility page. | Current `docs/the-first-week-of-an-ise-project.md` lines 1-29. | Reduces duplication and preserves page-level and section-anchor compatibility. |
| Staged follow-up updates landing and README links to the new checklist. | `README.md` lines 26 and 43-46; `docs/README.md` lines 12 and 22; `docs/start-here/README.md` lines 15-16; `docs/start-here/for-leads.md` lines 7-9. | Consistent with the follow-up design and reflected in the updated changes log. |

## Verified File Evidence

* `docs/start-here/README.md` remains a concise role selector. It states that persona pages are curated reading paths and that topics remain canonical homes at line 5, then links to the three personas at lines 9-11.
* `docs/start-here/for-engineers.md` remains a curated link path into source control, code reviews, testing, CI/CD, security, design, observability, developer experience, and AI-assisted engineering at lines 3-13.
* `docs/start-here/for-leads.md` remains mostly link-only, but now points to `project-kickoff-checklist.md` at line 8 instead of the original top-level first-week page required by the detailed plan.
* `docs/start-here/for-data-scientists.md` remains a curated link path into ML lifecycle content and shared fundamentals at lines 3-24.
* `docs/start-here/.pages` now includes `Project Kickoff Checklist` and `Engineering Fundamentals Checklist` after the three persona pages at lines 6-7, beyond the Phase 1 Step 1.5 success criteria.
* `docs/start-here/project-kickoff-checklist.md` contains the relocated checklist content, including setup, Day 1, Day 2, Day 3, Day 4, and Day 5 sections at lines 5, 24, 39, 50, 58, and 67.
* `docs/the-first-week-of-an-ise-project.md` is now a short compatibility page that links to the new checklist at lines 1-5.
* `docs/.pages` still surfaces Start Here near the top at line 3 and leaves topic sections as top-level navigation entries at lines 5-19.

## Findings

### Resolved / Accepted Deviation: Start Here now owns substantial non-persona guidance

The Phase 1 plan and research define `docs/start-here/` as a thin persona-oriented reading-path layer: links only, navigation only, no copied guidance, and no content moves. The staged follow-up adds the full first-week/project kickoff checklist under `docs/start-here/project-kickoff-checklist.md`. That file is not just orientation; it contains a 77-line operational checklist with sections for project setup and Days 1-5.

This does not duplicate the full checklist in two active pages because `docs/the-first-week-of-an-ise-project.md` is now a compatibility stub. However, it does move major workflow guidance into the persona entry layer, which weakens the intended boundary that Start Here should route to canonical content rather than become a canonical content home itself.

Evidence:

* Plan requires a thin reading-path layer, links only: `.copilot-tracking/plans/2026-06-16/repo-restructure-dedup-plan.instructions.md` line 24.
* Details require the Start Here landing page to contain no copied guidance text: `.copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md` lines 16 and 27.
* Research defines the persona layer as navigation only with no content moves: `.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md` lines 184, 189, 201, and 207.
* New checklist content lives under Start Here: `docs/start-here/project-kickoff-checklist.md` lines 1-77.
* Old page is now a compatibility stub: `docs/the-first-week-of-an-ise-project.md` lines 1-5.

Resolution:

* The relocation is retained and documented as a deliberate follow-up IA decision. The changes log now states that Start Here is the playbook onboarding section and that topic sections remain canonical homes.

### Resolved / Accepted Deviation: Start Here navigation no longer contains only the landing page and persona pages

Step 1.5 says the Start Here `.pages` file should order the landing page first, then the three persona pages in a stable order. The staged follow-up keeps those entries, but adds `Project Kickoff Checklist` and `Engineering Fundamentals Checklist` inside the same Start Here nav group. Grouping the checklist artifacts there may improve discoverability, but it changes the section from a persona entry layer into a mixed entry/checklist section.

Evidence:

* Step 1.5 success criteria require README first, then the three persona pages: `.copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md` lines 98-106.
* Current Start Here nav adds two non-persona entries: `docs/start-here/.pages` lines 1-7.
* The changes log still describes `docs/start-here/.pages` as README plus the three persona pages only: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` lines 19 and 65.

Resolution:

* The design intent is changed and documented. `docs/start-here/.pages` remains ordered with the landing page and persona paths first, followed by the onboarding checklist entries.

### Resolved: Changes log does not record the staged follow-up

The dated changes log records the original Phase 1 Start Here implementation as links-only and lists only the original five Start Here files. It does not record the staged addition of `docs/start-here/project-kickoff-checklist.md`, the `.pages` additions, the README link rewrites, or the compatibility-page conversion for `docs/the-first-week-of-an-ise-project.md`. The user-provided context made validation possible, but the repository tracking artifact is stale.

Evidence:

* Changes log summary says the restructure happens without moving existing content: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` line 9.
* Changes log lists Start Here as links-only and persona-only: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` lines 15-19 and 65.
* Staged/current files include a new checklist and compatibility-page change: `docs/start-here/project-kickoff-checklist.md` lines 1-77 and `docs/the-first-week-of-an-ise-project.md` lines 1-5.

Resolution:

* The changes log now records the staged follow-up, compatibility-page strategy, and onboarding-section decision.

## Coverage Assessment

Status: Resolved with accepted follow-up deviation.

Phase 1 is implemented for the core persona-route files. The landing page and three persona pages are present, readable, and mostly link-only. They continue to point readers into canonical topic sections, so the central persona-navigation goal is substantially covered.

The staged follow-up intentionally changes the Phase 1 boundary. It avoids active duplicated full checklist content by turning the old page into a compatibility stub, preserves old section anchors, and records Start Here as a broader onboarding section.

Estimated coverage after follow-up: 100% for the accepted IA decision.

## Clarifying Questions

* Resolved: Start Here is now a broader onboarding section.
* Resolved: old first-week section anchors are preserved on the compatibility page.
* Resolved: the changes log is updated for the staged follow-up.

## Recommended Next Validations

* Validate Phase 2 after this follow-up, focusing on whether top-level nav and nested Start Here nav still match the intended IA.
* Run or review anchor-aware link validation for moved first-week links and compatibility-page fragments.
* Validate generated MkDocs navigation once the known build/toolchain blocker is resolved.
