# Accepted workplace accommodation review closure and case-tracker synchronization

## Linked pattern(s)

- `workflow-hand-off-and-completion`

## Domain

HR.

## Scenario summary

A restricted workplace-accommodation review team has already recorded an accepted or deferred final disposition for an accommodation case in the authoritative review system after the upstream reviewers completed their decision-making work. That disposition is final for this workflow and must not be reopened, reinterpreted, or extended into accommodation adjudication, undue-hardship interpretation, manager instruction, employee communication, accessibility or workplace-system changes, payroll action, or any new review. The remaining execute step is limited to low-risk post-decision closure bookkeeping: detect the final-disposition event, recheck that the accommodation case identifier, disposition version, and approved archive references still match the source record, close the restricted review queue item, sync the accommodation case tracker and accommodation ledger to the recorded review-complete state, attach archive references for the final review memo and supporting packet, record completion state in the audit store, and notify the internal HR accommodation coordinator that closure propagation is complete. If the case was reopened, the disposition changed, an archive reference drifted, or the target tracker points to a different accommodation episode, the workflow should stop and route manual follow-up instead of guessing.

## Target systems / source systems

- Restricted workplace-accommodation review system that records the accepted or deferred final disposition and emits the authoritative state-change event
- Accommodation case tracker and accommodation ledger that need the review-complete state reflected
- Restricted post-review queue holding the case until closure bookkeeping finishes
- Archive or evidence store containing the final review memo, supporting packet, and closure note references
- Internal HR accommodation coordinator notification channel plus audit store for completion traces, idempotency markers, and manual follow-up records

## Why this instance matters

This grounds the pattern in HR work where the consequential accommodation review judgment is already complete and the remaining need is safe closure propagation across restricted internal systems. Accommodation programs can accumulate drift when a final accepted or deferred disposition is recorded in the authoritative review system but the case tracker still appears open, the accommodation ledger lacks archive links, or a restricted closure queue continues to hold the episode. The example shows why execute-automate is useful for authoritative post-decision closure, replay-safe synchronization, privacy-minimizing bookkeeping, and explicit auditability while keeping adjudication, hardship analysis, employee outreach, workplace changes, payroll action, and renewed review activity outside scope.

## Likely architecture choices

- An event-driven completion worker can subscribe to accepted or deferred final-disposition events from the restricted review system and start the closure sequence only for approved post-decision states.
- The worker should re-read the current source record before writing anywhere so a reopened accommodation case, superseded disposition, or changed archive reference is not propagated from a stale event.
- Durable completion state should track queue closure, case-tracker synchronization, accommodation-ledger synchronization, archive linkage, notification delivery, and skipped idempotent actions because duplicate events or partial retries are normal operational conditions.
- Human follow-up should trigger when the accommodation-episode mapping is missing, the archive reference no longer matches the finalized review packet, or a requested next step would cross into adjudication, manager instruction, employee communication, workplace-system updates, payroll action, or any new review.

## Governance notes

- The workflow should copy only the accommodation case identifiers, final closure state, archive references, and timestamps needed for internal record synchronization rather than medical narrative, disability detail, manager correspondence, workplace-change requests, or reviewer discussion.
- Audit traces should record the source event id, verified disposition version, queue item closed, tracker and ledger records updated, archive references attached, notification target, and whether any step was skipped because it had already completed.
- Every automatic update should be reversible and idempotent so replay does not create duplicate queue cleanup, conflicting closure timestamps, repeated archive attachments, or duplicate coordinator notices.
- The automation must stop for manual follow-up when identifiers do not match, when the final-disposition state is no longer authoritative, or when any requested action would require accommodation adjudication, undue-hardship interpretation, manager instruction, employee communication, accessibility or workplace-system change, payroll action, or initiation of a new review.

## Evaluation considerations

- Percentage of accepted or deferred workplace-accommodation review dispositions that reach queue closure, case-tracker synchronization, ledger synchronization, archive linkage, audit recording, and coordinator notification without manual bookkeeping repair
- Rate of stale, duplicate, or mismapped final-disposition events detected before incorrect closure state is propagated across restricted HR systems
- Completeness of audit traces linking the authoritative review event to queue, tracker, ledger, archive, and notification updates
- Reliability of replay-safe recovery when one target is already updated or temporarily unavailable while other closure steps remain pending
