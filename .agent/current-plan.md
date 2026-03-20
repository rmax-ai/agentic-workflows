# Current Plan

## Iteration focus

Use the newly expanded grounded-instance layer as the baseline for returning to Phase 5 with a narrow canonical pattern batch in one of the remaining empty families.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: a second canonical pattern batch now covers planning, recommendation, and execution families in addition to the initial gather, investigate, and monitor anchors
- Phase 6: the repository now has six grounded instances spanning research, engineering, finance, operations, compliance, and HR

## Ordered tasks

1. Add the first canonical pattern in `optimize-adapt` or `human-agent-collaborative-work`, choosing the family with the clearest vocabulary-supported problem structure and strongest governance framing.
2. Re-read the relevant family overview doc, schema, vocabularies, neighboring patterns, and coverage matrix before authoring the next seed pattern.
3. Keep the next pattern batch modest and dependency-aware: prefer one or two strong canonical entries over broad shallow expansion.
4. Treat `transform-process` as still blocked unless a justified vocabulary refinement or clearly supported pattern candidate emerges.
5. Use the new grounded instances to inform future example domains and cross-links without duplicating their concrete scenario prose into canonical YAML.

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

The next iteration should leave the repository with at least one new canonical pattern in a previously empty family and a clearer path for closing the remaining family-level gaps.
