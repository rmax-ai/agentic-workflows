# Redacted third-party due diligence case batch to governance-review dataset

## Linked pattern(s)

- `batch-content-transformation`

## Domain

Compliance.

## Scenario summary

An anti-bribery and corruption (ABC) compliance team is preparing an annual programme-effectiveness review for the audit and compliance committee. The raw batch includes third-party due diligence investigation files spanning several hundred intermediaries, agents, and joint-venture partners: intake questionnaires, background-screening reports, beneficial-ownership declarations, high-risk-country exception narratives, payment justification memos, escalation notes, and prior-approval correspondence. Many files contain the legal names, passport or registration numbers, home-country addresses, and bank details of named individuals; commercially sensitive transaction amounts and deal structures; and unresolved investigation findings that may intersect with pending regulatory matters. Before any committee review, cross-programme benchmarking, or external counsel read-out can begin, the workflow must transform that batch into a redacted structured governance-review dataset with pseudonymous third-party identifiers, normalised risk-tier and jurisdiction codes, due-diligence outcome fields, exception-category tags, escalation-stage markers, restricted-content flags, and trace links held inside the approved compliance boundary while removing individual identifiers, banking details, commercial transaction specifics, and active-investigation references from the release-safe package.

## Target systems / source systems

- Restricted compliance case-management repository holding due diligence files, screening reports, exception memos, and escalation correspondence
- Redaction and de-identification tooling for personal identifiers, financial account references, investigation-sensitive content, and deal-specific commercial terms across text, PDFs, and attached spreadsheets
- ABC-programme schema registry defining approved review fields, controlled risk-tier and jurisdiction taxonomies, and audience-specific release constraints for committee reporting
- Review workbench and governed staging store for the redacted dataset, transformation trace, and batch approval manifest
- Exception queue for ABC legal, privacy, and investigations review before any material leaves the restricted due-diligence workspace

## Why this instance matters

This grounds the transform pattern in a compliance setting where committee-level governance depends on structured programme-wide views that cannot expose the personal data, commercially sensitive transaction details, or active-investigation references contained in individual due diligence files. The useful output is a reviewed, release-safe structured dataset for internal governance oversight, not a regulatory submission, adjudication of any individual intermediary relationship, or operational instruction to business lines. The instance shows why multi-layer redaction, policy-constrained generalisation, and human approval are necessary when compliance batches combine identity records, financial details, and investigation narratives that can remain identifying or legally sensitive even after obvious names are removed.

## Likely architecture choices

- An orchestrated multi-agent workflow can divide file parsing and segmentation, sensitive-element detection across personal identifiers and financial fields, jurisdiction and risk-tier normalisation, and release-package validation so that each stage exposes its reasoning and residual-risk findings independently.
- Human reviewers should remain in the normal loop because due diligence files often contain contextual investigation narratives, cross-referenced individuals, and unresolved escalation threads that automated detectors cannot release safely without ABC-programme and legal judgment.
- The workflow should emit only a release-safe committee review dataset and reviewed manifest rather than updating live intermediary records, generating a regulatory position, or instructing relationship managers on remediation actions.
- Approved rules may generalise jurisdiction references into risk-tier buckets, collapse specific payment amounts into broad bands, and replace intermediary names with scoped pseudonyms, but unsupported inference about culpability, regulatory exposure, or relationship-exit recommendations must not be added to the transformed output.

## Governance notes

- Every structured field should retain restricted-boundary lineage to the source case file, screening-report section, or exception-memo paragraph that supports it so ABC legal, audit, or investigations reviewers can verify disputed redaction or category choices without expanding general committee access to raw files.
- The workflow should route exceptions when a file contains active regulatory inquiry references that cannot be generalised safely, when a named individual or entity appears in multiple cases in a way that could still reveal identity after single-record pseudonymisation, or when commercial terms are so distinctive that amount-band generalisation would still expose the underlying transaction.
- Lossy transformations, such as compressing multi-page exception narratives into short coded escalation reasons or collapsing specific jurisdiction names into high-risk-region tags, should be visible in the trace and approval manifest rather than hidden behind a polished committee dataset.
- ABC compliance, legal, and privacy reviewers must decide whether the batch is safe for the intended governance audience; the transformation workflow stops at the reviewed staging dataset and does not adjudicate any due diligence relationship or trigger any downstream operational action.

## Evaluation considerations

- Percentage of transformed due diligence case records accepted by the audit and compliance committee review without reopening restricted source files
- Rate of residual personal-identifier, financial-account, or active-investigation findings discovered during reviewer sampling after batch approval
- Quality of semantic preservation when detailed exception narratives and screening-report findings are converted into normalised risk-tier codes, outcome fields, and escalation-stage markers
- Reliability of the handoff when files contain scanned identification documents, mixed-language correspondence, deal structures spanning multiple entities, or newly classified high-risk jurisdiction designations
