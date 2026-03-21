# Proposal: validate prompt-context file references before subagent handoff

## Problem

The iteration prompt and subagent brief referenced `instances/hr/work-authorization-renewal-gap-anomaly-review.md`, but that file does not exist in the repository. The intended neighboring context was still inferable from existing HR monitor examples, but the broken reference created avoidable friction and weakens confidence that subagents are reading the exact intended grounding set.

## Proposed change

Add a lightweight pre-handoff validation step in the repository loop tooling that checks every file path mentioned in the assembled operator prompt or subagent brief against the working tree. If a referenced path does not exist, fail fast with a clear message or replace it with the nearest matching existing file before the prompt is handed to a subagent.

## Why this helps

The loop already depends on prompt-composed context for scoped work, so invalid file references directly degrade iteration quality. Catching broken references before a subagent starts would reduce wasted exploration, keep subagent context deterministic, and make the execution-memory trail more trustworthy.

## Scope

- Prompt assembly and validation logic in the loop tooling.
- No ontology or pattern-schema changes.
- Prefer a checked-in Python helper invoked through `uv` so the validation is reusable and easy to extend.
