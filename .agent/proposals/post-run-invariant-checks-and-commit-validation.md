# Proposal: Post-Run Invariant Checks And Commit Validation

- Status: proposed
- Date: 2026-03-20
- Scope: loop safety and repository integrity
- Related areas: YAML validation, `.agent/` memory integrity, commit discipline, deterministic artifacts

## Question

What should the loop verify after agent execution so a run is only considered successful when it leaves the repository in a coherent state?

## Proposal Summary

Add a post-run validation stage that checks repository invariants, validates changed structured files, and confirms the run respected the repository's commit and artifact rules.

## Why This Matters

An iteration can finish without crashing and still leave the repository in a worse state.

Examples:

1. YAML files parse individually but references drift
2. `.agent/` memory files become inconsistent with repo reality
3. generated artifacts become nondeterministic or noisy
4. the run violates the intended commit shape even though files were changed successfully

The loop needs a definition of success stricter than "the command exited zero."

## Proposed Invariants

### Structured-file integrity

Verify:

- changed YAML still parses
- changed views reference allowed ids
- later, changed pattern files validate against schema and vocabulary constraints

### Memory integrity

Verify:

- core `.agent/` files still exist
- files referenced from current memory still exist
- repo map and status files are not obviously stale relative to changed areas when they were expected to change

### Commit-shape integrity

Verify at a coarse level that:

- the run did not create broad unrelated diffs
- memory updates were not silently skipped when a substantive content batch required them
- the resulting diff is scoped to the claimed task

### Deterministic artifact behavior

Verify that generated or derived artifacts use stable ordering and do not introduce meaningless churn.

This matters especially for future helpers that generate views, reports, or snapshot-like artifacts.

## Recommended Checks

Initial version:

1. run YAML validation
2. run `.agent/` memory checks when those files changed
3. flag unexpectedly broad diffs

Later version:

1. validate views
2. validate canonical patterns
3. compare derived coverage summaries to tracked coverage state

## Recommended Implementation

This proposal works best as a composition of small helpers rather than one large validator.

Likely helpers:

- `scripts/python/validate_yaml.py`
- `scripts/python/check_agent_memory.py`
- `scripts/python/validate_views.py`
- `scripts/python/validate_patterns.py`

The shell loop can orchestrate them and treat failure as a post-run validation error.

## Benefits

1. fewer false-positive successful runs
2. less repository drift over time
3. better confidence in unattended execution
4. smaller, cleaner diffs

## Risks And Tradeoffs

### Risk: validation becomes noisy

Mitigation:

1. separate warnings from blocking errors
2. validate only what is mature enough to check reliably
3. expand the rule set gradually

### Risk: commit-shape rules are subjective

Mitigation:

1. start with coarse guards
2. focus on clearly action-worthy mismatches
3. keep human review possible for ambiguous cases

## Acceptance Criteria

This proposal should be considered implemented when:

1. successful runs must pass a post-run validation stage
2. changed structured files are validated automatically
3. obviously inconsistent or overly broad runs are flagged
4. future derived artifacts are expected to be deterministic by default

## Decision Request

If accepted later, this proposal should define repository coherence checks as a required stage after agent execution and before a run is considered healthy.

