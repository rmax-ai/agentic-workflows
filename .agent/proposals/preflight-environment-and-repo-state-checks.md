# Proposal: Preflight Environment And Repo-State Checks For The Loop

- Status: proposed
- Date: 2026-03-20
- Scope: loop robustness and execution safety
- Related areas: shell entrypoints, uv-managed Python helpers, git state, `.agent/` execution memory

## Question

What should the loop verify before an iteration begins so that it fails early on unsafe or unsupported repository state instead of failing mid-run?

## Proposal Summary

Add a dedicated preflight stage that verifies tool availability, required repository files, branch and git state expectations, and the chosen dirty-tree policy before prompt assembly or agent execution begins.

The goal is to reject invalid execution contexts early and consistently.

## Why This Matters

The current loop already checks a few prerequisites, but those checks are incomplete relative to the repository's actual operating contract.

The repository depends on:

1. committed execution-memory files under `.agent/`
2. a predictable git context
3. available local tooling such as `copilot`, `git`, `uv`, and the pinned Python runtime
4. a known policy for whether uncommitted changes are allowed during autonomous execution

Without a formal preflight step, the loop can begin in a partially invalid state and fail later after spending time assembling prompts or invoking the agent.

## Proposed Checks

### Tool availability

Verify:

- `git`
- `copilot`
- `uv`
- the configured Python 3.14 runtime through `uv`

### Repository structure

Verify:

- required `.agent/` files exist
- required prompt files exist or can be safely bootstrapped
- expected top-level directories exist

### Git context

Verify:

- execution is happening inside a git repository
- the current branch is allowed for loop execution
- the repository head can be resolved cleanly

### Dirty-tree policy

Make the policy explicit rather than implicit.

Possible modes:

1. `fail` if the tree is dirty
2. `warn` but continue
3. `scoped` where only approved transient or loop-owned paths may be dirty

### Memory integrity

Verify at a coarse level that:

- `.agent/current-plan.md` exists
- `.agent/backlog.yaml` exists
- `.agent/ontology-status.yaml` exists
- `.agent/repo-map.md` exists
- `.agent/decisions.md` exists

This should be existence and shape checking first, not deep semantic validation.

## Recommended Implementation

Introduce a helper such as `scripts/python/preflight_check.py` and have the shell loop call it before assembling the repository snapshot.

The helper should:

1. emit a human-readable summary
2. exit non-zero on blocking failures
3. record its results in the run directory when possible

## Policy Recommendations

### Default dirty-tree behavior

Default to `warn` for interactive runs and strongly consider `fail` or `scoped` for unattended repeated execution.

### Branch behavior

Allow execution on the current branch by default, but record the branch in preflight output and optionally warn when running on a non-default branch.

### Missing memory files

Treat missing core `.agent/` files as a blocking failure rather than allowing the loop to proceed in degraded mode.

## Benefits

1. faster failure on unsupported environments
2. less wasted iteration time
3. fewer mixed-state runs
4. safer unattended execution

## Risks And Tradeoffs

### Risk: over-strict preflight blocks useful work

Mitigation:

1. separate blocking checks from warnings
2. make dirty-tree behavior configurable
3. keep the first implementation conservative and observable

### Risk: duplicated logic between shell and Python

Mitigation:

1. move checks into the Python helper gradually
2. keep the shell wrapper thin once the helper is stable

## Acceptance Criteria

This proposal should be considered implemented when:

1. the loop runs a dedicated preflight stage before prompt assembly
2. tool and repository-state failures are reported clearly
3. dirty-tree behavior is explicit and documented
4. missing required `.agent/` files block execution predictably

## Decision Request

If accepted later, this proposal should establish preflight verification as a first-class loop stage rather than an ad hoc set of shell checks.

