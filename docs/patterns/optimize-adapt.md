# Optimize, adapt

**Family id:** `optimize-adapt`

This family covers workflows that improve future behavior using feedback from prior outcomes. Its main concern is adaptation under constraints: tuning plans, thresholds, policies, or actions so the system gets better over time without losing governance control.

## What belongs in this family

Use this family for patterns that:

- compare results against targets or expectations,
- adjust strategies, thresholds, or configurations in response,
- close continuous-improvement loops,
- refine behavior while preserving explicit policy or safety constraints.

The conceptual seed patterns already named in the browse tree are:

- `feedback-driven-optimization`
- `policy-constrained-adaptation`
- `continuous-improvement-loop`

## Problem-structure mapping

This family maps cleanly to the `problem_structure` term `feedback-driven-optimization`.

That mapping should anchor future canonical patterns when the primary structure is iterative improvement rather than initial planning or operational execution.

## Family boundary

This family is downstream of action and observation.

- If the main workflow is **ongoing detection and prioritization of new signals**, see [monitor-detect-triage](./monitor-detect-triage.md).
- If the main workflow is **sequencing checkpoints, coordination windows, or command timing under crisis pressure**, see [plan-coordinate-schedule](./plan-coordinate-schedule.md).
- If the main workflow is **choosing which human authority should decide a severe case**, see [recommend-decide-escalate](./recommend-decide-escalate.md).
- If the main workflow is **shared drafting, deliberation, or approval ownership between people and agents**, see [human-agent-collaborative-work](./human-agent-collaborative-work.md).
- If the main workflow is **executing approved work right now**, see [execute-automate](./execute-automate.md).

## Why this family is meaningfully agentic

These workflows are agentic when the system must interpret feedback, decide which adjustments are justified, and adapt without violating policy, quality, or risk constraints. Simple metrics dashboards do not qualify unless they feed governed adaptation behavior.

## Governance and evaluation concerns

Future patterns should state what can change automatically, what requires approval, how drift is detected, and what bounds keep optimization from exploiting the wrong objective. Evaluation should consider improvement quality, stability, unintended side effects, and whether the workflow remains inspectable as it adapts.

## Guidance for future seed patterns

A strong canonical pattern in this family should state:

- what feedback signals drive adaptation,
- what knobs or choices may change,
- what constraints limit adaptation,
- whether the loop stays automated or routes through collaborative review.

## Current canonical anchors

The current optimize/adapt anchors show the family across several governance levels:

- `adaptive-threshold-calibration` covers low-risk reversible tuning of sensitivity parameters inside pre-approved bounds.
- `queue-prioritization-optimization` covers moderate-risk learning loops that reorder existing work under explicit fairness and service guardrails.
- `governed-optimization-bundle-retuning` covers high-risk recommendation-only retuning of shared optimization state across coupled review surfaces.
- `critical-protected-priority-adaptation` anchors the critical slice with time-bounded severe-state optimization recommendations that protect scarce capacity, expiry discipline, and rollback readiness without drifting into authority selection, command planning, collaboration ownership, or direct execution.

Critical optimize/adapt work should remain centered on temporary optimization-state changes, protected-priority lane protection, or governed retuning packages. If the output starts naming who decides, sequencing the response, or triggering the live change directly, it belongs in an adjacent family instead.

## See also

- Previous family: [execute-automate](./execute-automate.md)
- Collaboration-oriented neighbor: [human-agent-collaborative-work](./human-agent-collaborative-work.md)
