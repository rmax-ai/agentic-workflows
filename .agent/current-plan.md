# Current Plan

This file is the rolling control document for the next bounded batch. Detailed execution history lives under `.agent/iterations/<year>/`.

## Iteration focus

- Active target: restore domain parity with one instance-only pass in a trailing domain (`engineering`, `compliance`, `operations`, `research`, or `hr`), preferably in a different family than `recommend-decide-escalate`.
- Selection rule: choose an already-canonical high-governance or approval-bound slice whose domain metadata and derived browse exposure already align so the batch can stay structurally neutral.
- Read-first set: this plan, the selected canonical pattern, one same-domain neighboring instance, one cross-domain neighboring instance, and the most recent relevant files in `.agent/iterations/2026/`.
- Boundary rule: keep the new example centered on the pattern's primary artifact boundary; stop before adjudication, downstream execution, external communication, or policy reinterpretation.

## Current phase

- Phase 2 through Phase 6 are complete; Phase 7 coverage refinement is active.
- Canonical pattern coverage spans all nine pattern families, all tracked architecture types, and the full `low` / `moderate` / `high` / `critical` risk ladder.
- Grounded coverage spans all seven modeled domains; current balancing pressure is on the trailing domains rather than on opening new structural work.
- Browse artifacts remain derived from canonical pattern truth and should only change when a new grounding exposes genuine drift.
- The validation and publication baseline remains `uv run python scripts/python/validate_yaml.py`, `uv run python scripts/python/build_site_docs.py`, and `uv run mkdocs build`.

## Ordered tasks

1. Reassess the trailing domains and pick one equally bounded already-canonical slice whose metadata and derived browse mapping already align.
2. Author exactly one new grounded instance and keep the batch instance-only unless the new example exposes real canonical or browse drift.
3. Validate YAML, rebuild derived site docs, and run the MkDocs build after the content change.
4. Refresh `.agent/current-plan.md`, the relevant status files, and one new `.agent/iterations/2026/<timestamp>.md` record after verification.
5. Keep publication tooling and deployment workflow aligned only when helper tooling or build outputs genuinely change.

## Recent checkpoints

- `20260321-231804`: `policy-constrained-escalation-routing` gained a first support grounding through `instances/support/sovereign-cloud-storage-corruption-restricted-artifact-escalation-routing.md`, staying bounded at authority-route recommendation and escalation-packet assembly.
- `20260321-231247`: `approval-gated-briefing-release` gained additional finance grounding through `instances/finance/quarter-close-earnings-sensitivity-briefing-revision-approved-for-disclosure-committee-circulation.md`, staying bounded at governed release of one exact briefing revision into one named visibility lane.
- `20260321-230743`: `approval-gated-recommendation-release` gained additional engineering grounding through `instances/engineering/build-provenance-exception-recommendation-packet-revision-approved-for-release-integrity-council-decision-lane.md`, staying bounded at governed release of one exact recommendation packet revision into one named decision lane.

## History location

- Detailed iteration history: `.agent/iterations/2026/`
- Durable repository policy: `.agent/decisions.md`
- Broad inventory and coverage state: `.agent/ontology-status.yaml` and `.agent/coverage-matrix.yaml`
