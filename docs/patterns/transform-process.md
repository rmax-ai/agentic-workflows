# Transform, process

**Family id:** `transform-process`

This family covers workflows that turn inputs into more usable forms through conversion, normalization, enrichment, extraction, or batch reshaping. The core value is structural transformation: making content or records operationally usable for later retrieval, analysis, reconciliation, execution, or reporting.

## What belongs in this family

Use this family for patterns that:

- convert documents or mixed inputs into structured data,
- normalize inconsistent fields or formats,
- enrich records so downstream workflows can reason over them,
- process content in batches where the main task is transformation rather than judgment.

The conceptual seed patterns already named in the browse tree are:

- `document-to-structured-data`
- `normalization-and-enrichment`
- `batch-content-transformation`

## Problem-structure mapping status

This family now maps directly to `structured-representation-transformation` in `data/vocabularies/problem-structures.yaml`.

Use that term when the primary deliverable is a normalized, enriched, or schema-aligned representation that can be handed off downstream without turning the workflow into synthesis, verification, or execution.

## Family boundary

This family is about changing representation, shape, or usability.

- If the main task is **assembling evidence into a brief**, see [gather-retrieve-synthesize](./gather-retrieve-synthesize.md).
- If the main task is **checking whether transformed output is correct or reconciling it with another source of truth**, see [investigate-reconcile-verify](./investigate-reconcile-verify.md).
- If the main task is **taking action on transformed outputs inside an operational workflow**, see [execute-automate](./execute-automate.md).

## Why this family is meaningfully agentic

The family matters when transformation is not a single static mapping. Agentic behavior appears when the workflow must choose extraction strategies, handle variable input quality, preserve important context across transformations, and adapt processing paths when inputs are incomplete, messy, or semantically ambiguous.

## Governance and evaluation concerns

Future patterns should be explicit about lossiness, schema fidelity, confidence signals, and when transformed outputs require verification before reuse. Evaluation should focus on semantic preservation, completeness, consistency, and downstream usability rather than only throughput.

## Guidance for future seed patterns

A strong canonical pattern in this family should state:

- what is being transformed and into what target form,
- what enrichment or normalization decisions are in scope,
- what ambiguity handling is allowed before human review,
- how transformed outputs are handed off to retrieval, reconciliation, execution, or reporting workflows.

## See also

- Previous family: [gather-retrieve-synthesize](./gather-retrieve-synthesize.md)
- Next family: [investigate-reconcile-verify](./investigate-reconcile-verify.md)
