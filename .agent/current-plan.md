# Current Plan

## Iteration focus

Iteration `20260321-041918` is complete: it added one research-domain `optimize-adapt` instance linked to `queue-prioritization-optimization` via `embargoed-benchmark-replication-review-queue-reprioritization`, giving the thinnest family a fourth grounded domain without widening scope into new canonical patterns, vocabularies, or schema work.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-six scenarios, and every top-level family now has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, and `gather-retrieve-synthesize` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement is now the active phase, with `optimize-adapt`, `investigate-reconcile-verify`, and `monitor-detect-triage` remaining the most visibly uneven families by domain and architecture coverage even after `optimize-adapt` expanded into research
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `queue-prioritization-optimization`, the four existing `optimize-adapt` instances, and adjacent uncovered-domain examples before authoring the next refinement batch.
2. Author one narrowly scoped `optimize-adapt` instance in another uncovered domain, preferably HR, so the family continues closing open domain slices while also helping one of the currently lighter-weight domains.
3. Keep the next scenario centered on feedback-driven queue reprioritization under explicit fairness, workload-balance, service-level, and rollback guardrails rather than drifting into planning, recommendation, or execution work.
4. Preserve the pattern-first rule by grounding only against `queue-prioritization-optimization` unless a genuine dependency issue appears.
5. After the next instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-041918`
- Completed subagent scope: authored `instances/research/embargoed-benchmark-replication-review-queue-reprioritization.md` as one research-domain `optimize-adapt` grounding change and committed it separately.
- Completed orchestrator follow-up: refresh execution memory so the new optimization coverage is reflected in status, coverage tracking, the repository map, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should add one more `optimize-adapt` grounding in an uncovered domain, continue balancing the thinnest family without widening scope, and leave the repository more even after another modest `.agent/` memory refresh.
