# Mission

Build `agentic-workflows` into a pattern-first ontology of agentic work that stays organized by reusable workflow structure before domain examples or implementation details.

## Repository mandate

- Treat **patterns** as the primary organizing spine.
- Treat **domains** as contextual leaves that show where a pattern appears.
- Treat **implementations and instances** as grounded examples that come after ontology structure is stable.
- Use **YAML** for canonical structured artifacts and **Markdown** for human-readable guidance, grounded scenarios, and execution memory.

## Current operating constraints

The repository is still in its bootstrap state. Today the ontology-specific assets are limited to:

- `README.md`
- `.agent/current-plan.md`
- `.agent/prompts/mega-prompt.txt`
- `.agent/prompts/operator-prompt.txt`
- `scripts/run-agentic-workflows-loop.sh`
- `scripts/run-agentic-workflows-forever.sh`

No schema, controlled vocabularies, navigation views, canonical patterns, or grounded instances exist yet.

## Curation rules

1. Work in dependency order: execution memory -> foundations and schema -> vocabularies -> views -> patterns -> instances.
2. Do not create shallow pattern files before the schema and controlled vocabularies exist.
3. Record durable ontology choices in `.agent/decisions.md` before they spread across new files.
4. Use `.agent/coverage-matrix.yaml` and `.agent/ontology-status.yaml` to drive systematic expansion instead of ad hoc additions.
5. Prefer representative, governance-aware coverage over large batches of weak entries.

## Definition of success

The repository is successful when it contains a coherent ontology, controlled vocabularies, pattern-first browse views, high-quality YAML pattern entries, linked Markdown instances, and enough execution memory for future iterations to continue consistently.
