# Approved production signing certificate issuance portal submission

## Linked pattern(s)

- `browser-based-form-completion-with-approval-gates`

## Domain

Engineering.

## Scenario summary

A certificate operations engineer needs to submit an already approved production signing certificate issuance request for the package-signing service used by customer-delivered release artifacts after the replacement certificate package has been prepared, the CSR fingerprint has been locked, and the issuance window has been reserved ahead of an expiring intermediate-trust deadline. The target enterprise PKI portal is browser-only, spreads the action across subscriber identity, certificate profile, SAN set, HSM custody attestations, issuance justification, and approver-attestation tabs, and final submission may proceed only after the release integrity owner, cryptography engineering manager, and security certificate authority delegate have all signed off in the governed issuance record. Because the portal action can place a new production signing credential into the issuance queue and bind sensitive trust-chain metadata that later release processes may depend on, the workflow must recheck approvals, confirm the approved CSR, profile, and subject scope still match the authoritative issuance packet, and halt safely if the live portal, prerequisite state, or confirmation path becomes ambiguous. Named owner accountability remains with Certificate Operations Owner Elena Park, who is responsible for the approved submission packet, takeover decisions, and evidence completeness, but not for downstream certificate issuance, key activation, deployment, or release execution.

```mermaid
flowchart TD
    A["Approved issuance packet, locked CSR fingerprint,<br>and reserved issuance window ready for submission"] --> B{"Release integrity owner, cryptography manager,<br>and CA delegate approvals still current<br>in the issuance record?"}
    B -->|"No"| H["Stop before submission, preserve draft state,<br>and return to Elena Park for approval refresh"]
    B -->|"Yes"| C{"CSR fingerprint, subscriber identity, certificate profile,<br>SAN scope, and HSM custody attestations still match<br>the approved prerequisite state?"}
    C -->|"No"| I["Hold request and expose blocker set<br>for controlled human takeover"]
    C -->|"Yes"| D["Enter subscriber, profile, SAN, custody,<br>justification, and approval references<br>in the browser-only PKI portal"]
    D --> E{"Portal warnings, issuance queue state, and final gate<br>remain inside approved scope and policy?"}
    E -->|"No"| J["Save draft or abandon session;<br>capture masked evidence and blocker details"]
    E -->|"Yes"| F{"Positive submission confirmation and request id<br>received without ambiguity?"}
    F -->|"No"| K["Bounded reconciliation hold;<br>human verifies status before any retry"]
    F -->|"Yes"| G["Record confirmation, approval trace,<br>and masked portal artifacts;<br>submission complete"]
```

## Target systems / source systems

- Engineering certificate-governance or issuance-record system holding the approved request, named owner, approval chain, segregation-of-duties evidence, and prerequisite checklist
- Browser-only enterprise PKI or certificate authority portal used to request production signing certificate issuance under controlled certificate profiles
- Approved CSR packet, subscriber-service identity record, SAN inventory, HSM custody attestation, and issuance-window reservation tied to the production signing service
- Cryptographic policy, certificate profile catalog, trust-chain inventory, expiration calendar, and environment registration records governing which production signing certificates may be requested
- Evidence store for masked screenshots, approval references, portal request identifiers, visible blocker notes, and safe-halt or takeover records

## Why this instance matters

This grounds the execution pattern in an engineering workflow where the browser submission can place a highly sensitive production credential request into an authoritative issuance lane without yet issuing or activating that certificate. The value is not certificate lifecycle automation in general. It is governed portal execution that proves the exact issuance request was already approved, the prerequisite cryptographic state remained valid at submit time, and the workflow stopped rather than guessing when approval integrity, subscriber scope, or portal confirmation no longer looked trustworthy.

## Likely architecture choices

