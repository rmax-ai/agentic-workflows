# Current Plan

## Iteration focus

`recommend-decide-escalate` is now grounded across finance, compliance, and operations after the new multi-site service-package feasibility example. The next modest batch should likely rebalance a thinner domain and family, with `human-agent-collaborative-work` in engineering looking like the cleanest adjacent target.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and now reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage now spans all nine top-level pattern families
- Phase 6: grounded instances now cover thirty-three total scenarios, with `gather-retrieve-synthesize` grounded across research, engineering, finance, compliance, operations, support, and HR, `investigate-reconcile-verify` grounded across engineering, finance, and compliance, `monitor-detect-triage` grounded across finance, compliance, and operations, `recommend-decide-escalate` grounded across finance, compliance, and operations, `execute-automate` grounded across finance, compliance, HR, operations, and support, and `optimize-adapt` grounded across support, operations, and compliance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the current collaboration-oriented instances, and at least one engineering instance so the next grounding batch stays inside the mixed-initiative family boundary.
2. Author exactly one engineering-domain instance linked to `analyst-copilot-loop`, framed as shared human-agent work around an artifact rather than pure synthesis, recommendation, or execution.
3. Keep the next batch limited to this single collaboration example so engineering-domain balance improves without widening the scope into multiple families.
4. Update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next dated iteration log after that grounding batch so execution memory stays current.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing more seed patterns immediately.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve coverage balance inside one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep the next iteration scoped to one small grounding batch plus required `.agent/` memory updates; do not expand the canonical pattern set unless dependency order changes.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.

## Expected outcome

The next iteration should improve engineering-domain balance by adding one mixed-initiative collaboration example without widening the repository beyond a single grounded Markdown artifact plus required memory updates.
