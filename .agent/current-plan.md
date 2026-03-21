# Current Plan

## Iteration focus

Iteration `20260321-042809` is now focused on one more Phase 7 grounding batch for `optimize-adapt`: add a finance-domain instance linked to `queue-prioritization-optimization` so the thinnest family closes another uncovered domain slice without widening scope into new schema, vocabulary, view, or pattern work.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-seven scenarios, and every top-level family now has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, and `gather-retrieve-synthesize` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement is now the active phase, with `optimize-adapt`, `investigate-reconcile-verify`, and `monitor-detect-triage` remaining the most visibly uneven families by domain and architecture coverage; within that set, `optimize-adapt` is still the most direct next improvement because only finance and engineering remain open; this iteration should take the finance slice with a queue-reprioritization scenario that stays centered on bounded backlog tuning rather than investigation, recommendation, scheduling, or execution
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `queue-prioritization-optimization`, all five existing `optimize-adapt` instances, and adjacent finance examples before authoring the next refinement batch.
2. Author one narrowly scoped finance-domain `optimize-adapt` instance so the family closes the finance slice without widening into new canonical patterns.
3. Keep the scenario squarely in optimize/adapt territory by focusing on bounded reprioritization of an existing finance queue, not investigation, recommendation memo writing, scheduling, or direct execution.
4. Preserve the pattern-first rule by grounding only against `queue-prioritization-optimization` unless a genuine dependency issue appears.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-042809`
- Planned subagent scope: author one finance-domain `optimize-adapt` instance linked to `queue-prioritization-optimization` and commit it separately.
- Planned orchestrator follow-up: refresh execution memory so the new optimization coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one finance-domain `optimize-adapt` grounding, continue balancing the thinnest family without widening scope, and leave the repository more even after another modest `.agent/` memory refresh.
