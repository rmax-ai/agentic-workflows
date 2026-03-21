# Proposal: Publish The Ontology As A Generated MkDocs Site

- Status: proposed
- Date: 2026-03-21
- Scope: repository publishing, documentation UX, derived site generation
- Related areas: docs, patterns, views, vocabularies, instances,
  Python helper tooling

## Question

How should the repository publish its Markdown documentation and YAML
ontology as a friendly website without reorganizing the source tree or
creating a second source of truth?

## Proposal Summary

Adopt MkDocs with the Material theme as a derived publishing layer over
the existing repository, and generate a presentation-oriented
documentation tree into `build/site-docs` from the canonical Markdown
and YAML sources.

The repository should keep its current source-of-truth split:

1. Markdown remains authoritative for human-readable documentation and
  grounded instances.
2. YAML remains authoritative for canonical patterns, browse views, and
  controlled vocabularies.
3. The website becomes a fully derived artifact produced by a checked-in
  Python helper script.

This keeps the ontology pattern-first, avoids content duplication, stays
aligned with the repository's existing Python-and-`uv` tooling
direction, and yields static HTML that can be served from GitHub Pages
or another static host.

## Why This Approach Fits The Repository

The repository already has the right raw material for a documentation
site:

1. Entry and orientation material in `README.md` and `docs/`.
2. Canonical family and ontology documentation under `docs/patterns/`
  and the foundational docs.
3. Canonical structured ontology data under `data/patterns/`,
  `data/views/`, and `data/vocabularies/`.
4. Grounded examples under `instances/` that already read like
  standalone pages.

However, the current tree is optimized for curation and canonical
storage, not direct publication. Pointing a static-site generator at the
repository root would expose too much raw structure, make navigation
awkward, and leave YAML reference content under-explained.

Generating a separate site-doc tree solves that cleanly:

1. Source files remain where they belong.
2. Reader-facing information architecture can differ from repository
  layout.
3. YAML can be rendered into readable reference pages instead of being
  copied by hand.
4. Navigation can be derived from canonical truth.

## Goals

1. Publish the ontology as a friendly, searchable, static website.
2. Keep `docs/`, `data/`, `instances/`, and `schema/` as the source of
  truth.
3. Avoid moving or rewriting existing content to fit the website.
4. Generate human-readable reference pages from canonical YAML.
5. Preserve the repository's pattern-first organization in the primary
  browse experience.
6. Stay within the current Python helper-tooling path managed by `uv`.
7. Support static HTML export first and optional PDF export second.

## Non-Goals

1. Do not turn the repository into a custom web application or React
  frontend.
2. Do not introduce a second authoring surface for patterns,
  vocabularies, or views.
3. Do not hand-maintain Markdown copies of YAML pattern entries.
4. Do not reorganize the repository around website needs.
5. Do not let the website redefine ontology semantics.

## Proposed End State

The repository should eventually include:

1. A checked-in `mkdocs.yml` configuration file.
2. MkDocs-related Python dependencies declared in `pyproject.toml`.
3. One checked-in Python generator script under `scripts/python/`.
4. A generated docs tree rooted at `build/site-docs`.
5. A built static site output directory such as `build/site/`.
6. Optional deployment automation for GitHub Pages.
7. Optional PDF aggregation for a single downloadable site artifact.

The source-of-truth directories remain:

1. `README.md`
2. `docs/`
3. `data/patterns/`
4. `data/views/`
5. `data/vocabularies/`
6. `instances/`
7. `schema/`

## Proposed Publishing Architecture

### 1. Source Layer

The current repository content remains authoritative.

Authoritative source groups:

1. Foundational and family documentation in `README.md` and `docs/`.
2. Canonical pattern entries in `data/patterns/`.
3. Derived browse truth in `data/views/`.
4. Controlled terminology in `data/vocabularies/`.
5. Grounded examples in `instances/`.
6. Structural contract in `schema/pattern.schema.json`.

### 2. Generation Layer

A Python script reads repository sources and writes
presentation-oriented Markdown into `build/site-docs`.

Generation responsibilities:

1. Copy existing Markdown pages into the derived site tree.
2. Render YAML patterns into readable reference pages.
3. Render browse views into browse pages.
4. Render vocabularies into glossary-style reference pages.
5. Build index pages for instances.
6. Emit or support derived navigation configuration.

This layer is disposable and should be safe to recreate from scratch.

### 3. Presentation Layer

MkDocs Material renders `build/site-docs` into static HTML.

Presentation responsibilities:

1. Site shell and theme.
2. Navigation rendering.
3. Full-text search.
4. Static HTML generation.
5. Optional PDF export and future polish.

## Why MkDocs Over Alternatives

MkDocs is the recommended choice because it matches the repository's
actual constraints better than the alternatives.

### MkDocs + Material

