# Mission

Build `agentic-workflows` into a pattern-first ontology of agentic work that stays organized by reusable workflow structure before domain examples or implementation details.

## Repository mandate

- Treat **patterns** as the primary organizing spine.
- Treat **domains** as contextual leaves that show where a pattern appears.
- Treat **implementations and instances** as grounded examples that come after ontology structure is stable.
- Use **YAML** for canonical structured artifacts and **Markdown** for human-readable guidance, grounded scenarios, and execution memory.

## Current operating constraints

The repository now has execution memory, foundational docs, the canonical pattern schema, controlled vocabularies, derived browse views, nine top-level family docs, canonical seed patterns across every top-level family, and the first grounded instance batches. The main ontology-specific assets are:

- `README.md`
- `docs/ontology.md`
- `docs/schema.md`
- `docs/index-tree.md`
- `docs/contribution-guide.md`
- `schema/pattern.schema.json`
- `data/vocabularies/problem-structures.yaml`
- `data/vocabularies/domains.yaml`
- `data/vocabularies/architectures.yaml`
- `data/vocabularies/capabilities.yaml`
- `data/vocabularies/autonomy-levels.yaml`
- `data/vocabularies/risk-levels.yaml`
- `data/views/index-tree.yaml`
- `data/views/by-domain.yaml`
- `data/views/by-architecture.yaml`
- `data/views/by-autonomy.yaml`
- `data/views/by-risk.yaml`
- `data/patterns/`
- `instances/`
- `.agent/current-plan.md`
- `.agent/prompts/mega-prompt.txt`
- `.agent/prompts/operator-prompt.txt`
- `scripts/run-agentic-workflows-loop.sh`
- `scripts/run-agentic-workflows-forever.sh`
- `scripts/run-mermaid-illustration-loop.sh`
- `scripts/run-mermaid-illustration-forever.sh`

Grounded coverage is still intentionally thin, so current work should keep expanding instances and representative pattern/domain combinations in small, dependency-aware batches instead of generating large shallow sets.

## Curation rules

1. Work in dependency order: execution memory -> foundations and schema -> vocabularies -> views -> patterns -> instances.
2. Do not create shallow pattern files before the schema and controlled vocabularies exist.
3. Record durable ontology choices in `.agent/decisions.md`, keep
   that index concise, and store detailed rationale in
   `.agent/decisions/` before choices spread across new files.
4. Keep `.agent/repo-map.md` as the concise repository map index
   and move bulky structural detail into `.agent/repo-map/`.
5. Use `.agent/coverage-matrix.yaml` and `.agent/ontology-status.yaml` to drive systematic expansion instead of ad hoc additions.
6. Prefer representative, governance-aware coverage over large batches of weak entries.

## Definition of success

The repository is successful when it contains a coherent ontology, controlled vocabularies, pattern-first browse views, high-quality YAML pattern entries, linked Markdown instances, and enough execution memory for future iterations to continue consistently.
