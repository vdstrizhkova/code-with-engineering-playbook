# Repository Content Catalog — Code-With Engineering Playbook

Status: Complete

Research date: 2026-06-16

## Research Topics / Questions

1. Walk the entire `docs/` tree; list every top-level section folder and subfolders.
2. Summarize each section: topics, key markdown files (workspace-relative paths), 1-2 sentence purpose from README.
3. Note rough size/depth (number of markdown files) per section.
4. Identify thematically related/overlapping sections.
5. Report current navigation structure from `mkdocs.yml` / `_config.yml`.
6. Read `docs/README.md` and `docs/engineering-fundamentals-checklist.md` for the intended organizing principle.

## Site / Build Configuration

- Site is built with **MkDocs + Material theme** (`mkdocs.yml` lines 1-37). `_config.yml` is a minimal Jekyll/GitHub-Pages fallback (`theme: jekyll-theme-slate`, includes CONTRIBUTING.md + LICENSE) and does NOT define navigation.
- Plugins: `search`, `git-revision-date-localized`, `awesome-pages` (`mkdocs.yml` lines 23-26). Theme features include `navigation.indexes` (so each folder `README.md` acts as a section index page).
- **Navigation is NOT hard-coded in `mkdocs.yml`.** It is driven by the `awesome-pages` plugin using `.pages` files plus folder/file ordering. Only three `.pages` files exist:
  - `docs/.pages` — top-level nav order.
  - `docs/automated-testing/.pages` — testing subsection order.
  - `docs/CI-CD/recipes/.pages` — CI/CD recipes order.
- The `- ...` token in each `.pages` file means "fill in remaining items here automatically" (alphabetical/file order), so most sub-navigation is implicit.

## Intended Organizing Principle

- `docs/README.md`: The site is the **"ISE Engineering Fundamentals Playbook"**. Core entry points: the **Engineering Fundamentals Checklist** and **The First Week of an ISE Project**. AI-Assisted Engineering is positioned as the shared baseline for AI tool use.
- `docs/engineering-fundamentals-checklist.md`: This checklist is the de-facto top-level taxonomy. Its sections map almost 1:1 onto the docs folders, in this order:
  1. Source Control → `source-control/`
  2. Work Item Tracking → `agile-development/backlog-management.md`
  3. Testing → `automated-testing/`
  4. CI/CD → `CI-CD/`
  5. AI-Assisted Engineering → `ai-assisted-engineering/`
  6. Security → `security/`
  7. Observability → `observability/`
  8. Agile/Scrum → `agile-development/`
  9. Design Reviews → `design/design-reviews/`
  10. Code Reviews → `code-reviews/`
  11. Retrospectives → `agile-development/ceremonies.md#retrospectives`
  12. Engineering Feedback → `engineering-feedback/`
  13. Developer Experience → `developer-experience/`
- Implication: "Engineering Fundamentals" is the intended top-level organizing principle; the checklist is the canonical index. Some checklist items (Work Item Tracking, Retrospectives, Design Reviews) are sub-pages inside larger sections, so the checklist order and the folder structure do not perfectly align — a restructure signal.

## Current Top-Level Navigation (`docs/.pages`)

Explicit order from `docs/.pages` (lines 1-9):

1. ISE Engineering Fundamentals Playbook → `README.md`
2. Engineering Fundamentals Checklist → `engineering-fundamentals-checklist.md`
3. The First Week of an ISE Project → `the-first-week-of-an-ise-project.md`
4. Who is ISE? → `ISE.md`
5. Agile Development → `agile-development/`
6. Automated Testing → `automated-testing/`
7. CI/CD → `CI-CD/`
8. `...` (awesome-pages fills remaining folders here, in file order):
   - `ai-assisted-engineering/`, `code-reviews/`, `design/`, `developer-experience/`,
     `documentation/`, `engineering-feedback/`, `ml-and-ai-projects/`,
     `non-functional-requirements/`, `observability/`, `resources/` (image only),
     `security/`, `source-control/`
