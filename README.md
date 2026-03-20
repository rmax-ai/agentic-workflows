# agentic-workflows

A pattern-first ontology of agentic workflows.

This repository treats reusable workflow **patterns** as the primary organizing spine, with **domains** as context and **implementations/examples** as downstream grounding.

## Purpose

The repository is intended to answer:

- what kinds of workflows are meaningfully agentic,
- why they require more than static automation,
- what capabilities and architectures they depend on,
- what autonomy, governance, and evaluation constraints apply,
- how the same workflow pattern recurs across domains.

## Organizing principle

The repository is curated in this order:

1. **pattern first**
2. **domain second**
3. **implementation/examples third**

That ordering is deliberate. The goal is to catalog reusable workflow structure before collecting sector-specific examples.

## Repository structure

```text
agentic-workflows/
├─ README.md
├─ docs/
├─ data/
│  ├─ vocabularies/
│  ├─ patterns/
│  └─ views/
├─ instances/
├─ schema/
└─ .agent/
```

## Foundational docs

Phase 1 establishes the repository's shared model and canonical schema:

- `docs/ontology.md` — ontology layers, core entities, relationships, and normalization rules
- `docs/schema.md` — canonical pattern fields, cardinality expectations, and schema usage guidance
- `docs/index-tree.md` — intended pattern-first browse tree and alternate browse views
- `docs/contribution-guide.md` — file placement, naming conventions, workflow, and dependency order
- `schema/pattern.schema.json` — JSON Schema for canonical YAML pattern entries

## Core concepts

### Pattern

A reusable workflow structure such as synthesis, reconciliation, monitoring, triage, planning, recommendation, execution, or optimization.

### Domain

A context where a pattern appears, such as engineering, finance, compliance, operations, research, support, or HR.

### Instance

A concrete example of a canonical pattern applied to a real workflow, system, or operating environment.

## Design rules

1. **Patterns are canonical.** Pattern entries carry the reusable structure.
2. **Domains are contextual.** Domains show where a pattern appears without redefining it.
3. **Instances are grounded.** Instances come after patterns and vocabularies are stable.
4. **Governance is first-class.** Autonomy, reversibility, approval boundaries, privacy, and auditability belong in the model, not just in prose.

## Contribution order

Work should proceed in dependency order:

1. foundations and schema
2. controlled vocabularies
3. browse views
4. canonical patterns
5. grounded instances
6. coverage refinement

See `docs/contribution-guide.md` for authoring rules and `docs/schema.md` for the canonical pattern contract.

## Development tooling

Repository helper scripts use `uv` with Python 3.14.

Typical setup:

1. `uv python install 3.14`
2. `uv sync`
3. `uv run python scripts/python/validate_yaml.py`

Keep shell entrypoints thin and put reusable repository logic in checked-in Python helpers instead of ad hoc interpreter snippets.

## Status

Foundational docs, schema, and core controlled vocabularies are now in place. The current priority is Phase 3 navigation views, with repository helper tooling standardized on `uv`-managed Python 3.14.

## License

See `LICENSE`.
