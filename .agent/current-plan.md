# Current Plan

## Iteration focus

The last iteration deepened `monitor-detect-triage` with two new grounded examples: pharmacovigilance safety-signal triage in compliance and cold-chain temperature excursion triage in operations. The next batch should stay modest and rebalance another thin family slice, with `investigate-reconcile-verify` now standing out more clearly than further monitoring expansion.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-four total scenarios, with `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `incident-root-cause-analysis` plus the current engineering anchor and nearby partial operations and support investigation instances to determine whether a finance or compliance investigation example adds the clearest structural value next.
2. Keep the next grounding batch modest: prefer one or two `investigate-reconcile-verify` instances that materially differ from the current engineering incident anchor rather than reopening already-strengthened monitoring coverage immediately.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the next grounding batch so repository memory reflects stronger investigation coverage.
4. Continue validating repository YAML with the existing uv-managed helper before closing each iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one modest investigation-grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should deepen `investigate-reconcile-verify` in finance or compliance with one or two grounded, governance-aware instances while preserving the repository's pattern-first structure and modest-batch discipline.
