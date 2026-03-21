# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: continue Phase 7 structural refinement by shifting from the now-deepened plan-family contingency slice to one thinner approval-bound monitor or investigate slice, preferably `approval-gated-triage-dispatch` or `evidence-gated-verification-for-release` in a domain already exposed by canonical metadata and browse views.
- Selection rule: choose a pattern/domain pair that already has one grounding so the next batch can remain instance-only while materially varying the governed packet, hold model, or release boundary rather than repeating the same scenario with new nouns.
- Read-first set: this plan, the selected canonical pattern, one same-domain same-pattern neighbor, one cross-domain same-pattern neighbor, the relevant coverage notes in `.agent/coverage-matrix.yaml`, and the newest relevant files in `.agent/iterations/2026/`, starting with `20260322-004621.md`.
- Boundary rule: keep the next example centered on one exact approval, dispatch, or verification boundary with explicit holds and lineage, and stop before adjudication, downstream execution, external communication, or policy reinterpretation.

## Current phase

- Phase 2 through Phase 6 are complete; Phase 7 coverage refinement is active.
- Phase 8 is now defined as the next breadth-expansion
  stage: add new patterns, newly justified domains, and
  their linked grounded instances only after Phase 7 closes
  the highest-leverage refinement pressure inside the current
  matrix.
- Canonical pattern coverage spans all nine pattern families, all tracked architecture types, and the full `low` / `moderate` / `high` / `critical` risk ladder.
- Grounded coverage now spans two hundred forty-six examples across all seven modeled domains; compliance is temporarily at thirty-six while engineering, finance, hr, operations, research, and support remain at thirty-five, confirming that Phase 7 can tolerate light asymmetry when it deepens structurally thinner slices.
- Browse artifacts remain derived from canonical pattern truth and should only change when a new grounding exposes genuine drift.
- The validation and publication baseline remains `uv run python scripts/python/validate_yaml.py`, `uv run python scripts/python/build_site_docs.py`, and `uv run mkdocs build`.

## Ordered tasks

1. Reassess thin approval-bound candidates in `monitor-detect-triage` and `investigate-reconcile-verify`, preferring a domain already exposed in canonical metadata so the next batch can remain instance-only.
2. Author one materially distinct grounded example for the selected pattern/domain pair, with explicit hold-state and boundary language that stays cleanly inside the chosen pattern.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, and the next dated iteration record after verification.
5. Carry the next-step target forward toward Phase 7 closure by continuing to deepen thin approval-bound or governance-heavy slices in underused families rather than by restoring domain-count parity.

## Recent checkpoints

- `20260322-004621`: `contingency-plan-activation-gate` gained additional `compliance` grounding through `instances/compliance/serious-adverse-event-manual-intake-continuity-activation-gate.md`, raising the repository to two hundred forty-six grounded examples through a structurally neutral, instance-only plan-family refinement bounded at approval-gated continuity-readiness planning rather than live fallback activation or safety-case intake execution.
- `20260322-004005`: `workflow-hand-off-and-completion` gained additional `hr` grounding through `instances/hr/accepted-dependent-benefits-verification-review-closure-and-exception-tracker-synchronization.md`, restoring HR to thirty-five grounded examples through a structurally neutral, instance-only execute-family refinement bounded at authoritative post-decision closure and internal bookkeeping only.
- `20260322-003245`: `approval-gated-transformation-release` gained additional `engineering` grounding through `instances/engineering/build-artifact-catalog-schema-transformation-approved-for-system-inventory-intake.md`, restoring engineering to thirty-five grounded examples through a structurally neutral, instance-only transform-family refinement.
- `20260322-002355`: `policy-constrained-escalation-routing` gained additional `compliance` grounding through `instances/compliance/regulatory-incident-breach-notification-escalation-routing.md`, restoring compliance to thirty-five grounded examples through a structurally neutral, instance-only recommend-family escalation-routing refinement.
- `20260322-001611`: `approval-gated-briefing-release` gained additional `operations` grounding through `instances/operations/gateway-port-berth-closure-impact-briefing-revision-approved-for-marine-continuity-cell-circulation.md`, restoring operations to thirty-five grounded examples through a structurally neutral, instance-only gather-family release-control refinement.

## History location

- Detailed iteration history: `.agent/iterations/2026/`
- Durable repository policy: `.agent/decisions.md`
- Broad inventory and coverage state: `.agent/ontology-status.yaml` and `.agent/coverage-matrix.yaml`
