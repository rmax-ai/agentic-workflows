# Current Plan

## Iteration focus

Begin Phase 5 by authoring a small, high-value batch of canonical YAML pattern entries now that the family overview docs are in place.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: start the first canonical pattern batch in `data/patterns/`

## Ordered tasks

1. Author a small first batch of canonical pattern YAML files in representative families with strong vocabulary support, starting with investigation, monitoring, and gather/synthesis workflows before broader expansion.
2. Keep every seed pattern aligned with `schema/pattern.schema.json`, the existing controlled vocabularies, `data/views/index-tree.yaml`, and the new `docs/patterns/` family boundaries.
3. Prefer patterns with clear governance and evaluation surfaces so the initial batch sets a high-quality template for later authoring.
4. Avoid `transform-process` until a concrete pattern is justified despite the current `problem-structures` vocabulary gap, or until that gap is deliberately refined.
5. Validate new YAML files with the existing `uv`-managed helper tooling after each pattern batch.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome

The next iteration should land a modest, schema-valid first batch of canonical pattern YAML files that establish the repository's pattern authoring standard without over-expanding coverage.
