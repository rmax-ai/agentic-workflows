# Regional aviation-fuel terminal contamination authority recommendation

## Linked pattern(s)

- `critical-escalation-authority-recommendation`

## Domain

Operations.

## Scenario summary

A critical fuel-quality threat has already been declared after conflicting laboratory and inline-sensor results suggest one regional aviation-fuel terminal may have loaded contaminated product into the hydrant supply chain serving multiple airport banks. Terminal operations, enterprise fuel supply, airport continuity teams, and executive safety leaders now need a governed recommendation about which human authority should decide the next step: keep the case inside terminal incident authority for tightly bounded isolation review, move it to enterprise fuel-supply command for network dispatch-suspension review, or escalate to executive safety and continuity authority because multi-airport service posture and protected continuity options may be implicated. The workflow must narrow the decision-ready option set and assemble the authority packet without releasing fuel, rerouting dispatches, changing airport conservation posture, or coordinating the wider response.

```mermaid
flowchart TD
    A["Critical fuel-quality threat<br>already declared at regional terminal"]
    B["Collect sample lineage, tank and hydrant traces,<br>loaded-truck history, airport stock posture,<br>delegation rules, and active hold state"]
    C{"Does the case remain inside terminal incident authority<br>for one-site isolation review under current<br>delegated safety and continuity limits?"}
    D{"Do multi-airport supply continuity, network allocation,<br>or protected executive hold triggers require<br>higher safety and continuity ownership?"}
    E["Recommend terminal incident authority<br>Limit options to bounded local isolation review<br>with network actions blocked"]
    F["Recommend enterprise fuel-supply command<br>Narrow options to terminal dispatch suspension<br>and controlled substitution review"]
    G["Recommend executive safety and continuity authority<br>Keep network conservation posture and airport-wide<br>service commitments on hold pending higher review"]
    H["Assemble authority packet with evidence,<br>blocked lower-authority paths,<br>bounded options, and annex references"]
    I{"Named human authority accepts<br>the recommended lane and option menu?"}
    J["Workflow stops at reviewed recommendation packet<br>No fuel is released, no dispatch is rerouted,<br>and no continuity posture is directed"]
    K["Hold state remains in effect, log the redirect,<br>and reroute only within the bounded<br>review path to the required authority"]

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

- Critical operations workspace with the declared contamination scope, current hold state, and prior packet revisions
- Terminal control and quality systems holding tank genealogy, inline-sensor telemetry, sample chain-of-custody records, and truck or hydrant loading history
- Airport stock and demand dashboards, regional dispatch schedules, substitution constraints, and continuity-threshold ledgers
- Safety, continuity, and delegation matrix covering terminal authority limits, enterprise fuel-supply decision rights, and executive escalation triggers
- Prior fuel-quality incidents, restricted annex tooling, and audit logs for human redirects, packet recipients, and protected evidence handling

## Why this instance matters

This grounds the critical recommendation pattern in operations without drifting into contamination investigation briefing, airport continuity planning, or live dispatch control. The hard problem is deciding which human authority should own the severe choice and what tightly bounded options they should see once one terminal's quality uncertainty may expand into multi-airport service risk that local operators cannot resolve alone.

## Likely architecture choices

```mermaid
flowchart LR
    subgraph S["Operations evidence and policy sources"]
        Q["Terminal control and quality systems<br>tank genealogy, inline-sensor telemetry,<br>sample chain-of-custody, and loading history"]
        A["Airport stock and demand dashboards<br>dispatch schedules, substitution constraints,<br>and continuity-threshold ledgers"]
        D["Safety, continuity, and delegation matrix<br>terminal authority limits, enterprise fuel-supply decision rights,<br>and executive escalation triggers"]
        R["Prior fuel-quality incidents<br>restricted annex tooling,<br>and audit logs"]
    end

    subgraph W["Workflow boundary: recommend authority only"]
        L["Critical operations workspace / shared critical-case ledger<br>declared contamination scope, current hold state,<br>and prior packet revisions"]
        O["Orchestrated multi-agent workflow<br>quality-evidence retrieval,<br>authority-matrix checking, option narrowing,<br>and packet assembly"]
        P["Authority recommendation packet<br>bounded options, blocked lower-authority paths,<br>evidence lineage, and annex references"]
    end

    subgraph H["Human review and acceptance boundary"]
        U["Named human authority review<br>terminal incident authority, enterprise fuel-supply command,<br>or executive safety and continuity authority"]
    end

    X["Blocked in this workflow<br>no fuel release, no dispatch reroute,<br>and no airport conservation posture direction"]

    Q --> O
    A --> O
    D --> O
    R --> O
    L <--> O
    O --> P
    P --> U
    P -.-> X
```

- An orchestrated multi-agent workflow can separate quality-evidence retrieval, authority-matrix checking, option narrowing, and packet assembly while preserving one shared critical-case ledger.
- Human-in-the-loop review is mandatory because the workflow should recommend the correct decision owner and bounded option set, not release fuel, suspend dispatches, or set airport conservation posture.
- Human-directed autonomy fits because terminal, enterprise fuel-supply, and executive continuity leaders must explicitly accept the authority lane before any irreversible supply decision is considered.

## Governance notes

- The output should distinguish options that remain inside terminal isolation authority from options that require enterprise fuel-supply or executive safety and continuity ownership because of multi-airport impact, service commitments, or protected continuity thresholds.
- Any narrowed option set should preserve reversibility boundaries around tank quarantine duration, terminal dispatch suspension scope, and network conservation posture rather than flattening them into one operationally convenient path.
- Sensitive sample results, airport stock vulnerabilities, and service-commitment detail should remain limited to authorized operations, safety, continuity, and executive reviewers, with broader packets using the minimum needed for authority selection.
- Recommendation packets should preserve evidence lineage, delegation state, blocked lower-authority routes, and human redirects so later review can reconstruct why one authority lane was chosen during the critical window.

## Evaluation considerations

- Time from declared critical fuel-quality threat to a reviewed packet naming the correct human authority and bounded decision options
- Reviewer agreement that blocked lower-authority paths and continuity-threshold triggers were surfaced before any fuel release, dispatch, or conservation decision was considered
- Quality of evidence linking contamination scope, airport stock posture, delegation rules, and reversibility limits to the authority recommendation
- Stability of the recommended authority lane when sample confirmation, loading-history reconstruction, or airport demand assumptions change during the critical window