9. UI/UX → `UI-UX/`

Note: `resources/` holds only `ms_icon.png` (no markdown) — it is theme assets, not a content section.

## Section Catalog

### 1. agile-development/  (~21 md files)
- Purpose: Agile/Scrum practices for the cross-functional delivery "Crew" — backlog, iterations, ceremonies, roles, team agreements; now includes AI tooling considerations.
- README: `docs/agile-development/README.md`
- Key files:
  - `docs/agile-development/backlog-management.md`
  - `docs/agile-development/ceremonies.md` (contains retrospectives anchor used by the checklist)
  - `docs/agile-development/roles.md`
  - `docs/agile-development/branching-and-cicd.md`  ← overlaps CI-CD + source-control
  - `docs/agile-development/async-collaboration-checklist.md`
  - `docs/agile-development/team-agreements/{definition-of-done,definition-of-ready,team-manifesto,working-agreement}.md`
  - `docs/agile-development/advanced-topics/backlog-management/{external-feedback,minimal-slices,risk-management}.md`
  - `docs/agile-development/advanced-topics/collaboration/{add-pairing-field-azure-devops-cards,pair-programming-tools,social-question,teaming-up,virtual-collaboration,why-collaboration}.md`
  - `docs/agile-development/advanced-topics/effective-organization/{delivery-plan,scrum-of-scrums}.md`

### 2. ai-assisted-engineering/  (1 md file)
- Purpose: Shared baseline for using AI tools in engineering while preserving human ownership, validation, security, privacy, accessibility, and governance. It is cross-linked from nearly every other section.
- README: `docs/ai-assisted-engineering/README.md` (the entire section is just this file)
- Note: This is a hub page that points outward to Developer Experience, Testing, Security, Observability, Source Control, Code Reviews, Documentation, and ML/AI. Heavy thematic overlap with `ml-and-ai-projects/` and `developer-experience/copilots.md`.

### 3. automated-testing/  (~24 md files)
- Purpose: Why/how to test; unit, integration, E2E, performance, and specialized testing types, with AI-assisted testing guidance.
- README: `docs/automated-testing/README.md`
- Has its own `.pages`: `docs/automated-testing/.pages`
- Key files / subfolders:
  - `docs/automated-testing/test-planning.md`
  - `docs/automated-testing/unit-testing/{README,authoring-example,custom-connector,mocking,tdd-example,why-unit-tests}.md`
  - `docs/automated-testing/integration-testing/README.md`
  - `docs/automated-testing/e2e-testing/{README,testing-comparison,testing-methods,recipes/gauge-framework,recipes/postman-testing}.md`
  - `docs/automated-testing/performance-testing/{README,iterative-perf-test-template,load-testing}.md`
  - `docs/automated-testing/{cdc-testing,fault-injection-testing,shadow-testing,smoke-testing,synthetic-monitoring-tests,ui-testing}/README.md`
  - `docs/automated-testing/ui-testing/teams-tests.md`
  - `docs/automated-testing/tech-specific-samples/{blobstorage-unit-tests/README,building-containers-with-azure-devops}.md`
  - `docs/automated-testing/templates/{case-study-template,test-type-template}.md`

