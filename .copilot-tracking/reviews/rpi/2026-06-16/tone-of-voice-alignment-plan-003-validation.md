<!-- markdownlint-disable-file -->
# RPI Validation: Tone-of-Voice Alignment — Phase 3 (Dense Enumeration Pages)

**Plan**: .copilot-tracking/plans/2026-06-16/tone-of-voice-alignment-plan.instructions.md
**Details**: .copilot-tracking/details/2026-06-16/tone-of-voice-alignment-details.md (Phase 3 = lines 76-108)
**Changes Log**: .copilot-tracking/changes/2026-06-16/tone-of-voice-alignment-changes.md
**Research/Rubric**: .copilot-tracking/research/2026-06-16/tone-of-voice-alignment-research.md
**Planning Log**: .copilot-tracking/plans/logs/2026-06-16/tone-of-voice-alignment-log.md
**Phase**: 3 — Dense Enumeration Pages (Steps 3.1–3.5)
**Validation date**: 2026-06-16
**Status**: Pass-with-minor

## Scope

Phase 3 covers five "dense enumeration" pages where long comma stacks and back-to-back
bare lists were to receive connective prose and splitting — TONE ONLY, no recommendation,
heading, link, or anchor changed except recorded deviations DD-02 and DD-03. Evidence below
is from working-tree edits (`git diff HEAD`).

## Voice Rubric (acceptance standard)

First-person plural / direct "you"; rationale before directive; framing sentence before
lists; max ~4 comma-separated items per bullet; mentoring/hedged tone; no list-after-list
without connective prose.

## Step-by-Step Comparison

### Step 3.1 — docs/security/threat-modelling.md

* **Plan/changes claim**: voiced "we" lead-in before each of the three lists; 13-item
  "Common controls include…" run-on split into FOUR themed groups (DD-02); preserve
  `#ai-systems-threat-modeling-considerations` and every risk item.
