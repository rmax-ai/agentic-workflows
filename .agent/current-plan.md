# Current Plan

## Iteration focus

This iteration will continue broadening `gather-retrieve-synthesize` in compliance with one evidence-first scenario that stays upstream of recommendation, investigation, and execution. The target shape is a governed compliance obligations synthesis brief that adds materially different source types and review concerns than the current research, finance, operations, and support examples.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-nine total scenarios, with `gather-retrieve-synthesize` grounded across research, finance, operations, and support, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `research-synthesis-with-citation-verification` plus the current research, finance, operations, and support gather/synthesis instances so the next example stays inside evidence retrieval and synthesis boundaries rather than drifting into recommendation, investigation, or collaboration.
2. Author exactly one compliance-domain instance linked to `research-synthesis-with-citation-verification`, centered on a current-state obligations synthesis artifact such as policy, control, or regulatory-response evidence assembly.
3. Review the new instance for family-boundary discipline, then update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log so repository memory reflects the new compliance grounding.
4. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the iteration scoped to one compliance-centered gather/synthesis grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The iteration should leave `gather-retrieve-synthesize` with a stronger compliance grounding example while preserving the repository's pattern-first structure and modest-batch discipline.
