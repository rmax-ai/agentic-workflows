# Approved real-time payments funding switch cutover staged execution

## Linked pattern(s)

- `staged-change-execution-with-rollback-holds`

## Domain

Finance.

## Scenario summary

After treasury operations, payments risk, and production-change authorities approve promotion of a new real-time payments funding switch to become the primary live path for outbound instant disbursements, payment operations must execute the cutover during a narrow high-volume release window. The workflow should start from that approved package and carry the change through explicit preflight on prefunded settlement balances, rail connectivity, duplicate-prevention state, acknowledgement parity, and legacy rollback health; then progress through shadow verification, limited-originator activation, broader rail-scope promotion, and a final protected hold before the old switch is retired. At each stage it should verify posting, acknowledgement, liquidity, and replay signals, keep rollback readiness intact, and stop visibly if the new live path begins to create ambiguous payment state or weaker reversibility.

```mermaid
flowchart TD
    A["Approved cutover window<br>traffic scope, release authorities, and rollback plan in force"] --> B["Run preflight checks<br>prefunded balances, rail connectivity, duplicate prevention, rollback health"]
    B --> C{"Preflight evidence within<br>approved payment and liquidity limits?"}
    C -- "No" --> D["Visible hold for treasury,<br>payments risk, and incident review"]
    C -- "Yes" --> E["Run shadow verification<br>on acknowledgements and settlement postings"]
    E --> F{"Shadow evidence and replay safeguards<br>remain healthy?"}
    F -- "No" --> D
    F -- "Yes" --> G["Activate limited approved originator cohort<br>while preserving legacy fallback"]
    G --> H{"Limited activation stays inside<br>error, liquidity, and duplicate thresholds?"}
    H -- "No" --> I["Restore legacy funding switch<br>and trigger bounded payment-operations escalation"]
    H -- "Yes" --> J["Human release hold before<br>broader rail-scope promotion"]
    J -- "Held" --> D
    J -- "Released" --> K["Promote the new switch across the approved live scope<br>and verify downstream posting alignment"]
    K --> L{"Broader-scope acknowledgements, postings,<br>and rollback readiness still stable?"}
    L -- "No" --> I
    L -- "Yes" --> M["Protected final hold before<br>retiring the legacy switch path"]
    M -- "Hold" --> D
    M -- "Release" --> N["Retire legacy switch path<br>and record authoritative-state confirmation"]
```

## Target systems / source systems

- Payments and treasury change-control record containing the approved cutover window, protected originator or rail scope, prefunding thresholds, and rollback plan
- New real-time payments funding switch, legacy funding switch, and the control plane used to move outbound instant-payment traffic between them
- Prefunded settlement account monitors, liquidity ledgers, and rail-status feeds used to confirm that the promoted path can fund and acknowledge live transactions safely
- Reconciliation, duplicate-detection, posting, and replay-protection systems used to verify each stage before the blast radius expands
- Audit store preserving checkpoint evidence, hold releases, fallback-restoration steps, and final authoritative-state confirmation

## Why this instance matters

This grounds the pattern in a finance workflow where the high-stakes action is a live payment-infrastructure cutover, not a forecasting promotion, browser submission, or recommendation packet. A real-time funding switch can look healthy at the transport layer while still creating duplicate-release risk, delayed acknowledgements, or prefunding stress that only appears after live payment traffic begins to move. The pattern matters because payment and treasury teams need disciplined staged execution that keeps release authorities, checkpoint evidence, and rollback viability explicit until the new switch proves it can carry production disbursements without creating ambiguous payment state.

## Likely architecture choices

```mermaid
flowchart LR
    CCR["Payments and treasury<br>change-control record"]
    CTRL["Funding-switch<br>control plane"]
    NEW["New real-time payments<br>funding switch"]
    LEG["Legacy real-time payments<br>funding switch"]
    LIQ["Settlement account monitors,<br>liquidity ledgers, and rail-status feeds"]
    VER["Reconciliation, duplicate-detection,<br>posting, and replay-protection systems"]
    AUD["Audit store"]

    subgraph HOLD["Human-in-the-loop holds<br>treasury, payments risk, and change authorities"]
        AUTH["Protected hold-release<br>and rollback decisions"]
    end

    CCR -->|"Sets approved cutover window,<br>protected scope, and rollback plan"| CTRL
    CCR -->|"Defines hold boundaries<br>and accountable authorities"| AUTH
    CTRL -->|"Routes approved cohort<br>and promoted live scope"| NEW
    CTRL -->|"Preserves rollback-ready<br>legacy path"| LEG
    LIQ -->|"Preflight balance, rail-health,<br>and live funding signals"| NEW
    LIQ -->|"Fallback funding and<br>connectivity baseline"| LEG
    NEW -->|"Acknowledgement, posting,<br>duplicate, and replay signals"| VER
    LEG -->|"Parity and rollback-health<br>comparison signals"| VER
    LIQ -->|"Prefunding and rail-status<br>checkpoint evidence"| AUTH
    VER -->|"Checkpoint evidence and<br>ambiguous-state stop signals"| AUTH
    AUTH -->|"Hold / release / restore direction"| CTRL
    CCR -->|"Approved package<br>and execution scope"| AUD
    CTRL -->|"Stage transitions and<br>fallback restoration steps"| AUD
    VER -->|"Verification evidence<br>and checkpoint lineage"| AUD
    AUTH -->|"Hold releases and<br>rollback decisions"| AUD
```

- Orchestrated multi-agent coordination fits because preflight validation, payment-rail verification, liquidity monitoring, and rollback-readiness checking often belong to separate payments, treasury, and platform roles.
- Human-in-the-loop holds should remain standard before promotion expands from the first approved originator cohort to the broader live rail scope and again before the legacy switch path is retired.
- Exception-gated autonomy keeps the workflow bounded: it may advance automatically through shadow checks and the first limited activation when thresholds remain healthy, but acknowledgement drift, duplicate-prevention ambiguity, or prefunding deterioration should force a visible hold or rollback packet.
- The execution record should show which treasury or payments authority released each protected hold and which checkpoint snapshot justified the release.

## Governance notes

- The workflow should confirm that approved originator scope, payment-type limits, cutover window boundaries, prefunded balance floors, and rollback credentials still match the signed change package before any live traffic moves.
- Checkpoint evidence should preserve rail acknowledgements, downstream posting completeness, duplicate-detection state, replay-buffer health, and prefunding consumption rather than relying on a single aggregate success signal.
- Logs and evidence should minimize exposure of payer or beneficiary identifiers, account details, and network secrets while still preserving enough lineage to reconstruct each staged decision.
- If the limited activation cohort shows delayed acknowledgements, duplicate-suppression uncertainty, prefunding stress, or inconsistent posting state, the workflow should hold or restore the legacy switch before widening live scope.
- Retirement of the prior switch path should remain a protected hold because it narrows rollback speed and can complicate recovery if a latent payment-state problem appears after broader promotion.

## Evaluation considerations

- Percentage of approved real-time payments switch cutovers completed without duplicate-release incidents, unplanned broad rollback, or material prefunding disruption
- Rate of acknowledgement drift, posting mismatch, or rollback-readiness loss caught at a visible hold before expansion beyond the initial originator cohort
- Completeness of the execution trail linking approvals, staged traffic changes, checkpoint evidence, hold releases, and any fallback restoration
- Time required to restore the legacy switch path when the new primary route passes basic transport health checks but fails deeper posting, liquidity, or duplicate-prevention verification
