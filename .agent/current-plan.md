# Current Plan

## Iteration focus

Close the remaining `human-agent-collaborative-work` grounding gap in `compliance` with one concrete copilot-loop instance that is distinct from the existing recommendation and execution examples. The target scenario should emphasize mixed-initiative drafting, evidence curation, and explicit accountability boundaries around a regulated compliance artifact rather than portal submission or recommendation ranking.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover twelve total scenarios, with broader research coverage and a stronger `human-agent-collaborative-work` family footprint, but many family/domain cells remain partial
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one new `instances/compliance/` collaboration example linked to `analyst-copilot-loop`, preferably around a regulator-response, exception-memo, or evidence-packet workflow where the human stays responsible for interpretation and outbound commitments.
2. Keep the instance materially distinct from the existing support escalation and research benchmarking copilot loops by centering governed compliance drafting, policy citation, and regulator- or reviewer-facing traceability.
3. Keep the instance tightly linked to the canonical pattern and focused on concrete systems, governance checkpoints, provenance, and evaluation hooks rather than generic compliance prose.
4. After the grounded example lands, update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the iteration log to reflect that `human-agent-collaborative-work` now has explicit compliance coverage.
5. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance across families and domains without forcing a broad cross-family sweep.
- Keep the next iteration scoped to one compliance collaboration instance plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should leave the repository with an explicitly grounded compliance example for `human-agent-collaborative-work`, plus updated memory files that make the remaining thin coverage cells easier to prioritize.
