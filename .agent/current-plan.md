# Current Plan

## Iteration focus

Iteration `20260321-045339` is now scoped: the next bounded Phase 7 move is to add one research-domain `monitor-detect-triage` instance linked to `risk-alert-triage`, closing the final open research slice in that family before broader balancing work resumes.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families
- Phase 6: grounded instances now cover sixty-two scenarios, and every top-level family has at least one grounded instance while `recommend-decide-escalate`, `transform-process`, `execute-automate`, `human-agent-collaborative-work`, `plan-coordinate-schedule`, `gather-retrieve-synthesize`, `optimize-adapt`, and `investigate-reconcile-verify` are grounded across all seven currently modeled domains
- Phase 7: coverage refinement remains the active phase, with `monitor-detect-triage` now grounded across six of seven domains; this iteration should close the last open research cell in that family with one tightly scoped monitoring example rather than widening into new patterns or views
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `risk-alert-triage`, the existing monitoring instances, and adjacent research examples before authoring the next refinement batch.
2. Author one narrowly scoped research-domain `monitor-detect-triage` instance so the family closes its last open domain slice without widening into new canonical patterns.
3. Keep the scenario squarely in monitor/detect/triage territory by focusing on alert intake, duplicate suppression, context assembly, prioritization, and human-routed escalation rather than recommendation memos, scheduling, execution, or retrospective investigation.
4. Use a research-governance scenario where continuous signals matter, such as benchmark-study disclosure, embargo, reproducibility, or dataset-rights risk alerts, so the example feels native to the existing research slice rather than compliance relabeling.
5. Preserve the pattern-first rule by grounding only against `risk-alert-triage` unless a genuine dependency issue appears.
6. After the next instance commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
7. Validate repository YAML with the existing uv-managed helper before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-045339`
- In-progress subagent scope: author one research-domain `risk-alert-triage` grounding as a single new instance file and commit it separately.
- Pending orchestrator follow-up: refresh execution memory so the new monitoring coverage is reflected in status, coverage tracking, the repository map, the dated iteration log, and the next-step plan.

## Constraints

- Keep the ontology pattern-first: add grounded instances only against existing canonical patterns rather than inventing new seed patterns.
- Treat `data/views/` as derived browse artifacts and keep any future updates aligned with stable vocabulary and pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer modest grounding batches that improve one thin family/domain slice rather than forcing a broad cross-family sweep.
- Keep governance, reversibility, privacy, and auditability explicit in grounded examples.
- Do not widen this iteration into pattern, vocabulary, or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

This iteration should add one research-domain `monitor-detect-triage` grounding to close the last open monitoring domain slice before the repository shifts back to broader architecture and risk-balancing work.
