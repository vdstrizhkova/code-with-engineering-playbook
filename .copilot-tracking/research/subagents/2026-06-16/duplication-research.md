# Documentation Duplication & Overlap Research

Repository: code-with-engineering-playbook (MkDocs site, all docs under `docs/`)
Date: 2026-06-16
Status: Complete

## Research Topics / Questions

Find concrete, evidence-based duplication and overlap across the playbook guides in these areas:

1. Testing guidance overlap (automated-testing vs CI-CD vs ml-and-ai vs design)
2. CI/CD overlap (CI-CD vs agile branching-and-cicd vs source-control vs dev-sec-ops)
3. Code reviews / pull requests (code-reviews vs source-control)
4. Source control / branching (source-control vs branching-and-cicd vs CI-CD)
5. Security (security vs CI-CD/dev-sec-ops vs non-functional-requirements)
6. Documentation practices (documentation vs scattered README advice)
7. Agile / ceremonies / team agreements internal + first-week + ML agile
8. AI/ML & AI-assisted engineering (ml-and-ai vs ai-assisted-engineering vs copilots)
9. Observability / non-functional-requirements
10. Onboarding / first-week guidance scattered across multiple files

Classification legend:
- **DUP** = true duplication (same/near-verbatim content in 2+ places)
- **PARTIAL** = partial overlap (same advice, different wording/scope)
- **XREF** = appropriate cross-referencing (canonical source + links, low concern)

---

## Finding 1 (HIGH) — CI/CD "Fundamentals" lists near-duplicated

Topic: Core CI/CD expectations (quality pipeline on PR, IaC provisioning, automated deploy to non-prod, automated rollback, e2e release validation).

Files:
- docs/CI-CD/README.md lines 26-32 ("## The Fundamentals")
- docs/agile-development/branching-and-cicd.md lines 60-66 ("## CI/CD guidance")

Evidence — CI-CD/README.md lines 27-32:
> - We run a quality pipeline (with linting, unit tests etc.) on each PR/update of the main branch
> - All cloud resources ... are provisioned through infrastructure as code templates – ex. Terraform, Bicep (ARM), Pulumi etc.
> - All release candidates are deployed to a non-production environment through an automated process
> - Releases are deployed to the production environment through an automated process
> - Release rollbacks are carried out through a repeatable process
> - Our release pipeline runs automated tests, validating all release candidate artifact(s) end-to-end against a non-production environment

Evidence — branching-and-cicd.md lines 61-66:
> - The integration (main) branch should be continuously shippable and stable ...
> - Run a quality pipeline (linting, unit tests, basic integration tests) on each PR and on merges to the integration branch.
> - Provision cloud resources and environment configuration via infrastructure-as-code (for example Terraform, Bicep, Pulumi) ...
> - Deploy release candidates automatically to a non-production environment ...
> - Automate release and rollback procedures so releases are repeatable and auditable.

Classification: **DUP / PARTIAL**. branching-and-cicd.md explicitly says it "complements the central CI/CD guidance" (line 59) and links to it, but then restates essentially the same five bullets. The cross-reference exists, yet the content is duplicated rather than deferred.

---

## Finding 2 (HIGH) — AI-assisted engineering guidance fanned out across many guides

Topic: Human oversight, data/context hygiene, treat-model-output-as-untrusted, testing/evaluation of AI output, authorship/traceability, threat coverage for prompt injection. The same baseline guidance is repeated (re-worded) in a hub page plus many domain guides.

Files (each carries its own restatement of the shared AI baseline):
- docs/ai-assisted-engineering/README.md (the designated hub) — full guidance, e.g. lines 22-39 (Human Oversight), 41-49 (Data/Context Hygiene), 71-79 (Testing/Evaluation), 95-101 (Authorship/Traceability)
- docs/developer-experience/copilots.md lines 104-130 (validation evidence, untrusted output, disclose AI assistance) and 134-160 (authorship/attribution)
- docs/automated-testing/README.md lines 18-30 ("## Testing AI-assisted and AI-enabled changes")
- docs/security/README.md lines 13-25 ("## AI and agent security")
- docs/source-control/README.md lines 13-20 (AI assistance + traceability)
- docs/code-reviews/README.md lines 13-25 ("## Reviewing AI-assisted changes")
- docs/code-reviews/process-guidance/reviewer-guidance.md line 70 (validation evidence)

