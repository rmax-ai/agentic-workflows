# Current Plan

## Iteration focus

The last iteration closed the final empty `gather-retrieve-synthesize` domain cell with an HR pay-transparency posting-obligations synthesis example. The next modest batch should decide whether to finish the family's remaining engineering partial slice or pivot to another thin family with only one or two grounded domains, while still preserving the repository's small-batch discipline.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-one total scenarios, with `gather-retrieve-synthesize` grounded across research, finance, compliance, operations, support, and HR and only engineering still partial within that family, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `research-synthesis-with-citation-verification` plus the current gather/synthesis instances and decide whether one engineering example is still the highest-leverage follow-on or whether another family now deserves the next balancing batch.
2. If `gather-retrieve-synthesize` remains the best target, author exactly one engineering instance linked to `research-synthesis-with-citation-verification`, centered on a cited architecture, migration, or operational-evidence brief that remains upstream of implementation or incident response.
3. Otherwise pick one equally thin family/domain slice and keep the batch to one or two tightly related grounded instances tied to existing canonical patterns only.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the next grounding batch so repository memory reflects the chosen coverage move.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one small grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should either complete the remaining engineering gather/synthesis slice or make an equally disciplined coverage-balancing move in another thin family while preserving the repository's pattern-first structure and modest-batch discipline.
