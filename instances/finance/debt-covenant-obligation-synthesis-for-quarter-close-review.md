# Debt covenant obligation synthesis for quarter-close review

## Linked pattern(s)

- `research-synthesis-with-citation-verification`

## Domain

Finance.

## Scenario summary

A controllership and treasury accounting team is preparing quarter-close support for a syndicated credit facility and a set of private placement notes. Before anyone finalizes covenant calculations, disclosure drafting, or lender reporting, the workflow needs a grounded synthesis of the currently effective leverage-ratio definitions, EBITDA add-back constraints, minimum-liquidity clauses, reporting deadlines, waiver conditions, and amendment precedence across executed agreements and internal close evidence. The value comes from retrieving the right source set, reconciling which documents are binding for the current quarter, and producing a cited brief that separates verified obligations from interpretation questions that still need legal or controller review.

## Target systems / source systems

- Controlled finance review workspace or close-management repository where the cited synthesis brief and evidence trace are stored
- Executed credit agreements, amendments, waiver letters, side letters, and lender notices in the legal document repository
- ERP or consolidation-system trial balance exports and account-mapping workpapers used in covenant calculations
- Treasury covenant workbook, prior compliance certificates, and quarter-close checklist artifacts
- SEC filing archive and disclosure-support repository for prior covenant and liquidity disclosures
- Legal interpretation memo library and exception or waiver register

## Why this instance matters

This grounds the gather/synthesize pattern in a finance workflow where fluent summarization alone would be risky. Quarter-close teams often work across layered amendments, prior waivers, and calculation workpapers that can quietly change which covenant terms are active, so the useful output is a source-grounded synthesis with inspectable provenance rather than a recommendation about financing strategy. The instance shows why evidence assembly, citation discipline, and explicit open questions matter before downstream disclosure, certification, or lender communication happens.

## Likely architecture choices

- A tool-using single agent can retrieve the active agreement set, extract candidate covenant clauses and deadlines, connect them to the current quarter's calculation support, and assemble a reviewable synthesis with claim-to-source mappings.
- Human-in-the-loop review should remain mandatory for amendment precedence, legal interpretation of ambiguous carve-outs, and confirmation that the brief is complete enough for quarter-close use.
- The workflow should preserve an evidence trace that distinguishes binding agreement language, internal calculation support, prior-period precedent, and unresolved interpretation notes.
- Retrieval and synthesis should stay scoped to approved finance and legal repositories; unsupported inference about EBITDA adjustments, waiver scope, or disclosure wording should be blocked.

## Governance notes

- Primary executed agreements and formally issued waivers should outrank slide decks, email summaries, or copied spreadsheet notes when the sources disagree.
- The synthesis should clearly separate verified covenant requirements, current-quarter calculation inputs, prior-period precedent, and unresolved interpretation questions instead of flattening them into one narrative.
- Effective dates, amendment supersession, and waiver expiration should be explicit because stale covenant text can create material reporting errors.
- Access to lender documents, legal memos, and close workpapers should stay within approved finance and legal permissions, with copied excerpts minimized to what reviewers need to inspect the cited claim.

## Evaluation considerations

- Percentage of material covenant, waiver, and reporting-deadline claims backed by inspectable citations to the current effective source set
- Reviewer correction rate for amendment precedence, calculation-scope interpretation, or citation mismatch during quarter-close review
- Rate at which missing waivers, superseded clauses, or unresolved interpretation gaps are surfaced explicitly before disclosure drafting or lender certification
- Usefulness of the open-questions section for accelerating controller, treasury, and legal review without forcing them to reassemble the source corpus from scratch
