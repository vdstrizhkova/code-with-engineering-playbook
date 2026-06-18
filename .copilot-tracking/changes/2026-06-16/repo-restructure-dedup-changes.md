<!-- markdownlint-disable-file -->
# Release Changes: Repository Restructure to Reduce Guide Duplication

**Related Plan**: repo-restructure-dedup-plan.instructions.md
**Implementation Date**: 2026-06-16

## Summary

Add a persona-oriented entry layer (`docs/start-here/`) over the existing topic-based MkDocs IA, collapse duplicated guidance into single canonical owners referenced by thin link stubs, and apply low-risk structural cleanups. A follow-up onboarding refinement moves the first-week checklist under Start Here while preserving the old page URL and section anchors as compatibility stubs.

## Changes

### Added

* docs/start-here/README.md - "How to use this playbook" landing page with a three-persona selector and links to the checklist and first-week pages (links only).
* docs/start-here/for-engineers.md - Curated engineer reading path (source-control → code-reviews → automated-testing → CI-CD → security → design → observability → developer-experience + ai-assisted-engineering baseline).
* docs/start-here/for-leads.md - Curated PM/Eng Lead reading path (agile-development → first-week → checklist → engineering-feedback → documentation + governance facets + TPM ML guide).
* docs/start-here/for-data-scientists.md - Curated Data Scientist reading path (ML lifecycle → ai-assisted-engineering + shared fundamentals).
* docs/start-here/.pages - awesome-pages ordering: README first, then the three persona pages.
* docs/start-here/project-kickoff-checklist.md - Follow-up onboarding checklist moved under Start Here so the first-week project workflow sits beside the role-based entry paths.
* docs/non-functional-requirements/README.md - New section index linking all NFR attribute pages plus the capture guide.

### Modified

* docs/.pages - Replaced the `- ...` auto-fill with an explicit checklist-ordered nav; inserted `Start Here: start-here` after README; `resources` omitted from rendered nav.
* docs/README.md - Added a brief role pointer to the Start Here guide (links only, no copied content).
* docs/start-here/README.md - Clarified that Start Here is the front door before choosing a role path; updated the kickoff link to the nested Project Kickoff Checklist.
* docs/start-here/.pages - Follow-up update: added Project Kickoff Checklist and Engineering Fundamentals Checklist entries after the three role paths, making Start Here a broader onboarding section.
* docs/start-here/for-engineers.md - Updated `../design/readme.md` link to `../design/README.md` after the casing rename.
* docs/start-here/for-leads.md - Updated `../design/readme.md` link to `../design/README.md` after the casing rename; follow-up update: retargeted the project kickoff step to `project-kickoff-checklist.md`.
* docs/the-first-week-of-an-ise-project.md - Follow-up update: converted the old first-week page to a compatibility page with the original section anchors preserved as link stubs into the Project Kickoff Checklist.
* README.md - Follow-up update: added Start Here to Resources and retargeted the sprint-structure link to the Project Kickoff Checklist.
* docs/design/README.md - Renamed from docs/design/readme.md via `git mv` (history preserved); normalizes section-index casing.
* README.md - Updated the repo-root Design link from `docs/design/readme.md` to `docs/design/README.md` after the rename (caught in validation; subagent sweep was scoped to docs/).

