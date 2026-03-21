# Accepted protected-leave review closure and case-tracker synchronization

## Linked pattern(s)

- `workflow-hand-off-and-completion`

## Domain

HR.

## Scenario summary

A restricted protected-leave or return-to-work review has already reached an accepted disposition in the occupational health or leave-program review system after the upstream reviewers completed their decision-making work. That authoritative decision is final for this workflow and must not be reopened, reinterpreted, or extended into employee outcome handling. The remaining execute step is limited to low-risk closure: detect the accepted-disposition event, recheck that the case identifier, disposition version, and approved packet references still match the source record, close the restricted review queue item, sync the leave case and return-to-work tracker to the recorded review-complete state, attach archive references for the final packet and closure note, record completion state in the audit store, and notify the internal HR coordinator that the review-closure bookkeeping is complete. If the case was reopened, the packet reference drifted, or the tracker points to a different leave episode, the workflow should stop and route manual follow-up instead of guessing.

## Target systems / source systems

- Restricted occupational-health or leave-program review system that records the accepted disposition and emits the authoritative state-change event
- Leave case tracker or return-to-work coordination record that needs the accepted review-closure state reflected
- Restricted review queue holding the case until post-decision closure is complete
- Archive or evidence store containing the final approved packet, closure note, and linked record references
- Internal HR coordinator notification channel plus audit store for completion traces, idempotency markers, and manual follow-up records

## Why this instance matters

This grounds the pattern in HR without drifting into higher-risk employee administration. Teams often finish the real review decision but still carry manual cleanup across the restricted queue, leave tracker, archive links, and coordinator handoff, which creates avoidable drift and weak audit trails. The example shows why execute-automate is useful for a tightly bounded, event-triggered completion slice after an authoritative disposition already exists, while keeping payroll, scheduling, access, employee messaging, and manager commitments explicitly out of scope.

## Likely architecture choices

- An event-driven completion worker can subscribe to accepted-disposition events from the restricted review system and start the closure sequence only for approved post-decision states.
- The worker should re-read the current source record before writing anywhere so a reopened case, superseded packet reference, or changed disposition is not propagated from a stale event.
- Durable completion state should track queue closure, tracker synchronization, archive linkage, notification delivery, and skipped idempotent actions because duplicate events or partial retries are normal operational conditions.
- Human follow-up should trigger when the leave episode mapping is missing, the archive reference no longer matches the accepted packet, or a requested next step would require live employee-action execution beyond bookkeeping.

## Governance notes

- The workflow should copy only the case identifiers, accepted closure state, archive references, and timestamps needed for internal record synchronization rather than medical narrative, employee-facing notes, or reviewer discussion.
- Audit traces should record the source event id, verified disposition version, queue item closed, tracker records updated, archive references attached, notification target, and whether any step was skipped because it had already completed.
- Every automatic update should be reversible and idempotent: replay must not create duplicate queue cleanup, conflicting closure timestamps, or repeated archive attachments.
- The automation must not decide return-to-work readiness, verify release sufficiency, change leave eligibility, notify the employee, remove access, change payroll, schedule meetings, or commit the manager to any outcome.

## Evaluation considerations

- Percentage of accepted protected-leave review dispositions that reach queue closure, tracker synchronization, archive linkage, and coordinator notification without manual bookkeeping repair
- Rate of stale, duplicate, or mismapped accepted-disposition events detected before incorrect closure state is propagated across restricted HR systems
- Completeness of audit traces linking the authoritative review event to queue, tracker, archive, and notification updates
- Reliability of replay-safe recovery when one target is already updated or temporarily unavailable while other closure steps remain pending
