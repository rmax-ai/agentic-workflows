# Network cold-chain emergency reroute activation gate

## Linked pattern(s)

- `contingency-plan-activation-gate`

## Domain

Operations.

## Scenario summary

During a regional refrigeration-control outage, network operations has already declared a bounded contingency path that would reroute temperature-sensitive inventory through alternate cross-docks and overflow cold storage if the primary network cannot recover before product-age thresholds are breached. Upstream monitoring and incident workflows have already established the trusted facility status and the named human approval lane. The planning workflow must now prepare one activation-ready reroute packet showing trailer commitments, receiving-site capacity, quality-release checkpoints, cold-chain monitoring coverage, and protected customer-communication holds. It should keep explicit holds for any lane that lacks confirmed carrier acceptance, receiving capacity, or quality sign-off, and stop at the approval gate instead of dispatching trucks, changing inventory state, or choosing a different emergency response.

```mermaid
flowchart TD
    A["Declared reroute scope<br>and authoritative readiness inputs"]
    B["Assemble lane-by-lane reroute readiness ledger<br>for trailers, receiving sites, quality checkpoints,<br>monitoring coverage, and communication holds"]
    C["Check each lane for confirmed carrier acceptance,<br>receiving capacity, quality sign-off,<br>and monitoring continuity"]
    D{"Any prerequisite missing<br>or still provisional?"}
    E["Record explicit hold state<br>for blocked lane and unmet prerequisite"]
    F["Compile activation-ready reroute packet<br>with ready lanes, protected holds,<br>resource commitments, and lineage"]
    G{"Human approval gate<br>for reroute activation packet?"}
    H["Held packet remains pending<br>with visible blockers and approval queue state"]
    I["Approved activation-ready packet<br>published as the gate output"]

    A --> B
    B --> C
    C --> D
    D -->|"Yes"| E
    D -->|"No"| F
    E --> F
    F --> G
    G -->|"Hold"| H
    G -->|"Approve"| I
```

## Target systems / source systems

- Network continuity runbooks and operations command workspace with the declared reroute scope, prior packet versions, and product-age constraints
- Facility-status, carrier-commitment, dock-capacity, and monitoring systems already designated as authoritative inputs for reroute preparation
- Quality-review records, delegate rosters, and scheduling tools for site leaders, carrier coordinators, food-safety reviewers, and network control
- Approval-routing and audit systems used to record open holds, packet lineage, and final human authorization before reroute activation
- Restricted communications tools for customer-impact and partner-notice timing that remain downstream of the planning gate

## Why this instance matters

This grounds the pattern in operations where the value is assembling one coherent contingency activation packet before any trucks move. It is distinct from contamination command-window resequencing because the workflow is not managing a live active command timeline after activation starts. It is also distinct from execution because the workflow remains bounded at readiness planning, capacity alignment, and visible hold management rather than dispatching the reroute itself.

## Likely architecture choices

```mermaid
flowchart LR
    A["Network continuity runbooks<br>and operations command workspace"]
    B["Facility-status, carrier-commitment,<br>dock-capacity, and monitoring systems"]
    C["Quality-review records,<br>delegate rosters, and scheduling tools"]
    H["Restricted communications tools<br>for customer-impact and partner-notice timing"]

    subgraph P["Reroute preparation and<br>approval-gated publication boundary"]
        D["Lane-by-lane reroute<br>readiness ledger"]
        E["Activation-ready reroute packet"]
        F["Open holds and packet lineage<br>in approval-routing and audit systems"]
        G["Human network-operations<br>approval gate"]
        I["Approved activation-ready<br>reroute packet"]
    end

    A -- "Provides declared reroute scope,<br>prior packet versions, and product-age constraints" --> D
    B -- "Supplies authoritative facility, carrier,<br>capacity, and monitoring inputs" --> D
    C -- "Adds quality state, delegate coverage,<br>and scheduling commitments" --> D
    D -- "Links trailer commitments, receiving-site capacity,<br>quality checkpoints, monitoring coverage,<br>and protected holds" --> E
    D -- "Preserves blocked lanes,<br>unmet prerequisites, and revisions" --> F
    F -- "Shows open holds and lineage<br>to the approval lane" --> G
    E -- "Submits one reroute activation packet<br>for human authorization" --> G
    G -- "Leaves blocked packets pending<br>with visible holds" --> F
    G -- "Approves publication of<br>the reroute activation packet" --> I
    I -- "Records final authorization<br>and packet lineage" --> F
    I -- "Keeps customer-impact and partner-notice timing<br>downstream of the planning gate" --> H
```

- Approval-gated execution fits because the reroute may be fully prepared in systems while still blocked pending a human operations approval.
- The readiness ledger should link trailer, carrier, receiving-site, monitoring, and quality checkpoints so network leadership can see which lanes are actually activation-ready.
- Holds should remain explicit for missing receiving capacity, incomplete quality release, or unconfirmed temperature-monitoring coverage.
- The workflow should stop at the approval packet and hold register rather than re-verifying the facility truth, recommending a broader crisis authority, or dispatching inventory movement.

## Governance notes

- Protected prerequisites such as food-safety release, cold-chain monitoring continuity, receiving-site acceptance, and customer-notice controls should be modeled as explicit holds before the packet can be approved.
- Shared packets should disclose only role-relevant lane, timing, and blocker state while restricted shipment, customer, and contractual details stay in narrower governed systems.
- Human network-operations ownership is required before the packet becomes the authoritative basis for any emergency reroute activation.
- Packet lineage should preserve which carrier, capacity, and site-readiness commitments changed across revisions so later reviews can distinguish planned readiness from executed action.

## Evaluation considerations

- Time from declared reroute-preparation request to a human-reviewable activation packet with complete lane readiness and hold visibility
- Rate at which blocked lanes or missing monitoring coverage remain visible rather than being masked by partial readiness elsewhere in the network
- Agreement between the workflow's reroute packet and the final human-approved contingency gate used for downstream activation
- Reliability of the packet when carrier acceptance, receiving capacity, or quality status changes repeatedly during the same product-risk window
