# Approved payroll status change submission

## Linked pattern(s)

- `browser-based-form-completion-with-approval-gates`

## Domain

HR.

## Scenario summary

An HR operations specialist needs to submit an approved employee status change for a shift supervisor moving from hourly to salaried payroll after promotion. The target payroll platform is browser-only, requires multiple tabs for compensation, effective date, tax handling, and benefits eligibility, and the submission may proceed only after the manager, HR business partner, and payroll approver have all signed off in the case system.

## Target systems / source systems

- HR case-management system with manager, HRBP, and payroll approvals
- Browser-only HRIS or payroll portal for worker status and compensation updates
- Employee master-data record and approved compensation change form
- Payroll calendar, effective-date rules, and deduction or tax reference tables
- Evidence store for screenshots, confirmation numbers, and exception notes

## Why this instance matters

This grounds the execution pattern in a sensitive HR workflow where the system action is real, consequential, and difficult to unwind after payroll closes. The value is not just form filling; it is controlled execution that proves the right approvals existed, the right fields were entered, and a human can take over safely if the portal behaves unexpectedly.

## Likely architecture choices

- Approval-gated execution should prepare the submission packet, verify current approvals, and block final commit until all required sign-offs are rechecked.
- A tool-using single agent can navigate the browser workflow, populate fields, upload support documents, and capture evidence at each checkpoint.
- Human-in-the-loop control remains standard for ambiguous effective dates, portal layout drift, failed validations, or any mismatch between approved compensation terms and live form values.

## Governance notes

- Approval state should be verified from the system of record immediately before final submission rather than trusted from cached case context.
- Screenshots, logs, and evidence bundles must minimize exposure of compensation, tax, and personal data while remaining audit-ready.
- The workflow should stop safely on effective-date conflicts, payroll cutoff issues, or missing approvals instead of submitting a partially trusted change.
- Human takeover steps should be explicit so payroll staff can resume from the saved state without duplicating or corrupting the submission.

## Evaluation considerations

- Percentage of approved payroll status changes submitted without post-payroll correction
- Rate of blocked or escalated cases that were stopped before an incorrect final commit
- Completeness of evidence bundles for internal audit or payroll dispute review
- Reliability of safe takeover when the portal changes, times out, or returns ambiguous confirmation
