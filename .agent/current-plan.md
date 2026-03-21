# Current Plan

## Iteration focus

Iteration `20260321-031454` is complete: it added a single finance-domain collaboration instance for `analyst-copilot-loop` via `quarter-close-covenant-clarification-package-copilot-loop`. The next modest batch should stay inside Phase 6 and rebalance the next thin family/domain slice without widening into schema, vocabulary, or pattern-authoring work. HR collaboration is now the strongest adjacent target because `human-agent-collaborative-work` spans every other currently modeled domain.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover forty-two scenarios, with `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across finance, compliance, operations, support, and HR, `execute-automate` grounded across finance, compliance, HR, operations, and support, `optimize-adapt` grounded across support, operations, and compliance, and `human-agent-collaborative-work` grounded across engineering, research, compliance, support, operations, and finance
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `analyst-copilot-loop`, the existing collaboration-oriented instances, and adjacent HR-domain artifacts so the next grounding example stays inside the mixed-initiative collaboration family boundary.
2. Author exactly one HR-domain instance linked to `analyst-copilot-loop`, framed as shared human-agent artifact production or review with explicit ownership boundaries rather than recommendation, investigation, execution, scheduling, monitoring, or optimization.
3. Prefer a scenario where HR staff and an agent iteratively build or refine a governed artifact such as an exception memo, employee-relations response packet, mobility-risk brief, or compensation-review narrative before a human makes the binding conclusion.
4. Keep the content batch limited to this single collaboration example so coverage improves without widening scope.
5. After the instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next dated iteration log so execution memory matches repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-031454`
- Completed subagent scope: authored `instances/finance/quarter-close-covenant-clarification-package-copilot-loop.md` as one finance-domain `analyst-copilot-loop` grounding change and committed it separately.
- Pending orchestrator follow-up for the next iteration: scope the HR collaboration batch before new substantive edits.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should add one HR-domain collaboration example, close the remaining domain gap in `human-agent-collaborative-work`, and leave the repository ready for another small grounding batch after the `.agent/` memory refresh.
