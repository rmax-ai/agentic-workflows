# Repository Map

## Current committed structure

### Root files
- `README.md` — repository mission, pattern-first framing, and intended target structure.
- `.gitattributes` — text normalization and Linguist hints for planned YAML and Markdown content.
- `.gitignore` — ignore rules that preserve committed `.agent/` memory while excluding runtime artifacts.
- `LICENSE` — repository license.

### Current automation
- `scripts/run-agentic-workflows-loop.sh` — runs one repository iteration by assembling prompt context and invoking Copilot.
- `scripts/run-agentic-workflows-forever.sh` — optional wrapper for repeated iterations with a stop-file check.

### Current execution-memory assets
- `.agent/current-plan.md` — current ordered iteration plan.
- `.agent/prompts/mega-prompt.txt` — master orchestration prompt for the repo-building loop.
- `.agent/prompts/operator-prompt.txt` — per-iteration operator instructions.
- `.agent/mission.md` — stable mission and curation rules created in this bootstrap.
- `.agent/backlog.yaml` — dependency-ordered task backlog created in this bootstrap.
- `.agent/proposals/` — staged ontology proposals for later review, adoption, or conversion into durable decisions.
- `.agent/iterations/` — one dated Markdown file per iteration, grouped by year.
- `.agent/decisions.md` — durable architectural and process decisions created in this bootstrap.
- `.agent/ontology-status.yaml` — status inventory and gap tracking created in this bootstrap.
- `.agent/coverage-matrix.yaml` — initial coverage grid created in this bootstrap.
- `.agent/glossary.md` — repository terminology guide created in this bootstrap.

## Not yet present but planned

### Foundational documentation
- `docs/ontology.md`
- `docs/schema.md`
- `docs/index-tree.md`
- `docs/contribution-guide.md`
- `docs/patterns/`
- `docs/domains/`
- `docs/architectures/`

### Structured ontology data
- `schema/pattern.schema.json`
- `data/vocabularies/`
- `data/views/`
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
