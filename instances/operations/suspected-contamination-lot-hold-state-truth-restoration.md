# Suspected contamination lot hold state truth restoration

## Linked pattern(s)

- `critical-authoritative-state-restoration`

## Domain

Operations.

## Scenario summary

During a declared contamination event, the command center finds that lot hold and movement status diverge across genealogy systems, warehouse quarantine records, shipment manifests, and quality-review workbenches. Some downstream pallets appear contained in one system but still in transit in another, while one facility's manual hold action has not propagated consistently across partner-facing tracking views. Before operations, quality, and legal leaders decide whether the exposed inventory picture is stable enough for recall scoping, partner direction, or regulator communication, the workflow must determine which lots are definitively quarantined, which shipments are still exposed, and which branches remain unresolved because authoritative evidence conflicts.

```mermaid
flowchart TD
    A["Collect genealogy, quarantine, shipment, and facility-hold evidence<br>with timestamps and lineage"]
    B["Compare authoritative lot and pallet state<br>under freshness, precedence, and identity rules"]
    C{"Do the authoritative records converge on<br>current containment status?"}
    D["Write the trusted containment ledger<br>for reconciled lots and pallet branches"]
    E["Place conflicting lot branches in an unresolved hold register<br>with evidence gaps and hold reasons"]
    F{"Can bounded reviewer-visible verification<br>resolve the remaining branch conflicts?"}
    G["Update the trusted containment ledger<br>with newly verified branch status"]
    H["Preserve unresolved branches alongside the trusted ledger<br>with explicit uncertainty and lineage"]
    I["Assemble the command-center handoff packet<br>from the trusted ledger and unresolved register"]

    A -->|"Collect evidence"| B
    B -->|"Check authoritative agreement"| C
    C -->|"Yes"| D
    C -->|"No"| E
    E -->|"Run bounded verification"| F
    F -->|"Yes"| G
    F -->|"No"| H
    D -->|"Prepare bounded handoff"| I
    G -->|"Prepare bounded handoff"| I
    H -->|"Prepare bounded handoff"| I
```

## Target systems / source systems

- Manufacturing genealogy, quality, and facility-hold systems containing authoritative lot and quarantine state
- Warehouse management, shipment manifest, and carrier-status systems showing inventory movement and in-transit holds
- Laboratory review records, incident command workbenches, and manual containment attestations from facility teams
- Partner-tracking or distribution-status views that may lag the internal hold systems
- Audit and hold-register tooling used to preserve unresolved lot branches and authoritative-state acceptance decisions

## Why this instance matters

This grounds the pattern in an operations workflow where the urgent task is restoring one trusted containment picture rather than packaging a safe external view, diagnosing the contamination source, or deciding the recall itself. Conflicting lot and shipment state during a safety event can create severe harm if teams assume containment that has not actually happened or overlook branches that remain exposed. The instance fits this family because it is centered on reconciling authoritative discrepancy and preserving unresolved truth gaps before any downstream action or communication is chosen.

## Likely architecture choices

```mermaid
flowchart LR
    genealogy["Genealogy, quality, and<br>facility-hold systems"]
    logistics["Warehouse, shipment-manifest,<br>and carrier-status systems"]
    reviews["Lab review records,<br>incident workbenches, and<br>manual containment attestations"]
    lagging["Lagging partner-tracking or<br>distribution-status views"]
    workspace["Command-center truth-restoration workspace<br>trusted containment ledger,<br>unresolved hold register, and case memory"]
    reviewers["Quality, operations, and legal<br>reviewers"]
    packet["State-restoration handoff packet<br>for downstream human decisions"]
    audit["Audit and hold-register tooling<br>authoritative-state acceptance,<br>superseded views, and rationale"]

    genealogy -->|"Authoritative lot, quarantine,<br>and facility-hold state"| workspace
    logistics -->|"Inventory movement and<br>in-transit hold evidence"| workspace
    reviews -->|"Review findings and<br>manual containment attestations"| workspace
    lagging -->|"Conflicting downstream views<br>kept visible for comparison"| workspace
    workspace -->|"Trusted ledger and<br>unresolved branch register"| reviewers
    reviewers -->|"Accepted current-state decisions<br>and protected conflict resolution"| workspace
    workspace -->|"Bounded trusted-state packet<br>with unresolved ambiguity"| packet
    workspace -->|"Lineage, hold reasons,<br>and superseded snapshots"| audit
    reviewers -->|"Authoritative-state acceptance<br>and hold approvals"| audit
```

- An orchestrated multi-agent workflow can separate genealogy retrieval, warehouse and shipment comparison, hold-branch classification, and handoff-packet assembly while maintaining one command-center truth ledger.
- Human reviewers should remain in the loop to confirm which sources outrank lagging partner views, accept the authoritative containment picture, and decide how unresolved branches are treated downstream.
- The workflow should stop at the trusted-state ledger, unresolved hold register, and command-center handoff packet rather than recommending recall scope, issuing partner instructions, or changing inventory state automatically.
- Shared case memory should preserve superseded lot views, late telemetry backfills, and reviewer-visible rationale for every hold or authoritative-state decision.

## Governance notes

- Every quarantine status, in-transit exposure flag, facility hold marker, and unresolved lot branch should retain lineage to the exact source records and timestamps that support it.
- The workflow should keep lot branches on hold whenever genealogy, shipment, and facility records cannot be reconciled inside approved freshness and precedence rules.
- Human quality, operations, and legal owners must approve any downstream use of the trusted-state packet for recall, partner communication, or regulator notification.
- Facility-specific and partner-sensitive identifiers should remain restricted when broader command-center consumers can work from generalized or aliased references.

## Evaluation considerations

- Time to first trusted containment ledger with complete lineage and explicit unresolved-branch handling
- Agreement between the workflow's authoritative lot-state picture and the final human-accepted current-state view
- Percentage of ambiguous shipment or pallet branches preserved in the hold register until evidence converges
- Reliability of the workflow when warehouse state, carrier updates, and manual facility holds arrive asynchronously during repeated command-center refreshes
