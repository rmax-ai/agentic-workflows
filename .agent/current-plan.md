# Current Plan

## Iteration focus

The last iteration closed the remaining `human-agent-collaborative-work` grounding gap in `compliance`, so the next Phase 6 batch should rebalance another thin family/domain slice. The cleanest candidates are `transform-process`, `execute-automate`, or `optimize-adapt`, where only one covered domain cell exists today.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twelve total scenarios, with broader research coverage and a stronger `human-agent-collaborative-work` family footprint, but many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the canonical patterns and grounded examples for `transform-process`, `execute-automate`, and `optimize-adapt` to choose the next small batch that closes the clearest partial cell without duplicating finance, HR, support, or the newly covered compliance collaboration scenario.
2. Prefer one or two new grounded instances in compliance or operations if they materially deepen thin coverage while staying tightly linked to the existing canonical patterns.
3. Keep new instances concrete about source systems, approval or governance checkpoints, provenance, and evaluation rather than drifting into domain overviews.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after the batch so memory reflects the new priority order.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance across families and domains without forcing a broad cross-family sweep.
- Keep the next iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should visibly improve one of the remaining thin transform, execution, optimization, or scheduling slices while preserving the repository's pattern-first structure.
