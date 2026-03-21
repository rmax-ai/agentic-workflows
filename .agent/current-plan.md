# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: restore trailing-domain parity by adding one compliance grounding for the already-canonical `policy-constrained-escalation-routing` pattern in `recommend-decide-escalate`.
- Selection rule: keep the batch instance-only because the canonical pattern metadata and derived browse exposure already align for compliance.
- Read-first set: this plan, `data/patterns/recommend-decide-escalate/policy-constrained-escalation-routing.yaml`, `instances/operations/regional-cold-chain-compressor-failure-escalation-routing.md`, `instances/support/sovereign-cloud-storage-corruption-restricted-artifact-escalation-routing.md`, and the newest relevant iteration file under `.agent/iterations/2026/`.
- Boundary rule: keep the new example centered on governed authority-route recommendation plus escalation-packet assembly and stop before adjudication, regulator notification, external communication, or incident-response execution.

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

1. Author exactly one new compliance-grounded instance for `policy-constrained-escalation-routing` and keep the batch instance-only unless the example exposes real canonical or browse drift.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, the relevant status files, and one new `.agent/iterations/2026/<timestamp>.md` record after verification.
5. Keep publication tooling and deployment workflow aligned only when helper tooling or build outputs genuinely change.

## Recent checkpoints

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
