# Current Plan

## Iteration focus

Resolve the remaining empty `transform-process` family by determining whether the problem-structure vocabulary should be extended and, if justified, defining a narrow first canonical seed candidate before more broad expansion.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: canonical patterns now cover `human-agent-collaborative-work` in addition to the initial gather, investigate, monitor, planning, recommendation, execution, and optimize/adapt anchors
- Phase 6: the repository now has seven grounded instances spanning research, engineering, finance, operations, compliance, support, and HR
- Remaining empty family: `transform-process`

## Ordered tasks

1. Re-read `docs/patterns/transform-process.md`, `data/vocabularies/problem-structures.yaml`, the schema, and neighboring family patterns to determine whether a new controlled problem-structure term is actually justified.
2. If the vocabulary gap is justified, record the ontology decision before it spreads and define the smallest safe refinement needed to support one canonical `transform-process` seed pattern.
3. Identify a single representative seed candidate for `transform-process` that stays transformation-first rather than drifting into synthesis, verification, or execution.
4. Validate repository YAML after any vocabulary, view, pattern, or memory updates.
5. Keep future instance work modest until the last empty family has a justified canonical anchor.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.
- Keep canonical pattern work tightly aligned with the existing schema, vocabularies, and family boundaries.
- Prefer tasks that improve coverage in still-empty families before adding more instances to already-grounded families.
- Favor next steps that make the coverage matrix more balanced across families, domains, architectures, autonomy levels, and risk levels.

## Expected outcome

The next iteration should leave the repository with either a justified `transform-process` vocabulary-and-seed plan or an explicit decision to keep that family blocked, along with refreshed execution memory that explains the reasoning.
