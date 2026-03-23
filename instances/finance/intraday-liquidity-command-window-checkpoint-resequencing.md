# Intraday liquidity command-window checkpoint resequencing

## Linked pattern(s)

- `critical-command-window-resequencing`

## Domain

Finance.

## Scenario summary

During a severe payment-rail disruption, treasury has declared a critical liquidity bridge window with a current sequence for bank confirmation review, collateral availability challenge, cash-state control sign-off, executive coordination, and market-open communication preparation. Then authoritative timing shifts land inside the same bridge: one bank confirmation arrives late, a control reviewer becomes unavailable and hands off to an approved delegate, and the market-open communication lock time moves earlier because of exchange and lender coordination pressure. The workflow must resequence the live bridge checkpoints, preserve explicit holds where prerequisite confirmation or authority is still missing, and produce one current bridge packet that leaders can adopt before any funding, payment-freeze, or disclosure action is considered.

```mermaid
flowchart TD
    A["Declared liquidity bridge window<br>and active checkpoint sequence"]
    B["Verify authoritative timing shifts for<br>bank confirmation freshness, collateral and cash-state readiness,<br>approved control delegate handoff, and earlier market-open lock time"]
    C{"Can treasury keep an in-policy<br>checkpoint order before the earlier<br>market-open boundary?"}
    D["Place blocked checkpoints on hold<br>and log timing, freshness, or authority conflicts<br>in the bridge ledger"]
    E["Bounded escalation to treasury and risk leaders<br>for protected-window or ownership resolution"]
    F{"Do leaders resolve the conflict<br>without crossing authority or timing rules?"}
    G["Keep the hold state active<br>and wait for new authoritative updates"]
    H["Assemble one updated bridge packet<br>with the resequenced checkpoint ledger,<br>hold register, and targeted participant deltas"]
    I{"Do treasury leaders adopt<br>the resequenced bridge packet?"}
    J["Publish the authoritative bridge timeline<br>and targeted checkpoint updates for<br>live liquidity coordination"]
    A --> B
    B --> C
    C -->|"No"| D
    D --> E
    E --> F
    F -->|"No"| G
    F -->|"Yes"| H
    C -->|"Yes"| H
    H --> I
    I -->|"No"| G
    I -->|"Yes"| J
```

## Target systems / source systems

- Treasury bridge workspace containing the declared critical scope, active checkpoint order, and prior packet versions
- Bank confirmation feeds, treasury cash-state tooling, and collateral dashboards publishing authoritative readiness changes
- Delegate records, calendars, and on-call schedules for treasury control, funding desk, risk review, and executive coordination roles
- Market-open and lender-communication deadline tracker showing protected external timing boundaries
- Audit and notification tooling used to log superseded timelines, held checkpoints, and targeted bridge updates

## Why this instance matters

This grounds the pattern in a finance coordination workflow where the main challenge is keeping the bridge timeline itself trustworthy while severe conditions change quickly. The workflow is not restoring the authoritative cash truth, choosing a funding strategy, or pushing any external communication. Instead, it keeps one current ordered set of bridge checkpoints, makes blocked sequencing visible, and protects human ownership over the live command timeline that downstream decisions depend on.

## Likely architecture choices

```mermaid
flowchart LR
    subgraph SRC["Authoritative source boundary"]
        READY["Bank confirmation feeds,<br>cash-state tooling, and collateral dashboards"]
        AUTH["Delegate records, calendars,<br>and on-call schedules"]
        DEADLINE["Market-open and lender<br>deadline tracker"]
    end

    subgraph BRIDGE["Governed bridge resequencing boundary"]
        WORK["Treasury bridge workspace<br>with declared scope, active checkpoint order,<br>and prior packet versions"]
        VERIFY["Readiness verification<br>lane"]
        CHECK["Protected-window and delegate<br>authority checker"]
        RESEQ["Checkpoint resequencer<br>and hold-state manager"]
        PACKET["Bridge packet assembler<br>with current ledger and hold register"]
    end

    subgraph HUMAN["Human adoption boundary"]
        LEADERS["Treasury and risk leaders"]
    end

    AUDIT["Audit and notification tooling"]
    STOP["Workflow stop boundary"]

    READY -->|"Provides authoritative bank,<br>cash-state, and collateral readiness"| VERIFY
    AUTH -->|"Provides approved delegate<br>and availability authority"| CHECK
    DEADLINE -->|"Provides protected market-open<br>and lender timing boundaries"| CHECK
    WORK -->|"Supplies declared bridge scope,<br>active sequence, and prior versions"| RESEQ
    VERIFY -->|"Passes verified readiness<br>changes and freshness state"| CHECK
    CHECK -->|"Passes allowed moves,<br>holds, and authority conflicts"| RESEQ
    RESEQ -->|"Builds the updated checkpoint order<br>and explicit hold states"| PACKET
    PACKET -->|"Stores superseded timelines,<br>participant deltas, and packet lineage"| WORK
    RESEQ -->|"Logs blocked checkpoints,<br>hold reasons, and resequencing changes"| AUDIT
    PACKET -->|"Publishes targeted bridge updates<br>and supersession notices"| AUDIT
    PACKET -->|"Routes the resequenced bridge packet<br>for human adoption"| LEADERS
    LEADERS -->|"Adopts the checkpoint order<br>or keeps the bridge on hold"| WORK
    PACKET -->|"Stops before funding decisions,<br>facility draws, or market communication execution"| STOP
```

- An orchestrated multi-agent workflow can split readiness verification, protected-window checking, checkpoint resequencing, and bridge-packet assembly while preserving one shared timeline.
- Human-directed control fits because treasury and risk leaders must adopt any changed checkpoint order before the new sequence can govern market-open coordination.
- The workflow should preserve explicit hold states when bank-confirmation freshness, delegate authority, or communication-boundary timing remains unresolved.
- The workflow should stop at the resequenced bridge ledger and hold register rather than recommending payment restrictions, facility draws, or lender messaging.

## Governance notes

- Protected checkpoints such as cash-state review, control challenge, executive coordination, and communication-preparation windows should be encoded separately from flexible timing preferences.
- Only approved delegate mappings for treasury control, risk, and executive coordination should be allowed to change live checkpoint ownership.
- Bridge packets should expose role-relevant timing and checkpoint state without copying full account, counterparty, or strategy detail into broad coordination channels.
- Human treasury ownership is required before the updated sequence becomes authoritative for consequential market-open, payment, or disclosure coordination.

## Evaluation considerations

- Time from authoritative timing shift to an adopted bridge packet with explicit checkpoint lineage and holds
- Percentage of blocked or cross-boundary bridge checkpoints kept visible in the hold register rather than hidden in the main timeline
- Agreement between the workflow's resequenced bridge ledger and the final human-adopted timeline for the disruption window
- Reliability of the workflow when multiple bank, control, and communication constraints change within one market-open cycle