* **Verified**:
  * Three lead-ins now "we"-voiced — [docs/security/threat-modelling.md](docs/security/threat-modelling.md#L23) ("As we model AI systems, we give extra attention…"), [#L34](docs/security/threat-modelling.md#L34) ("We also make sure the data-flow diagram names…"), [#L43](docs/security/threat-modelling.md#L43) ("As we walk each boundary, we ask questions like these…"). Rubric: rationale-first, mentoring "we". ✓
  * Controls run-on replaced by 4 themed sub-bullets — [#L55-L58](docs/security/threat-modelling.md#L55-L58). Each group ≤4 items.
  * Heading intact at [#L19](docs/security/threat-modelling.md#L19) → anchor `#ai-systems-threat-modeling-considerations` preserved. ✓
  * **DD-02 control accounting (13/13 present, none dropped)**:
    1. prompt and tool schema review → Input/output handling
    2. strict input and output validation → Input/output handling
    3. security-trimmed retrieval → Input/output handling
    4. sensitive data redaction → Input/output handling
    5. least-privilege tools → Least privilege
    6. user-context authorization → Least privilege
    7. human approval for privileged or irreversible actions → Least privilege
    8. rate limits → Operational safety
    9. circuit breakers → Operational safety
    10. dry-run modes for write paths → Operational safety
    11. audit logs → Operational safety
    12. rollback paths for prompts and indexes → Recovery and follow-up
    13. retesting after red-team findings are fixed → Recovery and follow-up
  * Risk-category, asset, and prompt list items unchanged (diff touches only lead-in lines). ✓
* **Result**: PASS. DD-02 confirmed — four groups, zero controls dropped.

### Step 3.2 — docs/ml-and-ai-projects/responsible-ai.md

* **Plan/changes claim**: one "we"-voiced framing sentence under each of the five question
  subsections; keep question format and all four cross-links.
* **Verified**:
  * Exactly five framing sentences added, one per subsection — [#L43](docs/ml-and-ai-projects/responsible-ai.md#L43), [#L53](docs/ml-and-ai-projects/responsible-ai.md#L53), [#L64](docs/ml-and-ai-projects/responsible-ai.md#L64), [#L73](docs/ml-and-ai-projects/responsible-ai.md#L73), [#L84](docs/ml-and-ai-projects/responsible-ai.md#L84). All first-person plural ("We ask these questions early…", "Whenever the system accepts untrusted input…", "Before we let an agent act…", "As we decide what to store…", "Once the system is live…"). ✓
  * Question bullets unchanged (diff adds only the framing lines + blank line).
  * Cross-links intact: threat-modelling [#L60](docs/ml-and-ai-projects/responsible-ai.md#L60), privacy + ml-observability [#L80](docs/ml-and-ai-projects/responsible-ai.md#L80), model-experimentation + test-planning [#L91](docs/ml-and-ai-projects/responsible-ai.md#L91), generative-ai + AI-Assisted Engineering [#L39](docs/ml-and-ai-projects/responsible-ai.md#L39). None modified. ✓
* **Result**: PASS.

### Step 3.3 — docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md

* **Plan/changes claim**: vary repetitive "Use [X] to…" openers; keep checklists; preserve
  `#review-the-system-across-disciplines` heading/anchor and all links. Lowest-risk Tier A
  page (DD-01 lighter treatment).
* **Verified**:
  * Ten bullets re-opened with ten distinct verbs — Lean on / Turn to / Let / Run / Plan with /
    Treat / Reach for / Check / Revisit / Bring … in — [#L69-L78](docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md#L69-L78). ✓
  * Heading intact at [#L65](docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md#L65) → anchor `#review-the-system-across-disciplines` preserved. ✓
  * Every link target unchanged (only the leading verb/preposition reworded; URLs byte-identical). ✓
* **Result**: PASS. See Minor-01 (comma stacks retained by design).

### Step 3.4 — docs/observability/README.md

* **Plan/changes claim**: split the 11-item capture mega-bullet into 3 grouped bullets
  (request context / operational signals / safety signals), each ≤4; keep surrounding
  bullets and shared-guide link.
* **Verified**:
  * Three grouped bullets — [#L41-L43](docs/observability/README.md#L41-L43): request context (model/provider/version; prompt template version; retrieval source IDs; tool calls = 4), operational (latency; token or cost; error rates; fallback paths = 4), safety (refusal rates; safety outcomes; escalation rates = 3). Each ≤4. ✓
  * **All 11 original items present**: model/provider/version, prompt template version, retrieval source IDs, tool calls, latency, token/cost, error rates, fallback paths, refusal rates, safety outcomes, escalation rates. ✓
  * Surrounding bullets and AI-Assisted Engineering shared-guide link [#L49](docs/observability/README.md#L49) untouched. ✓
* **Result**: PASS.

### Step 3.5 — docs/CI-CD/README.md

* **Plan/changes claim**: lead artifact paragraph with the principle then list six artifacts
  as a short sub-list; tighten the two added checklist items (DD-03 condenses one
  enumeration); preserve both deep links.
* **Verified**:
  * Principle-first sentence + 3-bullet sub-list — [#L65-L69](docs/CI-CD/README.md#L65-L69). All six artifacts retained (Prompts, safety policies, model configuration, grounding indexes, evaluation datasets, tool permission manifests). ✓
  * Both deep links preserved: AI-Assisted Engineering [#L71](docs/CI-CD/README.md#L71) and `#review-the-system-across-disciplines` [#L94](docs/CI-CD/README.md#L94). ✓
  * **DD-03**: checklist item 2 enumeration "prompt, model, retrieval, agent, safety, and regression behavior" → "safety, groundedness, and regression behavior" — [#L87](docs/CI-CD/README.md#L87). Recommendation ("AI-enabled systems include evaluation gates … where applicable") preserved; the gate requirement is intact. ✓ (see Minor-02)
  * Checklist item 1 also tightened: "tool-permission changes … attached to the PR or release record" → "tool changes … in the PR" — [#L86](docs/CI-CD/README.md#L86) (see Minor-03).
* **Result**: PASS. DD-03 confirmed — recommendation meaning preserved.

## Findings

### Critical

* None.

### Major

* None.

### Minor

* **Minor-01 — generative-ai bullets retain 6+ comma items.** Bullets such as "Lean on
  Responsible AI to review user impact, harms, transparency, accountability, human oversight,
  and post-deployment review cadence" still exceed the rubric's ~4-item guidance —
  [docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md](docs/ml-and-ai-projects/generative-ai-and-agentic-systems.md#L69). This is **within plan scope**: Step 3.3 and DD-01
  deliberately limited this page to opener variation, not stack splitting. No action required;
  recorded for completeness.
* **Minor-02 — DD-03 introduces a new term and narrows specificity.** The condensed gate list
  adds "groundedness" (absent from the original "prompt, model, retrieval, agent, safety,
  regression") and drops the prompt/model/retrieval/agent enumerations —
  [docs/CI-CD/README.md](docs/CI-CD/README.md#L87). The recommendation (require evaluation
  gates) is unchanged, so this stays a tone/specificity trade-off as logged in DD-03, but the
  swap to "groundedness" is a slight content shift rather than a pure "tighten." Consider a
  user confirmation that "groundedness" is an acceptable substitution.
* **Minor-03 — second checklist edit not separately logged.** Checklist item 1 was also
  tightened ("tool-permission changes" → "tool changes"; "attached to the PR or release
  record" → "in the PR") — [docs/CI-CD/README.md](docs/CI-CD/README.md#L86). The plan's
  Step 3.5 authorized tightening "the two added checklist items", so this is in scope, but
  only the item-2 change was captured as DD-03. Dropping "or release record" slightly narrows
  where evidence may live (PR only). Low impact; note for traceability.

## Coverage Assessment

All five Step 3.x plan items are implemented exactly as described in the changes log. Both
recorded deviations are verified:

* **DD-02** — 13 controls preserved across 4 themed groups; no control dropped. CONFIRMED.
* **DD-03** — checklist enumeration condensed; recommendation (require evaluation gates)
  unchanged. CONFIRMED (with Minor-02 nuance on "groundedness").

Both protected anchors confirmed intact: `#ai-systems-threat-modeling-considerations`
(threat-modelling.md L19) and `#review-the-system-across-disciplines`
(generative-ai L65, and the CI-CD deep link to it at L94). All cross-links and shared-guide
links preserved. No heading text changed on any of the five files. Edits are tone/structure
only — consistent with the "TONE ONLY" constraint.

Phase 3 coverage: **complete**. No missing implementations.

## Clarifying Questions

1. Is the substitution of "groundedness" for the original "prompt, model, retrieval, agent"
   gate enumeration (Minor-02) an intended semantic change, or should the original enumerated
   gate types be retained alongside "groundedness"?

## Recommended Next Validations (not performed this session)

* [ ] Phase 1 (Central Guide) validation — docs/ai-assisted-engineering/README.md.
* [ ] Phase 2 (Tone Seams) validation — copilots.md, automated-testing, privacy/data-handling, documentation.
* [ ] Phase 4 (Tier B Light Touch) validation — confirm the seven "left unchanged" pages truly pass the rubric.
* [ ] Repo-wide link/anchor check across all 12 modified files (changes log claims zero broken links; independent re-run not done here).
* [ ] Confirm the out-of-scope `.gitattributes` working-tree change (OOS-01) with the user.