Evidence of repeated "treat AI output as untrusted draft / keep a named human owner":
- ai-assisted-engineering/README.md line 24: "Treat AI output as draft material until a responsible person reviews, tests, and accepts it." / line 25: "Keep a named human owner for every AI-assisted pull request..."
- copilots.md line 104: "Before a pull request is merged, a human owner remains accountable for the result" / line 122: "Treat AI-generated output as a draft until a responsible person reviews and accepts it."
- code-reviews/README.md line 15: "AI-generated code is reviewed as untrusted code."
- security/README.md line 13: "Treat model output as untrusted input before rendering, executing, storing, or sending it..."

Evidence of repeated threat-coverage list (prompt injection, insecure output handling, sensitive info disclosure, excessive agency, unsafe tool calls, model/data poisoning, model theft, AI supply chain) appearing verbatim in 3 places:
- ai-assisted-engineering/README.md line 67
- security/README.md line 15
- security/threat-modelling.md AI section (lines 19-21) + copilots.md line 118 reference

Evidence of repeated "do not paste secrets/credentials/customer data into AI tools":
- ai-assisted-engineering/README.md line 44
- copilots.md line 93
- source-control/README.md line 18 ("Do not commit prompts, transcripts, or generated artifacts that contain secrets or customer data.")
- source-control/secrets-management.md line 16

Classification: **PARTIAL (intentional hub-and-spoke, but heavy re-statement)**. The hub (ai-assisted-engineering/README.md) is linked from each spoke, which is good practice, but each domain guide re-articulates the same principles in its own words rather than linking to a single canonical bullet list. This is the single most pervasive overlap in the repo. Risk: divergence over time (the lists are already worded slightly differently in each location).

---

## Finding 3 (MEDIUM-HIGH) — Testing "fundamentals" repeated as checklists in many guides

Topic: "Code is incomplete without tests; write unit tests that run before PR merge; integration/e2e test the whole system; load/performance tests where appropriate."

Files:
- docs/automated-testing/README.md lines 8-14 ("## The Fundamentals")
- docs/CI-CD/continuous-integration.md lines 44-46 (Unit Testing), 140-142 + 190-205 (E2E Integration Tests), 240 (end-of-day unit tests)
- docs/engineering-fundamentals-checklist.md lines 27-28 ("Unit tests cover the majority...", "Integration tests run to test the solution e2e"), 99, 126-127
- docs/agile-development/team-agreements/definition-of-done.md lines 12-13, 25-27 (unit/integration/performance/e2e tests pass)
- docs/non-functional-requirements/maintainability.md lines 9, 26 (unit, e2e, smoke, integration tests + CI)
- docs/agile-development/branching-and-cicd.md lines 47, 55 (linting, unit tests, basic integration tests on each PR)
- docs/code-reviews/evidence-and-measures/README.md line 8 (builds run unit tests)
- docs/the-first-week-of-an-ise-project.md line 38 (separate unit from integration/load/smoke tests)

Evidence — automated-testing/README.md lines 10-13:
> - We consider code to be incomplete if it is not accompanied by tests
> - We write unit tests ... that can run before every PR merge to validate that we don't have regressions
> - We write Integration tests/E2E tests that test the whole system end to end ...
> - We run load tests/performance tests where appropriate ...

Same expectations recur as checklist items in definition-of-done.md (lines 12-27) and engineering-fundamentals-checklist.md (lines 27-28, 126).

Classification: **PARTIAL**. Checklists legitimately summarize, but the same unit/integration/e2e/performance taxonomy and "no code without tests / block merge on failing tests" rule is independently restated in at least 6 files. continuous-integration.md (lines 190-246) re-explains E2E integration testing in depth, overlapping the dedicated automated-testing/e2e-testing/ guide.

