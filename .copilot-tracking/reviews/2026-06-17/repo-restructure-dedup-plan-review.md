<!-- markdownlint-disable-file -->
# Task Review: Repository Restructure Dedup Follow-Up

## Metadata

* Review date: 2026-06-17
* Related plan: `.copilot-tracking/plans/2026-06-16/repo-restructure-dedup-plan.instructions.md`
* Changes log: `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md`
* Research document: `.copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md`
* Conversation context: User asked whether readers should start with Start Here or the first-week guide, then requested implementation, review, fixes, and this task review.
* Reviewed scope: Current staged documentation/navigation follow-up on branch `review-ai-guidance`.

## Summary

The follow-up improves reader orientation by making `docs/start-here/README.md` the clear front door and by grouping the Project Kickoff Checklist and Engineering Fundamentals Checklist under the Start Here navigation group. The previous first-week page path is now retained as a compatibility page, which addresses the page-level URL churn identified during review.

The original review found two plan-alignment and traceability issues. Follow-up fixes now preserve the old first-week section anchors and document the intentional IA shift: Start Here is treated as a broader onboarding section, not only a strict persona-routing layer. Full MkDocs validation remains blocked by the unrelated existing rendering issue in the secrets-management recipe.

## Severity Counts

| Severity | Count |
|----------|-------|
| Critical | 0 |
| Major | 0 |
| Minor | 0 |

## Validation Activities

* Discovered related plan, changes, research, and prior review artifacts under `.copilot-tracking/`.
* Reviewed current staged diff for: `README.md`, `docs/.pages`, `docs/README.md`, `docs/start-here/.pages`, `docs/start-here/README.md`, `docs/start-here/for-leads.md`, `docs/start-here/project-kickoff-checklist.md`, and `docs/the-first-week-of-an-ise-project.md`.
* Ran RPI Validator for Phase 1 Persona Entry Layer.
* Ran RPI Validator for Phase 2 Navigation and Landing Updates.
* Attempted Implementation Validator full-quality validation; the subagent was blocked by lack of filesystem access in its execution environment.
* Ran public-reference grep for `the-first-week-of-an-ise-project`, `Project Kickoff Checklist`, and `project-kickoff-checklist`.
* Ran custom anchor-aware internal link checker: `.copilot-tracking/scripts/check_internal_links.py`.
* Re-ran `mkdocs build --strict` after fixes.

## RPI Validation Results

### Phase 1: Persona Entry Layer

* Validation file: `.copilot-tracking/reviews/rpi/2026-06-17/repo-restructure-dedup-plan-001-validation.md`
* Original status: Partial
* Current status: Resolved with accepted follow-up deviation
* Original findings, now resolved or accepted:
  * Major: Start Here now owns substantial non-persona workflow guidance in `docs/start-here/project-kickoff-checklist.md`.
  * Major: `docs/start-here/.pages` no longer contains only the landing page and three persona pages; it now includes the Project Kickoff Checklist and Engineering Fundamentals Checklist entries.
  * Minor: The changes log did not record the staged follow-up.

### Phase 2: Navigation and Landing Updates

* Validation file: `.copilot-tracking/reviews/rpi/2026-06-17/repo-restructure-dedup-plan-002-validation.md`
* Original status: Partial
* Current status: Resolved with known external validation blocker
* Original findings, now resolved:
  * Major: `docs/the-first-week-of-an-ise-project.md` preserved the old page path, but removed old published section anchors such as `#before-starting-the-project`, `#day-1`, `#day-2`, `#day-3`, `#day-4`, and `#day-5`.
  * Minor: The changes log did not reflect the staged Phase 2 follow-up.

## Implementation Quality Validation

* Validation file requested: `.copilot-tracking/reviews/implementation/2026-06-17/repo-restructure-dedup-plan-quality-validation.md`
* Status: Blocked
* Reason: The Implementation Validator subagent reported it could not access filesystem read/write tools in its environment.
* Manual quality checks performed in this review:
  * Staged diff reviewed for moved/updated links.
  * Public-facing docs references checked with grep.
  * Custom internal link checker run across `docs/`.
  * MkDocs strict build attempted.

## Synthesized Findings

### Resolved: First-week compatibility page preserves old section anchors

The old page path is restored, and `docs/the-first-week-of-an-ise-project.md` now retains the old section headings as lightweight link stubs into the moved checklist. External deep links to `#before-starting-the-project`, `#day-1`, `#day-2`, `#day-3`, `#day-4`, and `#day-5` now land on matching compatibility anchors and direct readers to the equivalent sections in `docs/start-here/project-kickoff-checklist.md`.

### Resolved: Start Here scope is documented as broader onboarding

