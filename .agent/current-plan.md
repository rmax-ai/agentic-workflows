# Current Plan

## Iteration focus

Resume Phase 3 navigation-view authoring on top of the new uv-managed Python helper baseline.

## Current phase

- Phase 2: controlled vocabularies are complete
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 3: create pattern-first and alternate browse views

## Ordered tasks

1. Create `data/views/index-tree.yaml` using the established pattern families and link strategy from `docs/index-tree.md`.
2. Create alternate browse views for domain, architecture, autonomy, and risk using the controlled vocabulary ids from `data/vocabularies/`.
3. Keep view artifacts reference-oriented so they can be regenerated once pattern files exist.
4. Extend Python helper tooling only when repository automation needs reusable logic beyond shell orchestration.
5. After views land, prepare the top-level `docs/patterns/` family docs before seed pattern authoring.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Do not add canonical pattern entries before navigation views and family docs exist.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome

The next iteration should land committed browse views that make the ontology more navigable, while relying on the new uv-managed Python helper path for any reusable validation needed along the way.