Strengths:

1. Native fit for Markdown-first documentation.
2. YAML configuration is simple and explicit.
3. Strong built-in search and navigation.
4. Static output is straightforward.
5. Keeps the implementation in Python, consistent with repository
  tooling.

### Docusaurus

Tradeoff:

1. Stronger if the site must become an interactive application quickly.
2. Heavier because it introduces a Node and React stack.
3. More customization overhead than the repository currently needs.

### Hugo

Tradeoff:

1. Good static-site engine.
2. More template-oriented and less naturally documentation-first.
3. Less aligned with the existing Python helper-tooling baseline.

The proposal therefore recommends MkDocs Material as the default path.

## Target Site Information Architecture

The website should not merely mirror the repository tree. It should
reflect how readers explore the ontology.

Recommended top-level navigation:

1. Home
2. Ontology
3. Pattern Families
4. Patterns
5. Browse
6. Instances
7. Vocabularies
8. Schema

### Home

Primary source:

1. `README.md`

Purpose:

1. Explain the repository mission.
2. Orient new readers.
3. Link into ontology, families, patterns, and instances.

### Ontology

Primary sources:

1. `docs/ontology.md`
2. `docs/schema.md`
3. `docs/index-tree.md`
4. `docs/contribution-guide.md`

Purpose:

1. Explain the ontology model.
2. Explain schema expectations.
3. Explain browse semantics.
4. Explain authoring constraints.

### Pattern Families

Primary sources:

1. `docs/patterns/README.md`
2. `docs/patterns/*.md`

Purpose:

1. Preserve family boundaries.
2. Keep the primary browse experience pattern-first.
3. Link family docs to canonical generated pattern pages.

### Patterns

Primary source:

1. Generated from `data/patterns/`

Purpose:

1. Present each canonical pattern as a readable reference page.
2. Surface structured ontology fields in a consistent, searchable form.

### Browse

Primary sources:

1. Generated from `data/views/index-tree.yaml`
2. Generated from `data/views/by-domain.yaml`
3. Generated from `data/views/by-architecture.yaml`
4. Generated from `data/views/by-autonomy.yaml`
5. Generated from `data/views/by-risk.yaml`

Purpose:

1. Expose alternate navigation paths.
2. Keep them visibly derived from canonical truth.
3. Improve discoverability for domain- or governance-driven readers.

### Instances

Primary source:

1. `instances/`

Purpose:

1. Make grounded examples easy to browse by domain.
2. Link examples back to the canonical patterns they instantiate.

### Vocabularies

Primary source:

1. `data/vocabularies/`

Purpose:

1. Publish the ontology's controlled vocabulary surface.
2. Make stable ids and labels legible to readers.
3. Link terms to the patterns that use them when feasible.

### Schema

Primary source:

1. `schema/pattern.schema.json`

Purpose:

1. Expose the structural contract.
2. Link raw schema to explanatory material.

## Proposed File And Directory Layout

Recommended additions:

```text
mkdocs.yml
build/
  site-docs/         # generated Markdown source for MkDocs
  site/              # generated HTML output
scripts/
  python/
   build_site_docs.py
```

Optional later additions:

```text
.github/
  workflows/
   docs.yml
```

`build/site-docs` should be treated as generated input for MkDocs
rather than as a manually edited documentation tree.

## MkDocs Configuration Proposal

The initial `mkdocs.yml` should stay minimal and explicit.

Recommended first-pass configuration shape:

```yaml
site_name: Agentic Workflows
site_description: Pattern-first ontology of agentic workflows
docs_dir: build/site-docs
site_dir: build/site

theme:
  name: material
  features:
   - navigation.indexes
   - navigation.sections
   - navigation.expand
   - search.suggest
   - search.highlight

plugins:
  - search

markdown_extensions:
  - admonition
  - attr_list
  - tables
  - toc:
    permalink: true
```

Possible later additions:

1. `mkdocs-awesome-nav` if directory-local nav files prove useful.
2. `mkdocs-exporter` for PDF output.
3. Additional Markdown extensions only when there is a clear need.

## Python Tooling And Dependency Proposal

The repository already standardizes helper logic on Python with `uv`,
so the site generator should follow that rule.

Recommended dependency additions to `pyproject.toml`:

1. `mkdocs`
2. `mkdocs-material`
3. optionally `mkdocs-awesome-nav`
4. optionally `mkdocs-exporter`
5. optionally `pymdown-extensions`

The site generator should live under `scripts/python/` and be runnable
via:

```bash
uv run python scripts/python/build_site_docs.py
uv run mkdocs serve
uv run mkdocs build
```

## Detailed Generation Plan

### Step 1: Recreate `build/site-docs`

The generator should:

1. Remove any prior generated docs tree.
2. Recreate `build/site-docs` from scratch.
3. Fail loudly on invalid source assumptions.

