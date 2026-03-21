# Current Plan

## Iteration focus

Iteration `20260321-044331` will target the last open HR slice in `investigate-reconcile-verify` by adding one bounded HR-domain instance linked to `incident-root-cause-analysis`. The goal is to close that family/domain gap cleanly before the repository returns to the remaining research and HR monitoring coverage holes.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover sixty scenarios, and every top-level family has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, `gather-retrieve-synthesize`, and `optimize-adapt` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement remains the active phase, with `investigate-reconcile-verify` grounded across six of seven domains and `monitor-detect-triage` still grounded across five of seven; the cleanest next move is to close the remaining HR investigation slice before returning to the open research and HR monitoring cells
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `incident-root-cause-analysis`, recent investigation instances, and adjacent HR examples before authoring the next refinement batch.
2. Author one narrowly scoped HR-domain `investigate-reconcile-verify` instance so the family closes its last open domain slice without widening into new canonical patterns.
3. Keep the scenario squarely in investigate/reconcile/verify territory by focusing on bounded evidence reconciliation and defensible root-cause analysis, not recommendation memos, scheduling, execution, or monitoring-only triage.
4. Preserve the pattern-first rule by grounding only against `incident-root-cause-analysis` unless a genuine dependency issue appears.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-044331`
- Planned subagent scope: author one HR-domain `incident-root-cause-analysis` grounding change and commit it separately.
- Planned orchestrator follow-up: refresh execution memory so the new investigation coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one HR-domain `investigate-reconcile-verify` grounding to close the last open investigation slice without widening scope, then reassess whether research or HR monitoring is the highest-leverage follow-on gap.
