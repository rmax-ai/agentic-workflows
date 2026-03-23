# Enterprise arrears settlement-band option recommendation

## Linked pattern(s)

- `delegated-authority-option-ranking`

## Domain

Finance.

## Scenario summary

An accounts-receivable operations team is reviewing a ninety-day-overdue enterprise invoice for a strategic customer that wants temporary relief while it completes an internal budget transfer. The collector can recommend only a narrow set of local options that sit inside a documented authority band, such as a capped late-fee waiver, a short installment plan, or a continued standard collections posture, but the customer is also asking for principal reduction and an extended payment holiday that would exceed delegated limits. The workflow must rank the in-band settlement options, show which requested terms are blocked by the collector authority matrix, and package escalation only if no locally permissible path remains appropriate before anyone changes billing records or sends a customer commitment.

```mermaid
flowchart TD
    A["Review overdue invoice case<br>and retrieve authority matrix, account history, and requested terms"] --> B["Check requested concessions against<br>delegated limits and hard guardrails"]
    B --> C{"Any requested term outside<br>collector authority?"}
    C -- "Yes" --> D["Record blocked terms and keep only<br>locally permissible settlement options"]
    C -- "No" --> E["Assemble the in-band option set<br>for local comparison"]
    D --> F{"Is account evidence current enough<br>for bounded review?"}
    E --> F
    F -- "No" --> G["Hold for refreshed payment, dispute,<br>or exposure evidence"]
    F -- "Yes" --> H["Rank the permissible options and<br>prepare a preferred recommendation"]
    H --> I{"Any defensible in-band<br>recommendation remains?"}
    I -- "Yes" --> J["Send the recommendation packet for<br>collector or finance lead review"]
    I -- "No" --> K["Package escalation for treasury/controller<br>before any billing or customer commitment change"]
```

## Target systems / source systems

- AR aging dashboard, invoice record, dispute notes, and collector work queue
- Contracted payment terms, late-fee policy, and delegated settlement authority matrix
- Customer account history, prior waivers, collections notes, and credit-risk flags
- Treasury or controller escalation criteria, precedent settlement cases, and write-off guardrails
- Recommendation log and audit trail for prior overrides or exception requests

## Why this instance matters

This grounds the pattern in finance where the hard problem is not adjudicating a write-off or editing the receivables system. The value is narrowing the recommendation to the safe local settlement options that remain inside collector authority, keeping blocked concession paths explicit, and escalating only when the request truly moves beyond the delegated envelope.

## Likely architecture choices

```mermaid
flowchart LR
    A["AR aging dashboard,<br>invoice record,<br>dispute notes, and collector work queue"] -->|"Read-only overdue case evidence"| F["Delegated settlement<br>option-ranking workflow"]
    B["Contracted payment terms,<br>late-fee policy, and delegated<br>settlement authority matrix"] -->|"Read-only policy guardrails"| F
    C["Customer account history,<br>prior waivers, collections notes,<br>and credit-risk flags"] -->|"Read-only account context"| F
    D["Treasury or controller escalation criteria,<br>precedent settlement cases,<br>and write-off guardrails"] -->|"Escalation and precedent context"| F
    F -->|"Produces bounded option ranking"| G["Recommendation packet:<br>in-band options,<br>blocked terms, or escalation-ready case"]
    F -->|"Writes rationale and threshold trace"| H["Recommendation log<br>and audit trail"]
    G -->|"Routes for governed judgment"| I["Collector or finance lead<br>decision boundary"]
    I -->|"Accepts local review path"| J["In-band recommendation review"]
    I -->|"Sends out-of-band case upward"| K["Treasury/controller<br>escalation lane"]
    F -.->|"Stops before billing mutation,<br>customer commitment, or write-off action"| L["Boundary guardrail"]
```

- A tool-using single agent can retrieve the authority bands, payment history, precedent cases, and current exposure values and turn them into one bounded settlement option ranking.
- Human-in-the-loop review still matters because the collector or finance lead chooses whether to accept the in-band recommendation locally or send the case upward for a larger concession review.
- Read-only integration with billing, contract, and collections systems is preferable so the recommendation workflow cannot silently waive fees, change payment dates, or post write-offs.

## Governance notes

- The output should distinguish locally permissible options, conditionally permissible options that depend on refreshed account evidence, and blocked requests such as principal forgiveness or payment holidays outside delegated caps.
- Prior waivers, disputed charges, and strategic-account notes should inform ranking inside the band but should never erase hard authority limits or write-off controls.
- Customer financial stress signals, contractual terms, and exception history should remain visible only to authorized collections, controller, treasury, and account reviewers.
- Recommendation packets should preserve threshold inputs, evidence freshness, blocked-option rationale, and any override requests so later audit can reconstruct why a local path was recommended or escalated.

## Evaluation considerations

- Rate at which accepted recommendations stay inside collector authority without later controller correction
- Time to produce a bounded settlement option packet after the overdue case enters delegated review
- Frequency with which blocked concession requests are surfaced before billing or customer-communication commitments are made
- Stability of option ranking when payment history, dispute status, or credit exposure changes during review
