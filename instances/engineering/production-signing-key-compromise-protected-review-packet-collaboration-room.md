# Production signing-key compromise protected review packet collaboration room

## Linked pattern(s)

- `critical-protected-artifact-collaboration`

## Domain

Engineering.

## Scenario summary

After a severe signing-key compromise is declared, platform security opens a protected collaboration room for one shared review packet that will later feed executive, legal, and release-governance handling. A staff security engineer owns the packet while agents help reconcile forensic updates, SRE objections, customer-impact wording disputes, and executive-only annex material about key-custody gaps and revocation blast radius. The room stays focused on keeping one protected artifact current: accepted text, contested sections, restricted annexes, and explicit release conditions all remain visible as reviewers challenge whether the packet is complete enough for the next human handoff. The human artifact owner remains responsible for deciding whether disagreement is tolerable, whether the packet is ready to leave the room, and whether downstream authority selection, command planning, or revocation action should begin elsewhere.

## Target systems / source systems

- Restricted severe-case collaboration workspace with the main review packet, disagreement ledger, annex map, and release-state controls
- Incident and forensic systems containing signing-key lineage, artifact inventory, package-signing logs, and current containment status
- Secure annex repository with executive-only custody details, root-store dependencies, and customer-impact sensitivity notes
- Release-governance and platform-policy repositories with revocation rules, protected communication boundaries, and handoff criteria
- Audit and access-log systems tracking section edits, annex access changes, and human release approvals

## Why this instance matters

This grounds the pattern in an engineering case where the hard problem is maintaining one severe shared artifact under protected access and visible disagreement, not deciding who should authorize the response or resequencing the response timeline. The packet is more than a crisis brief because humans and agents repeatedly negotiate wording, objection handling, annex scope, and release readiness inside the room. It shows why critical collaboration needs explicit human ownership and restricted annex discipline so a polished packet does not imply consensus or safe release before that is actually true.

## Likely architecture choices

- Human-in-the-loop collaboration should remain primary because only named security and legal owners can accept contested framing, narrow annex exposure, and release the packet into the next critical workflow.
- An orchestrated multi-agent setup fits when separate agent roles refresh forensic evidence, normalize reviewer objections, track annex boundaries, and update the protected trace without flattening disagreement.
- Agents may rewrite sections, refresh evidence links, and maintain the disagreement ledger, but choosing the deciding authority, launching revocation sequencing, or executing customer communication should remain outside the room and explicitly human-controlled.

## Governance notes

- The packet should distinguish accepted human language, agent-drafted revisions, contested sections, and executive-only annex references so downstream consumers can see where disagreement still exists.
- Every material statement about blast radius, artifact integrity, rollback feasibility, or customer impact should link to inspectable evidence or an explicitly labeled unresolved objection; unsupported certainty should block release readiness.
- Restricted custody details, secret-rotation evidence, and sensitive dependency mappings should stay in annexes with access logging rather than being copied broadly into the main packet.
- The release-state record should name the current human artifact owner, unresolved blockers, accepted residual disagreement, and the exact condition for handing the packet into authority recommendation or response planning.
- If the room cannot maintain one coherent packet because evidence is changing too quickly or access rules are unclear, the workflow should hold the handoff and escalate for direct human control rather than smoothing over the conflict.

## Evaluation considerations

- Time to produce a human-reviewable protected packet that keeps disagreement, annex scope, and release ownership synchronized
- Rate at which downstream executive or legal reviewers find hidden objections, stale evidence, or improper annex exposure after the room marked the packet handoff-ready
- Reliability of the disagreement ledger and annex map as the incident evolves and new forensic facts arrive
- Frequency with which humans override agent-proposed revisions because they drifted toward authority recommendation, command sequencing, or implied execution