The follow-up changes log now records that Start Here is intentionally treated as the playbook onboarding section. This accepts the IA shift from a strict persona routing layer to a broader entry section that contains role paths plus the project kickoff and fundamentals checklist links.

### Resolved: Changes log records staged follow-up

The changes log now records the new checklist page, the Start Here navigation additions, the old-page compatibility strategy, and the reason for the onboarding-section decision.

## Original Findings

### Major: First-week compatibility page does not preserve old section anchors

The old page path is restored, which avoids a page-level 404. However, the compatibility page now contains only an H1 and two short paragraphs at `docs/the-first-week-of-an-ise-project.md` lines 1-5. The relocated checklist contains the old sections at `docs/start-here/project-kickoff-checklist.md` lines 5, 24, 39, 50, 58, and 67.

The original plan selected a low-risk restructure specifically to avoid published URL churn because the site may have external inbound links and no redirect plugin is configured. Page-level compatibility is helpful, but old fragment links such as `#before-starting-the-project`, `#day-1`, `#day-2`, `#day-3`, `#day-4`, and `#day-5` no longer land on equivalent content.

Recommended fix: Add visible or HTML anchor-compatible section stubs to `docs/the-first-week-of-an-ise-project.md`, each pointing to the matching section in `docs/start-here/project-kickoff-checklist.md`, or add fragment-aware redirects if the site tooling supports them.

### Major: Start Here scope now differs from the original plan

The original plan and research describe `docs/start-here/` as a thin persona-oriented entry layer made of reading paths that link into canonical topic sections. The staged follow-up makes Start Here own `docs/start-here/project-kickoff-checklist.md`, a 77-line operational checklist, and adds non-persona entries to `docs/start-here/.pages` lines 6-7.

This may be the right product decision based on the user conversation: Start Here becomes a broader onboarding section, not only a persona selector. But it is a plan deviation and should be explicitly accepted or the implementation should be adjusted to keep the full checklist at the old top-level page with only links from Start Here.

Recommended fix: Decide whether Start Here is a broader onboarding section. If yes, update the plan/changes log to document the changed IA. If no, keep the full checklist at `docs/the-first-week-of-an-ise-project.md` and link to it from Start Here without moving the canonical content.

### Minor: Changes log is stale for the staged follow-up

The changes log still says the restructure avoids moving content and lists Start Here as a links-only persona layer. It does not record the new `docs/start-here/project-kickoff-checklist.md`, the `docs/start-here/.pages` additions, top-level nav removal of checklist/first-week entries, README link rewrites, or the compatibility-page strategy.

Recommended fix: Update `.copilot-tracking/changes/2026-06-16/repo-restructure-dedup-changes.md` or create a dated follow-up changes log for the 2026-06-17 navigation refinement.

## Validation Command Results

### `grep` public references

Status: Passed for public-facing references.

Observed references are to the new checklist path, the restored compatibility page, or the Start Here nav entries. No public-facing stale link to a deleted first-week path remains.

### `.copilot-tracking/scripts/check_internal_links.py`

Status: Failed with 39 existing internal link/anchor problems.

The failure list matches the known pre-existing validation debt recorded in the original implementation plan and changes log. No new error for `docs/start-here/project-kickoff-checklist.md` or `docs/the-first-week-of-an-ise-project.md` was reported. This does not validate external deep links to old first-week anchors, because those are not internal references in the current repo.

### `mkdocs build --strict`

Status: Blocked by unrelated existing rendering error.

The build fails while reading `docs/CI-CD/dev-sec-ops/secrets-management/recipes/detect-secrets-ado.md` with `'NoneType' object has no attribute 'replace'`. This is the same known blocker documented before this review and is outside the staged follow-up scope.

## Missing Work and Deviations

* The Start Here section now mixes persona routing with checklist/workflow content; this is documented as an accepted follow-up IA decision.
* Full implementation-quality subagent validation could not complete due to subagent filesystem access limitations.
* Full MkDocs build validation remains blocked by the known unrelated secrets-management recipe rendering issue.

## Follow-Up Recommendations

### Deferred or Existing Scope

* Resolve the known `mkdocs build --strict` blocker in `docs/CI-CD/dev-sec-ops/secrets-management/recipes/detect-secrets-ado.md`.
* Resolve or triage the 39 pre-existing internal-link checker findings recorded by `.copilot-tracking/scripts/check_internal_links.py`.

### Discovered During Review

* Re-run RPI validation if a clean formal sign-off is required after the follow-up fixes.

## Overall Status

Ready With Known External Validation Blocker

The staged follow-up is coherent after the anchor compatibility and traceability fixes. Remaining validation risk is external to this change: `mkdocs build --strict` is still blocked by the known unrelated secrets-management recipe rendering error, and the custom internal-link checker still reports known pre-existing issues outside this scoped follow-up.
