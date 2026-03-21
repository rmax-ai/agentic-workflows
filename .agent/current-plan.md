# Current Plan

## Iteration focus

Iteration `20260321-092058` is now scoped around `recommend-decide-escalate`'s missing `critical` risk slice. The target batch should add one bounded critical-risk recommendation pattern plus a few linked grounded instances, while keeping the family's primary artifact a severe escalation route or decision-support packet rather than a collaboration loop, command-window plan, or executed system change.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage spans thirty-five patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `transform-process` sits at five, `gather-retrieve-synthesize`, `investigate-reconcile-verify`, `monitor-detect-triage`, `plan-coordinate-schedule`, and `recommend-decide-escalate` sit at four, and the remaining families sit at three or four.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred twenty instance files now committed.
- Phase 7: coverage refinement remains active, and `plan-coordinate-schedule` now joins `gather-retrieve-synthesize`, `transform-process`, `investigate-reconcile-verify`, `monitor-detect-triage`, and `execute-automate` in spanning the full tracked risk ladder.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.

## Ordered tasks

1. Add a single `recommend-decide-escalate` canonical pattern that fills the family's `critical` risk gap without collapsing into downstream adjudication, coordination, collaboration, or execution.
2. Ground that critical recommendation pattern with a few domain-varied Markdown instances that keep the human decision owner explicit and stop at governed route recommendation or decision-support packaging.
3. Synchronize only the directly affected family doc and derived browse views so navigation stays consistent with canonical pattern truth.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after the content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-092058`
- Planned scope: author one critical-risk `recommend-decide-escalate` anchor, add a few linked grounded instances, and realign only the family doc plus directly affected browse views in one feature commit.
- Coverage hypothesis: this batch should close the family's last missing risk-level cell while potentially adding `human-directed` autonomy coverage if the recommendation remains explicitly human-owned under severe consequence.
- Reflection placeholder: evaluate after the content batch whether the new recommendation pattern stayed cleanly bounded at route recommendation and packet assembly rather than drifting into collaboration or execution.
- Planned orchestrator follow-up: validate the new YAML state, synchronize `.agent/` memory, and then re-evaluate whether `optimize-adapt` or `human-agent-collaborative-work` is the next narrow uncovered `critical`-risk target.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat recommendation-family work as in-family only if the primary output remains a severe escalation route, governed option narrowing, or decision-support packet rather than a human collaboration loop, approved command timeline, or executed system change.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `recommend-decide-escalate` with representative `critical` risk coverage through one bounded high-consequence recommendation anchor and a small set of grounded examples, while keeping the ontology pattern-first and the batch modest.
