# Root And Automation

## Root files

- `README.md` — repository mission, pattern-first framing, and intended target structure.
- `mkdocs.yml` — MkDocs publication config that renders the derived site from `build/site-docs` into `build/site`.
- `.python-version` — pinned local interpreter target for uv-managed Python helper scripts.
- `pyproject.toml` — Python helper-tool metadata and dependency declarations for uv.
- `uv.lock` — locked Python helper dependencies for reproducible local execution.
- `.gitattributes` — text normalization and Linguist hints for planned YAML and Markdown content.
- `.gitignore` — ignore rules that preserve committed `.agent/` memory while excluding runtime artifacts.
- `LICENSE` — repository license.

## Automation

- `scripts/run-agentic-workflows-loop.sh` — runs one repository iteration by assembling prompt context and invoking Copilot.
- `scripts/run-agentic-workflows-forever.sh` — optional wrapper for repeated iterations with a stop-file check.
- `scripts/run-mermaid-illustration-loop.sh` — runs the Mermaid-illustration orchestrator prompt through Copilot with a configurable batch size.
- `scripts/run-mermaid-illustration-forever.sh` — optional wrapper for repeated Mermaid illustration batches with a stop-file check.
- `scripts/python/validate_yaml.py` — uv-managed Python helper that validates repository YAML files without relying on ad hoc Ruby.
- `scripts/python/build_site_docs.py` — uv-managed Python helper that regenerates the MkDocs input tree in `build/site-docs` from canonical Markdown, YAML, instance, and schema sources.
- `scripts/python/publish_site_via_gh_pages.py` — uv-managed Python helper that runs `gh-pages` from a temporary npm workspace so local branch-based Pages publishing works in this Python-only repository.
- `.github/workflows/publish-site.yml` — GitHub Actions workflow that validates YAML, regenerates `build/site-docs`, builds `build/site`, and deploys the generated site through GitHub Pages.

## Derived publication layer

- `build/site-docs/` — generated Markdown source tree for MkDocs; disposable and rebuilt from canonical repository truth.
- `build/site/` — generated static HTML output from MkDocs.
