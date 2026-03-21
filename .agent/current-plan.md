# Current Plan

## Iteration focus

Iteration `20260321-072052` is complete: `shared-workbench-orchestration` now extends `human-agent-collaborative-work` with a low-risk shared-workbench upkeep anchor plus research, operations, and support grounding, and the derived browse views now expose the family's bounded-delegation and event-driven slices without drifting from canonical metadata.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-five patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the latest iteration closes the `human-agent-collaborative-work` family's low-risk and event-driven upkeep gaps while keeping family boundaries intact
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, `.agent/ontology-status.yaml`, and the `transform-process` family materials before choosing the next narrow Phase 7 refinement now that low-risk collaboration coverage is in place.
2. Prefer the next iteration to add one higher-risk or more governance-sensitive `transform-process` pattern that stays centered on structured handoff, governed lossiness, or sensitive normalization rather than drifting into recommendation, approval, or execution.
3. Keep any follow-on transform work distinct from `document-to-structured-data-handoff`, `normalization-and-enrichment`, and adjacent recommendation or execution families by preserving the family's representation-change center of gravity.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the next content batch so execution memory stays synchronized.
5. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-072052`
- Baseline context: iteration `20260321-071104` closed the investigate family's low-risk verification gap and left low-risk `human-agent-collaborative-work` as the cleanest family-specific refinement target.
- Completed subagent scope: added `shared-workbench-orchestration`, grounded it with new research, operations, and support instances, and updated the affected browse views so the collaboration family now includes bounded-delegation, low-risk, and event-driven coverage.
- Planned orchestrator follow-up: record the new collaboration coverage shape, then reassess whether the next best gap is a higher-risk transform slice or another similarly narrow refinement.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep any follow-on `transform-process` expansion distinct from `document-to-structured-data-handoff`, `normalization-and-enrichment`, `approval-packet-generation`, and `browser-based-form-completion-with-approval-gates` by centering it on governed representation change rather than recommendation packaging or downstream action.

## Expected outcome

The next iteration should move to another narrow family-specific governance slice, with higher-risk `transform-process` now a leading candidate because `human-agent-collaborative-work` has representative low-, moderate-, and high-risk coverage plus event-driven collaboration support without reopening broader repository scaffolding.
