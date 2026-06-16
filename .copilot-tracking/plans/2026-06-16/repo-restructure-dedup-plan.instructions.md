---
applyTo: '.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md'
---
<!-- markdownlint-disable-file -->
# Implementation Plan: Repository Restructure to Reduce Guide Duplication

## Overview

Add a persona-oriented entry layer (`docs/start-here/`) over the existing topic-based MkDocs IA, collapse duplicated guidance into single canonical owners referenced by thin "see also" stubs, and apply low-risk structural cleanups — without moving existing content or changing published URLs.

## Objectives

### User Requirements

* Find the duplications in the guides and minimize them — Source: conversation user request (2026-06-16).
* Propose/implement a restructure that is easier to read and reason about — Source: conversation user request.
* Make the repo easier to navigate for three personas (engineer, project manager, data scientist) — Source: conversation user request.

### Derived Objectives

* Preserve existing topic sections as canonical content homes and avoid URL churn — Derived from: site is published with external inbound links; `mkdocs-redirects` is not configured (research Scope/Assumptions).
* Reuse already-enabled `awesome-pages` + `navigation.indexes` infrastructure for persona landing pages — Derived from: research Navigation Pain Point 6 (unused infrastructure).
* Reorder top-level navigation to match the canonical Engineering Fundamentals Checklist taxonomy — Derived from: research Project Conventions (checklist is the de-facto taxonomy) and Pain Point 7 (structural mismatches).
* Keep personas as a thin reading-path layer (links only) so dedup and navigation reinforce rather than fight each other — Derived from: research Scenario A rationale.

## Context Summary

### Project Files

* docs/.pages - Top-level nav order (awesome-pages); edited to add the Start Here group and reorder topic sections to checklist order.
* mkdocs.yml - MkDocs Material config; `navigation.indexes` + `awesome-pages` already enabled (lines 19, 23-26); no `nav:` block, so nav is data-driven by `.pages`.
* docs/README.md - Playbook landing page; gains a link to the new Start Here persona pages.
* docs/ai-assisted-engineering/README.md - Canonical AI-assisted baseline (hub); target for dedup spokes to link into.
* docs/CI-CD/README.md - Canonical CI/CD fundamentals (lines 26-32); `branching-and-cicd.md` defers here.
* docs/automated-testing/README.md - Canonical testing taxonomy (lines 8-14); spokes link here.
* docs/source-control/README.md and docs/source-control/git-guidance/README.md - Canonical branching/merge workflow.
* docs/code-reviews/pull-requests.md - Canonical PR policy.
* docs/observability/tools/OpenTelemetry.md - Canonical OpenTelemetry guidance.
* docs/non-functional-requirements/ - Section with no root README (to be added).
* docs/design/readme.md - Lowercase filename to normalize to README.md.
* docs/documentation/guidance/pull-requests.md - Existing good thin-stub pattern to replicate.

### References

* .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md - Primary research: catalog, 11 duplication findings, persona mapping, selected Scenario A.
* .copilot-tracking/research/subagents/2026-06-16/duplication-research.md - Full duplication evidence with line numbers (Findings 1-11).
* .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md - Full section catalog and nav mechanics.
* .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md - Persona→section mapping and IA pattern options.

### Standards References

* /Users/vstrizhkova/.vscode/extensions/ise-hve-essentials.hve-core-all-3.2.2/.github/instructions/hve-core/markdown.instructions.md — Markdown authoring rules for all `.md` edits.
* /Users/vstrizhkova/.vscode/extensions/ise-hve-essentials.hve-core-all-3.2.2/.github/instructions/hve-core/writing-style.instructions.md — Voice/tone/language conventions for markdown content.

## Implementation Checklist

### [x] Implementation Phase 1: Persona Entry Layer

<!-- parallelizable: true -->

* [x] Step 1.1: Create `docs/start-here/README.md` landing page with persona selector
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 14-34)
* [x] Step 1.2: Create `docs/start-here/for-engineers.md` curated reading path
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 35-55)
* [x] Step 1.3: Create `docs/start-here/for-leads.md` curated reading path
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 56-76)
* [x] Step 1.4: Create `docs/start-here/for-data-scientists.md` curated reading path
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 77-97)
* [x] Step 1.5: Create `docs/start-here/.pages` to order persona pages
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 98-113)

### [x] Implementation Phase 2: Navigation and Landing Updates

<!-- parallelizable: false -->

