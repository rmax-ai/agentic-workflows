# Current Plan

## Iteration focus

This iteration will rebalance two thin Phase 6 slices with one modest grounding batch: add a finance example for `execute-automate` and an operations example for `optimize-adapt`. The goal is to convert two existing partial cells into covered ones without introducing new canonical patterns or cross-family sprawl.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover seventeen total scenarios, and `plan-coordinate-schedule` now has covered operations, support, and HR examples while `execute-automate` and `optimize-adapt` remain the clearest thin slices to rebalance next
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one finance instance linked to `browser-based-form-completion-with-approval-gates` that makes approval gating, browser execution risk, reversibility, and evidence capture concrete in a materially different workflow from the existing compliance and HR examples.
2. Add one operations instance linked to `queue-prioritization-optimization` that makes optimization objectives, rollback paths, fairness constraints, and operational context shifts concrete in a materially different workflow from the existing support example.
3. Keep both instances tightly grounded in specific systems, actors, and governance constraints rather than turning them into broad domain writeups.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next iteration log after the batch so memory reflects the newly covered finance execution and operations optimization cells.
5. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to two new instances plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The iteration should leave `execute-automate` with explicit finance grounding and `optimize-adapt` with explicit operations grounding while preserving the repository's pattern-first structure and modest-batch discipline.
