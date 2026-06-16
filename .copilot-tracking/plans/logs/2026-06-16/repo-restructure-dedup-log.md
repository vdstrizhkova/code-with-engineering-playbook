<!-- markdownlint-disable-file -->
# Planning Log: Repository Restructure to Reduce Guide Duplication

## Discrepancy Log

Gaps and differences identified between research findings and the implementation plan.

### Unaddressed Research Items

* DR-01: Folder casing normalization for URL-changing renames (`CI-CD`→`ci-cd`, `UI-UX`→`ui-ux`, `Images`→`images`)
  * Source: .copilot-tracking/research/subagents/2026-06-16/personas-navigation-research.md (Pain Point 4; IA pattern "naming/casing normalization")
  * Reason: Excluded from this plan because it changes published URLs and `mkdocs-redirects` is not configured; cosmetic benefit only. Deferred to follow-on work (WI-01).
  * Impact: low

* DR-02: Full Diátaxis overlay (tutorials/how-to/reference/explanation split across all sections)
  * Source: .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md (Scenario D)
  * Reason: High effort across ~250 files; not requested. Deferred (WI-02).
  * Impact: low

* DR-03: Onboarding consolidation (first-week vs developer-experience onboarding-guide-template vs checklist)
  * Source: .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 8)
  * Reason: Partially mitigated by the Start Here landing page (orientation), but the underlying three competing onboarding entry points are not merged in this plan to avoid content rewrites. Deferred (WI-03).
  * Impact: medium

* DR-04: Definition-of-Done restatement across 5+ agile sub-docs
  * Source: .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 9)
  * Reason: Lower priority PARTIAL overlap within one section; not in the HIGH/MEDIUM dedup scope of Phase 3. Deferred (WI-04).
  * Impact: low

