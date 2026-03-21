# Current Plan

## Iteration focus

Iteration `20260321-032458` will stay inside Phase 6 and rebalance the next thinnest grounded family without widening into schema, vocabulary, view, or new pattern authoring work. `transform-process` remains the strongest adjacent target because it still has grounded examples only in finance, compliance, and operations, so this batch should add exactly one support-domain instance linked to `document-to-structured-data-handoff`.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover forty-three scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, operations, support, and HR, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, support, operations, finance, and HR
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `document-to-structured-data-handoff`, the existing transform-process instances, and adjacent support-domain artifacts before adding another grounded handoff scenario.
2. Author exactly one new support-domain instance linked to `document-to-structured-data-handoff` so the next batch deepens a thin family rather than opening a new front.
3. Keep the scenario anchored on governed document-to-record or packet-to-staging transformation with provenance, exception routing, and human review boundaries rather than drifting into recommendation, execution, or investigation.
4. Keep the content batch limited to this single transform-process example so coverage improves without widening scope.
5. After the next instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/iterations/2026/20260321-032458.md` so execution memory matches repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-032458`
- Planned subagent scope: author one support-domain `document-to-structured-data-handoff` grounding change and commit it separately.
- Planned orchestrator follow-up: refresh execution memory so transform-family support coverage is reflected in status and coverage tracking.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The current iteration should add one support-domain `transform-process` example, deepen one of the thinnest grounded families, and leave the repository ready for another small Phase 6 grounding batch after the `.agent/` memory refresh.
