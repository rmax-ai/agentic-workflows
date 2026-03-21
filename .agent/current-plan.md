# Current Plan

## Iteration focus

Iteration `20260321-110310` is now in progress: target the remaining `approval-gated-execution` gap in `monitor-detect-triage` with one family-safe pattern that gates triage dispatch without drifting into downstream recommendation or response execution.

## Current phase

- Phase 2: controlled vocabularies are complete and stable enough for bounded Phase 7 refinement.
- Phase 3: navigation views are complete and should remain derived from canonical pattern inventory.
- Phase 4: top-level family overview docs are complete under `docs/patterns/`.
- Phase 5: canonical coverage now spans forty-four patterns across all nine top-level pattern families. `recommend-decide-escalate` and `transform-process` now each sit at six canonical patterns; `investigate-reconcile-verify`, `optimize-adapt`, `plan-coordinate-schedule`, and `execute-automate` remain at five; and `gather-retrieve-synthesize`, `monitor-detect-triage`, and `human-agent-collaborative-work` remain at four. Future additions should remain narrow and land only where a remaining autonomy or architecture gap maps to a genuinely reusable workflow shape.
- Phase 6: grounded instances cover all nine families across all seven currently modeled domains, with one hundred forty-six instance files now committed.
- Phase 7: coverage refinement remains active, all nine top-level families span the full tracked `low` / `moderate` / `high` / `critical` risk ladder, `transform-process` now spans all tracked architecture types, and `monitor-detect-triage` is the next candidate for closing its remaining architecture gap.
- Tooling baseline: `uv`-managed Python 3.14 helper workflow remains the validation path.
- Derived-view baseline: browse artifacts should continue to follow canonical pattern truth, especially when autonomy or architecture classifications change during refinement work.
- Current refinement target: the remaining obvious structural holes are the still-empty `approval-gated-execution` cells in `gather-retrieve-synthesize`, `monitor-detect-triage`, `recommend-decide-escalate`, `optimize-adapt`, and `human-agent-collaborative-work`; this iteration is scoped only to `monitor-detect-triage` because approval-gated dispatch of a triaged packet appears to be the cleanest next reusable shape.

## Ordered tasks

1. Add one `monitor-detect-triage` canonical pattern for approval-gated dispatch of an already-triaged packet, keeping the family boundary at governed routing release rather than downstream recommendation or action.
2. Ground that pattern with two or three linked instances in domains where severe triage dispatch routinely requires explicit approval before escalation queues or crisis channels activate.
3. Update the family doc, derived browse views, and `.agent/` execution memory, then validate repository YAML with `uv run python scripts/python/validate_yaml.py`.

## Iteration checkpoint

- Timestamp: `20260321-110310`
- Planned scope: add one approval-gated routing pattern under `monitor-detect-triage`, link a small cross-domain instance batch, update the monitor family doc, and refresh the derived index, domain, architecture, autonomy, and risk views.
- Working hypothesis: the clean family-safe stop point is a triage packet plus explicit approval gate and dispatch manifest, where approval releases downstream routing without auto-triggering the investigation, recommendation, or execution workflows that follow.
- Reflection target: confirm that the new pattern remains about governed dispatch of already-triaged work, not about deciding the response or performing it.

## Constraints

- Keep the ontology pattern-first: choose the next expansion because it fills a structural coverage gap, not because a domain example sounds appealing.
- Ensure every subagent task ends with exactly one git commit and leaves no unrelated file churn behind.
- Prefer one modest normalization batch over broader family expansion whenever derived views or execution memory drift from canonical pattern data.
- Keep governance, reversibility, privacy, and auditability explicit in every new pattern and instance.
- Keep future critical-risk refinements centered on each target family's own primary artifact boundary rather than letting severe workflows collapse into adjacent families.
- Treat future transform-family additions as in-family only if the primary artifact remains a transformed package, lineage trace, explicit hold state, or approval/release manifest rather than a crisis brief, evidence verdict, recommendation, or downstream execution step.
- Treat collaboration-family work as in-family only if the primary output remains a critical shared artifact, explicit approval-readiness collaboration loop, or human-owned joint work surface rather than authority choice, command sequencing, or executed action.
- Treat future recommendation-family additions as in-family only if the output remains a bounded recommendation or narrowed option set inside delegated authority limits; anything that resolves the approval itself or commits the downstream change belongs in an adjacent family.
- Treat future optimize-family batches as in-family only if the main output remains an adaptive optimization-state change, sampled-policy adjustment, or bounded self-tuning artifact rather than alert triage, recommendation, scheduling, or executed operational change.
- Treat future monitor-family additions as in-family only if the output remains watchlisting, anomaly packet assembly, or triage routing; anything that binds approval to downstream action or settles truth should stay in an adjacent family.
- Treat this iteration's monitor-family addition as valid only if approval governs the release of a triaged packet into a downstream queue or command channel while leaving response selection, authority choice, and operational action to adjacent patterns.

## Expected outcome

This iteration should leave the repository with one more family-safe structural slice covered only if the added pattern is as clean and reusable as `approval-gated-transformation-release`, with browse views and `.agent/` memory synchronized to that canonical truth.
