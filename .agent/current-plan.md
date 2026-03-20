# Current Plan

## Iteration focus
Bootstrap repository execution memory and foundational ontology files in dependency order.

## Current phase
- Phase 0: bootstrap `.agent/`
- Phase 1: create foundational docs and schema

## Ordered tasks
1. Create the mandatory `.agent/` memory files with initial mission, backlog, status, coverage, repo map, and decisions.
2. Create foundational docs in `docs/` and the canonical JSON schema in `schema/`.
3. Review repository state and add a new dated file under `.agent/iterations/`, then update `.agent/ontology-status.yaml`, `.agent/coverage-matrix.yaml`, and this plan with the next iteration targets.

## Constraints
- Do not add pattern entries before schema and vocabularies exist.
- Keep this iteration modest and focused on prerequisites.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome
The repository should end this iteration with working execution memory, foundational documentation, and a canonical schema that can support vocabulary work next.
