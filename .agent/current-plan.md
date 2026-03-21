# Current Plan

## Iteration focus

Iteration `20260321-031019` is now scoped around one small grounding task: add a single operations-domain collaboration instance for `analyst-copilot-loop`. The repository memory already identified this as the highest-leverage next step because operations has broad adjacent family coverage but still lacks an explicit `human-agent-collaborative-work` example. This iteration should stay narrow and avoid widening into schema, vocabulary, or new canonical pattern authoring.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover forty scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, operations, support, and HR, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, and support
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the existing collaboration-oriented instances, and adjacent operations-domain artifacts so the new grounding example stays inside the mixed-initiative collaboration family boundary.
2. Author exactly one operations-domain instance linked to `analyst-copilot-loop`, framed as shared human-agent artifact production or review with explicit ownership boundaries rather than recommendation, investigation, execution, scheduling, monitoring, or optimization.
3. Prefer a scenario where operations staff and an agent iteratively build or refine a governed artifact such as an exception packet, supplier response, network-readiness memo, or remediation brief before a human makes the binding conclusion.
4. Keep the content batch limited to this single collaboration example so coverage improves without widening scope.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/iterations/2026/20260321-031019.md` so execution memory matches repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-031019`
- Current scoped content target: one new operations-domain `analyst-copilot-loop` instance.
- Pending orchestrator follow-up after the content commit: refresh `.agent/` memory, validate YAML, and record the iteration outcome.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one operations-domain collaboration example, deepen `human-agent-collaborative-work`, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
