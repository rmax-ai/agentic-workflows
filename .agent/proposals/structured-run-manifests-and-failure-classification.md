# Proposal: Structured Run Manifests And Failure Classification

- Status: proposed
- Date: 2026-03-20
- Scope: loop observability and recovery
- Related areas: `.agent/runs/`, iteration artifacts, run diagnosis, resume strategy

## Question

How should the loop record execution state so failures, no-op iterations, and partial results are easier to inspect and recover from?

## Proposal Summary

Add a machine-readable run manifest for each loop execution and classify outcomes into a small set of failure and non-failure states.

This would complement the existing text logs rather than replace them.

## Problem

The current run directory structure is useful for manual inspection, but it is mostly text-first. That makes automated diagnosis, reporting, and future recovery logic harder than it needs to be.

The loop would benefit from a single structured record that answers:

1. what version of the environment ran
2. what git state it started from
3. whether it failed before or after agent execution
4. whether it made changes
5. whether the run was a clean success, a no-op, or a classified failure

## Proposed Manifest

Add a JSON file such as:

- `.agent/runs/<timestamp>/run-manifest.json`

Suggested fields:

- timestamp
- branch
- head_sha
- start_time
- end_time
- duration_seconds
- tool_versions
- preflight_status
- prompt_build_status
- agent_execution_status
- post_run_validation_status
- overall_status
- changed_files
- commits_created
- failure_category
- failure_message
- no_op_reason

## Outcome Classes

Use a small consistent status vocabulary such as:

- `success`
- `success_noop`
- `failed_preflight`
- `failed_prompt_build`
- `failed_agent_execution`
- `failed_post_run_validation`
- `timed_out`

## Failure Classification

The main value is distinguishing where the run failed.

Examples:

### Preflight failure

The run never started safely.

### Prompt-build failure

Snapshot or prompt assembly failed before agent invocation.

### Agent-execution failure

The agent invocation failed, returned an error, or hung.

### Post-run validation failure

The run completed but left the repository in a state that violated expected checks.

## No-Op Runs

Treat a deliberate no-op as distinct from failure.

Examples:

- no dependency-safe step available
- only unsafe edits identified
- preconditions met, but the best action was to defer

This should still produce a successful run artifact with an explicit `no_op_reason`.

## Resume Guidance

The loop does not need full automatic resume immediately, but the manifest should make a future resume strategy possible.

Useful first step:

1. record the last completed stage
2. record whether repository mutations occurred
3. record whether cleanup or human review is needed before retry

## Recommended Implementation

Add a helper such as `scripts/python/write_run_manifest.py` or expand a broader run-orchestration helper later.

The shell loop should keep text logs and add the manifest alongside them.

## Benefits

1. clearer debugging
2. safer future automation
3. better visibility into no-op versus failed runs
4. easier trend analysis across many iterations

## Risks And Tradeoffs

### Risk: extra instrumentation adds complexity

Mitigation:

1. keep the schema small initially
2. prefer append-only run metadata
3. do not block loop execution on non-critical metadata enrichment

### Risk: status categories become too granular

Mitigation:

1. start with a small vocabulary
2. add categories only when they improve actionability

## Acceptance Criteria

This proposal should be considered implemented when:

1. each run emits a structured manifest
2. success, no-op, and failure states are distinguishable
3. failures are classified by stage
4. the manifest makes it clear whether the run changed repository state

## Decision Request

If accepted later, this proposal should establish structured run metadata as a required companion to human-readable logs.