---

## Finding 4 (MEDIUM) — Branching + feature-branch + PR-merge workflow described in multiple places

Topic: Work in short-lived feature branches off main/trunk, lock the default branch, merge via PR, enforce branch protection / required reviewers / required CI.

Files:
- docs/source-control/git-guidance/README.md lines 83-148 (Branching, Pushing, Merging, PR process)
- docs/source-control/README.md lines 28-40 (Creating a New Repository: agree branch/release/merge strategy, lock default branch, merge via PRs, branch naming)
- docs/agile-development/branching-and-cicd.md lines 7-18 (trunk-based, short-lived feature branches, branch protection rules)
- docs/CI-CD/continuous-integration.md lines 222-235 (Branch Policy Enforcement, Branch Strategy)
- docs/code-reviews/pull-requests.md lines 3-14 (changes to main must use PRs; enforced by policies)

Evidence — source-control/git-guidance/README.md line 83:
> To avoid adding code that has not been peer reviewed to the main branch ... we typically work in feature branches, and merge these back to the main trunk with a Pull Request ... the main or develop branch ... are locked so that you can't make changes without a Pull Request.

Evidence — branching-and-cicd.md lines 8-9:
> - Prefer trunk-based development ... Use short-lived feature branches ... merge frequently into the default integration branch ...
> - Use branch protection rules on the integration branch to enforce quality gates (required passing CI, required code reviews, status checks).

Evidence — CI-CD/continuous-integration.md lines 224-226 (Branch Policy Enforcement):
> Protected branch policies should be setup on the main branch ... Broken builds should block pull request reviews. Prevent commits directly into main branch.

Classification: **PARTIAL**. Four guides independently describe branch protection / required reviewers / required CI before merge. branching-and-cicd.md (a newer, short policy page) overlaps most directly with source-control/README.md "Creating a New Repository" and CI-CD branch policy sections.

---

## Finding 5 (MEDIUM) — Branch protection / merge gate "checklist" duplicated

Topic: Merge requires passing CI + ≥1 approving reviewer + linked work item + docs updated.

Files:
- docs/agile-development/branching-and-cicd.md lines 19-22 (Example branch protection rules) and 36-41 (Merge policy checklist)
- docs/the-first-week-of-an-ise-project.md line 58 ("Set up Build Validation for Pull Requests (2 reviewers, linters, automated tests)")
- docs/code-reviews/evidence-and-measures/README.md lines 5-9 (policies on main branch as evidence of code review)
- github_conf/branch_protection_rules.json (machine config of the same rules)

Evidence — branching-and-cicd.md lines 37-40:
> - [ ] Code compiles and automated tests pass in CI
> - [ ] At least one approving reviewer has reviewed the change
> - [ ] The change has an associated work item or issue
> - [ ] Documentation updated where applicable

Classification: **PARTIAL**. Same merge-gate rules appear as prose in source-control, checklist in branching-and-cicd, and first-week setup task.

---

## Finding 6 (MEDIUM) — Secrets management split across source-control and dev-sec-ops

Topic: Keep secrets out of source control; credential scanning in CI/CD.

Files:
- docs/source-control/secrets-management.md lines 1-20 (Working with Secrets in Source Control)
- docs/CI-CD/dev-sec-ops/secrets-management/README.md (canonical Secrets Management)
- docs/CI-CD/dev-sec-ops/secrets-management/credential_scanning.md lines 1-5
- docs/security/README.md line 28 (links to credential scanning)
- docs/engineering-fundamentals-checklist.md line 13 (secrets not in commit history)

Evidence — source-control/secrets-management.md line 12:
> For more details on proper management of credentials and secrets in source control ... please refer to the [Secrets Management](../CI-CD/dev-sec-ops/secrets-management/README.md) document ...

Classification: **XREF (mostly good)**. source-control/secrets-management.md is a short stub that defers to the dev-sec-ops canonical doc. Low concern; noted because two top-level sections (source-control and CI-CD/security) both own "secrets" surface area.

---

