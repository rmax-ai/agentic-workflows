# Quarter-close control-bundle revision approved for live use

## Linked pattern(s)

- `approval-gated-optimization-state-release`

## Domain

Finance.

## Scenario summary

A controllership optimization steward has prepared one exact quarter-close control-bundle revision covering exception-materiality weighting, entity-aging buffers, and reviewer-balance parameters used across the close-review surfaces. Simulation against the prior two closes suggests the revision reduces controller overrides and protects covenant-sensitive entities more consistently, but the bundle should not become live until a controller approves the exact revision id, bounded cycle scope, expiry at close completion, and rollback packet. The workflow therefore centers on governed release of one exact optimization-state revision into live close use, without deciding accounting treatment, rescheduling the close calendar, or executing journal postings.

```mermaid
flowchart TD
    A["Candidate quarter-close control-bundle revision<br>is prepared for the current cycle"] --> B["Verify exact revision id,<br>simulation evidence, bounded scope,<br>expiry, and rollback packet"]
    B --> C{"Verification and policy<br>checks pass?"}
    C -- "No" --> H["Hold revision attempt<br>until evidence, scope, or rollback readiness is corrected"]
    C -- "Yes" --> D["Controller reviews the release manifest<br>for the exact revision and close cycle"]
    D --> E{"Controller approves the exact revision<br>for bounded live use?"}
    E -- "No" --> H
    E -- "Yes" --> F["Activate the approved bundle revision<br>in live close-review surfaces"]
    F --> G{"Do override, protected-entity aging,<br>and fairness guardrails remain acceptable?"}
    G -- "No" --> I["Rollback to the prior trusted bundle<br>and record the rollback action"]
    G -- "Yes" --> J["Expire the revision at close completion<br>and restore the prior trusted bundle"]
```

## Target systems / source systems

- Shared close-control parameter registry with active and candidate bundle versions plus supersession lineage
- Close replay workspace with controller overrides, late-close incidents, reopened packages, and fairness checks for slower-documenting entities
- Controller approval and manifest tooling used to authorize one bundle revision for the current close cycle
- Audit and rollback services that can restore the last trusted bundle if override frequency or protected-entity aging worsens
- Close-review queues, disclosure-support surfaces, and evidence-sufficiency screens that consume the active bundle

## Why this instance matters

This instance shows a finance case where the approval-gated step is not a recommendation to adopt a better bundle and not an operational execution workflow. The central reusable artifact is one exact optimization bundle revision entering live use under controller approval, with explicit validity and restore controls. That cleanly captures the optimize/adapt slice where live governance attaches to a versioned tuning artifact rather than to an accounting decision or execution step.

## Likely architecture choices

```mermaid
flowchart LR
    Steward["Controllership optimization steward"]
    Controller["Controller"]
    Replay["Close replay workspace<br>with controller overrides,<br>late-close incidents, and fairness checks"]
    Approval["Controller approval and<br>manifest tooling"]
    Audit["Audit and rollback services"]
    subgraph LiveScope["Bounded live current close cycle"]
        Registry["Shared close-control<br>parameter registry"]
        Surfaces["Close-review queues,<br>disclosure-support surfaces,<br>and evidence-sufficiency screens"]
    end

    Steward -->|"Submits exact bundle revision<br>for the current cycle"| Approval
    Replay -->|"Provides simulation evidence<br>and guardrail checks"| Approval
    Controller -->|"Approves exact revision<br>for bounded live use"| Approval
    Approval -->|"Activates approved bundle revision"| Registry
    Registry -->|"Publishes active bundle"| Surfaces
    Approval -->|"Records manifest, expiry,<br>and rollback packet"| Audit
    Replay -->|"Tracks override, aging,<br>and fairness signals"| Audit
    Audit -->|"Restores prior trusted bundle<br>on rollback or expiry"| Registry
```

- Approval-gated execution fits because the bundle revision can be activated through the shared registry only after the controller signs the release manifest for that exact cycle-bound version.
- Human-in-the-loop review is necessary because the controller must explicitly accept the trade-offs among throughput, protected-entity handling, and fairness posture before the revision becomes live.
- A governed release agent can verify the revision id, compare it with simulation evidence, record the prior trusted bundle, and arm expiry and rollback controls, but it should not reinterpret accounting policy or broaden the live scope to other close cycles.

## Governance notes

- Approval should be tied to one exact bundle revision, one current close cycle, and one controller signer so a later parameter tweak or a future quarter cannot inherit authority implicitly.
- Expiry discipline matters because close-specific tuning should restore the prior trusted bundle automatically when the cycle ends unless controller leadership explicitly extends it.
- Rollback criteria should include controller-override spikes, worsening aging on covenant-sensitive entities, and hidden fairness regression across smaller subsidiaries.
- Audit lineage should preserve the prior and released bundle ids, simulation windows, blocked revision attempts, approval timing, expiry behavior, and any manual extension or rollback action.
- The workflow must not decide accounting treatment, route exceptions to a committee, or post journals; it only governs live release of the shared close optimization-state revision.

## Evaluation considerations

- Reduction in controller overrides, late close-critical aging, and hidden fairness regressions after the approved bundle revision becomes live
- Percentage of live bundle releases whose manifest, cycle scope, and expiry metadata match the exact approved revision without later correction
- Speed and clarity of rollback when a live revision improves throughput but harms protected entity handling or controller trust
- Frequency of automatic expiry and safe restoration to the prior trusted bundle at cycle end
