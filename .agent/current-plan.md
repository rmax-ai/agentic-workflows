# Current Plan

## Iteration focus

Iteration `20260321-063819` is complete: `control-requirement-attestation-recommendation` now extends `recommend-decide-escalate` with a low-risk attestation-guidance pattern plus new engineering, finance, and compliance grounding.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans twenty-one patterns across all nine top-level pattern families, and every top-level family now has at least two canonical patterns
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains
- Phase 7: coverage refinement remains active, and the newest attestation-guidance work further shifts the next highest-leverage gap away from missing low-risk recommendation coverage and toward narrower family-specific architecture and governance slices
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Re-read `.agent/coverage-matrix.yaml`, `.agent/ontology-status.yaml`, and the `gather-retrieve-synthesize` plus `monitor-detect-triage` family docs before choosing the next narrow Phase 7 refinement now that the low-risk recommendation slice is covered.
2. Prefer the next iteration to compare two similarly bounded follow-ons: a low-risk `gather-retrieve-synthesize` pattern or a moderate-risk `monitor-detect-triage` pattern, and pick the cleaner family boundary rather than reopening broad expansion.
3. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and the dated iteration log after the next content batch so execution memory stays synchronized.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing each iteration.

## Iteration checkpoint

- Timestamp: `20260321-063819`
- Baseline context: prior iteration `20260321-062746` completed moderate-risk, event-driven readiness-disposition coverage for `recommend-decide-escalate`, leaving low-risk recommendation support as the cleanest remaining in-family risk gap.
- Completed subagent scope: added `control-requirement-attestation-recommendation`, grounded it with engineering, finance, and compliance instances, updated the affected browse views, and validated repository YAML successfully.
- Planned orchestrator follow-up: record the new low-risk recommendation coverage, then use `gather-retrieve-synthesize` low-risk and `monitor-detect-triage` moderate-risk as the first two candidate gap slices for the next dependency-safe refinement step.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new instance.
- Keep any follow-on `recommend-decide-escalate` work distinct from `risk-alert-triage`, `approval-centered-collaboration`, `calendar-conflict-coordination`, and `workflow-hand-off-and-completion` by centering it on governed decision support rather than alert intake, review-loop collaboration, scheduling, or downstream closure.

## Expected outcome

The next iteration should move to another narrow family-specific architecture or governance slice, with low-risk `gather-retrieve-synthesize` and moderate-risk `monitor-detect-triage` now the leading candidates because `recommend-decide-escalate` has representative low-, moderate-, and high-risk recommendation coverage without reopening broader repository scaffolding.