```mermaid
flowchart LR
    OWNER["Elena Park<br>Accountable owner"]
    GOV["Certificate-governance / issuance-record system<br>Approved request, approval chain, and prerequisite checklist"]
    PACKET["Approved CSR packet / subscriber identity / SAN inventory /<br>HSM custody attestation / issuance-window reservation"]
    POLICY["Cryptographic policy / profile catalog / trust-chain inventory /<br>expiration calendar / environment registration records"]
    REVIEWER["CA reviewer<br>Controlled takeover path"]

    subgraph BOUNDARY["Approval-gated submission boundary"]
        EXEC["Tool-using portal submission agent"]
        PORTAL["Browser-only enterprise PKI portal"]
        EVID["Evidence store<br>Masked screenshots, approval references,<br>request identifiers, and blocker notes"]
    end

    OWNER -->|"owns packet integrity,<br>approval freshness, and takeover routing"| GOV
    GOV -->|"authorizes approved request<br>and named-owner context"| EXEC
    PACKET -->|"supplies exact CSR, subscriber,<br>SAN, custody, and timing inputs"| EXEC
    POLICY -->|"constrains profile, trust chain,<br>expiration timing, and environment scope"| EXEC
    EXEC -->|"submits approved fields only<br>after approval recheck"| PORTAL
    PORTAL -->|"returns warnings,<br>queue state, and request confirmation"| EXEC
    EXEC -->|"records masked evidence,<br>approval trace, and blockers"| EVID
    EXEC -->|"halts and hands off on ambiguity,<br>scope drift, or policy mismatch"| REVIEWER
    REVIEWER -->|"resumes controlled review<br>or portal takeover"| EXEC
```

- Approval-gated execution should assemble the issuance packet, verify that release-integrity, cryptography-management, and certificate-authority approvals remain current, and block final commit until those approvals are rechecked immediately before submit.
- A tool-using single agent can navigate the PKI portal, populate subscriber, profile, SAN, and custody fields, attach or reference the approved issuance artifacts, and capture masked evidence at each gated checkpoint.
- Human-in-the-loop control should remain standard for CSR or SAN drift, unexpected certificate-profile changes, trust-chain warnings, portal layout changes, duplicate pending requests, or any prompt that suggests the submission would create a broader certificate request than the approved packet allows.

## Governance notes

- The workflow should confirm prerequisite state before any browser entry begins: the CSR fingerprint is the approved one, subscriber identity and environment registration are current, HSM-backed key custody attestations are still valid, the requested certificate profile is authorized for production signing use, and the reserved issuance window has not expired or been superseded.
- Screenshots and logs should preserve which authoritative approvals unlocked the submission, which exact CSR and profile references were used, which visible blockers were checked, and which portal confirmation was returned, while minimizing exposure of private key material, token identifiers, full certificate metadata, internal trust-anchor details, or sensitive service topology.
- If the portal shows a different certificate profile, an expanded SAN set, a conflicting subscriber record, a pending compromise or revocation investigation, a duplicate open issuance request, or a missing approval gate, the workflow should stop at a saved draft or abandon the session rather than guess and submit a request that exceeds the approved boundary.
- Safe-halt behavior should preserve current page state, entered-but-unsubmitted values, uploaded attachments or references, approval identifiers, blocker visibility, and the exact reason for the halt so Elena Park or the designated certificate authority reviewer can resume safely without duplicating the request or widening certificate scope.
- Accountability should remain explicit: Elena Park owns packet integrity, approval freshness, and takeover routing for this submission, while downstream issuance ceremony steps, certificate activation, release-system enrollment, and production signing usage remain outside this workflow boundary and require separate governed processes.

## Evaluation considerations

- Percentage of approved production signing certificate issuance submissions completed without duplicate requests, profile-scope errors, or post-submission correction to subscriber or SAN data
- Rate of stale approvals, prerequisite-state mismatches, duplicate pending requests, or PKI-portal anomalies caught before final submission
- Completeness of evidence bundles linking the submitted request to the approved issuance packet, named accountable owner, prerequisite attestations, and human approval chain
- Reliability of safe halt and human takeover when the PKI portal changes, times out, or returns unclear confirmation during a high-governance production certificate request
