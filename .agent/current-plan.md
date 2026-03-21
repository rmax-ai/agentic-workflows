# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: restore trailing-domain parity with one more instance-only pass in a remaining trailing domain (`engineering` or `hr`) while preferring a different family than the just-used `recommend-decide-escalate`, the just-before-that `gather-retrieve-synthesize`, and the recently used `human-agent-collaborative-work`.
- Selection rule: choose an already-canonical approval-bound or otherwise governance-heavy slice whose domain metadata and derived browse exposure already align so the next batch can stay structurally neutral.
- Read-first set: this plan, the selected canonical pattern, one same-domain neighboring instance, one cross-domain neighboring instance, and the most recent relevant files in `.agent/iterations/2026/`.
- Boundary rule: keep the next example centered on the pattern's primary artifact boundary and stop before adjudication, downstream execution, external communication, or policy reinterpretation.

## Current phase

- Phase 2 through Phase 6 are complete; Phase 7 coverage refinement is active.
- Phase 8 is now defined as the next breadth-expansion
  stage: add new patterns, newly justified domains, and
  their linked grounded instances only after Phase 7 closes
  the highest-leverage refinement pressure inside the current
  matrix.
- Canonical pattern coverage spans all nine pattern families, all tracked architecture types, and the full `low` / `moderate` / `high` / `critical` risk ladder.
- Grounded coverage spans all seven modeled domains; current balancing pressure is on the trailing domains rather than on opening new structural work.
- Browse artifacts remain derived from canonical pattern truth and should only change when a new grounding exposes genuine drift.
- The validation and publication baseline remains `uv run python scripts/python/validate_yaml.py`, `uv run python scripts/python/build_site_docs.py`, and `uv run mkdocs build`.

## Ordered tasks

1. Reassess the remaining trailing domains and pick one equally bounded already-canonical slice whose metadata and derived browse mapping already align.
2. Author exactly one new grounded instance and keep the batch instance-only unless the new example exposes real canonical or browse drift.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, the relevant status files, and one new `.agent/iterations/2026/<timestamp>.md` record after verification.
5. Keep publication tooling and deployment workflow aligned only when helper tooling or build outputs genuinely change.

## Recent checkpoints

- `20260322-002355`: `policy-constrained-escalation-routing` gained additional `compliance` grounding through `instances/compliance/regulatory-incident-breach-notification-escalation-routing.md`, restoring compliance to thirty-five grounded examples through a structurally neutral, instance-only recommend-family escalation-routing refinement.
- `20260322-001611`: `approval-gated-briefing-release` gained additional `operations` grounding through `instances/operations/gateway-port-berth-closure-impact-briefing-revision-approved-for-marine-continuity-cell-circulation.md`, restoring operations to thirty-five grounded examples through a structurally neutral, instance-only gather-family release-control refinement.
- `20260322-001125`: `approval-gated-collaborative-artifact-release` gained additional `research` grounding through `instances/research/participant-consent-language-variance-clarification-packet-approved-for-human-subjects-ethics-pre-review-intake.md`, staying bounded at governed release of one exact collaborative artifact revision into one named ethics pre-review lane.
- `20260322-000846`: defined Phase 8 as pattern,
  domain, and linked-instance breadth expansion after
  Phase 7, added Phase 9 as the follow-on
  architecture/governance/consistency deepening stage,
  and aligned backlog, ontology status, prompt guidance,
  and decisions memory with that sequencing.
- `20260321-231804`: `policy-constrained-escalation-routing` gained a first support grounding through `instances/support/sovereign-cloud-storage-corruption-restricted-artifact-escalation-routing.md`, staying bounded at authority-route recommendation and escalation-packet assembly.
- `20260321-231247`: `approval-gated-briefing-release` gained additional finance grounding through `instances/finance/quarter-close-earnings-sensitivity-briefing-revision-approved-for-disclosure-committee-circulation.md`, staying bounded at governed release of one exact briefing revision into one named visibility lane.
- `20260321-230743`: `approval-gated-recommendation-release` gained additional engineering grounding through `instances/engineering/build-provenance-exception-recommendation-packet-revision-approved-for-release-integrity-council-decision-lane.md`, staying bounded at governed release of one exact recommendation packet revision into one named decision lane.

## History location

- Detailed iteration history: `.agent/iterations/2026/`
- Durable repository policy: `.agent/decisions.md`
- Broad inventory and coverage state: `.agent/ontology-status.yaml` and `.agent/coverage-matrix.yaml`
