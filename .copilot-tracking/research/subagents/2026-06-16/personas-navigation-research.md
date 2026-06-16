# Personas & Navigation Research — Code-With Engineering Playbook

Status: Complete

## Research Topics / Questions

1. Who is the audience and stated purpose of the playbook?
2. For each of three personas — (1) Software Engineer, (2) Project Manager / Engineering Lead, (3) Data Scientist / ML Engineer — which existing `docs/` sections are most relevant? Where do sections serve multiple personas?
3. What navigation pain points exist (persona entry points, scattered guides, "start here" paths, deep nesting, inconsistent folder casing)?
4. Is there existing role/persona-oriented content?
5. What documentation IA patterns suit a multi-persona engineering playbook (Diátaxis, persona landing pages, "start here")?

## 1. Audience & Stated Purpose

Sources read: `README.md` (repo root), `docs/README.md`, `docs/ISE.md`, `docs/the-first-week-of-an-ise-project.md`, `docs/engineering-fundamentals-checklist.md`, `mkdocs.yml`, `docs/.pages`.

- Site identity: "ISE Engineering Fundamentals Playbook" (MkDocs Material site at https://microsoft.github.io/code-with-engineering-playbook).
- Audience stated explicitly in root `README.md`: "An engineer **or data scientist** working on an ISE project..." — confirms at least two of the three personas are first-class.
- Purpose (both READMEs): increase team efficiency, reduce mistakes/pitfalls, share experience. Engineers are expected to "know their playbook... fix it... share it."
- Primary entry artifacts the playbook itself promotes as starting points:
  - `docs/engineering-fundamentals-checklist.md` — "If you do nothing else, follow the checklist."
  - `docs/the-first-week-of-an-ise-project.md` — sequences the playbook by Agile sprint cadence (Before project / Day 1–5).
  - `docs/ai-assisted-engineering/README.md` — shared baseline for AI tool use.
- `docs/ISE.md` — context on who the ISE team is (no persona structure; background only).

### Audience observations

- The playbook is **role-aware in prose but not in navigation**. The root README even splits content into "Engineering Fundamentals" vs. "Fundamentals for Specific Technology Areas" (ML/AI, UI), hinting at a latent specialization split that the nav does not expose.
- `the-first-week-of-an-ise-project.md` is effectively a **task/workflow-oriented onboarding path** (closest thing to a "start here" sequence), but it is framed for the whole team at once rather than per persona.

## 2. Persona → Section Mapping

Folder inventory under `docs/` (top-level): `agile-development`, `ai-assisted-engineering`, `automated-testing`, `CI-CD`, `code-reviews`, `design`, `developer-experience`, `documentation`, `engineering-feedback`, `ml-and-ai-projects`, `non-functional-requirements`, `observability`, `security`, `source-control`, `UI-UX`, `resources`, plus root pages (`README.md`, `engineering-fundamentals-checklist.md`, `the-first-week-of-an-ise-project.md`, `ISE.md`).

Relevance legend: ●●● primary / core, ●●○ secondary, ●○○ occasional.

| Section (docs/) | Software Engineer | Project Manager / Eng Lead | Data Scientist / ML Engineer | Notes |
|---|---|---|---|---|
| `source-control/` | ●●● | ●○○ | ●●○ | Core dev workflow; DS needs it but lighter. Cross-cutting baseline. |
| `code-reviews/` | ●●● | ●●○ | ●●○ | PM cares about process/policy; DS reviews notebooks/MLOps code. |
| `automated-testing/` | ●●● | ●○○ | ●●○ | DS path: `testing-data-science-and-mlops-code`, AI eval testing. |
| `CI-CD/` | ●●● | ●○○ | ●●○ | Shared; DS overlaps via MLOps deployment. Casing outlier (`CI-CD`). |
| `security/` | ●●● | ●●○ | ●●○ | Shared baseline; PM owns risk; DS needs AI/agent security. |
| `design/` | ●●● | ●●○ | ●●○ | Design reviews + non-functional capture cut across all three. |
| `observability/` | ●●● | ●○○ | ●●○ | Shared; DS via AI observability section. |
| `developer-experience/` | ●●● | ●○○ | ●●○ | Inner-loop, devcontainers; DS benefits too. |
| `non-functional-requirements/` | ●●○ | ●●○ | ●●○ | Cross-cutting (accessibility, privacy). Serves all. |
| `documentation/` | ●●○ | ●●● | ●●○ | Process + recipes; PM-relevant for project docs. Cross-cutting. |
| `agile-development/` | ●●○ | ●●● | ●●○ | PM **primary**: ceremonies, backlog, roles, team-agreements, scrum-of-scrums. |
| `engineering-feedback/` | ●●○ | ●●● | ●●○ | PM/lead-driven feedback loop to Microsoft product teams. |
| `engineering-fundamentals-checklist.md` | ●●● | ●●● | ●●○ | Shared "do this first" artifact for all personas. |
| `the-first-week-of-an-ise-project.md` | ●●○ | ●●● | ●●○ | PM/lead-oriented project kickoff sequence; serves as de-facto onboarding. |
| `ai-assisted-engineering/` | ●●● | ●●○ | ●●● | Cross-cutting baseline; explicitly shared by Eng + DS. |
| `ml-and-ai-projects/` | ●○○ | ●●○ | ●●● | DS **primary**: ML lifecycle, data-exploration, responsible-ai, MLOps, gen-AI/agents. Contains its own PM guide (`tpm-considerations-for-ml-projects`). |
| `UI-UX/` | ●●○ | ●○○ | ●○○ | Specialist track (UI engineers); narrow audience. |
| `ISE.md` | ●○○ | ●○○ | ●○○ | Org background; not persona-specific. |
| `resources/` | ●○○ | ●○○ | ●○○ | Assets/images; non-navigational. |

### Persona summaries

- **Software Engineer (primary owner of most sections):** core path = `source-control` → `code-reviews` → `automated-testing` → `CI-CD` → `security` → `design` → `observability` → `developer-experience`, with `ai-assisted-engineering` as the shared baseline. This is essentially the bulk of the site.
- **Project Manager / Engineering Lead:** primary path = `agile-development` (ceremonies, backlog-management, roles, team-agreements, advanced-topics/effective-organization), `engineering-feedback`, `the-first-week-of-an-ise-project`, `engineering-fundamentals-checklist`, plus `documentation`. Also cares about *process* facets of code-reviews, security, design (governance/risk), and the ML PM guide.
- **Data Scientist / ML Engineer:** primary path = `ml-and-ai-projects` (envisioning, feasibility, data-exploration, model-experimentation, responsible-ai, MLOps/testing, generative-ai-and-agentic-systems) + `ai-assisted-engineering`, layered on shared engineering fundamentals (`source-control`, `automated-testing`, `CI-CD`, `security`, `observability`).

### Cross-cutting / shared sections

`ai-assisted-engineering`, `engineering-fundamentals-checklist`, `non-functional-requirements`, `security`, `documentation`, `design` (design reviews) serve all three personas. `ml-and-ai-projects` deliberately links back into shared Engineer sections (Testing, Security, Observability) for AI-enabled work, and even embeds a PM sub-guide — evidence the personas already overlap inside content but not in nav.

## 3. Navigation Pain Points

Evidence: `docs/.pages` nav block and `mkdocs.yml`.

- **Nav is purely topic-based and alphabetical, with no persona entry points.** `docs/.pages` pins a few top items then uses `...` (awesome-pages) to auto-list everything else alphabetically:
  ```yaml
  nav:
    - ISE Engineering Fundamentals Playbook: README.md
    - Engineering Fundamentals Checklist: engineering-fundamentals-checklist.md
    - The First Week of an ISE Project: the-first-week-of-an-ise-project.md
    - Who is ISE?: ISE.md
    - Agile Development: agile-development
    - Automated Testing: automated-testing
    - CI/CD: CI-CD
    - ...
    - UI/UX: UI-UX
  ```
  There is no "For Engineers / For Leads / For Data Scientists" grouping; a reader must already know the topic taxonomy to find their path.
- **No per-persona "start here."** The only onboarding-style page is `the-first-week-of-an-ise-project.md`, which mixes all roles into one sprint timeline. There is no landing page that says "If you are a Data Scientist, start here." The root README's split into "Engineering Fundamentals" vs "Fundamentals for Specific Technology Areas" is the closest signal but lives outside the nav sidebar.
- **Related guides are scattered across siblings.** AI guidance is split across `ai-assisted-engineering/`, `ml-and-ai-projects/` (generative-ai-and-agentic-systems, responsible-ai), and AI sub-sections inside `security`, `observability`, and `automated-testing`. PM/lead guidance is split across `agile-development/`, `engineering-feedback/`, `the-first-week-of-an-ise-project.md`, and `ml-and-ai-projects/tpm-considerations-for-ml-projects.md`. A persona must hop between top-level peers.
- **Inconsistent folder naming / casing.** Top-level folders mix conventions: `CI-CD` and `UI-UX` (uppercase + hyphen) vs. `ml-and-ai-projects`, `ai-assisted-engineering`, `agile-development` (lowercase-kebab). Sub-folders also drift: `design/diagram-types/Images` and `design/.../decision-log/examples/memory/Architecture` use capitalized folder names while peers use lowercase `images`. Also `docs/design/readme.md` is lowercase while most use `README.md`. This is cosmetic but signals lack of a naming standard and affects URL consistency.
- **Deep nesting in places.** Directory depth histogram (levels below repo root): depth 4 = 8 dirs, depth 5 = 3, depth 6 = 3. Deepest paths are under `design/design-reviews/decision-log/examples/memory/{Architecture,Deployment,trade-studies}` and `CI-CD/recipes/github-actions/runtime-variables/images`. These are example/recipe trees, so deep nesting is tolerable, but `design/design-reviews/decision-log/...` buries reusable artifacts far from where a lead/engineer would look.
- **`navigation.indexes` enabled but no persona index pages exist.** `mkdocs.yml` enables `navigation.indexes` and `awesome-pages`, so the infrastructure to add section landing/index pages (and therefore persona landing pages) is already present and unused for personas.

## 4. Existing Role/Persona-Oriented Content

- `docs/agile-development/roles.md` — defines Agile/Scrum roles (Product Owner, Scrum Master / "Process Lead", Development Team) via links to scrumguides.org. This is the only explicit *role* page, and it is Agile-role-based (not reader-persona-based).
- `docs/ml-and-ai-projects/tpm-considerations-for-ml-projects.md` — a PM/TPM-targeted guide nested inside the DS section (persona content embedded under a topic).
- Root `README.md` "Fundamentals for Specific Technology Areas" (ML/AI, UI) — implicit specialization grouping, not surfaced in site nav.
- No `personas/`, `start-here/`, or "by role" landing pages exist anywhere under `docs/`.

## 5. IA Patterns for a Multi-Persona Restructure

External reference: [Diátaxis](https://diataxis.fr/) — organizes docs by the four *user needs*: tutorials (learning), how-to guides (task/goal), reference (information), explanation (understanding). Adopted by Cloudflare, Gatsby, Vonage. Relevant because the playbook today is mostly **explanation + how-to** with little tutorial/reference separation.

Options relevant to this repo:

- **Persona-based landing pages (recommended primary).** Add `docs/start-here/` (or top-of-nav) landing pages: "For Software Engineers", "For Project Managers / Eng Leads", "For Data Scientists / ML Engineers". Each curates an ordered reading path into existing topic sections (no content moves required). Low risk, leverages `navigation.indexes` already enabled. Mirrors the root README's latent split.
- **"Start here" / onboarding path per persona.** Generalize `the-first-week-of-an-ise-project.md` into per-persona quick-start checklists, or add a persona selector at the top. Keeps the strong existing sprint-sequenced content but makes the entry role-aware.
- **Diátaxis overlay.** Keep topic sections but tag/group content within them by need (e.g., separate "how-to recipes" from "explanation/principles"). The repo already has `recipes/` and `templates/` folders (in `automated-testing`, `CI-CD`, `code-reviews`, `documentation`, `design`) — a partial how-to/reference split exists and could be made consistent.
- **Hybrid (recommended overall): persona landing pages as an *entry layer* over the existing topic-based IA.** Personas are an access/orientation layer; topics remain the canonical home for content (avoids duplication and content churn). Add cross-links from each persona page into shared/cross-cutting sections, and consolidate scattered AI guidance via "see also" links rather than moving files.
- **Naming/casing normalization (supporting task).** Standardize top-level folder casing (e.g., decide on lowercase-kebab; `CI-CD`→`ci-cd`, `UI-UX`→`ui-ux`) and `images`/`README.md` casing. Note: renaming changes published URLs — would need redirects (`mkdocs-redirects`) to avoid breaking inbound links; treat as optional/secondary.

## Key Discoveries (Evidence Summary)

- The playbook explicitly names engineers and data scientists as its audience (root `README.md`), and separates ML/AI + UI as "specific technology areas" — but the **nav exposes none of this persona/specialization structure**; it is flat, topic-based, alphabetical (`docs/.pages` + `...`).
- A de-facto onboarding path exists (`the-first-week-of-an-ise-project.md`) but is team-wide, not per-persona.
- Persona content already overlaps inside topics (PM guide inside `ml-and-ai-projects`; AI guidance split across 4+ sections), confirming that an **entry/orientation layer** would help more than restructuring content.
- Infrastructure for landing pages already exists (`navigation.indexes`, `awesome-pages`) and is unused for personas.
- Folder casing is inconsistent (`CI-CD`/`UI-UX` vs kebab-case; `Images`/`images`; `readme.md`/`README.md`).

## Clarifying Questions

- Should a restructure prioritize a **non-destructive entry layer** (persona landing pages + curated paths, no file moves) over a **full IA reorganization** (renames/moves with redirects)? The former is far lower risk for a published site with external inbound links.
- Are there personas beyond the three named (e.g., UX/UI Engineer, Cloud/Infra/DevOps Engineer) that should get first-class entry points, given `UI-UX/` and `CI-CD/dev-sec-ops/` exist?
- Is changing published URLs acceptable (folder casing normalization), or must existing links be preserved via redirects?

## Recommended Next Research (not completed)

- [ ] Inventory every cross-persona "see also" link already present in section READMEs to quantify existing interconnection density.
- [ ] Audit `recipes/`/`templates/` folders across sections to assess feasibility of a consistent Diátaxis how-to/reference split.
- [ ] Check whether `mkdocs-redirects` (or equivalent) is configured/available before proposing any folder renames.
- [ ] Review analytics (if available) to validate which sections each persona actually visits most.