This ensures the published site always reflects current repository
truth.

### Step 2: Copy Core Markdown Sources

Copy and normalize these sources into the derived site tree:

1. `README.md` -> home page
2. `docs/ontology.md`
3. `docs/schema.md`
4. `docs/index-tree.md`
5. `docs/contribution-guide.md`
6. `docs/patterns/README.md`
7. `docs/patterns/*.md`
8. `instances/**/*.md`

Normalization tasks may include:

1. Rewriting internal relative links where required.
2. Adding generated section landing pages where the raw repo does not
  already provide them.
3. Inserting reader-facing backlinks to canonical pattern pages for
  instances.

### Step 3: Render Pattern Reference Pages From YAML

Each file under `data/patterns/` should become a generated page under a
patterns reference section.

Recommended page structure:

1. Pattern title
2. Summary
3. Metadata panel
4. Workflow goal
5. Inputs
6. Outputs
7. Environment
8. Capability requirements
9. Execution architecture
10. Autonomy profile
11. Risk and governance
12. Why agentic
13. Failure modes
14. Evaluation
15. Implementation notes
16. Related patterns
17. Canonical source path

Rendering rules:

1. Preserve both label and id for vocabulary-backed fields when
  available.
2. Render lists of objects as repeatable subsections rather than raw
  YAML dumps.
3. Keep sections stable across all generated patterns.
4. Link related patterns internally when the destination page exists.

### Step 4: Render Browse Pages From View YAML

The view YAML files should produce browse pages rather than raw YAML
displays.

For each view page:

1. Show the grouping logic clearly.
2. Link to canonical generated pattern pages.
3. Optionally surface matching instances beneath patterns or at the
  group level.
4. Make it clear the page is a derived view, not a canonical pattern
  definition.

This preserves the repository's distinction between canonical pattern
data and browse artifacts.

### Step 5: Render Vocabulary Pages

Each vocabulary file under `data/vocabularies/` should become a
reader-facing reference page.

Recommended page structure:

1. Vocabulary title
2. Summary
3. Source fields
4. Usage notes
5. Terms list

For each term include:

1. Stable id
2. Display label
3. Short authoring guidance or definition
4. Optional links to patterns using that term

### Step 6: Render Schema Reference Material

The site should expose the schema in a readable but lightweight form.

First-pass implementation:

1. Publish `docs/schema.md` prominently.
2. Add a generated schema reference page that links to
  `schema/pattern.schema.json`.
3. Optionally list major top-level schema sections.

This avoids overengineering schema rendering in the first version.

### Step 7: Generate Instance Indexes

The instance pages already exist as Markdown, but the site should
improve their discoverability.

Recommended generated indexes:

1. Instances by domain
2. Instances by linked pattern
3. Optional instances by family if the pattern linkage is complete and
  easy to derive

This yields a significantly better browsing experience without
rewriting instance content.

## Navigation Strategy

The website navigation should be generated or at least derived, not
hand-maintained as one large fragile list.

Recommended approach:

1. Generate section landing pages in `build/site-docs`.
2. Either emit a stable `nav:` block into `mkdocs.yml` or use
  directory-local nav files under the generated tree.
3. Keep family-first browsing as the primary path.
4. Treat alternate view sections as secondary browse surfaces.

Preferred top-level nav:

1. Home
2. Ontology
3. Pattern Families
4. Patterns
5. Browse
6. Instances
7. Vocabularies
8. Schema

## Cross-Linking Strategy

The site becomes much more useful if generated pages cross-link
ontology artifacts.

Recommended cross-links:

1. Family docs -> canonical pattern pages in that family
2. Pattern pages -> family doc
3. Pattern pages -> related pattern pages
4. Pattern pages -> grounded instance pages
5. Instance pages -> linked pattern pages
6. Vocabulary term pages -> patterns using that term
7. Browse pages -> canonical pattern pages

These links should be generated from repository truth rather than
authored by hand.

## Implementation Details For `build_site_docs.py`

The generator can start as one file and split later only if complexity
justifies it.

Recommended internal responsibilities:

1. `reset_output_tree()`
2. `copy_static_markdown_sources()`
3. `render_pattern_pages()`
4. `render_view_pages()`
5. `render_vocabulary_pages()`
6. `render_schema_pages()`
7. `render_instance_indexes()`
8. `build_navigation_artifacts()`

Expected implementation style:

1. Use standard library plus `PyYAML` where needed.
2. Keep filesystem logic explicit and deterministic.
3. Prefer small pure functions for rendering fragments.
4. Keep templates simple, likely as Python string assembly at first.
5. Only introduce a templating engine if the rendering surface becomes
  hard to maintain.

## Suggested Rendering Conventions

To keep the site coherent, generated pages should follow fixed
formatting rules.

