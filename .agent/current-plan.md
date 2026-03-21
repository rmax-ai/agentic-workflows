# Current Plan

## Iteration focus

Iteration `20260321-053410` is complete: it added `schedule-adjustment-and-replanning` as the second canonical pattern in `plan-coordinate-schedule`, giving that family a moderate-risk, recommendation-only, human-reviewed replanning anchor without drifting into recommendation or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans fifteen patterns across all nine top-level pattern families, with `plan-coordinate-schedule` now joining the already-strengthened multi-pattern families
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with `investigate-reconcile-verify`, `execute-automate`, and `human-agent-collaborative-work` still holding only one canonical pattern each
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, the remaining one-entry family docs, and neighboring canonical patterns before selecting the next thin structural cell.
2. Prefer the next bounded batch to add one second canonical pattern in either `execute-automate`, `investigate-reconcile-verify`, or `human-agent-collaborative-work`, with the strongest preference currently on `execute-automate`.
3. For the next content batch, aim to cover `exception-aware-orchestration` or another underrepresented execution slice without repeating the current `critical` risk and `approval-gated-execution` emphasis.
4. Keep derived browse views aligned with canonical pattern inventory, and verify view structure semantically as well as syntactically whenever a new pattern is inserted.
5. After the next content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
6. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-053410`
- Completed subagent scope: authored `data/patterns/plan-coordinate-schedule/schedule-adjustment-and-replanning.yaml` and updated the linked browse views in one focused content commit.
- Completed orchestrator follow-up: revalidated repository YAML and refreshed execution memory so pattern inventory, coverage tracking, the repository map, and the dated iteration log reflect the new planning-family anchor.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Treat `data/views/` as derived browse artifacts and keep updates aligned with stable vocabulary ids and canonical pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest, dependency-aware batch that strengthens one family without forcing schema, vocabulary, or instance churn in the same iteration.
- Keep governance, reversibility, privacy, and auditability explicit in the canonical pattern wording.
- Do not widen the next batch into vocabulary or schema changes unless a dependency issue makes that unavoidable.

## Expected outcome

The next iteration should likely add one carefully chosen second canonical pattern in another still-thin family, with a preference for broadening `execute-automate` beyond the current critical-risk, approval-gated anchor while preserving a crisp execution boundary.
