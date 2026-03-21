# Intraday liquidity facility-draw authority recommendation

## Linked pattern(s)

- `critical-escalation-authority-recommendation`

## Domain

Finance.

## Scenario summary

During a severe payment-rail disruption, treasury has already opened a critical bridge after incoming settlement delays, collateral timing drift, and one counterparty funding shortfall compress the firm's liquidity runway before market close. The workflow must recommend whether the next decision belongs with the treasury funding desk under existing contingency limits, the CFO-led liquidity committee, or an executive risk and legal authority because a central-bank facility draw, selective payment restriction, or lender communication posture may be required. It must narrow the governed option set and assemble a decision packet without drawing facilities, restricting payments, or issuing any market-facing statement.

```mermaid
flowchart TD
    A["Critical treasury bridge<br>already opened before market close"]
    B["Collect intraday cash-state evidence,<br>collateral timing, payment deadlines,<br>authority matrix, and active hold state"]
    C{"Does the case remain inside treasury funding desk<br>contingency limits for recommendation review?"}
    D{"Do facility-draw, selective payment restriction,<br>or lender communication triggers require<br>executive risk and legal ownership?"}
    E["Recommend treasury funding desk<br>Narrow options to in-limit contingency paths<br>with external actions still held"]
    F["Recommend CFO-led liquidity committee<br>Bound review to committee-owned contingency options<br>with desk-only paths blocked"]
    G["Recommend executive risk and legal authority<br>Keep facility draw, payment restriction,<br>and lender communication on hold"]
    H["Assemble authority packet with evidence,<br>blocked lower-authority lanes,<br>bounded options, and timing constraints"]
    I{"Named human authority accepts<br>the recommended lane and option set?"}
    J["Workflow stops at reviewed recommendation packet<br>No facility is drawn, no payments are restricted,<br>and no market-facing statement is issued"]
    K["Maintain hold state, log the redirect,<br>and reroute only within the bounded<br>review path to the required authority"]

    A --> B --> C
    C -- "Yes" --> E
    C -- "No" --> D
    D -- "No" --> F
    D -- "Yes" --> G
    E --> H
    F --> H
    G --> H
    H --> I
    I -- "Yes" --> J
    I -- "No" --> K
```

## Target systems / source systems

- Treasury bridge workspace with declared severity, prior decision packets, and active hold state
- Intraday cash-state tooling, settlement-status feeds, collateral dashboards, and contingency-funding prerequisites
- Authority matrix covering desk limits, CFO committee triggers, executive risk review, and legal sign-off thresholds
- Payment-obligation calendar, market-close deadlines, and lender or central-bank communication constraints
- Prior contingency-funding cases, audit records, and restricted-review channel controls for market-sensitive material

## Why this instance matters

This grounds the pattern in finance where the key challenge is not restoring the authoritative cash picture or resequencing the bridge timeline. The value is selecting the correct human decision lane and exposing only the bounded options that remain policy- and market-safe before anyone commits the organization to a facility draw, payment restriction, or external communication.

## Likely architecture choices

- An orchestrated multi-agent workflow can split cash and collateral evidence retrieval, delegation checking, option narrowing, and packet assembly while preserving one critical-case ledger.
- Human-in-the-loop review is mandatory because the workflow should advise on authority ownership and allowable decision paths, not trigger funding, hold payments, or contact lenders.
- Human-directed autonomy fits because treasury, finance, risk, and legal authorities must explicitly adopt the decision lane before a market-sensitive action is even considered.

## Governance notes

- The output should distinguish options that remain inside desk or committee limits from options that require executive risk and legal ownership because of market, disclosure, or capital consequences.
- Any narrowed option set should preserve reversibility boundaries around payment restrictions, central-bank facility use, and lender communication timing rather than treating them as interchangeable tactical choices.
- Market-sensitive exposure detail, counterparty information, and privileged funding assumptions should remain confined to authorized treasury, risk, legal, and executive reviewers.
- Recommendation packets should preserve policy citations, timing constraints, prior redirects, and evidence freshness so later review can reconstruct why a particular authority lane was recommended.

## Evaluation considerations

- Time from critical bridge activation to a reviewed authority packet with bounded contingency options
- Agreement between the workflow's recommended authority lane and the final human-accepted decision owner for the liquidity event
- Rate at which blocked lower-authority paths and disclosure-sensitive constraints are surfaced before any facility or payment action is approved
- Reliability of authority recommendations when cash-state, collateral, or deadline assumptions change rapidly before market close
