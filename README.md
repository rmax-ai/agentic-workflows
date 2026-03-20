# Agentic Workflows

A pattern-first encyclopedia of agentic workflows.

This repository stores:

- **YAML** as the canonical structured ontology of workflow patterns
- **Markdown** as grounded instances, scenarios, target systems, and real-world examples

The organizing principle is:

- **pattern first**
- **domain second**
- **implementation/examples third**

## Purpose

This repo is a knowledge base for understanding and cataloging work that benefits from agentic workflows.

It is not a list of industries or AI demos.

It aims to capture:

- what kinds of workflows are agentic
- why they are agentic rather than ordinary automation
- what architectures and capabilities they require
- what autonomy and governance constraints apply
- how similar workflow patterns appear across different domains

## Core concepts

### Pattern
A reusable workflow/problem type such as:

- investigate
- reconcile
- monitor
- triage
- plan
- coordinate
- recommend
- execute
- optimize

### Domain
A context where a pattern appears, such as:

- finance
- engineering
- compliance
- support
- operations
- research
- HR

### Instance
A concrete example of a pattern applied to a real environment, target system, or workflow.

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
````

### `data/patterns/`

Canonical YAML entries for workflow patterns.

### `data/vocabularies/`

Controlled vocabularies for problem structures, domains, architectures, capabilities, autonomy, and risk.

### `data/views/`

Navigation and browse views such as the pattern-first index tree and alternate views by domain or architecture.

### `instances/`

Markdown files for concrete, grounded examples linked back to canonical patterns.

### `docs/`

Human-readable documentation for ontology design, schema, contribution rules, and pattern families.

### `.agent/`

Persistent execution memory for the repo-building loop, including plans, logs, coverage status, and decisions.

## Design principles

### 1. Pattern is the spine

The ontology is organized by workflow structure, not by industry.

For example, “competitive intelligence” and “medical literature review” may both be instances of a multi-source synthesis pattern.

### 2. Domain is a leaf

Domains provide examples and context, but they are not the primary organizing backbone.

### 3. Why agentic is load-bearing

A workflow belongs here only if it benefits from one or more of:

* multi-step planning
* nontrivial tool use
* exception-heavy execution
* long-horizon state
* reflection / verification loops
* multi-agent or multi-party coordination
* human-in-the-loop checkpoints

### 4. Governance matters

This repo treats autonomy, reversibility, failure cost, privacy, auditability, and approval boundaries as first-class concerns.

## What a pattern entry captures

A canonical YAML pattern entry typically includes:

* identity and summary
* problem structure
* domains
* workflow goal
* inputs and outputs
* environment and systems
* capability requirements
* recommended architectures
* autonomy profile
* risk and governance
* why agentic
* failure modes
* evaluation criteria
* related patterns

## What an instance file captures

A Markdown instance typically includes:

* the scenario
* linked canonical pattern(s)
* target systems or source systems
* domain context
* governance constraints
* architecture options
* evaluation notes

## Contribution model

Work should happen in dependency order:

1. ontology foundations
2. schema
3. vocabularies
4. navigation views
5. pattern entries
6. instance files
7. coverage refinement

Do not add many shallow patterns before vocabularies and schema are stable.

## Near-term goals

* establish the canonical schema
* define controlled vocabularies
* create the pattern-first index tree
* seed the first set of high-quality pattern entries
* add grounded instance examples across major domains
* track coverage in `.agent/`

## Long-term goals

* broad pattern coverage across major domains
* consistent governance-aware ontology
* machine-readable structured data
* documentation suitable for a docs site
* future mapping to benchmarks and challenge generation

## Status

This repository is being built iteratively with an orchestrated agent loop that maintains execution memory in `.agent/`.

## License

See `LICENSE`.
