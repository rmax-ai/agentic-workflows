# Current Plan

## Iteration focus

Iteration `20260321-040927` is complete: it added one engineering-domain `recommend-decide-escalate` instance linked to `deal-desk-recommendation-support` via `managed-database-major-version-upgrade-exception-recommendation`, closing the engineering domain gap in that family.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover fifty-four scenarios, with `transform-process` grounded across engineering, finance, compliance, operations, support, HR, and research, `investigate-reconcile-verify` grounded across engineering, finance, compliance, operations, and support, `monitor-detect-triage` grounded across engineering, finance, compliance, operations, and support, `recommend-decide-escalate` grounded across engineering, finance, compliance, operations, support, and HR, `execute-automate` grounded across engineering, finance, compliance, HR, operations, research, and support, `optimize-adapt` grounded across support, operations, and compliance, `human-agent-collaborative-work` grounded across engineering, research, compliance, support, operations, finance, and HR, and `plan-coordinate-schedule` grounded across engineering, finance, compliance, operations, research, support, and HR
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `deal-desk-recommendation-support`, the existing recommendation instances, and adjacent research-domain artifacts before authoring the next grounding.
2. Author exactly one new research-domain instance linked to `deal-desk-recommendation-support` so the next batch closes the family's last open domain slice.
3. Keep the scenario anchored on recommendation-only decision support with explicit policy thresholds, escalation boundaries, and evidence-backed trade-offs rather than drifting into planning, synthesis, or execution work.
4. Prefer a research workflow such as benchmark publication go/no-go recommendation support, dataset access exception recommendation, or trial protocol change recommendation support where the main value is governed recommendation and escalation packaging before any commitment is made.
5. Keep the content batch limited to this single research recommendation example so coverage improves in a controlled, dependency-aware way.
6. After the next instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the next dated iteration log so execution memory continues to match repository reality.
7. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-040927`
- Completed subagent scope: authored `instances/engineering/managed-database-major-version-upgrade-exception-recommendation.md` as one engineering-domain `recommend-decide-escalate` grounding change and committed it separately.
- Completed orchestrator follow-up: refreshed execution memory so the new engineering recommendation coverage is reflected in status, coverage tracking, the repository map, and the dated iteration log.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen the next iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should add one research-domain `recommend-decide-escalate` example, close that family's last open domain slice, and leave the repository better balanced after another modest `.agent/` memory refresh.
