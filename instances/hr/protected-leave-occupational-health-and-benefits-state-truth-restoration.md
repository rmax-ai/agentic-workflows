# Protected leave occupational health and benefits state truth restoration

## Linked pattern(s)

- `critical-authoritative-state-restoration`

## Domain

HR.

## Scenario summary

After a restricted protected-leave escalation, the leave operations team finds that the employee's current status has diverged across the leave case system, occupational-health review tracker, benefits administration ledger, and HR case notes. One system shows the leave episode still open with an active medical restriction review, another shows the occupational-health packet as complete but tied to a different effective date, and the benefits record reflects a continuation state that no longer matches the leave case timeline. Before HR leadership, occupational health, benefits, and employee-relations reviewers decide whether any downstream action is appropriate, the workflow must restore the trusted current state of the protected-leave episode, occupational-health review status, and benefits-state dependencies, while preserving explicit holds for every conflict that cannot yet be reconciled under approved source-of-truth rules.

## Target systems / source systems

- Restricted leave case-management records, leave episode timelines, and reviewer notes used as candidate authoritative state for protected-leave status
- Occupational-health review tracker, certification packet references, restriction-status markers, and effective-date history
- Benefits administration eligibility and continuation ledgers, vendor status feeds, and exception records linked to the leave episode
- HRIS worker-status fields, case cross-reference identifiers, and manual escalation notes that may lag or contradict restricted systems
- Audit, hold-register, and authoritative-state acceptance tooling used to preserve unresolved discrepancies and human-reviewed restoration outcomes

## Why this instance matters

This grounds the pattern in an HR workflow where the urgent need is one trusted picture of current protected-leave-related state, not a decision about accommodation scope, return-to-work timing, payroll treatment, access changes, or employee communication. Conflicting leave, occupational-health, and benefits records can create severe harm if teams assume a case is settled when a protected dependency is still unresolved or if they treat stale downstream status as authoritative. The instance belongs in this family because it centers on reconciling current-state discrepancy, surfacing unresolved holds, and handing off a bounded trusted-state packet without adjudicating what should happen next.

## Likely architecture choices

- An orchestrated multi-agent workflow can separate restricted leave retrieval, occupational-health comparison, benefits-state reconciliation, and hold-register assembly while preserving one shared authoritative-state ledger.
- Human reviewers should remain in the loop to confirm which restricted systems outrank lagging HR or vendor views, accept the trusted current-state picture, and decide how unresolved holds are handled downstream.
- The workflow should stop at the trusted-state ledger, unresolved discrepancy register, and restricted HR handoff packet rather than determining accommodation scope, setting return-to-work dates, changing payroll or access, or notifying the employee.
- Shared case memory should preserve superseded state claims, late vendor updates, effective-date conflicts, and reviewer-visible rationale for every authoritative-state acceptance or hold.

## Governance notes

- Every leave-status, occupational-health review marker, benefits continuation state, and unresolved dependency should retain lineage to the exact source record, timestamp, and effective date that supports it.
- The workflow should keep the case on explicit hold whenever leave, occupational-health, and benefits systems cannot be reconciled inside approved precedence and freshness rules.
- Human leave, occupational-health, benefits, and employee-relations owners must approve any downstream use of the trusted-state packet for accommodation review, return-to-work planning, payroll coordination, access handling, or employee communication.
- Protected medical and benefits detail should remain minimized in the main handoff packet, with restricted evidence views used when broader reviewers only need generalized state references and hold reasons.

## Evaluation considerations

- Time to first human-reviewable trusted protected-leave state ledger with complete source lineage and explicit unresolved-hold handling
- Agreement between the workflow's restored current-state picture and the final human-accepted leave, occupational-health, and benefits status view
- Percentage of materially conflicting state branches preserved in the hold register until evidence converges or humans adjudicate them
- Reliability of the workflow when effective dates, vendor feeds, or restricted reviewer updates arrive asynchronously during repeated case refreshes
