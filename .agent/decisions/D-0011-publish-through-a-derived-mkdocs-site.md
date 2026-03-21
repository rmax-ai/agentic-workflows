# D-0011 — Publish through a derived MkDocs site

- Status: accepted
- Decision: Publish the repository through a derived MkDocs site that generates presentation-oriented Markdown into `build/site-docs` from the canonical Markdown, YAML, and schema sources, then renders static HTML into `build/site`.
- Rationale: This keeps Markdown and YAML as the only authoring surfaces, preserves the repository's pattern-first ontology and source tree, stays aligned with the existing Python and `uv` helper-tooling baseline, and avoids creating a second source of truth for website content.
