# Proposal: Execution Guards For Locks, Timeouts, And Safe Retries

- Status: proposed
- Date: 2026-03-20
- Scope: loop process safety and unattended execution
- Related areas: overlapping runs, hung processes, retry policy, repeated execution mode

## Question

What runtime guards should the loop add so unattended or repeated execution is safer under concurrency, hangs, and transient failures?

## Proposal Summary

Add explicit process guards for overlapping execution, timeout handling for hung runs, and a narrow retry policy for failures that are safe to retry.

## Problem

Autonomous or repeated loop execution becomes fragile when any of these are possible:

1. two loop processes run against the same repository at once
2. the agent invocation hangs indefinitely
3. transient startup failures require a safe retry path
4. retries happen after repository state has already been mutated in unclear ways

## Proposed Guards

### Run lock

Add a lock file or process guard so only one loop instance can operate on the repository at a time.

The lock should:

1. be created at run start
2. include enough metadata to identify the owner process
3. be cleared on normal exit and trap-based cleanup

### Timeout handling

Add a maximum iteration duration and optionally a shorter inactivity timeout for the agent invocation.

When a timeout occurs, the run should:

1. record the timeout clearly
2. preserve partial artifacts
3. avoid pretending the run completed cleanly

### Safe retry policy

Retries should be narrow and explicit.

Retry candidates:

1. transient tool startup failures
2. temporary agent invocation transport failures

Non-retry candidates without manual review:

1. failed post-run validation after repository mutations
2. semantic failures caused by bad repository state
3. ambiguous partial-write states

## Recommended Implementation

Extend the shell wrapper first, then move logic into a Python helper if the control flow grows.

Useful later helper:

- `scripts/python/loop_guard.py`

## Benefits

1. safer repeated execution
2. fewer corrupted overlapping runs
3. better behavior under tool flakiness
4. clearer failure states for hung iterations

## Risks And Tradeoffs

### Risk: stale locks block future runs

Mitigation:

1. include PID and timestamp data
2. allow explicit lock override with operator intent
3. clean up through shell traps

### Risk: retries hide real failures

Mitigation:

1. keep retry count low
2. retry only classified safe failures
3. record every retry in run metadata

## Acceptance Criteria

This proposal should be considered implemented when:

1. overlapping loop executions are prevented by default
2. hung runs terminate with a classified timeout state
3. retries are explicit, bounded, and limited to safe failure categories
4. timeout and retry outcomes are recorded in run artifacts

## Decision Request

If accepted later, this proposal should define execution safety guards as part of the loop contract rather than optional operator discipline.

