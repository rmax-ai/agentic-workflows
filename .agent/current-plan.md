# Current Plan

## Iteration focus

Iteration `20260321-043256` is in progress: it should add one engineering-domain `optimize-adapt` instance linked to `queue-prioritization-optimization`, closing the last open domain slice in the thinnest family before re-evaluating thinner research or HR gaps in `investigate-reconcile-verify` and `monitor-detect-triage`.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-eight scenarios, and every top-level family now has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, and `gather-retrieve-synthesize` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement is now the active phase, with `optimize-adapt`, `investigate-reconcile-verify`, and `monitor-detect-triage` remaining the most visibly uneven families by domain and architecture coverage; within that set, `optimize-adapt` is still the most direct next improvement because engineering is the only remaining open domain slice, while `investigate-reconcile-verify` and `monitor-detect-triage` still leave research and HR open if deeper cross-domain balancing becomes worthwhile
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `queue-prioritization-optimization`, the six existing `optimize-adapt` instances, and adjacent engineering examples before authoring the next refinement batch.
2. Author one narrowly scoped engineering-domain `optimize-adapt` instance so the family closes its last uncovered domain slice without widening into new canonical patterns.
3. Keep the scenario squarely in optimize/adapt territory by focusing on bounded reprioritization of an existing engineering queue, not investigation, recommendation memo writing, scheduling, or direct execution.
4. Preserve the pattern-first rule by grounding only against `queue-prioritization-optimization` unless a genuine dependency issue appears.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-043256`
- Planned subagent scope: author one engineering-domain `optimize-adapt` instance grounded only in `queue-prioritization-optimization` and commit it separately.
- Planned orchestrator follow-up: refresh execution memory so the completed engineering optimization coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one engineering-domain `optimize-adapt` grounding, finish domain coverage for the thinnest family without widening scope, and then reassess whether the next highest-leverage gap is the research or HR slice in `investigate-reconcile-verify` or `monitor-detect-triage`.
