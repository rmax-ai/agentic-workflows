# Proposal: Prompt Budget And Context-Composition Controls

- Status: proposed
- Date: 2026-03-20
- Scope: loop prompt assembly and context stability
- Related areas: repository snapshot generation, prompt quality, long-run scalability

## Question

How should the loop control prompt size and composition so iteration quality remains stable as the repository and execution memory grow?

## Proposal Summary

Add explicit prompt-budget checks and deterministic composition rules before invoking the agent.

The loop should measure what it is sending, detect oversized or low-signal inputs, and trim or warn in a predictable way.

## Problem

As the repository grows, prompt assembly becomes a hidden failure mode.

Common issues:

1. repository snapshots become too large
2. low-value context crowds out high-value context
3. prompts drift in composition between runs, reducing reproducibility
4. failures caused by prompt bloat are hard to diagnose after the fact

## Proposed Controls

### Prompt-size budget

Measure the total prompt size before invoking the agent and compare it to a configured threshold.

### Section-level budgeting

Track the contribution of sections such as:

- orchestration prompt
- operator prompt
- repository snapshot
- recent execution metadata

### Deterministic section ordering

Assemble prompt sections in a stable order and avoid incidental variation.

### Low-value context trimming

When the prompt exceeds budget, trim from the lowest-value sources first.

Examples:

1. overly long tree listings
2. excessive recent-commit history
3. stale or redundant snapshot content

## Recommended Implementation

Introduce a helper such as `scripts/python/build_prompt.py` or `scripts/python/check_prompt_budget.py`.

It should:

1. compute size metrics
2. emit a short per-section report
3. optionally fail or warn when budget is exceeded
4. trim deterministically when trimming is enabled

## Benefits

1. more stable iteration quality
2. easier diagnosis of prompt-related failures
3. better scalability as `.agent/` memory and repository content grow
4. less accidental context noise

## Risks And Tradeoffs

### Risk: over-trimming removes useful context

Mitigation:

1. trim only low-priority sections first
2. log what was trimmed
3. make thresholds configurable

### Risk: budgeting logic becomes too complicated

Mitigation:

1. keep the first version simple
2. optimize only after real prompt-size pressure appears

## Acceptance Criteria

This proposal should be considered implemented when:

1. prompt size is measured before agent invocation
2. oversized prompts produce a clear warning or failure
3. section ordering is deterministic
4. any trimming behavior is explicit and reproducible

## Decision Request

If accepted later, this proposal should make prompt assembly a controlled, observable stage rather than an opaque concatenation step.

