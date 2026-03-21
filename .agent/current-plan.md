# Current Plan

## Iteration focus

Iteration `20260321-043256` is complete: it added one engineering-domain `optimize-adapt` instance linked to `queue-prioritization-optimization`, closing the last open domain slice in that family and shifting the next likely gap toward research or HR coverage in `investigate-reconcile-verify` and `monitor-detect-triage`.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-nine scenarios, and every top-level family now has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, `gather-retrieve-synthesize`, and `optimize-adapt` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement is now the active phase, with `investigate-reconcile-verify` and `monitor-detect-triage` remaining the most visibly uneven families by domain coverage; within that set, a research-domain investigation example now looks like the cleanest next improvement because it would deepen one of the lowest-count domains while shrinking the remaining open slices in `investigate-reconcile-verify`
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `incident-root-cause-analysis`, the existing investigation instances, and adjacent research examples before authoring the next refinement batch.
2. Author one narrowly scoped research-domain `investigate-reconcile-verify` instance so the family starts closing its remaining open domain slices without widening into new canonical patterns.
3. Keep the scenario squarely in investigate/reconcile/verify territory by focusing on bounded evidence reconciliation and defensible root-cause analysis, not recommendation memos, scheduling, execution, or monitoring-only triage.
4. Preserve the pattern-first rule by grounding only against `incident-root-cause-analysis` unless a genuine dependency issue appears.
5. After the next instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-043256`
- Completed subagent scope: authored `instances/engineering/ci-pipeline-failure-review-queue-reprioritization.md` as one engineering-domain `optimize-adapt` grounding change and committed it separately.
- Completed orchestrator follow-up: refreshed execution memory so the completed engineering optimization coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should likely add one research-domain `investigate-reconcile-verify` grounding, begin closing the remaining open investigation slices without widening scope, and then reassess whether HR investigation or research/HR monitoring is the highest-leverage follow-on gap.
