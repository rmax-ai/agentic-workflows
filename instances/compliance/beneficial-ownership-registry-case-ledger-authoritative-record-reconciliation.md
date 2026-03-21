# Beneficial ownership registry and case-ledger authoritative record reconciliation

## Linked pattern(s)

- `authoritative-record-reconciliation`

## Domain

Compliance.

## Scenario summary

After a cross-border entity restructuring and a time-compressed annual review, a compliance operations team discovers that the current beneficial ownership picture for several regulated subsidiaries no longer agrees across the internal KYC case ledger, the corporate transparency registry snapshot, the legal-entity master, and the sanctions-screening ownership graph. One source shows a newly added intermediate holding company with an effective date tied to board approval, another still treats the prior natural-person controller as the active reportable owner, and the most recent review packet contains supporting ownership percentages that match the new chain but not the controlling-person designation now reflected in one downstream system. Before any registry amendment is filed, any customer risk tier is changed, any alert disposition is revisited, or any team decides whether the drift came from late filings, mapping error, or stale ingestion, the workflow must restore one trusted current beneficial ownership state for each affected entity, keep unresolved conflicts visible, and hand off a correction-ready package for controlled record repair.

## Target systems / source systems

- Internal KYC or customer due-diligence case ledger holding current beneficial-owner assertions, review decisions, and evidence references
- Corporate transparency or beneficial ownership registry snapshots, filing extracts, and reported effective-date history
- Legal-entity master records, approved ownership-chain diagrams, capitalization tables, and corporate-secretary change packets
- Sanctions-screening or customer-risk reference graph storing controller relationships, screened-owner aliases, and downstream entity-link mappings
- Reconciliation workspace tooling used to preserve field-level discrepancy ledgers, unresolved identity or effective-date exceptions, and reversible correction packages

## Why this instance matters

This grounds the pattern in a compliance workflow where the pressing problem is not deciding why ownership records drifted or what filing or screening action should happen next, but restoring one defensible authoritative current-state record before regulated decisions rely on contradictory ownership data. Beneficial ownership state often spans registries, internal case systems, and screening references, so a single apparently updated record can still be unsafe when controller identity, effective date, or ownership percentage lineage does not align across sources. The instance stays in this family because it centers on authoritative-state restoration, discrepancy visibility, and correction-ready handoff rather than root-cause investigation, regulator communication, customer outreach, screening adjudication, or filing execution.

## Likely architecture choices

- A tool-using single agent can gather case-ledger extracts, registry snapshots, ownership-chain evidence, and screening-reference records into one bounded reconciliation run.
- Human-in-the-loop review should remain standard for conflicting controller identity, threshold-edge ownership percentages, disputed effective dates, or any case where a proposed correction would change a regulated ownership assertion.
- The workflow should stop at the reconciled beneficial-ownership ledger, unresolved exception queue, and staged correction package rather than submitting a registry update, re-screening customers, changing risk ratings, or directing investigative follow-up.
- Shared reconciliation memory should preserve superseded ownership claims, applied source-precedence logic, prior steward adjudications, and rollback references so later reviewers can inspect exactly why one ownership state became authoritative.

## Governance notes

- Every entity identifier, beneficial-owner attribute, percentage, effective date, and controller designation should retain lineage to the exact source record and extraction time that supports the reconciled state.
- The workflow should place an entity into explicit reconciliation hold whenever the case ledger, registry snapshot, and ownership evidence cannot be aligned inside approved precedence and freshness rules.
- Human compliance or corporate-governance owners must approve publication of ambiguous, bulk, or regulator-sensitive corrections into authoritative systems even when routine in-policy field repairs are otherwise reversible.
- Working ledgers and handoff packets should minimize exposed personal identifiers for natural-person owners, using masked values or stable internal references wherever full detail is not necessary for steward review.

## Evaluation considerations

- Time to produce a human-reviewable authoritative beneficial-ownership ledger with complete field-level lineage and visible unresolved exceptions
- Agreement between the workflow's reconciled ownership state and the final steward-accepted current-state view before any registry or screening updates proceed
- Percentage of ownership conflicts routed into explicit hold or review queues rather than silently overwritten during reconciliation
- Reliability of correction-package generation when registry extracts, review packets, or downstream screening references refresh during repeated reconciliation runs