* [x] Step 2.1: Update `docs/.pages` to add Start Here group and reorder topic sections to checklist order
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 118-140)
* [x] Step 2.2: Add a Start Here pointer to `docs/README.md`
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 141-157)

### [x] Implementation Phase 3: Canonical Hub-and-Spoke Deduplication

<!-- parallelizable: false -->

* [x] Step 3.1: Deduplicate AI-assisted baseline — link spokes to canonical hub (Finding 1)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 162-188)
* [x] Step 3.2: Deduplicate CI/CD fundamentals — defer `branching-and-cicd.md` to canonical (Finding 2)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 189-208)
* [x] Step 3.3: Deduplicate testing taxonomy — summarize-and-link in spokes (Finding 3)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 209-230)
* [x] Step 3.4: Deduplicate branching/merge-gate — single workflow + PR-policy owners (Findings 4, 5)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 231-251)
* [x] Step 3.5: Deduplicate OpenTelemetry blurb — link to canonical tool page (Finding 10)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 252-272)
* [x] Step 3.6: Deduplicate AI threat-modeling list — link to canonical (Findings 1, 11)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 273-293)

### [x] Implementation Phase 4: Structural Cleanups

<!-- parallelizable: true -->

* [x] Step 4.1: Add `docs/non-functional-requirements/README.md` section index
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 298-317)
* [x] Step 4.2: Normalize `docs/design/readme.md` to `README.md`
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 318-337)
* [x] Step 4.3: Remove empty `resources/` from rendered nav (keep asset)
  * Details: .copilot-tracking/details/2026-06-16/repo-restructure-dedup-details.md (Lines 338-356)

### [x] Implementation Phase N: Validation

<!-- parallelizable: false -->

* [x] Step N.1: Build the MkDocs site and resolve link/build errors
  * Run `pip install -r requirements-docs.txt` (if needed) then `mkdocs build --strict`
  * Run anchor/fragment-aware link checking (MANDATORY, not optional): `lychee ./docs` per `lychee.toml`, because dedup relies on deep `#anchor` links that `mkdocs build --strict` does not validate
  * Result: `mkdocs build --strict` blocked by a pre-existing pygments/pymdownx vs `markdown==3.3.*` crash in the unmodified `detect-secrets-ado.md` (DD-09 / WI-06); `lychee` not installable offline (no cargo/binary). Substituted a deterministic anchor-aware checker (`.copilot-tracking/scripts/check_internal_links.py`) that slugifies headings like python-markdown/MkDocs.
* [x] Step N.2: Fix minor validation issues
  * Repair broken internal links AND broken `#anchor` fragments introduced by dedup stubs and the `design/readme.md` rename
  * Confirm Start Here pages and reordered nav render correctly
  * Result: zero anchor/link issues in any changed file; fixed stale repo-root `README.md` Design link (DD-10). The 39 reported problems are all in unmodified files (pre-existing).
* [x] Step N.3: Report blocking issues
  * Document any issue requiring deeper change (e.g., URL-changing renames) and defer to follow-on work
  * Result: `mkdocs build --strict` toolchain defect recorded as DD-09 and deferred to WI-06; pre-existing broken anchors deferred to WI-06.
  * Avoid large-scale refactoring within this phase

## Planning Log

See .copilot-tracking/plans/logs/2026-06-16/repo-restructure-dedup-log.md for discrepancy tracking, implementation paths considered, and suggested follow-on work.

## Dependencies

* MkDocs + Material, `awesome-pages`, `git-revision-date-localized` (from `requirements-docs.txt` / `mkdocs.yml`).
* Python environment to run `mkdocs build --strict`.
* `lychee` link checker (REQUIRED for anchor/fragment validation, per `lychee.toml`).

## Success Criteria

* `docs/start-here/` exists with a landing page + three persona reading-path pages, surfaced at the top of the nav — Traces to: user requirement (persona navigation).
* Each HIGH/MEDIUM duplication finding has one canonical owner; restated copies replaced with thin link stubs — Traces to: user requirement (minimize duplicates); research Findings 1-5, 10, 11.
* Top-level nav reordered to checklist taxonomy; `resources/` no longer renders empty; NFR has a section README; `design/README.md` casing normalized — Traces to: Derived Objectives; research Pain Points 4, 7.
* `mkdocs build --strict` succeeds with no broken internal links, and `lychee ./docs` reports no broken `#anchor` fragments — Traces to: Success Criteria verifiability; DD-07.
* No existing topic-section URL changes (no redirects required) — Traces to: Derived Objective (avoid URL churn).
