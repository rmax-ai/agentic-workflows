# Current Plan

## Iteration focus

Resume Phase 5 expansion with a second canonical pattern batch in still-empty families, using the newly proven instance layer as grounding support rather than expanding instances broadly again immediately.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: first canonical pattern batch landed in `data/patterns/`
- Phase 6: first grounded instances have landed under `instances/`, proving the initial instance format and cross-linking model

## Ordered tasks

1. Author a second seed-pattern batch in still-empty families such as `plan-coordinate-schedule`, `recommend-decide-escalate`, or `execute-automate`.
2. Prioritize combinations that improve structural coverage rather than adding more variants inside already-started families.
3. Use the existing schema, vocabularies, browse views, and the new instance layer to keep new patterns normalized and easy to ground later.
4. After the next pattern batch lands, update derived views and then add follow-on instances only for the newly stable patterns that most improve domain or governance coverage.
5. Look for opportunities to cover low-risk or critical-risk cells and the currently empty `approval-gated-execution` architecture bucket.
6. Continue to avoid `transform-process` until a concrete pattern is justified despite the current `problem-structures` vocabulary gap, or until that gap is deliberately refined.

## Constraints

- Keep Python tooling narrowly scoped to repository automation and helper scripts.
- Prefer standard-library Python first and add third-party packages only when justified.
- Keep shell entrypoints thin even if helper logic moves into Python.
- Use checked-in Python helpers instead of ad hoc Ruby for reusable validation or parsing tasks.
- Use the family overview docs as narrative constraints, not as alternate canonical data.
- Keep views aligned with the controlled vocabulary ids and treat them as derived browse artifacts.
- Ensure every subagent task ends with exactly one git commit.
- Keep instance work tightly tied to existing canonical patterns; do not create standalone domain essays.
- Prefer pattern additions that unlock new family, architecture, autonomy, or risk coverage rather than duplicating already-represented cells.

## Expected outcome

The next iteration should leave the repository with a broader but still normalized canonical pattern set, ready for another small instance batch once additional families are stable.
