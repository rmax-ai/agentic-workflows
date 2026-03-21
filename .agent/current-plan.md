# Current Plan

## Iteration focus

Iteration `20260321-093716` is now scoped to close the remaining `critical` risk gap in `human-agent-collaborative-work` with one family-clean severe collaboration pattern plus a few grounded instances. The batch must stay centered on a protected shared artifact, explicit human ownership, contested edits, and bounded handoff readiness rather than drifting into authority recommendation, crisis planning, briefing synthesis, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans thirty-seven patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `transform-process` and `recommend-decide-escalate` sit at five; `gather-retrieve-synthesize`, `investigate-reconcile-verify`, `monitor-detect-triage`, `plan-coordinate-schedule`, `execute-automate`, and `optimize-adapt` sit at four; and `human-agent-collaborative-work` sits at three.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred twenty-six instance files now committed.
- Phase 7: coverage refinement remains active, and `optimize-adapt` now joins `gather-retrieve-synthesize`, `transform-process`, `investigate-reconcile-verify`, `monitor-detect-triage`, `plan-coordinate-schedule`, `recommend-decide-escalate`, and `execute-automate` in spanning the full tracked risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.

## Ordered tasks

1. Add one canonical `human-agent-collaborative-work` pattern at `critical` risk that anchors on severe shared-artifact collaboration, protected work surfaces, explicit ownership, and visible disagreement.
2. Ground that pattern with a small set of linked instances in domains where severe shared-work is clearly primary and still family-clean.
3. Synchronize the collaboration family doc and the directly affected derived browse views so they reflect the new canonical inventory without drift.
4. Validate repository YAML with `uv run python scripts/python/validate_yaml.py`, then update `.agent/` execution memory, coverage tracking, and this plan before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-093716`
- Planned scope: add one critical collaboration anchor in `human-agent-collaborative-work`, a few linked severe shared-work instances, and the directly affected family/view synchronization in one feature commit.
- Coverage target: fill the final uncovered `pattern_family_x_risk` cell by giving `human-agent-collaborative-work` explicit `critical` representation while preserving clean separation from recommendation, planning, synthesis, and execution families.
- Planned orchestrator follow-up: validate YAML, update status and coverage memory, record this iteration, and queue the next narrow refinement only after the collaboration family cleanly spans the full tracked risk ladder.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest batch with one new canonical pattern and a few instances over broader family expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `human-agent-collaborative-work` with representative `critical` risk coverage through one bounded severe shared-work pattern and a small linked instance set, while keeping the ontology family boundaries clean and the derived browse artifacts synchronized to canonical truth.