### 4. CI-CD/  (~29 md files)
- Purpose: Continuous Integration & Continuous Delivery practices, DevSecOps, GitOps, and recipes (Terraform, GitHub Actions, secrets).
- README: `docs/CI-CD/README.md`
- Key files / subfolders:
  - `docs/CI-CD/continuous-integration.md`, `docs/CI-CD/continuous-delivery.md`
  - `docs/CI-CD/dev-sec-ops/{README,azure-devops-service-connection-security,dependency-and-container-scanning,evaluate-open-source-software,penetration-testing}.md`
  - `docs/CI-CD/dev-sec-ops/secrets-management/{README,credential_scanning,secrets_rotation,static-code-analysis}.md` + `recipes/{detect-secrets-ado,detect-secrets}.md`
  - `docs/CI-CD/gitops/{deploying-with-gitops,github-workflows}.md` + `secret-management/{README,azure-devops-secret-management-per-branch,secret-rotation-in-pods}.md`
  - `docs/CI-CD/recipes/` (has `.pages`): `cd-on-low-code-solutions.md`, `ci-pipeline-for-better-documentation.md`, `ci-with-jupyter-notebooks.md`, `inclusive-linting.md`, `reusing-devcontainers-within-a-pipeline.md`, `github-actions/runtime-variables/README.md`, `terraform/{save-output-to-variable-group,share-common-variables-naming-conventions,terraform-structure-guidelines}.md`

### 5. code-reviews/  (~22 md files)
- Purpose: Peer code review goals, process guidance, author/reviewer roles, language-specific recipes, plus reviewing AI-assisted changes as untrusted code.
- README: `docs/code-reviews/README.md`
- Key files / subfolders:
  - `docs/code-reviews/pull-requests.md`, `docs/code-reviews/pull-request-template.md`
  - `docs/code-reviews/faq.md`, `docs/code-reviews/tools.md`, `docs/code-reviews/inclusion-in-code-review.md`
  - `docs/code-reviews/process-guidance/{README,author-guidance,reviewer-guidance}.md`
  - `docs/code-reviews/evidence-and-measures/README.md`
  - `docs/code-reviews/recipes/{azure-pipelines-yaml,bash,csharp,go,java,javascript-and-typescript,markdown,python,terraform}.md`

