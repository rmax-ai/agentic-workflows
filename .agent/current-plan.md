# Current Plan

## Iteration focus

Complete Phase 3 navigation-view authoring in one scoped batch, then update repository memory to mark browse-view prerequisites as satisfied.

## Current phase

- Phase 2: controlled vocabularies are complete
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 3: create pattern-first and alternate browse views

## Ordered tasks

1. Create `data/views/index-tree.yaml` using the established pattern families and link strategy from `docs/index-tree.md`.
2. Create alternate browse views for domain, architecture, autonomy, and risk using the controlled vocabulary ids from `data/vocabularies/`.
3. Keep view artifacts reference-oriented so they can be regenerated once pattern files exist.
4. Validate the new YAML view files with the existing `uv`-managed helper tooling.
5. After views land, move immediately to top-level `docs/patterns/` family docs before seed pattern authoring.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Do not add canonical pattern entries before navigation views and family docs exist.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.

## Expected outcome

This iteration should land committed browse views that make the ontology more navigable, validate them with the checked-in Python helper path, and leave the repository ready for Phase 4 pattern-family docs.
