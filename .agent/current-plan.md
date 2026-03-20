# Current Plan

## Iteration focus
Stabilize repository memory to match the committed foundations, then complete Phase 2 controlled vocabularies in a narrow, dependency-safe batch.

## Current phase
- Phase 1: foundational docs and schema are complete
- Phase 2: create controlled vocabularies for core classification fields

## Ordered tasks
1. Normalize `.agent/` state so plan and backlog reflect the already-committed foundations and schema.
2. Author the six core controlled vocabulary files under `data/vocabularies/`.
3. Review the new vocabularies for consistency with the schema and docs.
4. Add the iteration summary under `.agent/iterations/`, then update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, `.agent/repo-map.md`, and this plan with the next dependency-ordered step.

## Constraints
- Do not add navigation views or pattern entries before controlled vocabularies are coherent.
- Keep vocabulary ids stable, lower-kebab-case, and aligned with the schema field names.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome
The repository should end this iteration with committed controlled vocabularies and execution memory that accurately points the next loop toward navigation views.
