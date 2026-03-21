# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: continue Phase 7 structural refinement with an instance-only `approval-gated-triage-dispatch` batch in `hr`, adding a second HR grounding that materially changes the protected dispatch packet, hold model, and downstream review lane without reopening canonical pattern or browse assets.
- Selection rule: stay inside a pattern/domain pair that already has one grounding and vary the governed packet, reviewer boundary, and hold-state logic rather than renaming the same scenario with new nouns.
- Read-first set: this plan; `data/patterns/monitor-detect-triage/approval-gated-triage-dispatch.yaml`; the existing HR dispatch instance; one cross-domain dispatch neighbor such as the compliance or research example; the relevant coverage notes in `.agent/coverage-matrix.yaml`; and the newest relevant files in `.agent/iterations/2026/`, starting with `20260322-004621.md`.
- Boundary rule: keep the new HR example centered on one exact approval-gated dispatch boundary with explicit signer scope, hold visibility, and lineage, and stop before eligibility adjudication, worker or manager outreach, legal interpretation, or downstream review execution.

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

1. Author one materially distinct `approval-gated-triage-dispatch` instance in `instances/hr/` that keeps the workflow bounded at governed packet release into one restricted downstream review lane.
2. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
3. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, and `.agent/iterations/2026/20260322-005359.md` after verification.
4. Carry the next-step target forward toward Phase 7 closure by continuing to deepen thin approval-bound or governance-heavy slices in underused families rather than by restoring domain-count parity.

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
