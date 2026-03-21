# Current Plan

## Iteration focus

Iteration `20260321-075051` is in progress: target the narrow `plan-coordinate-schedule` event-driven architecture gap with one trigger-driven coordination pattern that refreshes or reissues coordination state after authoritative scheduling conditions change, while also correcting any closely coupled derived-view drift discovered during scoping.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-seven patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the latest iteration closed the `transform-process` family's open event-driven slice while adding representative `exception-gated-autonomy` coverage without drifting into recommendation, approval adjudication, or execution
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one canonical `plan-coordinate-schedule` pattern centered on event-triggered coordination refresh or resynchronization after authoritative scheduling conditions change, keeping the output bounded at updated schedule state, participant coordination, and explicit human adoption checkpoints.
2. Ground the new pattern with a few representative instances in domains that reinforce the family's coordination boundary instead of reopening broad domain expansion.
3. Update all affected derived browse views, including `data/views/index-tree.yaml`, so the new planning pattern is represented and the previously discovered transform omission is corrected in the same consistency pass.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the content batch so execution memory stays synchronized.
5. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-075051`
- Baseline context: iteration `20260321-074055` closed the event-driven `transform-process` gap and left event-driven `plan-coordinate-schedule` as the clearest next family-specific architecture slice.
- Scope for this iteration: add one trigger-driven planning or coordination pattern plus a small grounding set, and repair coupled derived-view drift so pattern inventory and views stay aligned.
- Planned orchestrator follow-up: record the new planning coverage shape, refresh status and matrix counts, validate YAML, and queue the next narrow refinement based on the remaining uncovered family/architecture/risk combinations.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep the new planning pattern distinct from `calendar-conflict-coordination`, `schedule-adjustment-and-replanning`, `change-triggered-representation-refresh`, and `workflow-hand-off-and-completion` by centering it on authoritative-change coordination refresh rather than free-form replanning, data reshaping, or downstream completion.
- Treat trigger-driven planning work as in-family only when it stops at updated coordination artifacts, refreshed participant alignment, and visible human adoption boundaries rather than option adjudication or operational execution.

## Expected outcome

This iteration should leave `plan-coordinate-schedule` with representative event-driven coverage, fix the closely related derived-view inventory drift found during scoping, and keep the next step focused on another narrow uncovered architecture or risk slice rather than broad expansion.