### Pattern pages

1. Use a short lead summary at the top.
2. Use second-level headings for canonical field groups.
3. Use bulleted lists for repeated items like inputs and outputs.
4. Use bold label lines for metadata blocks when tables would become
  awkward.
5. Show canonical source path at the bottom.

### Vocabulary pages

1. Group terms under a single terms section.
2. Show ids prominently because they matter for ontology stability.
3. Prefer concise definitions over prose-heavy commentary.

### Instance index pages

1. Show title and short summary or first paragraph.
2. Include linked pattern labels.
3. Group by domain or pattern depending on the page.

## Export Strategy

The first supported export should be static HTML.

The second supported export can be a full-site PDF bundle using
`mkdocs-exporter`.

Recommended second-phase PDF configuration:

```yaml
plugins:
  - search
  - exporter:
    formats:
      pdf:
       enabled: true
       aggregator:
        enabled: true
        output: documentation.pdf
        covers: all
```

PDF export should be optional for the initial rollout because the HTML
site provides the primary value and is simpler to validate first.

## Deployment Strategy

Recommended deployment target:

1. GitHub Pages

Why:

1. The output is static.
2. The repository is already on GitHub.
3. Hosting overhead stays minimal.

Recommended CI flow:

1. Install Python and `uv`.
2. Sync dependencies.
3. Run `uv run python scripts/python/build_site_docs.py`.
4. Run `uv run mkdocs build`.
5. Publish `build/site/`.

Optional later hosts:

1. Netlify
2. Cloudflare Pages

## Migration Plan

### Phase A: Minimal viable site

1. Add MkDocs dependencies.
2. Add `mkdocs.yml`.
3. Add `scripts/python/build_site_docs.py`.
4. Generate `build/site-docs` from `README.md`, `docs/`, and
  `instances/`.
5. Generate canonical pattern pages from `data/patterns/`.
6. Confirm local `mkdocs serve` and `mkdocs build` work.

This is the smallest useful deliverable.

### Phase B: Derived ontology browsing

1. Generate browse pages from `data/views/`.
2. Generate vocabulary reference pages from `data/vocabularies/`.
3. Add cross-links from patterns to instances and vocabularies.
4. Improve landing pages and navigation.

### Phase C: Publishing and export polish

1. Add GitHub Pages workflow.
2. Add PDF export.
3. Add minor visual polish or template overrides only if the default
  Material experience proves insufficient.

## Risks And Tradeoffs

### Risk: Generated pages drift from source semantics

Mitigation:

1. Keep generated pages faithful to canonical fields.
2. Link raw source locations visibly.
3. Rebuild from scratch on every run.

### Risk: Navigation becomes hard to maintain

Mitigation:

1. Derive navigation from repository truth or generated section indexes.
2. Avoid one giant hand-maintained `nav` block when the site grows.

### Risk: The first version feels too documentation-heavy

Mitigation:

1. Accept documentation-first as the intentional starting point.
2. Add richer browse indexes before adding custom frontend code.

### Risk: Extra dependencies in a content repository

Mitigation:

1. Keep the dependency set narrow.
2. Reuse the existing Python-and-`uv` helper path rather than adding a
  separate stack.

## Acceptance Criteria

This proposal should be considered implemented when:

1. The repository can generate `build/site-docs` from canonical sources
  with one checked-in Python helper.
2. MkDocs can build a static site from `build/site-docs` into
  `build/site/`.
3. The site publishes the foundational docs, family docs, pattern
  references, and grounded instances.
4. The site exposes browse pages derived from canonical view data.
5. No canonical ontology content must be moved or rewritten to keep the
  site current.
6. Navigation and search are good enough for a reader to move from
  family -> pattern -> instance and from alternate browse view ->
  canonical pattern.

## Recommended First Implementation Batch

The first implementation batch should stay intentionally narrow:

1. Add MkDocs and theme dependencies in `pyproject.toml`.
2. Add `mkdocs.yml` using `build/site-docs` as `docs_dir`.
3. Add `scripts/python/build_site_docs.py`.
4. Copy foundational docs and instances into `build/site-docs`.
5. Generate pattern reference pages from `data/patterns/`.
6. Generate a simple top-level navigation.
7. Verify local build output.

This creates a working publish surface quickly without forcing the
repository into a broader web-app effort.

## Decision Request

If accepted later, this proposal should lead to a durable decision
stating:

1. The repository publishes through a derived MkDocs site rather than
  direct hand-authored website content.
2. `build/site-docs` is the generated documentation source for site
  builds.
3. Markdown and YAML remain the canonical authoring formats in their
  existing directories.
4. Python helper scripts under `scripts/python/` own site generation.
5. The initial published experience is documentation-first and
  pattern-first, with richer interactive browsing deferred until there
  is a demonstrated need.
