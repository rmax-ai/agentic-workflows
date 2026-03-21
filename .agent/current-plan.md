# Current Plan

## Iteration focus

This iteration will deepen the governed `optimize-adapt` slice by adding one compliance-grounded instance linked to `queue-prioritization-optimization`. The goal is to turn the current compliance optimization cell from a planned opportunity into a concrete, audit-heavy example without broadening the batch into multiple families.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover nineteen total scenarios, with `execute-automate` grounded across finance, compliance, and HR and `optimize-adapt` grounded across support and operations
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Author one new compliance instance for `queue-prioritization-optimization` that emphasizes bounded reprioritization, deadline pressure, fairness, rollback, and supervisory review.
2. Keep the batch modest: do not expand the pattern set or add unrelated instances unless the chosen compliance example proves structurally insufficient.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log after the instance lands so repository memory reflects the newly grounded optimization slice.
4. Continue validating repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to one modest compliance-grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The iteration should close the compliance cell for `optimize-adapt` with one grounded, governance-aware instance while preserving the repository's pattern-first structure and modest-batch discipline.