## Finding 7 (MEDIUM) — Pull Requests guidance with strong cross-referencing (low duplication)

Topic: PR creation, description, template, size, reviewer/author guidance.

Files:
- docs/code-reviews/pull-requests.md (canonical PR guidance)
- docs/code-reviews/pull-request-template.md (canonical template)
- docs/documentation/guidance/pull-requests.md lines 1-11 (documenting PRs — links back to code-reviews canonical)
- docs/source-control/README.md lines 30-32 (links to code-reviews/pull-requests.md)
- docs/code-reviews/faq.md lines 7-22 (PR vs code review distinction)

Evidence — documentation/guidance/pull-requests.md lines 3-7 defers entirely:
> When we create [Pull Requests](../../code-reviews/pull-requests.md), we must ensure they are properly documented:
>   - [Pull Request Description](../../code-reviews/pull-requests.md#pull-request-description)
>   - [Pull Request Template](../../code-reviews/pull-request-template.md)

Classification: **XREF (good)**. This is the pattern the AI-assisted and CI/CD areas should follow: a single canonical owner with thin linking stubs elsewhere. Included as a positive contrast example.

---

## Finding 8 (MEDIUM) — Onboarding / first-week guidance scattered

Topic: Onboarding new team members; project first-week setup checklist.

Files:
- docs/the-first-week-of-an-ise-project.md (whole file: first-week setup checklist — branch naming, code style, build validation, DoD, standups, retro)
- docs/developer-experience/README.md lines 132-136 ("### Create an Onboarding Guide") + 36, 88-89
- docs/developer-experience/onboarding-guide-template.md (onboarding doc template)
- docs/engineering-fundamentals-checklist.md (overlapping checklist of fundamentals)

Evidence — developer-experience/README.md line 134:
> When welcoming new team members ... codebase, coding standards, team agreements, and team culture. By adopting a strong onboarding practice such as an onboarding guide ...

Evidence — onboarding-guide-template.md line 3 lists nearly the same contents: "engagement scope, team processes, codebase, coding standards, team agreements, software requirements and setup details."

Overlap: the-first-week-of-an-ise-project.md duplicates the same setup concerns (branch naming line 41, code style line 57, DoD line 58, standups line 50, retro line 75) that also appear in engineering-fundamentals-checklist.md (standup line 74, sprint planning line 86) and the agile team-agreements docs.

Classification: **PARTIAL**. onboarding-guide-template.md and developer-experience/README.md "Create an Onboarding Guide" overlap (template vs prose). the-first-week file and engineering-fundamentals-checklist overlap as two competing "setup checklist" entry points.

---

## Finding 9 (LOW-MEDIUM) — Agile ceremonies / team agreements: first-week + ML reference same anchors

Topic: Sprint planning, stand-ups, retrospectives, estimation, definition of done, working agreement.

Files:
- docs/agile-development/ceremonies.md (canonical: sprint planning, standup, estimation, retrospectives)
- docs/the-first-week-of-an-ise-project.md lines 16, 50, 75 (links into ceremonies.md anchors)
- docs/ml-and-ai-projects/agile-development-considerations-for-ml-projects.md lines 16-21, 27, 46 (links into ceremonies.md anchors)
- docs/agile-development/team-agreements/definition-of-done.md, working-agreement.md, team-manifesto.md (DoD/working agreement repeated across the three)

Evidence — ML agile considerations lines 16-21 link to the same ceremony anchors the first-week file links to (retrospectives, sprint-planning, stand-up, estimation).

Definition of Done appears as: definition-of-done.md (canonical), working-agreement.md line 35, team-manifesto.md line 51, backlog-management.md lines 7/13, ceremonies.md line 146, the-first-week line 15/58.

Classification: **XREF (good) for ML/first-week** (they link, not copy), but **PARTIAL** for DoD/working-agreement which is referenced and partially restated across 5+ agile sub-docs. ML agile doc is largely a thin adaptation layer that correctly defers to canonical agile docs.

---

## Finding 10 (LOW) — Observability / non-functional-requirements overlap

Topic: Performance testing, end-to-end tracing, telemetry/monitoring.

Files:
- docs/non-functional-requirements/performance.md line 30, capacity.md lines 26-32 (Performance Testing) → also docs/automated-testing/performance-testing/README.md (canonical)
- docs/observability/* (tracing, correlation-id, microservices, OpenTelemetry) repeat the same OpenTelemetry "end-to-end distributed transactions over heterogeneous components" blurb in 4 files:
  - observability/correlation-id.md line 30
  - observability/pillars/tracing.md line 22
  - observability/microservices.md line 55
  - observability/tools/OpenTelemetry.md lines 7, 53

Evidence: identical recommendation text "Consider using OpenTelemetry as it implements open-source cross-platform context propagation for end-to-end distributed transactions over heterogeneous components out-of-the-box" appears verbatim in correlation-id.md, tracing.md, and microservices.md.

Classification: **DUP (small, localized)** for the OpenTelemetry blurb; **XREF** for performance testing (NFR pages link to automated-testing/performance-testing).

---

## Finding 11 (LOW) — Threat modeling described in multiple security entry points

Topic: Threat modeling phases + AI threat-modeling considerations.

Files:
- docs/security/threat-modelling.md (canonical: phases, AI considerations lines 19-21)
- docs/security/threat-modelling-example.md (worked example)
- docs/security/README.md lines 15, 29 (AI threat list + link)
- docs/ai-assisted-engineering/README.md line 67 (same AI threat list)
- docs/developer-experience/copilots.md line 118 (links to threat-modelling AI anchor)

Classification: **PARTIAL/XREF**. threat-modelling.md is canonical; the AI threat enumeration is duplicated into security/README.md and ai-assisted-engineering/README.md rather than linked.

---

## Prioritized Summary (most significant first)

1. **AI-assisted engineering baseline** (Finding 2) — most pervasive; same principles re-stated across ai-assisted-engineering, copilots, automated-testing, security, source-control, code-reviews, CI-CD. Hub exists but spokes re-articulate instead of linking. Highest divergence risk.
2. **CI/CD "Fundamentals" lists** (Finding 1) — near-verbatim five-bullet duplication between CI-CD/README.md and agile-development/branching-and-cicd.md.
3. **Testing fundamentals taxonomy** (Finding 3) — unit/integration/e2e/performance + "no code without tests" repeated across automated-testing, CI-CD/continuous-integration, engineering-fundamentals-checklist, definition-of-done, maintainability, branching-and-cicd.
4. **Branching + PR-merge workflow** (Finding 4) and **merge-gate checklist** (Finding 5) — overlapping ownership across source-control (README + git-guidance), branching-and-cicd, CI-CD/continuous-integration, code-reviews.
5. **Onboarding / first-week / fundamentals checklist** (Finding 8) — multiple competing "setup checklist" + onboarding-guide entry points.
6. **Secrets management** (Finding 6), **threat modeling AI list** (Finding 11), **OpenTelemetry blurb** (Finding 10) — smaller, more localized.

Positive pattern to replicate: documentation/guidance/pull-requests.md (Finding 7) and the ML agile-considerations doc (Finding 9) — thin stubs that defer to a single canonical owner via links.

## Clarifying Questions
- None blocking. (If a follow-up consolidation is desired, the natural canonical owners are: CI-CD/README.md for CI/CD fundamentals, automated-testing/README.md for testing taxonomy, ai-assisted-engineering/README.md for AI baseline, code-reviews/pull-requests.md for PRs, source-control for branching.)

## Recommended Next Research (not completed this session)
- [ ] Quantify exact duplicated line counts per finding (diff-style) if a consolidation PR is planned.
- [ ] Check design/ (design-patterns, design-reviews) for testing/observability advice overlapping NFR and automated-testing.
- [ ] Review code-reviews/recipes/*.md language-specific files for repeated lint/unit-test boilerplate across languages.
- [ ] Inspect engineering-fundamentals-checklist.md fully against each section README to map every checklist item to its canonical guide.
