# Current Plan

## Iteration focus

Ground the support domain with a first linked Markdown instance now that `analyst-copilot-loop` gives the repository a direct collaboration-oriented support anchor. Prefer a concrete escalation workflow where a support lead and copilot iteratively shape a customer-facing response while `transform-process` remains blocked until vocabulary support is justified.

## Current phase

- Phase 2: controlled vocabularies are complete
- Phase 3: navigation views are complete
- Phase 4: top-level family overview docs are complete under `docs/patterns/`
- Tooling baseline: uv-managed Python 3.14 helper workflow is in place
- Phase 5: canonical patterns now cover `human-agent-collaborative-work` in addition to the initial gather, investigate, monitor, planning, recommendation, execution, and optimize/adapt anchors
- Phase 6: the repository now has six grounded instances spanning research, engineering, finance, operations, compliance, and HR
- Remaining empty family: `transform-process`

## Ordered tasks

1. Add the first support-domain grounded instance in `instances/support/`, tied to `analyst-copilot-loop`, so the support domain is no longer canonical-only.
2. Re-read the relevant pattern YAML, neighboring support-relevant patterns, coverage matrix, and existing instance conventions before authoring the new Markdown file.
3. Keep the instance specific to a concrete support escalation or case-workflow scenario, with explicit links back to one or more canonical pattern entries.
4. Validate repository YAML after memory updates and any new instance-adjacent YAML changes.
5. Keep `transform-process` blocked unless a justified direct problem-structure mapping and seed candidate emerge.

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

The next iteration should leave the repository with the first support-domain grounded example, refreshed execution memory, and a clearer decision about whether the following step should target additional support grounding or a justified `transform-process` ontology refinement.
