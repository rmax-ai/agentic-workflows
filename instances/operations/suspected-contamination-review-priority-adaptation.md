# Suspected contamination review priority adaptation

## Linked pattern(s)

- `critical-protected-priority-adaptation`

## Domain

Operations.

## Scenario summary

Operations leadership has already declared a severe contamination-response state after distribution and field reports suggest one refrigerated product lot may be spreading risk across multiple facilities and routes. Several existing review surfaces now compete for the same constrained specialist pool: lot-hold evidence review, traceability-gap assessment, field-inspection triage, and routine quality-exception follow-up. The normal prioritization state still surfaces easy documentation cleanup and lower-consequence inspection backlog items while supervisors repeatedly override the queues to protect potential spread paths, regulator-visible holds, and at-risk facility reviews. The workflow must recommend a temporary emergency optimization state that protects contamination-critical review lanes, preserves explicit expiry and rollback controls, and reallocates scarce attention without choosing the response authority, sequencing the command playbook, releasing or holding inventory, or dispatching corrective work directly.

## Target systems / source systems

- Command dashboard with the declared contamination scope, active review backlogs, and current lot or facility hold state
- Traceability systems, facility quality-event feeds, inspection backlogs, and route-exposure analysis tools
- Supervisor override history, review-aging telemetry, and rollback records from prior severe-quality events
- Emergency safety and quality governance rules covering protected contamination classes, regulator-visible review requirements, reserve-capacity floors, and expiry review timing
- Versioned queue-policy and audit systems used by operations, quality, and safety leaders to adopt or restore temporary severe-mode prioritization

## Why this instance matters

This grounds the pattern in operations where the hard problem is adapting existing review and routing logic under a declared severe safety state rather than investigating root cause, coordinating the command timeline, or executing lot-disposition actions. A weak critical adaptation could let routine follow-up work crowd out contamination-spread review and protected inspection lanes just when reversibility is shrinking fastest. The workflow remains inside optimize/adapt territory because it ends at a human-adopted temporary optimization state with rollback and expiry controls, not direct operational action.

## Likely architecture choices

- Orchestrated multi-agent coordination fits because telemetry review, protected-lane checking, severe-mode simulation, and rollback packaging can be separated while keeping one coherent contamination-response state.
- Human-in-the-loop review is required because quality and safety leaders must explicitly adopt, extend, or reject any temporary reprioritization that affects protected contamination-review work.
- Human-directed autonomy keeps the workflow bounded: it can recommend temporary lane reservations and urgency weights, but it must not choose the incident authority, sequence field actions, or release or hold product directly.

## Governance notes

- Potential spread-path review, regulator-visible hold checks, and at-risk facility inspections should remain protected lanes that severe-mode optimization cannot weaken for throughput reasons.
- Every package should make clear which routine quality tasks are deferred temporarily and why that trade-off remains reversible and acceptable under the severe state.
- Auditability should preserve baseline and temporary queue states, supervisor overrides, expiry reviews, extension approvals, and rollback events for later safety and quality review.
- Sensitive facility, supplier, and lot-detail evidence should be minimized in the main adaptation packet and confined to authorized annexes where possible.
- The workflow must not select who owns the response, plan the command sequence, or trigger operational execution; it only recommends temporary optimization-state changes for existing review surfaces.

## Evaluation considerations

- Reduction in aging and override frequency for contamination-critical traceability, hold-review, and field-inspection work after the temporary state is adopted
- Speed from severe contamination declaration to a reviewed adaptation packet with clear expiry and rollback controls
- Evidence that protected contamination-review lanes remain surfaced even while routine quality backlog remains present
- Reliability of rollback when containment confidence improves or when the emergency tuning no longer strengthens protected-priority handling