* docs/security/threat-modelling.md - Added the canonical 8-item AI threat enumeration to the AI section (single home per DD-06).
* docs/ai-assisted-engineering/README.md - Replaced the verbatim threat-coverage enumeration with a link to the canonical threat-modelling anchor.
* docs/security/README.md - Replaced the restated AI threat enumeration with a pointer to the canonical threat-modelling AI section.
* docs/code-reviews/README.md - Removed duplicated AI-baseline lines; pointed to the hub for the shared baseline, kept review-specific bullets.
* docs/automated-testing/README.md - Moved the hub link up with anchor; removed redundant restatement, kept testing-specific bullets.
* docs/source-control/README.md - Removed the duplicated "record AI assistance" bullet; folded authorship into the hub link, kept traceability bullets.
* docs/developer-experience/copilots.md - Reframed "Validating AI-Assisted Work" to defer the draft principle to the hub (#human-oversight); preserved operating-model/attribution content.
* docs/agile-development/branching-and-cicd.md - Removed duplicated CI/CD fundamentals bullets, branch-protection examples, and merge-policy checklist; linked CI/CD, source-control, and code-reviews canonical owners; kept unique CI gate YAML and tips.
* docs/CI-CD/continuous-integration.md - Added canonical testing-taxonomy links and canonical workflow links to Branch Policy Enforcement, keeping CI-specific guidance.
* docs/agile-development/team-agreements/definition-of-done.md - Added a one-line note linking the canonical testing taxonomy; checklists unchanged.
* docs/non-functional-requirements/maintainability.md - Replaced re-listed test types with a link to the canonical taxonomy.
* docs/observability/correlation-id.md - Replaced verbatim OpenTelemetry blurb with a correlation-ID-specific link.
* docs/observability/pillars/tracing.md - Replaced verbatim OpenTelemetry blurb with a tracing-specific link.
* docs/observability/microservices.md - Replaced verbatim OpenTelemetry blurb with a trace-context-specific link.

### Removed

## Additional or Deviating Changes

* Phase 1/3 subagents could not read the host-path instruction files (markdown/writing-style) because they live on the macOS host extension path, not mounted in the dev container.
  * Mitigation: applied standard markdown/writing-style conventions (single H1, sentence-case headings, relative links, concise active voice). Conformance to be re-checked in validation.
* Phase 1 link substitution: `design` section index is lowercase `readme.md`; persona pages link to ../design/readme.md (to be normalized in Phase 4 Step 4.2 — update links after rename).
  * Reason: `design/README.md` does not yet exist at Phase 1 time.
* Phase 3 Step 3.6: the canonical threat-modelling.md AI section previously held threats only as prose; the explicit 8-item enumeration was added there to make the link target authoritative (consistent with DD-06).
* Validation (Phase N): `mkdocs build --strict` could not run — it crashes in the unmodified `docs/CI-CD/.../detect-secrets-ado.md` due to a pre-existing pygments/pymdown-extensions vs `markdown==3.3.*` incompatibility (DD-09). Anchor/fragment validation was done instead with a deterministic custom checker (`.copilot-tracking/scripts/check_internal_links.py`); zero issues in any file changed by this work (the 39 reported problems are all in unmodified files). Tracked as WI-06.
* Validation caught a stale repo-root `README.md` Design link missed by the docs-scoped Phase 4 sweep (DD-10); fixed.
* Follow-up navigation decision (2026-06-18): Start Here is now treated as the playbook onboarding section, not only a strict persona-routing layer.
  * Reason: user review identified confusion between Start Here and the first-week guide; nesting kickoff and fundamentals entries under Start Here makes the reading order explicit while preserving topic sections as canonical homes.
  * Compatibility: `docs/the-first-week-of-an-ise-project.md` remains published as a lightweight compatibility page and preserves old section anchors (`#before-starting-the-project`, `#day-1` through `#day-5`) as link stubs.

## Release Summary

**Scope:** Persona entry layer + canonical hub-and-spoke deduplication + low-risk structural cleanups for the ISE Engineering Fundamentals Playbook (MkDocs Material), plus a follow-up onboarding refinement that nests the project kickoff checklist under Start Here. Published page URL and first-week section anchors are preserved through compatibility stubs.

**Files affected: 7 added, 20 modified, 1 renamed, 0 removed.**

* Added (7):
  * docs/start-here/README.md, docs/start-here/for-engineers.md, docs/start-here/for-leads.md, docs/start-here/for-data-scientists.md, docs/start-here/.pages — persona entry layer (links only).
  * docs/non-functional-requirements/README.md — new section index.
  * docs/start-here/project-kickoff-checklist.md — onboarding checklist nested under Start Here.
* Renamed (1): docs/design/readme.md → docs/design/README.md (`git mv`, history preserved).
* Modified (20): docs/.pages, docs/README.md, README.md (root), docs/the-first-week-of-an-ise-project.md, and 16 content/navigation files deduplicated or retargeted to canonical hubs (security/threat-modelling.md, ai-assisted-engineering/README.md, security/README.md, code-reviews/README.md, automated-testing/README.md, source-control/README.md, developer-experience/copilots.md, agile-development/branching-and-cicd.md, CI-CD/continuous-integration.md, agile-development/team-agreements/definition-of-done.md, non-functional-requirements/maintainability.md, observability/correlation-id.md, observability/pillars/tracing.md, observability/microservices.md, docs/start-here/README.md, docs/start-here/for-leads.md).

**Dependency/infrastructure changes:** None to the site (no new plugins; reused already-enabled `awesome-pages` + `navigation.indexes`). Nav switched from `awesome-pages` auto-fill (`- ...`) to an explicit checklist-ordered list with a new "Start Here" group; `resources/` excluded from rendered nav (asset retained for logo/favicon).

**Validation:** Internal links and `#anchor` fragments across `docs/` verified clean for all changed files via the custom anchor-aware checker; repo-wide grep confirms no stale `design/readme.md` references. `mkdocs build --strict` is blocked by a pre-existing toolchain defect unrelated to these changes (DD-09 / WI-06).

**Deployment notes:** Pure documentation change. Before merge, run `mkdocs build --strict` in a correctly pinned environment (or CI) once WI-06 resolves the pygments/pymdownx pin, and run `lychee ./docs` for external-link coverage.

