# Current Plan

## Iteration focus

Iteration `20260321-045924` will add one second canonical pattern in `gather-retrieve-synthesize` so the repository improves thin structural coverage instead of widening domain-first grounding. The targeted gap is the currently empty `orchestrated-multi-agent` architecture cell outside `investigate-reconcile-verify`, with a secondary goal of improving sparse `high` risk coverage outside the current investigation, monitoring, and recommendation anchors.

## Current phase

- Phase 2: controlled vocabularies are complete, including the `transform-process` mapping term `structured-representation-transformation`
- Phase 3: navigation views are complete and reference canonical patterns in all nine top-level families
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical seed coverage spans all nine top-level pattern families, but most families still have only one canonical pattern
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, with the highest-leverage gaps now centered on thin architecture and risk cells rather than family/domain presence
- Tooling baseline: uv-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one reusable `gather-retrieve-synthesize` pattern that stays inside the family boundary by ending in a governed packet or brief rather than a recommendation or execution step.
2. Prefer `approval-packet-generation` as the bounded canonical addition because it can legitimately use `orchestrated-multi-agent` specialization for retrieval, evidence assembly, and verification while keeping the output inspectable and human-reviewed.
3. Update the derived browse views so the new pattern appears in the pattern-first tree and in the relevant architecture, autonomy, risk, and domain views.
4. Re-run `uv run python scripts/python/validate_yaml.py` before closing the iteration.
5. After the content commit, refresh `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log so execution memory matches repository reality.

## Iteration checkpoint

- Timestamp: `20260321-045924`
- Planned subagent scope: author one new canonical `gather-retrieve-synthesize` pattern and the linked browse-view updates in a single focused commit.
- Planned orchestrator follow-up: refresh execution memory to reflect the expanded canonical pattern inventory and the newly covered architecture/risk cells.

## Constraints

- Keep the ontology pattern-first: do not widen this batch into new grounded instances, vocabulary edits, or schema changes unless a hard dependency issue appears.
- Preserve the `gather-retrieve-synthesize` family boundary by ending the pattern at packet generation and human review rather than downstream approval decisions or operational execution.
- Treat `data/views/` as derived browse artifacts and keep them aligned with stable pattern ids and existing family order.
- Ensure the subagent task ends with exactly one git commit.
- Keep governance, provenance, privacy, and auditability explicit because this pattern intentionally raises the family's risk posture.

## Expected outcome

At the end of this iteration, the repository should have a second `gather-retrieve-synthesize` canonical pattern, improved `orchestrated-multi-agent` and `high` risk coverage in that family, updated browse views, validated YAML, and refreshed execution memory describing the new structural coverage.
