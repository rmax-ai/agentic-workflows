# Vendor master and treasury settlement instruction authoritative record reconciliation

## Linked pattern(s)

- `authoritative-record-reconciliation`

## Domain

Finance.

## Scenario summary

After an ERP-payables integration and a rushed vendor-admin role change, accounts payable and treasury discover that payment instructions for several high-value suppliers no longer agree across the ERP vendor master, the treasury settlement-instruction repository, the approved bank-account hash register, and the callback-verification case log. One supplier record shows a newly imported IBAN and SWIFT pair with a recent portal-sync timestamp, another source still marks the prior account as the active settlement instruction for the next payment run, and the callback record supports the new account ownership evidence but not the effective date now shown in the ERP profile. Before any payment batch is released, any bank-account change is submitted, or any control owner decides whether fraud, admin error, or migration drift occurred, the workflow must restore one trusted current remittance state for each affected supplier, keep unreconciled conflicts visible, and hand off a correction-ready package for controlled record repair.

## Target systems / source systems

- ERP accounts-payable vendor master records, active payment-method fields, remittance profiles, and integration update logs
- Treasury settlement-instruction repository, bank-account reference hashes, effective-date history, and signer-approved instruction snapshots
- Vendor onboarding or maintenance case records holding callback-verification notes, account-ownership evidence, and prior approved change packets
- Payment-run staging tables, supplier cross-reference mappings, and exception ledgers that show which instructions are queued for upcoming disbursements
- Audit and reconciliation workspace tooling used to preserve field-level discrepancy ledgers, unresolved review items, and reversible correction packages

## Why this instance matters

This grounds the pattern in a finance workflow where the urgent problem is not deciding why the instruction drift happened or whether the next payment should go out, but restoring one defensible authoritative record before downstream action uses inconsistent vendor data. Vendor payment instructions sit at the intersection of fraud control, treasury accuracy, and operational timeliness, so a superficially clean master record can still be dangerous when the evidence chain does not line up across approval and settlement systems. The instance stays in this family because it focuses on authoritative-state restoration, discrepancy visibility, and correction-ready handoff rather than root-cause investigation, payment execution, supplier outreach, or broader master-data redesign.

## Likely architecture choices

- A tool-using single agent can fetch vendor-master extracts, treasury instruction snapshots, callback-verification records, and payment-staging references into one bounded reconciliation run.
- Human-in-the-loop review should remain standard for mismatched legal-entity mappings, conflicting effective dates, account-ownership ambiguity, or any case where a proposed correction would affect a pending high-value payment.
- The workflow should stop at the reconciled remittance ledger, unresolved exception queue, and staged correction package rather than submitting bank changes, approving payment release, or redesigning supplier-governance controls.
- Shared reconciliation memory should preserve superseded account values, applied source-precedence logic, prior adjudications, and rollback references so later stewards can inspect exactly why one instruction became authoritative.

## Governance notes

- Every supplier identifier, settlement-instruction field, effective date, approval reference, and hash-match result should retain lineage to the exact source record and extraction time that supports the reconciled state.
- The workflow should place a supplier on explicit reconciliation hold whenever the ERP active instruction, treasury authoritative snapshot, and callback-verification evidence cannot be aligned inside approved precedence and freshness rules.
- Human AP and treasury owners must approve any publication of ambiguous, bulk, or payment-cycle-sensitive corrections into authoritative systems even when routine in-policy field updates are otherwise reversible.
- Working ledgers and handoff packets should minimize exposed bank-account detail, using masked values or hashes wherever full routing and account numbers are not necessary for steward review.

## Evaluation considerations

- Time to produce a human-reviewable authoritative remittance ledger with complete field-level lineage and visible unresolved exceptions
- Agreement between the workflow's reconciled supplier payment-instruction state and the final steward-accepted current-state view before the next payment cycle
- Percentage of instruction conflicts routed into explicit hold or review queues rather than silently overwritten during reconciliation
- Reliability of correction-package generation when integration timestamps, callback evidence, or pending-payment indicators change during repeated refreshes
