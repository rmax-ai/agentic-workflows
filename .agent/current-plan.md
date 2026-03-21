# Current Plan

## Iteration focus

Iteration `20260321-070112` is in progress: the next bounded Phase 7 refinement is a moderate-risk `monitor-detect-triage` addition that should fill the family's canonical `tool-using-single-agent` and `bounded-delegation` gap without drifting into investigation or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-two patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the current iteration is intentionally scoped to one moderate-risk `monitor-detect-triage` slice that also strengthens the family's canonical architecture and autonomy coverage
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one moderate-risk `monitor-detect-triage` pattern that stays centered on explainable mid-severity monitoring and governed routing rather than critical corroboration, downstream investigation, or execution.
2. Prefer a pattern shape that canonically covers the family's still-open `tool-using-single-agent` and `bounded-delegation` slices while remaining compatible with `event-driven-monitoring` and `human-in-the-loop`.
3. Ground the new pattern with a small linked instance batch in domains that are still thin at the canonical monitor-pattern layer, then refresh the directly affected browse views.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the content batch so execution memory stays synchronized.
5. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-070112`
- Baseline context: iteration `20260321-065119` closed the low-risk gather/context-briefing gap, leaving a moderate-risk monitor refinement as the cleanest narrow follow-on step.
- Current subagent scope: author one new canonical `monitor-detect-triage` pattern plus a few linked instances and directly affected browse-view updates, with a bias toward the family's still-open `tool-using-single-agent` and `bounded-delegation` slices.
- Planned orchestrator follow-up: review the monitor refinement batch, validate repository YAML, then record the new coverage state and choose the next narrow Phase 7 gap.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep the new `monitor-detect-triage` work distinct from `risk-alert-triage`, `critical-signal-corroboration-triage`, `incident-root-cause-analysis`, and `exception-aware-task-execution` by centering it on explainable mid-severity monitoring and governed routing rather than critical corroboration, investigation, or downstream response.

## Expected outcome

This iteration should leave `monitor-detect-triage` with explicit moderate-risk canonical coverage and stronger architecture/autonomy representation without reopening broad repository scaffolding.
