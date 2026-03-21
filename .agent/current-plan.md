# Current Plan

## Iteration focus

Iteration `20260321-082538` is now scoped: the highest-leverage narrow gap is still `monitor-detect-triage`'s missing `low` risk slice, so this iteration should add one bounded low-stakes monitoring pattern plus a few grounded examples without drifting into briefing, recommendation, investigation, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans thirty patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `execute-automate`, `transform-process`, and `recommend-decide-escalate` sit at four
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred five instance files now committed
- Phase 7: coverage refinement remains active, and the latest iteration closed `execute-automate`'s missing `high` risk slice while also adding representative `exception-gated-autonomy` coverage without drifting into recommendation, approval adjudication, or low-risk closure
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one new `monitor-detect-triage` canonical pattern that fills the family's uncovered `low` risk cell without duplicating `risk-alert-triage`, `anomaly-detection-review`, or `critical-signal-corroboration-triage`.
2. Keep the new monitoring pattern bounded at explainable watchlisting, low-stakes signal review, or noise suppression rather than contextual briefing, recommendation, verification, investigation, or execution.
3. Ground the new pattern with a small cross-domain set of Markdown instances that show low-stakes monitoring value in routine but still stateful environments.
4. Update the coupled family doc and derived browse views so the new pattern appears consistently across family, index, architecture, autonomy, domain, and risk navigation.
5. Refresh `.agent/current-plan.md`, `.agent/backlog.yaml`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the content batch so execution memory stays synchronized.
6. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-082538`
- Baseline context: iteration `20260321-081148` closed `execute-automate`'s uncovered `high` risk slice, leaving `monitor-detect-triage` as the clearest remaining family-specific risk gap.
- Scoped subagent objective: add one low-risk monitoring pattern with a few grounded instances and synchronize the family doc plus derived views in the same commit-sized batch.
- Planned orchestrator follow-up: record the new monitoring coverage shape, refresh status and matrix counts, validate YAML, and queue the next highest-leverage narrow gap after this low-risk monitoring slice is filled.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep any follow-on `monitor-detect-triage` work distinct from `change-triggered-context-briefing`, `policy-constrained-escalation-routing`, `claimed-state-verification`, and `risk-alert-triage` by centering it on bounded low-stakes signal review, explainable watchlisting, or noise suppression rather than contextual briefing, route recommendation, deep verification, or urgent high-risk triage.
- Treat monitoring work as in-family only when it ends at queueing, watchlisting, or attention routing rather than recommendation adjudication, collaborative drafting, or downstream execution.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `monitor-detect-triage` with representative low-risk coverage through one cleanly bounded monitoring pattern and a few linked instances, reducing the remaining global gaps to narrower architecture or critical-risk slices in other families.
