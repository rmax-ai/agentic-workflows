# Recommend, decide, escalate

**Family id:** `recommend-decide-escalate`

This family covers workflows that evaluate alternatives, justify a proposed course of action, and determine when a decision should be escalated rather than taken automatically. It sits between analysis and action, with governance-sensitive choice at the center.

## What belongs in this family

Use this family for patterns that:

- rank options against policy, evidence, or objectives,
- present rationale for a proposed decision,
- determine whether authority exists locally or must be escalated,
- support human or downstream system choice without yet performing the operational steps.

The conceptual seed patterns already named in the browse tree are:

- `decision-support-recommendation`
- `policy-aware-escalation`
- `option-ranking-with-rationale`

## Problem-structure mapping

This family maps cleanly to the `problem_structure` term `recommendation-and-decision-support`.

That mapping should anchor future canonical patterns when the main deliverable is a justified recommendation or governed choice.

## Family boundary

This family ends when a decision is supported, selected, or escalated.

- If the hard part is **constructing the plan or coordinating dependencies**, see [plan-coordinate-schedule](./plan-coordinate-schedule.md).
- If the hard part is **carrying out the chosen action under approvals or exception handling**, see [execute-automate](./execute-automate.md).
- If collaboration itself is the core workflow shape rather than one decision checkpoint, see [human-agent-collaborative-work](./human-agent-collaborative-work.md).

## Why this family is meaningfully agentic

The family becomes agentic when the system must weigh trade-offs, apply policy or risk constraints, expose rationale, and recognize when confidence or authority is insufficient for automatic progression. It is not just scoring; it is governed judgment support.

## Governance and evaluation concerns

Future patterns should identify decision rights, escalation triggers, rationale requirements, and the cost of bad recommendations. Evaluation should emphasize calibration, policy alignment, explanation quality, and whether escalation behavior is appropriately conservative.

## Guidance for future seed patterns

A strong canonical pattern in this family should state:

- what options or cases are being evaluated,
- what policy, evidence, or goals shape the ranking,
- who owns the final decision,
- when the output should hand off to execution, monitoring, or collaborative review.

## See also

- Previous family: [plan-coordinate-schedule](./plan-coordinate-schedule.md)
- Next family: [execute-automate](./execute-automate.md)
