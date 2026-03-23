# Network cold-chain excursion command crisis briefing evidence synthesis

## Linked pattern(s)

- `crisis-briefing-evidence-synthesis`

## Domain

Operations.

## Scenario summary

An operations command center has already declared a critical cold-chain event after temperature excursions propagate across multiple distribution hubs handling time-sensitive medical inventory. Before anyone decides recall scope, reroutes shipments, authorizes disposal, or initiates regulator notifications, the workflow must assemble one command briefing that compresses confirmed affected inventory, sensor confidence, facility conditions, transit status, quality-hold rules, and unresolved containment questions into a provenance-preserving brief. The goal is a time-sensitive shared picture that separates verified current state from lower-authority field notes and incomplete recovery assumptions so human crisis leaders can coordinate from grounded context rather than fragmented spreadsheets and bridge traffic.

```mermaid
flowchart TD
    A["Declared cold-chain event<br>and briefing scope"]
    B["Retrieve authoritative sensor,<br>calibration, inventory, and facility evidence"]
    C["Check source authority,<br>timestamps, and freshness"]
    D["Reconcile shipment state,<br>hold rules, and site conditions"]
    E["Assemble command brief with<br>verified facts, provenance, and open questions"]
    F["Human reviewer confirms<br>brief scope and evidence framing"]
    G["Handoff approved crisis brief<br>and supersession-ready record"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
```

## Target systems / source systems

- Operations command workspace where reviewed crisis briefs, restricted annexes, and superseded versions are stored
- Cold-chain sensor telemetry platform, excursion alarms, and calibration-history records for the affected lanes and hubs
- Warehouse management, shipment-tracking, and route-manifest systems showing current inventory location and in-transit status
- Quality-hold system, product disposition rules, and regulatory playbooks governing quarantine and release boundaries
- Facility maintenance logs, backup-power status, staffing rosters, and manual field check-ins from impacted sites
- Prior command briefs and unresolved-question tracker for continuity as the event evolves

## Why this instance matters

This grounds the pattern in an operations crisis where many live data feeds matter, but none alone provides a trustworthy situation picture. Critical excursions quickly mix sensor noise, manual readings, routing updates, and quality-policy constraints that carry different authority and freshness. The instance shows why a bounded crisis-briefing synthesis pattern is useful: leaders need fast cross-source compression with explicit provenance before they decide consequential inventory, safety, and regulatory steps.

## Likely architecture choices

```mermaid
flowchart LR
    subgraph approved["Approved operations, quality,<br>and safety repositories"]
        telemetry["Cold-chain sensor telemetry platform<br>excursion alarms and calibration-history records"]
        logistics["Warehouse management,<br>shipment-tracking, and route-manifest systems"]
        policy["Quality-hold system,<br>product disposition rules, and regulatory playbooks"]
        facilities["Facility maintenance logs,<br>backup-power status, staffing rosters, and manual field check-ins"]
        prior["Prior command briefs<br>and unresolved-question tracker"]
    end

    telemetry -->|"provides calibrated sensor evidence"| retrieve["Orchestrated multi-agent design<br>telemetry validation, shipment-and-inventory retrieval,<br>and policy-context assembly"]
    logistics -->|"provides inventory location<br>and transit status"| retrieve
    policy -->|"provides approved hold rules<br>and regulatory context"| retrieve
    facilities -->|"provides facility conditions<br>and manual field check-ins"| retrieve
    prior -->|"provides prior brief continuity<br>and open questions"| retrieve
    retrieve -->|"updates one shared command-state model"| state["Shared command-state model<br>provenance and freshness trace"]
    state -->|"feeds final briefing composition"| compose["Final briefing composition<br>review-ready crisis brief"]
    compose -->|"submits the brief for review"| review["Human reviewer<br>scope and evidence framing"]
    review -->|"hands off approved crisis brief<br>and supersession-ready record"| workspace["Operations command workspace<br>reviewed crisis briefs, restricted annexes, and superseded versions"]
```

- An orchestrated multi-agent design can split telemetry validation, shipment-and-inventory retrieval, policy-context assembly, and final briefing composition across specialized roles while preserving one shared command-state model.
- Human-in-the-loop review should remain mandatory because affected-product counts, manual temperature overrides, and regulator-facing statements can have safety and compliance consequences if overstated.
- The workflow should maintain a provenance and freshness trace that distinguishes calibrated sensor evidence, system-of-record inventory state, approved hold policies, and lower-authority site commentary.
- Retrieval should stay within approved operations, quality, and safety repositories, and the synthesis should stop at briefing handoff instead of recommending disposal, recall, or rerouting actions.

## Governance notes

- Calibrated sensor data, authoritative inventory records, and approved quality-hold rules should outrank ad hoc bridge notes or locally maintained spreadsheets when the event picture conflicts.
- Lot identifiers, shipment destinations, and customer-sensitive fulfillment details should be minimized or masked outside the restricted audiences that need them.
- Each brief revision should make stale facility checks and superseded route assumptions visible so command leaders do not treat old recovery reports as current fact.
- Open questions such as unverified pallet exposure, incomplete facility inspection, or uncertain carrier handoff state should remain explicit rather than being collapsed into confident product-status statements.

## Evaluation considerations

- Median time from critical cold-chain declaration to reviewer-approved command brief with complete source and freshness trace
- Percentage of affected-inventory, facility-status, shipment-state, and policy-constraint statements backed by inspectable authoritative sources
- Reviewer correction rate for sensor-authority handling, inventory scoping, or stale-site-status reuse across successive crisis briefs
- Rate at which unresolved containment, release, or regulator-trigger questions are surfaced explicitly before downstream operational decisions are made
