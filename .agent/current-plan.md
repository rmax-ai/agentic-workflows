# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: restore domain parity with one instance-only pass in the trailing `research` domain through `approval-gated-collaborative-artifact-release`.
- Selection rule: keep the batch structurally neutral by staying inside a pattern/domain slice already listed in canonical metadata and already exposed under `data/views/by-domain.yaml`.
- Read-first set: this plan, `data/patterns/human-agent-collaborative-work/approval-gated-collaborative-artifact-release.yaml`, the same-domain neighbor `instances/research/benchmark-claim-clarification-packet-approved-for-publication-integrity-review-intake.md`, the cross-domain neighbors `instances/engineering/payments-tokenization-exception-packet-approved-for-architecture-review-intake.md` and `instances/hr/protected-leave-return-to-work-exception-packet-approved-for-occupational-health-review-intake.md`, and the most recent relevant files in `.agent/iterations/2026/`.
- Boundary rule: keep the new example centered on governed release of one collaborative artifact revision into one bounded review lane; stop before adjudication, downstream execution, external communication, or policy reinterpretation.

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

1. Author exactly one new `research`-grounded instance for `approval-gated-collaborative-artifact-release` and keep the batch instance-only unless the new example exposes real canonical or browse drift.
2. Validate that `research` moves back into parity with the current leading domains without reopening Phase 8 breadth work.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, the relevant status files, and one new `.agent/iterations/2026/<timestamp>.md` record after verification.
5. Keep publication tooling and deployment workflow aligned only when helper tooling or build outputs genuinely change.

## Recent checkpoints

- `20260322-000846`: defined Phase 8 as pattern,
  domain, and linked-instance breadth expansion after
  Phase 7, added Phase 9 as the follow-on
  architecture/governance/consistency deepening stage,
  and aligned backlog, ontology status, prompt guidance,
  and decisions memory with that sequencing.
- `20260322-000318`: completed the `.agent`
  memory-structure cleanup by sharding `.agent/repo-map.md`
  into a compact index plus four on-demand detail files,
  recording D-0015, and aligning AGENTS plus `.agent`
  prompts/docs around index-first reading for both
  decisions and repo-map.
- `20260321-231804`: `policy-constrained-escalation-routing` gained a first support grounding through `instances/support/sovereign-cloud-storage-corruption-restricted-artifact-escalation-routing.md`, staying bounded at authority-route recommendation and escalation-packet assembly.
- `20260321-231247`: `approval-gated-briefing-release` gained additional finance grounding through `instances/finance/quarter-close-earnings-sensitivity-briefing-revision-approved-for-disclosure-committee-circulation.md`, staying bounded at governed release of one exact briefing revision into one named visibility lane.
- `20260321-230743`: `approval-gated-recommendation-release` gained additional engineering grounding through `instances/engineering/build-provenance-exception-recommendation-packet-revision-approved-for-release-integrity-council-decision-lane.md`, staying bounded at governed release of one exact recommendation packet revision into one named decision lane.

## History location

- Detailed iteration history: `.agent/iterations/2026/`
- Durable repository policy: `.agent/decisions.md`
- Broad inventory and coverage state: `.agent/ontology-status.yaml` and `.agent/coverage-matrix.yaml`