* DR-05: documentation/guidance/* overlap with owning sections (rest-apis, work-items, engineering-feedback)
  * Source: .copilot-tracking/research/subagents/2026-06-16/repo-catalog-research.md (documentation section note)
  * Reason: The pull-requests stub is already correct; the remaining guidance/* files need case-by-case review. Deferred (WI-05).
  * Impact: low

* DR-06: Findings 6 (secrets-management split) and 7 (PR guidance) have no Phase 3 dedup step and no prior log entry [added by plan-validator]
  * Source: .copilot-tracking/research/subagents/2026-06-16/duplication-research.md (Finding 6, Finding 7); research main doc Suggested canonical owners (secrets → CI-CD/dev-sec-ops/secrets-management/)
  * Reason: Both are classified XREF/positive-pattern in research (the `source-control/secrets-management.md` stub and `documentation/guidance/pull-requests.md` stub are already correct), so no edit is required. However, the plan does not record them as deliberate no-ops, leaving Findings 6-7 unaccounted for in the Findings 1-11 → step mapping. Recommend an explicit "no action — already canonical XREF" note so coverage of all 11 findings is traceable.
  * Impact: low
  * RESOLVED: Findings 6 (secrets-management split) and 7 (PR guidance) are deliberate no-ops — already correct canonical XREF/stub patterns; no Phase 3 step needed. Recorded here for full 1-11 coverage.

### Plan Deviations from Research

* DD-01: Start Here placed above the Engineering Fundamentals Checklist in nav
  * Research recommends: illustrative `.pages` lists Start Here first, then the checklist (research Scenario A YAML).
  * Plan implements: same — Start Here first, then checklist/first-week/ISE, then topic sections in checklist order.
  * Rationale: Consistent with research; recorded for traceability. The checklist remains the canonical taxonomy and is linked prominently from the Start Here landing page.
  * [plan-validator note] This is NOT a deviation — the plan matches the research illustrative ordering exactly. The details file (Step 2.1) labels it "DD-01: deviates from research illustrative ordering," which contradicts this entry's own "Plan implements: same" statement. Recommend reclassifying as an intentional design decision (or removing the "deviates" wording in details) to avoid a false deviation flag. Severity: minor.
  * RESOLVED: details Step 2.1 reworded to "DD-01: design decision (not a deviation)"; no longer flagged as a deviation.

* DD-02: `design/readme.md` → `README.md` rename treated as zero-URL-impact
  * Research recommends: normalize casing (flagged as URL-affecting in general).
  * Plan implements: rename only the section index file, relying on folder-level URL resolution (`design/`) so the public URL is unchanged.
  * Rationale: Section index pages resolve at the folder URL; impact is expected to be nil, but validation (Phase N) must confirm no broken links to the old `readme.md`.

* DD-03: Dedup uses summarize-and-link rather than hard-cut removal
  * Research recommends: collapse duplicates to a single canonical owner.
  * Plan implements: spokes retain a domain-specific 1-2 sentence framing plus a link, instead of deleting all local context.
  * Rationale: Preserves readability and section self-containment while still removing the duplicated canonical content; matches the proven `documentation/guidance/pull-requests.md` pattern.

* DD-04: Plan→details cross-reference line numbers are systematically inaccurate [added by plan-validator]
  * Research recommends: N/A — this is a plan/details internal-consistency discrepancy surfaced during validation.
  * Plan implements: every Implementation Checklist step cites a details line range (e.g., Step 2.1 "Lines 138-168", Step 3.1 "Lines 190-220", Step 4.3 "Lines 368-384"). Verified against the actual details file, the headings sit at lines 116, 160, and 333 respectively. Only Step 1.1's start line (12) is correct; from Step 1.2 onward the cited ranges drift upward by ~9 lines, growing to ~35 lines by Phase 4. Step 4.x citations (350-384) fall inside the Validation phase (heading at line 352) and Dependencies section rather than the referenced steps.
  * Rationale: Citations appear copied from an earlier, longer draft of the details file. An implementer following them would land on the wrong (or non-existent) content. Recommend regenerating all 16 step line references against the current details file. Severity: major.
  * RESOLVED: All 16 step line references in the plan regenerated against the current details file (Phase 1: 14-113; Phase 2: 118-157; Phase 3: 162-293; Phase 4: 298-356).

* DD-05: Duplication Finding numbers collide between the two research documents [added by plan-validator]
  * Research recommends: a single, stable numbering for Findings 1-11.
  * Plan implements: plan/details step titles use the main research doc numbering (Finding 1 = AI baseline, Finding 2 = CI/CD fundamentals), while the details "Context references" point to the subagent `duplication-research.md`, which uses the opposite numbering (Finding 1 = CI/CD, Finding 2 = AI baseline). Step 3.1 (AI baseline) therefore cites "Finding 2 evidence" and Step 3.2 (CI/CD) cites "Finding 1 evidence." The referenced content is correct, but the conflicting numbers undermine the Findings 1-11 → step traceability the plan claims.
  * Rationale: Normalize on one numbering scheme (preferably the main research doc's) and annotate the subagent cross-references with the subagent's local number to avoid mis-navigation. Severity: major (traceability), low (functional, since targets are correct).
  * RESOLVED: details Context Reference now declares the MAIN research doc numbering as authoritative (Finding 1 = AI baseline, Finding 2 = CI/CD); subagent context references reworded to topic names instead of the subagent's conflicting numbers.

* DD-06: Canonical owner for the 8-item AI threat list is left ambiguous [added by plan-validator]
  * Research recommends: a single canonical owner per duplicated block (AI baseline → `ai-assisted-engineering/README.md`; threat modeling → `security/threat-modelling.md`).
  * Plan implements: Step 3.1 success criteria places the verbatim threat list canonically in `ai-assisted-engineering/README.md` ("plus security/threat-modelling.md if domain-appropriate"), while Step 3.6 designates `security/threat-modelling.md` as canonical for the AI threat enumeration and defers the decision ("coordinate with Step 3.1"). The single canonical home is therefore unresolved at plan time.
  * Rationale: Pick one definitive owner for the enumerated AI threat list before implementation so Steps 3.1 and 3.6 do not both claim/defer it. Severity: minor.
  * RESOLVED: single canonical home for the enumerated AI threat list = docs/security/threat-modelling.md. Step 3.1 now states the AI hub references (does not own) the list; Step 3.6 owns it. Recorded as DD-06 in details Steps 3.1 and 3.6.

* DD-07: Validation phase (`mkdocs build --strict`) does not verify the anchor fragments the dedup relies on [added by plan-validator]
  * Research recommends (Success Criteria): "`mkdocs build --strict` succeeds with no broken internal links."
  * Plan implements: Phase N runs `mkdocs build --strict` (and optional `lychee`). However, the deduplication approach replaces restated prose with deep links to specific section anchors (e.g., ai-assisted-engineering hub anchors, `security/threat-modelling.md` AI section, `code-reviews/pull-requests.md#pull-request-description`). `mkdocs build --strict` validates page existence but does not validate intra-page anchor fragments, so broken `#anchor` deep links can ship undetected. `lychee` (which can check fragments) is marked optional.
  * Rationale: Make the anchor/fragment check mandatory (promote `lychee` from optional to required, or add an explicit anchor-existence verification step) and verify each canonical anchor exists before linking. Severity: major.
  * RESOLVED: plan Phase N Step N.1 and details Step N.1 now make anchor/fragment-aware `lychee ./docs` MANDATORY (not optional), explicitly because `mkdocs build --strict` does not validate intra-page #anchors.

* DD-08: `lychee` is MANDATORY in validation Step N.1 but still labeled "optional" in both Dependencies sections [added by plan-validator]
  * Research recommends: N/A — plan/details internal-consistency discrepancy surfaced during second-pass validation of the DD-07 fix.
  * Plan implements: the DD-07 fix promoted `lychee ./docs` to MANDATORY in plan Step N.1 (plan line 115) and details Step N.1 (details line 366), but the residual Dependencies entries were not updated: plan Dependencies still reads "`lychee` link checker (optional, per `lychee.toml`)" (plan line 131) and details Dependencies still reads "Optional: lychee link checker" (details line 383). The plan/details Success Criteria also still gate only on `mkdocs build --strict` and do not mention the now-required anchor/fragment check.
  * Rationale: Reconcile the Dependencies wording with Step N.1 — mark `lychee` as required, and add the anchor/fragment link check to the Success Criteria so the mandatory gate is traceable. Functional impact is low because Step N.1 already states MANDATORY, so the check will run; this is a documentation-consistency residual from the DD-07 fix. Severity: minor.
  * RESOLVED: Dependencies updated to "REQUIRED/Required" and Success Criteria now gate on `lychee ./docs` anchor checks in both the plan and details files.

* DD-09: `mkdocs build --strict` cannot run in this dev container due to a pre-existing toolchain incompatibility [added during validation]
  * Research recommends (Success Criteria): "`mkdocs build --strict` succeeds with no broken internal links."
  * Plan implements: Phase N Step N.1 runs `mkdocs build --strict`. In this container the build crashes with `AttributeError: 'NoneType' object has no attribute 'replace'` while rendering `docs/CI-CD/dev-sec-ops/secrets-management/recipes/detect-secrets-ado.md` — a file NOT modified by this work. Root cause is the globally installed `pygments`/`pymdown-extensions` versions vs the pinned `markdown==3.3.*` stack (pymdownx highlight passes `filename=None`); reproduces on a plain ```yaml fence and persisted across pygments 2.20.0/2.16.1/2.11.2 and pymdownx 10.4/9.11. The crash halts the build before any of this work's files are reached.
  * Rationale: This is an environment/toolchain defect independent of the restructure. Anchor/fragment validation was performed instead with a deterministic custom checker (`.copilot-tracking/scripts/check_internal_links.py`) that slugifies headings the same way python-markdown/MkDocs does and verifies every internal link + `#anchor` across `docs/`. Result: zero problems in any file changed by this work (the 39 reported issues are all in unmodified files — UI-UX, design/sustainability, code-reviews, documentation/* — pre-existing anchor-casing/emoji-slug mismatches). Severity: medium (validation-tool blocker, not a content defect). Tracked as WI-06.

* DD-10: Phase 4 design-rename reference sweep was scoped to `docs/`, missing the repo-root `README.md` [added during validation]
  * Plan implements: Step 4.2 updates references to the renamed `design/readme.md`. The subagent grep was scoped to `docs/`, so the repo-root `README.md` line 56 (`[Design](docs/design/readme.md)`) was left stale, which would 404 after the rename.
  * Rationale: Fixed during validation — root `README.md` now links `docs/design/README.md`. Repo-wide grep confirms zero remaining `design/readme.md` references. Severity: minor (caught and fixed). Lesson: reference sweeps for renames must cover the whole repo, not just `docs/`.

## Implementation Paths Considered

### Selected: Persona entry layer + canonical hub-and-spoke dedup (Scenario A)

* Approach: Add `docs/start-here/` persona reading-path pages (links only) over the existing topic IA; collapse HIGH/MEDIUM duplications to single canonical owners with thin link stubs; apply low-risk structural cleanups; reorder nav to checklist taxonomy. No content moves, no URL changes.
* Rationale: Lowest risk for a published site; satisfies all four user requests; reuses already-enabled `awesome-pages` + `navigation.indexes`; keeps topics as the single canonical home so dedup and navigation reinforce each other.
* Evidence: .copilot-tracking/research/2026-06-16/repo-restructure-dedup-research.md (Scenario A, "Why selected").

### IP-01: Full persona-first reorganization (Scenario B)

* Approach: Physically relocate sections under `engineers/`, `leads/`, `data-scientists/`, `shared/` roots.
* Trade-offs: Strong persona clarity, but most sections are multi-persona, forcing duplication or arbitrary ownership; rewrites nearly every published URL.
* Rejection rationale: Large redirect burden (`mkdocs-redirects` not configured), high contributor churn, contradicts the established "Engineering Fundamentals" organizing principle.

### IP-02: Naming/casing normalization + redirects (Scenario C)

* Approach: Standardize all folder casing and add `mkdocs-redirects` for old URLs.
* Trade-offs: Consistent URLs, but cosmetic benefit for real cost; requires a new plugin and redirect map.
* Rejection rationale: URL-changing renames deferred to WI-01; only the zero-URL-change cleanups were adopted into Phase 4.

### IP-03: Diátaxis overlay (Scenario D)

* Approach: Re-tag/split every section into tutorials/how-to/reference/explanation.
* Trade-offs: Strong content-need clarity, but very high effort and increased nav depth for an explanation-heavy corpus.
* Rejection rationale: Out of scope; kept as a future option (WI-02) since `recipes/`/`templates/` already form a partial how-to layer.

## Suggested Follow-On Work

Items identified during planning that fall outside current scope.

* WI-01: Folder casing normalization + redirects — rename `CI-CD`→`ci-cd`, `UI-UX`→`ui-ux`, `Images`→`images`; add `mkdocs-redirects` with a redirect map (medium)
  * Source: DR-01 / research Pain Point 4
  * Dependency: Confirm `mkdocs-redirects` availability and inbound-link inventory first.

* WI-02: Diátaxis consistency pass on `recipes/`/`templates/` folders (low)
  * Source: DR-02 / research Scenario D
  * Dependency: None; can follow this plan.

* WI-03: Consolidate onboarding entry points (first-week + onboarding-guide-template + checklist) behind the new Start Here layer (medium)
  * Source: DR-03 / Finding 8
  * Dependency: Phase 1 (Start Here layer) complete.

* WI-04: Single-source the Definition of Done across agile team-agreements docs (low)
  * Source: DR-04 / Finding 9
  * Dependency: None.

* WI-05: Review `documentation/guidance/*` for remaining stub-vs-duplicate decisions (rest-apis, work-items, engineering-feedback) (low)
  * Source: DR-05 / catalog note
  * Dependency: None.

* WI-06: Fix the local docs toolchain so `mkdocs build --strict` runs, and clear pre-existing broken anchors (medium)
  * Source: DD-09 / validation run
  * Detail: Pin a `pygments`/`pymdown-extensions` combination compatible with `markdown==3.3.*` (or bump the whole stack) so `detect-secrets-ado.md` renders; then triage the 39 pre-existing internal-anchor mismatches surfaced by the custom checker (UI-UX `#resources-*`/emoji headings, design/sustainability `#electricity-consumption` et al., code-reviews `#Configuring*` casing, documentation `#vs-code-extensions`).
  * Dependency: None; independent of this restructure.

* WI-07: Add an explicit Start Here pointer to the repo-root `README.md` persona/sections list for parity with `docs/README.md` (low)
  * Source: validation observation
  * Dependency: None.
