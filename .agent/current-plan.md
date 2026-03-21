# Current Plan

## Iteration focus

The last iteration deepened `monitor-detect-triage` with two new grounded examples: pharmacovigilance safety-signal triage in compliance and cold-chain temperature excursion triage in operations. This iteration should stay modest and rebalance the thinner `investigate-reconcile-verify` family with grounded finance and compliance examples that materially differ from the existing engineering incident anchor.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-four total scenarios, with `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `incident-root-cause-analysis`, the engineering investigation anchor, and nearby governed finance/compliance instances so the next examples stay inside investigation boundaries rather than drifting into triage, recommendation, or execution.
2. Add a modest batch of one or two grounded `investigate-reconcile-verify` instances, preferably covering finance and compliance with evidence-reconciliation, explicit uncertainty handling, and human-owned closure decisions.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the grounding batch so repository memory reflects stronger investigation coverage.
4. Continue validating repository YAML with the existing uv-managed helper before closing each iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep this iteration scoped to one modest investigation-grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

This iteration should deepen `investigate-reconcile-verify` in finance and/or compliance with one or two grounded, governance-aware instances while preserving the repository's pattern-first structure and modest-batch discipline.
