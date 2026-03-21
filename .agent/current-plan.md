# Current Plan

## Iteration focus

Iteration `20260321-084930` is now scoped around `transform-process`'s missing `critical` risk slice. The goal is to add one bounded canonical transform pattern plus a few grounded instances that cover high-consequence representation handling and review-safe handoff without drifting into recommendation, investigation, or execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Phase 5: canonical coverage spans thirty-two patterns across all nine top-level pattern families, and every top-level family now has at least three canonical patterns while `gather-retrieve-synthesize`, `monitor-detect-triage`, `execute-automate`, `transform-process`, and `recommend-decide-escalate` sit at four
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred eleven instance files now committed
- Phase 7: coverage refinement remains active, and the latest closed gap was `gather-retrieve-synthesize`'s `critical` risk slice; the current bounded refinement target is `transform-process`'s still-open `critical` cell
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path

## Ordered tasks

1. Author one `transform-process` canonical pattern that fills the family's missing `critical` risk slice while staying centered on high-consequence representation handling, review-safe packaging, and explicit lineage.
2. Ground that pattern with a small, domain-diverse set of linked instances that reinforce transform boundaries instead of crossing into recommendation, adjudication, or execution.
3. Synchronize the directly affected family doc and derived browse views so canonical inventory, risk placement, and family guidance stay aligned.
4. Continue validating repository YAML with `uv run python scripts/python/validate_yaml.py` after the content batch before closing the iteration.

## Iteration checkpoint

- Timestamp: `20260321-084930`
- Scoped content batch: add one `transform-process` canonical pattern for a `critical` risk slice, 2-3 linked grounded instances, and only the directly affected family/view updates required to keep derived navigation aligned.
- Coverage hypothesis: `transform-process` can plausibly gain `critical` coverage through a bounded pattern for emergency-safe representation handling, restricted rendering, or channel-safe packaging where the main output remains a governed transformed artifact rather than a recommendation or action.
- Reflection status: pending until the content batch and validation finish.
- Planned orchestrator follow-up: validate the refreshed repository state, synchronize `.agent/` memory, and re-evaluate the next narrow uncovered cell after this family-specific refinement lands.

## Constraints

- Keep the ontology pattern-first: choose the expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer a modest, dependency-aware batch that strengthens one family with one new pattern and a few instances rather than reopening broad expansion.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep this critical-risk refinement distinct from adjacent families by centering it on transformed artifact safety, restricted rendering, lineage, and reviewable handoff rather than triage, route recommendation, deep diagnosis, or downstream execution.
- Treat transform work as in-family only when the primary output is a changed representation or package rather than a brief, verdict, schedule, decision, or executed system change.
- Prefer one modest batch with one new canonical pattern and a few instances over broad family expansion.

## Expected outcome

This iteration should leave `transform-process` with representative `critical` risk coverage via one bounded high-consequence transformation anchor and a small set of grounded examples, while keeping the ontology pattern-first and the content batch modest.
