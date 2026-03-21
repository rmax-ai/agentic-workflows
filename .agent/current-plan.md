# Current Plan

## Iteration focus

Iteration `20260321-074055` will target the next narrow `transform-process` gap by adding one event-driven representation-refresh pattern plus a small set of grounded instances. The goal is to cover trigger-based reshaping without drifting into recommendation, approval adjudication, or downstream execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-six patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the latest iteration closed the `transform-process` family's open high-risk slice while adding representative `approval-gated`, `human-in-the-loop`, and `orchestrated-multi-agent` coverage without drifting into recommendation, approval adjudication, or execution
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add a trigger-driven `transform-process` pattern centered on refreshing or re-materializing a staged structured representation when upstream source state changes.
2. Keep the new pattern distinct from `document-to-structured-data-handoff`, `normalization-and-enrichment`, and `batch-content-transformation` by making source-change detection the entry condition and reviewed downstream-safe representation refresh the terminal state.
3. Ground the new pattern with a few instances in domains where source changes regularly invalidate previously staged representations.
4. Update derived browse views touched by the new canonical metadata so architecture, risk, autonomy, and domain indexes stay aligned.
5. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the content batch, then validate repository YAML with `uv run python scripts/python/validate_yaml.py`.

## Iteration checkpoint

- Timestamp: `20260321-074055`
- Baseline context: iteration `20260321-073210` closed the high-risk governed batch transformation gap and left event-driven `transform-process` coverage as the clearest remaining family-specific architecture slice.
- Planned subagent scope: add one event-driven transform pattern, wire it into the derived browse views, and ground it with a small set of change-triggered staged-representation examples.
- Planned orchestrator follow-up: record the new transform coverage shape, refresh status and matrix counts, validate YAML, and queue the next narrow refinement based on the remaining uncovered family/architecture combinations.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep any follow-on `transform-process` expansion distinct from `document-to-structured-data-handoff`, `normalization-and-enrichment`, `approval-packet-generation`, and `browser-based-form-completion-with-approval-gates` by centering it on governed representation change rather than recommendation packaging or downstream action.
- Treat de-identification, redaction, or other sensitive-lossiness work as transform scope only when the pattern ends at a reviewed staging package or release-safe representation rather than an external publication or operational change.

## Expected outcome

This iteration should close the event-driven `transform-process` gap with one clearly bounded refresh-oriented pattern and a few grounded examples, leaving the repository with stronger architecture and autonomy coverage without reopening broad family expansion.