### 6. design/  (~36 md files — largest section)
- Purpose: Software/architecture design practices: design patterns, design reviews, decision logs (ADRs), trade studies, diagram types, sustainability, exception handling.
- README: `docs/design/readme.md` (lowercase filename — inconsistent with other sections' `README.md`)
- Key files / subfolders:
  - `docs/design/exception-handling.md`
  - `docs/design/design-patterns/{README,cloud-resource-design-guidance,data-heavy-design-guidance,distributed-system-design-reference,network-architecture-guidance-for-azure,network-architecture-guidance-for-hybrid,non-functional-requirements-capture-guide,object-oriented-design-reference,rest-api-design-guidance}.md`
  - `docs/design/design-reviews/README.md` + `recipes/` (async-design-reviews, engagement-process, engineering-feasibility-spikes, high-level-design-recipe, milestone-epic-design-review-recipe, preferred-diagram-tooling, technical-spike + `templates/`) + `decision-log/` (ADRs + memory example) + `trade-studies/{README,template}.md`
  - `docs/design/diagram-types/{README,class-diagrams,component-diagrams,deployment-diagrams,sequence-diagrams}.md`
  - `docs/design/sustainability/{README,sustainable-action-disclaimers,sustainable-engineering-principles}.md`
- Note: `non-functional-requirements-capture-guide.md` lives here but a whole `non-functional-requirements/` section also exists (overlap).

### 7. developer-experience/  (~10 md files)
- Purpose: Inner-loop developer experience — build/test/start/debug ease, devcontainers, local pipelines, fake services, Copilots/AI tooling, onboarding.
- README: `docs/developer-experience/README.md`
- Key files:
  - `docs/developer-experience/copilots.md` (AI-assisted authorship + team operating model; cross-linked from source-control & ai-assisted-engineering)
  - `docs/developer-experience/{client-app-inner-loop,cross-platform-tasks,devcontainers-getting-started,devcontainers-going-further,execute-local-pipeline-with-docker,fake-services-inner-loop,onboarding-guide-template,toggle-vnet-dev-environment}.md`

### 8. documentation/  (~21 md files)
- Purpose: Why/how to document projects; best practices, guidance per artifact type (code, PRs, REST APIs, work items, engineering feedback), recipes (MkDocs, DocFx, wiki sync), and tools.
- README: `docs/documentation/README.md`
- Key files / subfolders:
  - `docs/documentation/best-practices/{automation,establish-and-manage,good-documentation}.md`
  - `docs/documentation/guidance/{code,engineering-feedback,project-and-repositories,pull-requests,rest-apis,work-items}.md`
  - `docs/documentation/recipes/{deploy-docfx-azure-website,static-website-with-mkdocs,sync-wiki-between-repos,using-docfx-and-tools}.md`
  - `docs/documentation/tools/{automation,integrations,languages,wikis}.md`
- Note: `guidance/engineering-feedback.md`, `guidance/pull-requests.md`, `guidance/rest-apis.md`, `guidance/work-items.md` overlap with `engineering-feedback/`, `code-reviews/`, `design/design-patterns/rest-api-design-guidance.md`, and `agile-development/backlog-management.md` respectively.

### 9. engineering-feedback/  (4 md files)
- Purpose: How/why/when to submit "voice of the customer" Microsoft Engineering Feedback, with examples, FAQ, and AI tooling feedback categories.
- README: `docs/engineering-feedback/README.md`
- Key files: `docs/engineering-feedback/{feedback-examples,feedback-faq,feedback-guidance}.md`

### 10. ml-and-ai-projects/  (~15 md files)
- Purpose: Machine Learning / AI engineering fundamentals across the ML lifecycle (envisioning, data exploration, experimentation, MLOps, Responsible AI), now extended to generative AI / agentic systems.
- README: `docs/ml-and-ai-projects/README.md`
- Key files:
  - `docs/ml-and-ai-projects/{ml-fundamentals-checklist,ml-model-checklist}.md`
  - `docs/ml-and-ai-projects/{envisioning-and-problem-formulation,envisioning-summary-template,feasibility-studies,data-exploration,model-experimentation,proposed-ml-process}.md`
  - `docs/ml-and-ai-projects/{agile-development-considerations-for-ml-projects,tpm-considerations-for-ml-projects}.md`  ← overlap with agile-development
  - `docs/ml-and-ai-projects/{profiling-ml-and-mlops-code,testing-data-science-and-mlops-code}.md`  ← overlap with automated-testing & observability/profiling
  - `docs/ml-and-ai-projects/{responsible-ai,generative-ai-and-agentic-systems}.md`  ← overlap with ai-assisted-engineering
- Note: Strong thematic overlap with `ai-assisted-engineering/` and `observability/ml-observability.md`.

### 11. non-functional-requirements/  (~19 md files)
- Purpose: Catalog of quality attributes / NFRs (accessibility, availability, capacity, compliance, performance, privacy, reliability, scalability, etc.). Flat file-per-attribute layout.
- README: **None at section root** (no `docs/non-functional-requirements/README.md`); only `privacy/README.md` exists. Entry is via individual files.
- Key files:
  - `docs/non-functional-requirements/{accessibility,availability,capacity,compliance,data-integrity,disaster-recovery,internationalization,interoperability,maintainability,performance,portability,reliability,scalability,usability}.md`
  - `docs/non-functional-requirements/privacy/{README,data-handling,privacy-frameworks}.md`
- Note: Overlaps `design/design-patterns/non-functional-requirements-capture-guide.md`, `automated-testing/performance-testing/`, and `security/` (compliance/privacy). UI-UX README deep-links into accessibility/usability/maintainability here.

### 12. observability/  (~26 md files)
- Purpose: Building observable systems — pillars (logs/metrics/tracing), dashboards, best practices, tooling, observability-as-code, and domain-specific observability (microservices, ML, Databricks, pipelines).
- README: `docs/observability/README.md`
- Key files:
  - `docs/observability/pillars/{logging,metrics,tracing,dashboard}.md`
  - `docs/observability/{log-vs-metric-vs-trace,best-practices,alerting,correlation-id,diagnostic-tools,pitfalls,profiling,recipes-observability,observability-as-code,observability-pipelines}.md`
  - `docs/observability/{microservices,ml-observability,observability-databricks,logs-privacy}.md`
  - `docs/observability/tools/{README,KubernetesDashboards,OpenTelemetry,Prometheus,loki}.md`
- Note: `ml-observability.md` overlaps ml-and-ai-projects; `logs-privacy.md` overlaps non-functional-requirements/privacy; `profiling.md` overlaps ml profiling.

### 13. resources/  (0 md files)
- Contents: `docs/resources/ms_icon.png` only. Theme/branding asset, not a content section. Listed in nav by awesome-pages `...` but renders empty.

### 14. security/  (4 md files)
- Purpose: Secure design/implementation per OWASP Top 10; security review rules of engagement; threat modelling; AI/agent security.
- README: `docs/security/README.md`
- Key files: `docs/security/{rules-of-engagement,threat-modelling,threat-modelling-example}.md`
- Note: Major secrets/DevSecOps content actually lives under `CI-CD/dev-sec-ops/` (overlap); compliance/privacy split with `non-functional-requirements/`.

### 15. source-control/  (7 md files)
- Purpose: Git/source-control practices — repo creation, branching, merge strategies, naming, component versioning, secrets management, with AI-assisted traceability links.
- README: `docs/source-control/README.md`
- Key files:
  - `docs/source-control/{component-versioning,merge-strategies,naming-branches,secrets-management}.md`
  - `docs/source-control/git-guidance/{README,git-lfs-and-vfs}.md`
- Note: `secrets-management.md` overlaps `CI-CD/dev-sec-ops/secrets-management/`; branching overlaps `agile-development/branching-and-cicd.md` and `CI-CD/`.

### 16. UI-UX/  (2 md files)
- Purpose: User interface / front-end / web development guidance; mostly pointers into non-functional-requirements (accessibility, usability, maintainability) and recommended technologies.
- README: `docs/UI-UX/README.md`
- Key files: `docs/UI-UX/recommended-technologies.md`

## Top-Level Loose Files (not in a section)
- `docs/README.md` — playbook landing page.
- `docs/engineering-fundamentals-checklist.md` — canonical taxonomy/checklist.
- `docs/the-first-week-of-an-ise-project.md` — sprint-structured walkthrough that links across all sections.
- `docs/ISE.md` — "Who is ISE?".

## Approximate Size / Depth Ranking
1. design/ — ~36 (deepest: design-reviews has recipes/templates/decision-log/trade-studies)
2. CI-CD/ — ~29 (deep: dev-sec-ops + gitops + recipes/terraform)
3. observability/ — ~26
4. automated-testing/ — ~24
5. code-reviews/ — ~22
6. documentation/ — ~21
7. agile-development/ — ~21
8. non-functional-requirements/ — ~19
9. ml-and-ai-projects/ — ~15
10. developer-experience/ — ~10
11. source-control/ — 7
12. engineering-feedback/ — 4
13. security/ — 4
14. UI-UX/ — 2
15. ai-assisted-engineering/ — 1
16. resources/ — 0 (image asset only)

## Thematically Related / Overlapping Clusters (duplication candidates)

1. **Secrets / DevSecOps / credential management** (split across 3+ locations):
   - `docs/CI-CD/dev-sec-ops/secrets-management/` (README, credential_scanning, secrets_rotation, static-code-analysis, recipes/detect-secrets*)
   - `docs/CI-CD/gitops/secret-management/`
   - `docs/source-control/secrets-management.md`
   - `docs/security/` (high-level OWASP) — links out to CI-CD secrets pages

2. **Security / Compliance / Privacy** (split across security, NFR, observability):
   - `docs/security/` (OWASP, threat modelling)
   - `docs/non-functional-requirements/{compliance,privacy/*}.md`
   - `docs/observability/logs-privacy.md`

3. **AI / ML guidance** (largest overlap cluster):
   - `docs/ai-assisted-engineering/README.md` (cross-cutting hub)
   - `docs/ml-and-ai-projects/` (lifecycle, responsible-ai, generative-ai-and-agentic-systems)
   - `docs/developer-experience/copilots.md` (AI authorship/operating model)
   - `docs/observability/ml-observability.md`
   - Plus "AI tooling" subsections injected into nearly every README (agile, testing, code-reviews, design, documentation, security, UI-UX, engineering-feedback).

4. **Testing** (core + scattered):
   - `docs/automated-testing/` (canonical)
   - `docs/ml-and-ai-projects/testing-data-science-and-mlops-code.md`
   - `docs/security/` security testing + `CI-CD/dev-sec-ops/penetration-testing.md`
   - `docs/automated-testing/performance-testing/` vs `docs/non-functional-requirements/performance.md`

5. **CI/CD ⇄ Source Control ⇄ Agile branching**:
   - `docs/CI-CD/` + `docs/agile-development/branching-and-cicd.md` + `docs/source-control/{naming-branches,merge-strategies}.md`

6. **Non-Functional Requirements** (defined in two homes):
   - `docs/non-functional-requirements/*` (per-attribute catalog)
   - `docs/design/design-patterns/non-functional-requirements-capture-guide.md`
   - `docs/UI-UX/README.md` deep-links into NFR accessibility/usability/maintainability

7. **Documentation guidance ⇄ owning sections**:
   - `docs/documentation/guidance/pull-requests.md` ⇄ `docs/code-reviews/pull-requests.md`
   - `docs/documentation/guidance/engineering-feedback.md` ⇄ `docs/engineering-feedback/`
   - `docs/documentation/guidance/rest-apis.md` ⇄ `docs/design/design-patterns/rest-api-design-guidance.md`
   - `docs/documentation/guidance/work-items.md` ⇄ `docs/agile-development/backlog-management.md`

8. **Profiling / performance**:
   - `docs/observability/profiling.md` ⇄ `docs/ml-and-ai-projects/profiling-ml-and-mlops-code.md` ⇄ `docs/automated-testing/performance-testing/`

9. **Agile considerations duplicated for ML**:
   - `docs/agile-development/` ⇄ `docs/ml-and-ai-projects/agile-development-considerations-for-ml-projects.md` + `tpm-considerations-for-ml-projects.md`

## Structural Inconsistencies Noted (restructure signals)
- `docs/design/readme.md` is lowercase while every other section uses `README.md`.
- `docs/non-functional-requirements/` has no section-root README (only `privacy/README.md`), unlike all other sections.
- `docs/resources/` appears in nav but has no content (image asset only).
- Checklist order (engineering-fundamentals-checklist.md) treats Work Item Tracking, Retrospectives, and Design Reviews as top-level fundamentals, but in the folder tree they are sub-pages of `agile-development/` and `design/`.
- AI guidance is both a standalone section (`ai-assisted-engineering/`) and inlined into nearly every other section README — a deliberate cross-link pattern but a heavy duplication surface.

## Clarifying Questions (none blocking)
- None — task was fully answerable from the repository. (Open design question for the later restructure: should the top-level nav be reordered to match the engineering-fundamentals-checklist order, and should overlapping clusters above be consolidated or cross-linked?)

## Recommended Next Research (not done this session)
- [ ] Build a link/back-reference graph to quantify how often each "owning" page is duplicated vs cross-linked (e.g., grep inbound links to secrets-management pages).
- [ ] Diff the actual prose of overlapping pairs (e.g., source-control/secrets-management.md vs CI-CD/dev-sec-ops/secrets-management/README.md) to determine true duplication vs complementary content.
- [ ] Inspect `the-first-week-of-an-ise-project.md` in full to map its sprint-based ordering against the checklist and folder structure.
- [ ] Confirm whether any `.pages` `...` expansion produces a confusing nav order (e.g., resources/ empty entry, ml-and-ai-projects placement).
