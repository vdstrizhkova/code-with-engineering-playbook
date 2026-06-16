<!-- markdownlint-disable-file -->
# Release Changes: Tone Review Rework Fixes

**Related Plan**: tone-rework-review-fixes-plan.instructions.md
**Implementation Date**: 2026-06-16

## Summary

Resolved the two Major findings from the tone-of-voice alignment review: restored the CI-CD evaluation-gate recommendation coverage that a tone edit had narrowed (MAJ-01), split the rubric-breaching comma stack in the privacy fundamentals intro (MAJ-02), and cleared one optional Minor comma stack in already-edited test guidance (MIN-01). All edits are tone/coverage-only.

## Changes

### Added

* (none)

### Modified

* docs/CI-CD/README.md — Restored the evaluation-gate checklist item to cover prompt, model, retrieval, and agent behavior plus safety and regression checks (reversing the DD-03 narrowing), removed the unrequested "groundedness" addition, and restored the adjacent item's "tool-permission" precision and "or release record" location. No 6+ item comma stack; checkbox count unchanged (MAJ-01 / PD-01 Option A, PD-02 Option A).
* docs/non-functional-requirements/privacy/README.md — Split the 7-item comma stack in the "AI Privacy Review Prompts" intro into three grouped clauses (user-facing inputs / processing systems / retained data); all seven data surfaces preserved and both cross-links unchanged (MAJ-02).
* docs/automated-testing/README.md — Regrouped the 6-item scenario comma stack into adversarial/malformed inputs and refusal/fallback/escalation behavior; all six scenarios preserved, `#testing-and-evaluation` link unchanged (MIN-01).

### Removed

* (none)

## Additional or Deviating Changes

* PD-01 resolved as Option A: "groundedness" removed rather than retained, honoring "preserve, not expand, the recommendation".
* PD-02 resolved as Option A: CI-CD checklist Item 1 restored to the exact original 5-item wording (under the 6+ hard bar; the ~4-item target is advisory and outranked by recommendation fidelity).
* OOS-01 unchanged: the unrelated `.gitattributes` working-tree change remains untouched, still pending a user keep/commit/revert decision.

## Release Summary

Three documentation files modified (0 added, 0 removed) to clear the two merge-blocking Major review findings plus one optional Minor finding. Validation: `get_errors` clean on all three; internal-link checker clean; grep confirms restored gate-type coverage with "groundedness" removed and all privacy data surfaces preserved. No heading, link, or anchor target changed. Remaining deferred items: Minor findings MIN-02..06 (rubric-advisory, mostly Tier B term-of-art enumerations) and the out-of-scope `.gitattributes` decision.
