# Managed-database major-version upgrade exception recommendation

## Linked pattern(s)

- `deal-desk-recommendation-support`

## Domain

Engineering.

## Scenario summary

A platform engineering review group is evaluating whether to support an accelerated production upgrade of the managed PostgreSQL version used by the checkout and order-history services after the cloud provider shortens support for the current major version. The requesting team wants approval to compress the normal compatibility window, accept a shorter rollback checkpoint, and combine the database engine upgrade with a required driver update before the seasonal release freeze begins. The workflow must recommend whether engineering should support the exception as scoped, counter with a narrower staged path, or escalate because rollback uncertainty, dependency compatibility, customer-impact risk, and change-governance thresholds move outside delegated approval limits before any production change is committed.

## Target systems / source systems

- Engineering change record, architecture exception request, and service-owner rationale for the proposed accelerated upgrade
- Managed-database platform inventory, vendor support timeline, environment topology, and current version exposure across production and staging
- Application dependency manifest, database-driver compatibility matrix, migration test evidence, and known query-behavior regressions
- Release calendar, production freeze policy, delegated approval matrix, and prior upgrade exception register
- Observability baselines, rollback runbook, recovery time objectives, and downstream dependency notes from site reliability and incident leadership

## Why this instance matters

This instance grounds the recommendation pattern in engineering where the hard problem is not generating upgrade steps or scheduling the cutover. The value is packaging a governed recommendation about whether an exception path is supportable, which safer fallback should be preferred if it is not, and exactly when the case must move to higher change authority because reversibility or blast-radius assumptions are no longer strong enough for local approval.

## Likely architecture choices

- A recommendation-only workflow can retrieve support deadlines, compatibility evidence, rollback readiness, precedent exceptions, and release-policy thresholds into one ranked option set for engineering review.
- Human-in-the-loop review is mandatory because the workflow should advise on acceptable upgrade paths and escalation triggers, not approve the exception, edit the production change record, or start the migration.
- Read-only integration with change management, cloud inventory, test evidence, and observability systems is preferable so the agent cannot silently convert a recommendation into a live infrastructure modification or deployment commitment.

## Governance notes

- The output should distinguish in-band upgrade options, conditional paths that depend on stronger rollback evidence or staged rollout controls, and blocked paths that breach freeze policy, recovery objectives, or dependency-support constraints.
- Any recommendation that relies on precedent should show whether the earlier case matched service criticality, engine-version gap, traffic profile, rollback mechanism, and coupling to application-driver changes.
- Requests that shorten rollback checkpoints, combine schema-sensitive application changes, bypass the standard pre-production soak, or move inside a freeze window should trigger explicit escalation rather than weighted scoring alone.
- Service topology details, customer-impact estimates, production incident history, and privileged infrastructure metadata should remain visible only to authorized engineering, reliability, security, and change-approval reviewers under normal access controls.
- Recommendation packets should preserve the assumptions, policy checks, evidence links, and reviewer comments used so change leaders can later audit why an accelerated path was supported, narrowed, or escalated.

## Evaluation considerations

- Reviewer agreement with the recommended upgrade path and escalation route before any production exception is approved
- Rate at which rollback, compatibility, or freeze-policy blockers are surfaced before engineering leaders commit to the accelerated change window
- Quality of evidence linking support deadlines, test results, recovery constraints, and precedent fit to the recommendation
- Stability of recommendations when vendor timelines, regression findings, or release-window constraints change during governed review
