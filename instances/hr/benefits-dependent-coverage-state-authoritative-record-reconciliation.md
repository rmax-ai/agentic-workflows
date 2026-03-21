# Benefits dependent coverage state authoritative record reconciliation

## Linked pattern(s)

- `authoritative-record-reconciliation`

## Domain

HR.

## Scenario summary

After a mid-year family-status change and a delayed eligibility-feed correction, people operations discovers that dependent coverage state for several employees no longer agrees across the benefits-administration platform, the carrier eligibility ledger, the dependent-verification case tracker, and the HRIS life-event record. One source shows a newly added dependent as active for medical coverage with a corrected qualifying-event date, another still treats the prior election set as current for the same plan year, and the verification tracker contains approved document evidence that supports the relationship change but not the effective date now reflected in the carrier-facing ledger. Before any payroll deduction adjustment is executed, any carrier outreach is initiated, or any benefits specialist decides whether the drift came from stale enrollment feeds, late documentation, or manual processing error, the workflow must restore one trusted current dependent-coverage state for each affected enrollment, keep unresolved conflicts visible, and hand off a correction-ready package for controlled record repair.

## Target systems / source systems

- Benefits-administration enrollment records, dependent coverage elections, plan-tier fields, and life-event processing logs
- Carrier eligibility ledgers, member-coverage extracts, effective-date history, and inbound enrollment acknowledgment files
- Dependent-verification case records holding document-review outcomes, approved relationship evidence, and exception notes
- HRIS life-event entries, employee and dependent cross-reference identifiers, and qualifying-event timestamps used to anchor source-of-truth matching
- Audit and reconciliation workspace tooling used to preserve field-level discrepancy ledgers, unresolved review items, and reversible correction packages

## Why this instance matters

This grounds the pattern in an HR workflow where the urgent problem is not deciding whether an employee's change request should have been approved or what deduction, communication, or carrier action should happen next, but restoring one defensible authoritative record before downstream teams rely on contradictory dependent-coverage data. Benefits state often drifts across HRIS, enrollment, carrier, and verification systems because each platform updates on different clocks and under different evidence rules, so a seemingly current record can still be unsafe when plan tier, dependent status, or effective date lineage does not align. The instance stays in this family because it focuses on authoritative-state restoration, discrepancy visibility, and correction-ready handoff rather than adjudication, payroll execution, employee communication, carrier negotiation, or root-cause analysis.

## Likely architecture choices

- A tool-using single agent can gather enrollment extracts, carrier eligibility snapshots, dependent-verification records, and HRIS life-event references into one bounded reconciliation run.
- Human-in-the-loop review should remain standard for conflicting dependent identity mappings, disputed qualifying-event dates, missing verification evidence, or any case where a proposed correction would alter current medical, dental, or vision coverage state.
- The workflow should stop at the reconciled dependent-coverage ledger, unresolved exception queue, and staged correction package rather than changing deductions, transmitting carrier updates, or deciding appeal outcomes.
- Shared reconciliation memory should preserve superseded election values, applied source-precedence logic, prior steward adjudications, and rollback references so later reviewers can inspect exactly why one coverage state became authoritative.

## Governance notes

- Every employee and dependent identifier, coverage-tier field, effective date, verification outcome, and acknowledgment reference should retain lineage to the exact source record and extraction time that supports the reconciled state.
- The workflow should place an enrollment on explicit reconciliation hold whenever the benefits platform, carrier ledger, and verification evidence cannot be aligned inside approved precedence and freshness rules.
- Human benefits and HR operations owners must approve publication of ambiguous, bulk, or plan-sensitive corrections into authoritative systems even when routine in-policy field repairs are otherwise reversible.
- Working ledgers and handoff packets should minimize exposed personal and health-related detail, using masked dependent identifiers or internal references wherever full relationship documentation is not necessary for steward review.

## Evaluation considerations

- Time to produce a human-reviewable authoritative dependent-coverage ledger with complete field-level lineage and visible unresolved exceptions
- Agreement between the workflow's reconciled enrollment state and the final steward-accepted current-state view before any downstream deduction or carrier update proceeds
- Percentage of dependent-coverage conflicts routed into explicit hold or review queues rather than silently overwritten during reconciliation
- Reliability of correction-package generation when life-event timestamps, verification decisions, or carrier acknowledgments refresh during repeated reconciliation runs
