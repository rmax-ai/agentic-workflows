# Current Plan

## Iteration focus

Iteration `20260321-041918` is now in progress. It will add one research-domain `optimize-adapt` instance linked to `queue-prioritization-optimization` so Phase 7 starts by strengthening the thinnest family-level grounding area without widening scope into new canonical patterns, vocabularies, or schema work.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-five scenarios, and every top-level family now has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, and `gather-retrieve-synthesize` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement is now the active phase, with `optimize-adapt`, `investigate-reconcile-verify`, and `monitor-detect-triage` remaining the most visibly uneven families by domain and architecture coverage
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `queue-prioritization-optimization`, the existing `optimize-adapt` instances, and nearby research examples before authoring the next refinement batch.
2. Author one narrowly scoped `optimize-adapt` instance in research so the family no longer depends only on support, operations, and compliance grounding.
3. Keep the scenario centered on feedback-driven queue reprioritization under explicit fairness, embargo, review-capacity, and rollback guardrails rather than drifting into recommendation, scheduling, or collaboration work.
4. Preserve the pattern-first rule by grounding only against `queue-prioritization-optimization` unless a genuine dependency issue appears.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/iterations/2026/20260321-041918.md` so execution memory matches repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-041918`
- Planned subagent scope: author one research-domain `optimize-adapt` grounding file tied to `queue-prioritization-optimization` and commit it separately.
- Planned orchestrator follow-up: refresh execution memory so the new optimization coverage is reflected in status, coverage tracking, the repository map, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one research `optimize-adapt` grounding, improve the most visibly thin family without widening scope, and leave the repository more balanced after another modest `.agent/` memory refresh.
