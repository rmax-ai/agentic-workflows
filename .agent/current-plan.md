# Current Plan

## Iteration focus

This iteration should rebalance `gather-retrieve-synthesize`, which remains comparatively thin at the instance layer after recent monitoring and investigation grounding. The batch should stay small and add grounded evidence-synthesis examples in underrepresented non-research domains, with finance and operations as the preferred targets if suitable scenarios can stay clearly inside retrieval and synthesis boundaries.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twenty-six total scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `research-synthesis-with-citation-verification` plus the existing research gather/synthesis grounding and nearby finance, compliance, or operations instances so the next examples stay inside evidence retrieval and synthesis boundaries rather than drifting into recommendation, investigation, or collaboration.
2. Keep the next grounding batch modest: prefer one or two `gather-retrieve-synthesize` instances in underrepresented domains, with finance and operations as the leading candidates for this iteration.
3. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the required iteration log after the next grounding batch so repository memory reflects stronger gather/synthesis coverage.
4. Continue validating repository YAML with the existing uv-managed helper before closing each iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one modest gather/synthesis grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should deepen `gather-retrieve-synthesize` with one or two grounded, governance-aware finance or operations instances while preserving the repository's pattern-first structure and modest-batch discipline.
