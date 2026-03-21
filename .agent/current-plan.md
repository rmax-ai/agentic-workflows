# Current Plan

## Iteration focus

Iteration `20260321-070112` is complete: `anomaly-detection-review` now extends `monitor-detect-triage` with a moderate-risk, bounded-delegation, tool-using-single-agent anomaly-review pattern plus new support, research, and HR grounding.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-three patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the latest iteration closes the monitor family's moderate-risk, bounded-delegation, and tool-using-single-agent canonical gap while shifting the next narrow candidate toward a low-risk `investigate-reconcile-verify` or similarly bounded family-specific slice
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, `.agent/ontology-status.yaml`, and the `investigate-reconcile-verify` family materials before choosing the next narrow Phase 7 refinement now that the monitor family's moderate-risk gap is closed.
2. Prefer the next iteration to add one low-risk `investigate-reconcile-verify` pattern that stays centered on bounded verification or discrepancy confirmation rather than broad synthesis, record transformation, or downstream business action.
3. Keep any follow-on low-risk investigation work distinct from `authoritative-record-reconciliation`, `incident-root-cause-analysis`, and nearby gather/transform patterns by choosing a cleaner bounded niche instead of broadening generic review work.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the next content batch so execution memory stays synchronized.
5. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-070112`
- Baseline context: iteration `20260321-065119` closed the low-risk gather/context-briefing gap, leaving a moderate-risk monitor refinement as the cleanest narrow follow-on step.
- Completed subagent scope: added `anomaly-detection-review`, grounded it with support, research, and HR instances, updated the affected browse views, and validated repository YAML successfully.
- Planned orchestrator follow-up: record the new monitor coverage shape, then use a low-risk `investigate-reconcile-verify` slice as the leading candidate for the next dependency-safe refinement step.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep any follow-on `investigate-reconcile-verify` work distinct from `authoritative-record-reconciliation`, `incident-root-cause-analysis`, `research-synthesis-with-citation-verification`, and `document-to-structured-data-handoff` by centering it on bounded low-risk verification rather than broad reconciliation, synthesis, or downstream transformation.

## Expected outcome

The next iteration should move to another narrow family-specific governance slice, with low-risk `investigate-reconcile-verify` now the leading candidate because the monitor family has representative moderate-, high-, and critical-risk coverage plus canonical bounded-delegation and tool-using-single-agent support without reopening broader repository scaffolding.
