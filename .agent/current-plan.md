# Current Plan

## Iteration focus

The last iteration broadened `plan-coordinate-schedule` with grounded support and HR examples, so the next Phase 6 batch should rebalance another thin slice. The clearest remaining candidates are `execute-automate` and `optimize-adapt`, where grounded coverage still concentrates in only one or two domains.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover seventeen total scenarios, and `plan-coordinate-schedule` now has covered operations, support, and HR examples while `execute-automate` and `optimize-adapt` remain thinner
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read the canonical pattern and grounded examples for `browser-based-form-completion-with-approval-gates` and `queue-prioritization-optimization` to choose the next modest batch that closes the clearest partial cells.
2. Prefer one or two new grounded instances in finance, operations, support, or compliance if they materially deepen `execute-automate` or `optimize-adapt` without duplicating existing compliance, HR, or support coverage.
3. Keep new instances concrete about approval gates, policy boundaries, optimization objectives, reversibility, and evaluation rather than drifting into general domain overviews.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next iteration log after the batch so memory reflects the next rebalanced family/domain slice.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to instance authoring plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should visibly improve either the execution or optimization slice while preserving the repository's pattern-first structure and the recently strengthened scheduling coverage.
