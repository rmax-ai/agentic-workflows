# Current Plan

## Iteration focus

This iteration should rebalance the thinnest `plan-coordinate-schedule` slice by grounding the existing `calendar-conflict-coordination` pattern in two still-partial domains: `support` and `hr`. The batch should stay instance-only, add no new canonical pattern files, and make the low-risk bounded-delegation scheduling pattern feel representative beyond the existing operations example.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifteen total scenarios, and `plan-coordinate-schedule` still has only one covered operations example while support and HR remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `calendar-conflict-coordination`, the family doc, and the existing operations scheduling instance to keep the next grounded examples structurally aligned.
2. Add one support scheduling instance and one HR scheduling instance that clearly exercise multi-party constraint reconciliation, bounded delegation, and escalation boundaries without drifting into recommendation or execution patterns.
3. Keep both instances concrete about calendars, coordinator roles, timezone or availability constraints, reversible holds, and evaluation criteria.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after the batch so memory reflects that `plan-coordinate-schedule` now has broader grounded coverage.
5. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside a single family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The iteration should leave `plan-coordinate-schedule` grounded in operations, support, and HR so the family is no longer represented by a single operational scheduling scenario.
