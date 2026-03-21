# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: resume Phase 7 structural refinement now that domain counts are balanced, preferring one thinner approval-bound neighboring slice outside the recently used `execute-automate`, `transform-process`, `recommend-decide-escalate`, `gather-retrieve-synthesize`, and `human-agent-collaborative-work` families.
- Selection rule: choose an already-canonical governance-heavy or approval-bound pattern whose domain metadata and derived browse exposure already align so the next batch can stay structurally neutral and instance-only unless real drift appears.
- Read-first set: this plan, the selected canonical pattern, one same-family neighboring instance in the target domain, one cross-domain neighboring instance in the same family, the relevant coverage notes in `.agent/coverage-matrix.yaml`, and the newest relevant files in `.agent/iterations/2026/`.
- Boundary rule: keep the next example centered on the selected pattern's primary governed artifact or bounded handoff and stop before adjudication, downstream execution, external communication, or policy reinterpretation.

## Current phase

- Phase 2 through Phase 6 are complete; Phase 7 coverage refinement is active.
- Phase 8 is now defined as the next breadth-expansion
  stage: add new patterns, newly justified domains, and
  their linked grounded instances only after Phase 7 closes
  the highest-leverage refinement pressure inside the current
  matrix.
- Canonical pattern coverage spans all nine pattern families, all tracked architecture types, and the full `low` / `moderate` / `high` / `critical` risk ladder.
- Grounded coverage spans all seven modeled domains at parity, so current balancing pressure has shifted away from trailing-domain counts and back toward thinner structural refinement targets.
- Browse artifacts remain derived from canonical pattern truth and should only change when a new grounding exposes genuine drift.
- The validation and publication baseline remains `uv run python scripts/python/validate_yaml.py`, `uv run python scripts/python/build_site_docs.py`, and `uv run mkdocs build`.

## Ordered tasks

1. Reassess the thinnest remaining approval-bound or governance-heavy neighboring slices in families that were not used in the last several instance-only passes, and pick one already-canonical target whose metadata and browse exposure already align.
2. Author a modest, structurally neutral refinement batch for that target, defaulting to one new grounded instance unless the selected slice clearly justifies a slightly broader but still dependency-safe batch.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, and `.agent/iterations/2026/20260322-004005.md` after verification.
5. Carry the next-step target forward toward Phase 7 closure by refining structurally thinner coverage notes rather than by chasing domain-count parity.

## Recent checkpoints

- `20260322-004005`: `workflow-hand-off-and-completion` gained additional `hr` grounding through `instances/hr/accepted-dependent-benefits-verification-review-closure-and-exception-tracker-synchronization.md`, restoring HR to thirty-five grounded examples through a structurally neutral, instance-only execute-family refinement bounded at authoritative post-decision closure and internal bookkeeping only.
- `20260322-003245`: `approval-gated-transformation-release` gained additional `engineering` grounding through `instances/engineering/build-artifact-catalog-schema-transformation-approved-for-system-inventory-intake.md`, restoring engineering to thirty-five grounded examples through a structurally neutral, instance-only transform-family refinement.
- `20260322-002355`: `policy-constrained-escalation-routing` gained additional `compliance` grounding through `instances/compliance/regulatory-incident-breach-notification-escalation-routing.md`, restoring compliance to thirty-five grounded examples through a structurally neutral, instance-only recommend-family escalation-routing refinement.
- `20260322-001611`: `approval-gated-briefing-release` gained additional `operations` grounding through `instances/operations/gateway-port-berth-closure-impact-briefing-revision-approved-for-marine-continuity-cell-circulation.md`, restoring operations to thirty-five grounded examples through a structurally neutral, instance-only gather-family release-control refinement.
- `20260322-001125`: `approval-gated-collaborative-artifact-release` gained additional `research` grounding through `instances/research/participant-consent-language-variance-clarification-packet-approved-for-human-subjects-ethics-pre-review-intake.md`, staying bounded at governed release of one exact collaborative artifact revision into one named ethics pre-review lane.

## History location

- Detailed iteration history: `.agent/iterations/2026/`
- Durable repository policy: `.agent/decisions.md`
- Broad inventory and coverage state: `.agent/ontology-status.yaml` and `.agent/coverage-matrix.yaml`
