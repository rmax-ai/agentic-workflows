# Current Plan

## Iteration focus

Iteration `20260321-054920` is complete: it added `authoritative-record-reconciliation` as the second canonical pattern in `investigate-reconcile-verify`, giving that family a moderate-risk, bounded-delegation, record-reconciliation anchor that stays distinct from the diagnosis-heavy `incident-root-cause-analysis` pattern.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans seventeen patterns across all nine top-level pattern families, with `investigate-reconcile-verify` now joining the already-strengthened multi-pattern families
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with `human-agent-collaborative-work` now the only remaining one-entry family
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, `docs/patterns/human-agent-collaborative-work.md`, and `data/patterns/human-agent-collaborative-work/analyst-copilot-loop.yaml` before selecting the next thin structural cell.
2. Prefer the next bounded batch to add one second canonical pattern in `human-agent-collaborative-work`, ideally covering a structurally distinct mixed-initiative workflow rather than another generic drafting copilot.
3. Keep derived browse views aligned with canonical pattern inventory, and spot-check domain, architecture, autonomy, and risk buckets against the source YAML whenever a new pattern is inserted.
4. After the next content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory continues to match repository reality.
5. Validate repository YAML with the existing uv-managed helper before closing the next iteration.

## Iteration checkpoint

- Timestamp: `20260321-054920`
- Completed subagent scope: authored `data/patterns/investigate-reconcile-verify/authoritative-record-reconciliation.yaml` and updated the linked browse views in one focused content commit.
- Completed orchestrator follow-up: corrected a few derived-view bucket mismatches, revalidated repository YAML, and refreshed execution memory so pattern inventory, coverage tracking, the repository map, and the dated iteration log reflect the new investigation-family anchor.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Treat `data/views/` as derived browse artifacts and keep updates aligned with stable vocabulary ids and canonical pattern ids.
- Ensure every subagent task ends with exactly one git commit.
- Prefer a modest, dependency-aware batch that strengthens one family without forcing schema, vocabulary, or instance churn in the same iteration.
- Keep governance, reversibility, privacy, and auditability explicit in the canonical pattern wording.
- Do not widen the next batch into vocabulary or schema changes unless a dependency issue makes that unavoidable.
- Keep the next human-agent pattern distinct from `analyst-copilot-loop` by centering it on another collaboration shape such as negotiated planning, evidence review, or explicit handoff control rather than generic co-drafting.

## Expected outcome

The next iteration should likely add one carefully chosen second canonical pattern in `human-agent-collaborative-work`, broadening that family beyond the current analyst copilot anchor while preserving a crisp mixed-initiative collaboration boundary.
