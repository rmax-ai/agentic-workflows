# Monitor, detect, triage

**Family id:** `monitor-detect-triage`

This family covers workflows that watch streams of events, identify notable conditions, and decide what deserves attention first. Its focus is continuous awareness and prioritization, not deep root-cause analysis or final resolution.

## What belongs in this family

Use this family for patterns that:

- monitor changing operational, user, or environmental signals,
- detect anomalies, incidents, or intake items worth surfacing,
- classify urgency, severity, or likely routing,
- queue work for deeper investigation, coordination, or action.

The conceptual seed patterns already named in the browse tree are:

- `event-monitoring-and-alert-triage`
- `anomaly-detection-review`
- `issue-intake-triage`

## Problem-structure mapping

This family maps cleanly to the `problem_structure` term `continuous-monitoring-and-triage`.

That term should anchor future canonical patterns when the persistent challenge is ongoing signal watching plus prioritization.

## Family boundary

This family usually stops at prioritization and routing.

- If the main challenge becomes **explaining why a flagged issue exists or reconciling records**, move to [investigate-reconcile-verify](./investigate-reconcile-verify.md).
- If the main challenge becomes **choosing and sequencing coordinated next steps**, move to [plan-coordinate-schedule](./plan-coordinate-schedule.md).
- If the workflow directly **acts on the alert under control rules**, it may cross into [execute-automate](./execute-automate.md).

## Why this family is meaningfully agentic

These workflows are agentic when the system must interpret noisy signals, adapt thresholds or routing logic to context, suppress unhelpful churn, and preserve just enough structured context for downstream responders. Static alerting alone is too shallow for the family boundary defined here.

## Governance and evaluation concerns

Future patterns should make attention cost, escalation thresholds, false-positive tolerance, and missed-event risk explicit. Evaluation should consider signal quality, prioritization usefulness, latency, and whether the workflow helps humans focus on the right work rather than simply generating more noise.

## Guidance for future seed patterns

A strong canonical pattern in this family should state:

- what event or signal stream is being monitored,
- what counts as notable or urgent,
- what contextual evidence accompanies a triaged item,
- where the handoff goes next: investigation, planning, execution, or human review.

## See also

- Previous family: [investigate-reconcile-verify](./investigate-reconcile-verify.md)
- Next family: [plan-coordinate-schedule](./plan-coordinate-schedule.md)
