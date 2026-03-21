# Medical leave certification packet to leave case record handoff

## Linked pattern(s)

- `document-to-structured-data-handoff`

## Domain

HR.

## Scenario summary

An HR leave operations team receives a multi-document intake packet after a manufacturing supervisor requests protected medical leave following an unplanned surgery with an expected intermittent rehabilitation period. The packet combines the employee's leave request form from the HR portal, a clinician certification with handwritten restrictions, hospital discharge paperwork, a faxed return-to-work note, a manager attendance summary, and scanned identity or relationship documentation needed to open the case under the employer's leave policy. Before any leave eligibility determination, payroll update, accommodation analysis, or employee-facing commitment occurs, the workflow must transform the packet into a structured leave-case staging record with required fields for employee identity, employer entity, leave event type, requested start date, expected duration window, intermittent-leave indicators, document inventory, restriction summary, missing-information flags, privacy tags, and source-evidence links while preserving uncertainty and contradictions.

## Target systems / source systems

- Leave-management or HR case-intake staging system with a versioned schema for new leave cases
- Secure employee portal, HR leave inbox, and restricted document repository holding request forms, clinician certifications, discharge papers, faxed notes, and supporting identity documents
- OCR and document-parsing service tuned for handwritten medical certifications, faxed forms, and mixed PDF packets
- HRIS worker master, employer-entity roster, leave-policy reference tables, and approved leave-reason taxonomy used for normalization only
- Exception queue for leave administrator or employee-relations review before any adjudication, payroll coordination, or outbound employee communication begins

## Why this instance matters

This grounds the transform pattern in an HR workflow where the valuable handoff is a trustworthy staged case record, not a benefits decision or automated leave action. Real leave packets arrive through mixed channels, often contain sensitive medical details, and can be incomplete or internally inconsistent in ways that a schema-valid output could hide if provenance and uncertainty are dropped. The instance shows why HR needs structured transformation with privacy-aware traceability and explicit exception routing before authorized humans decide what additional documentation is needed or whether the case can move into formal review.

## Likely architecture choices

- A tool-using single agent can assemble the packet, extract candidate case fields, normalize employee and employer identifiers against approved reference data, and emit a structured leave-case staging record plus transformation trace.
- The workflow should write only to a reviewable staging area in the leave case-management system rather than opening an adjudicated leave event, changing attendance status, or notifying payroll.
- Approved reference data may standardize employer entity, work location, leave-reason categories, and document types, but unsupported inference about medical severity, eligibility, protected-status qualification, or expected return date should force exception routing.
- Human review remains necessary when clinician dates conflict with the employee request, the packet implies intermittent leave without a usable frequency statement, identity or relationship evidence is incomplete, or the medical material appears to exceed what the initial leave-intake role is permitted to view.

## Governance notes

- Every consequential field should retain provenance to the exact portal submission, document page, fax section, or HRIS lookup that supports it, especially for leave start date, employee identity, leave event type, work restrictions, expected duration window, and missing-information flags.
- Least-privilege handling should separate document inventory and case-routing metadata from full medical attachments so reviewers who only need staging or exception triage do not receive unnecessary clinical detail.
- The workflow should route exceptions instead of handing off when the packet mixes multiple employees, contains contradictory provider dates, lacks the minimum identifiers needed to stage a case safely, or includes medical/supporting documents outside approved intake channels.
- Lossy normalization, such as compressing narrative rehabilitation restrictions into a controlled restriction-summary field or mapping free-text leave reasons into a standard taxonomy, should be explicit in the transformation trace rather than hidden behind a complete-looking case record.
- Human leave administrators, employee-relations staff, or designated medical-review personnel must decide whether the packet is sufficient for formal leave review, whether additional certification is needed, and what information may be shared with managers; the transformation workflow stops at a reviewable staged record.

## Evaluation considerations

- Percentage of staged leave-case records accepted by downstream leave administrators without manual re-entry of core intake fields
- Rate of incomplete, contradictory, or overexposed medical leave packets correctly diverted to exception review before adjudication or payroll-related downstream actions
- Completeness of field-level provenance and privacy tagging for identity, timing, restriction-summary, and document-inventory fields during audit or employee-dispute review
- Reliability of the handoff when clinician forms are handwritten, supporting documents arrive out of order, policy taxonomies change, or the staging schema adds a new required intake field
