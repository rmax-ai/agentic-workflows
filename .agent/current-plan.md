# Current Plan

## Iteration focus

The last iteration deepened `transform-process` with new compliance and operations grounding, so the next Phase 6 batch should rebalance another thin family/domain slice. The clearest remaining candidates are `plan-coordinate-schedule`, `execute-automate`, and `optimize-adapt`, where grounded coverage still concentrates in only one or two domains.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifteen total scenarios, and `transform-process` now has concrete finance, compliance, and operations examples, but many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the canonical patterns and existing grounded examples for `plan-coordinate-schedule`, `execute-automate`, and `optimize-adapt` to choose the next modest batch that closes the clearest partial cells without duplicating the newly expanded transform slice.
2. Prefer one or two new grounded instances in support, HR, compliance, or operations if they materially deepen one thin family while staying tightly linked to an existing canonical pattern.
3. Keep new instances concrete about approval boundaries, scheduling or optimization constraints, provenance, and evaluation rather than drifting into domain overviews.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after the batch so memory reflects the next rebalanced family/domain slice.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance across families and domains without forcing a broad cross-family sweep.
- Keep the next iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should visibly improve one of the remaining thin scheduling, execution, or optimization slices while preserving the repository's pattern-first structure.
