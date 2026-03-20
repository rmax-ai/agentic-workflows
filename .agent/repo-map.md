# Repository Map

## Current committed structure

### Root files

- `README.md` — repository mission, pattern-first framing, and intended target structure.
- `.python-version` — pinned local interpreter target for uv-managed Python helper scripts.
- `pyproject.toml` — Python helper-tool metadata and dependency declarations for uv.
- `uv.lock` — locked Python helper dependencies for reproducible local execution.
- `.gitattributes` — text normalization and Linguist hints for planned YAML and Markdown content.
- `.gitignore` — ignore rules that preserve committed `.agent/` memory while excluding runtime artifacts.
- `LICENSE` — repository license.

### Current automation

- `scripts/run-agentic-workflows-loop.sh` — runs one repository iteration by assembling prompt context and invoking Copilot.
- `scripts/run-agentic-workflows-forever.sh` — optional wrapper for repeated iterations with a stop-file check.
- `scripts/python/validate_yaml.py` — uv-managed Python helper that validates repository YAML files without relying on ad hoc Ruby.

### Current execution-memory assets

- `.agent/current-plan.md` — current ordered iteration plan.
- `.agent/prompts/mega-prompt.txt` — master orchestration prompt for the repo-building loop.
- `.agent/prompts/operator-prompt.txt` — per-iteration operator instructions.
- `.agent/mission.md` — stable mission and curation rules for the repository.
- `.agent/backlog.yaml` — dependency-ordered task backlog.
- `.agent/iterations/` — one dated Markdown file per iteration, grouped by year.
- `.agent/decisions.md` — durable architectural and process decisions.
- `.agent/ontology-status.yaml` — status inventory and gap tracking.
- `.agent/coverage-matrix.yaml` — coverage grid for planned pattern/domain/architecture/risk combinations.
- `.agent/glossary.md` — repository terminology guide.

### Current foundational ontology assets

- `docs/ontology.md` — canonical explanation of ontology layers, relationships, and normalization rules.
- `docs/schema.md` — field-by-field guide to the canonical pattern schema.
- `docs/index-tree.md` — proposed pattern-first browse tree and derived view strategy.
- `docs/contribution-guide.md` — dependency-aware authoring and placement rules.
- `schema/pattern.schema.json` — canonical JSON Schema for YAML pattern entries.

### Current controlled vocabularies

- `data/vocabularies/problem-structures.yaml` — reusable workflow problem forms for `problem_structure`.
- `data/vocabularies/domains.yaml` — approved contextual domain ids for `domain`.
- `data/vocabularies/architectures.yaml` — execution architecture ids for `execution_architecture`.
- `data/vocabularies/capabilities.yaml` — reusable capability ids for `capability_requirements`.
- `data/vocabularies/autonomy-levels.yaml` — autonomy ladder for `autonomy_profile.level`.
- `data/vocabularies/risk-levels.yaml` — governance-sensitive levels for `risk_governance.level`.

### Current navigation views

- `data/views/index-tree.yaml` — canonical family-ordered browse tree scaffold that keeps the default navigation pattern-first.
- `data/views/by-domain.yaml` — derived domain view that groups future canonical patterns by domain while preserving family order.
- `data/views/by-architecture.yaml` — derived architecture view that organizes future canonical patterns by execution style.
- `data/views/by-autonomy.yaml` — derived autonomy view that organizes future canonical patterns by discretion and control boundary.
- `data/views/by-risk.yaml` — derived risk view that organizes future canonical patterns by governance posture.

## Not yet present but planned

### Additional documentation

- `docs/patterns/`
- `docs/domains/`
- `docs/architectures/`

### Structured ontology data

- `data/patterns/`

### Grounded examples

- `instances/`

## Reading order for future contributors and agents

1. `README.md`
2. `.agent/current-plan.md`
3. `.agent/mission.md`
4. `.agent/backlog.yaml`
5. `.agent/ontology-status.yaml`
6. `.agent/coverage-matrix.yaml`
7. `.agent/decisions.md`
8. `data/vocabularies/`
9. `schema/pattern.schema.json`
