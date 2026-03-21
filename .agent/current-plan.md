# Current Plan

## Iteration focus

Iteration `20260321-083459` is now scoped: the next highest-leverage gap is `gather-retrieve-synthesize`'s missing `critical` risk slice, so this iteration should add one tightly bounded crisis-briefing evidence-assembly pattern plus a few grounded instances without drifting into triage, recommendation, investigation, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans thirty-one patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `monitor-detect-triage`, `execute-automate`, `transform-process`, and `recommend-decide-escalate` sit at four
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred eight instance files now committed
- Phase 7: coverage refinement remains active, and the latest iteration closed `monitor-detect-triage`'s missing `low` risk slice while also adding representative `exception-gated-autonomy` coverage without drifting into anomaly review, recommendation, investigation, or execution
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Add one `gather-retrieve-synthesize` canonical pattern that fills the family's uncovered `critical` risk cell without duplicating `approval-packet-generation`, `research-synthesis-with-citation-verification`, or `change-triggered-context-briefing`.
2. Keep the new pattern bounded at time-sensitive evidence assembly, cross-source compression, provenance-preserving synthesis, and crisis-briefing handoff rather than alert triage, recommendation, investigation, or execution.
3. Add a small set of grounded Markdown instances linked to the new pattern in domains where critical-risk evidence assembly is plausible and governance-sensitive.
4. Update directly derived family and browse-view artifacts that reference the new canonical pattern so navigation stays synchronized with pattern truth.
5. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and `.agent/iterations/2026/20260321-083459.md` after the content batch so execution memory stays synchronized.
6. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-083459`
- Baseline context: iteration `20260321-082538` closed `monitor-detect-triage`'s uncovered `low` risk slice, leaving `gather-retrieve-synthesize` as the clearest next family-specific risk gap because it still lacks `critical` coverage.
- Planned subagent scope: add one bounded critical-risk synthesis pattern, create a few linked grounded instances, and synchronize the gather/synthesize family doc plus the directly affected browse views in one feature commit.
- Planned orchestrator follow-up: review the new critical-risk synthesis coverage shape, refresh status and matrix counts, validate YAML, and queue the next narrow gap after this family-specific closure.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep any next-step critical-risk synthesis work distinct from `risk-alert-triage`, `critical-signal-corroboration-triage`, `policy-constrained-escalation-routing`, and `incident-root-cause-analysis` by centering it on evidence assembly and briefing handoff rather than triage, route recommendation, deep diagnosis, or downstream execution.
- Treat synthesis work as in-family only when it ends at evidence assembly and briefing handoff rather than signal prioritization, route recommendation, collaborative drafting loops, or downstream execution.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `gather-retrieve-synthesize` with representative `critical` risk coverage via one bounded crisis-briefing synthesis anchor and a few grounded examples, while keeping the ontology pattern-first and the content batch modest.
