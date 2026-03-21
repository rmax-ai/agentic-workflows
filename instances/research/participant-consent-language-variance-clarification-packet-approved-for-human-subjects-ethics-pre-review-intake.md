# Participant consent-language variance clarification packet approved for human-subjects ethics pre-review intake

## Linked pattern(s)

- `approval-gated-collaborative-artifact-release`

## Domain

Research.

## Scenario summary

A principal investigator, a clinical research operations lead, and human-subjects governance partners are co-producing one governed consent-language variance clarification packet because translated participant-facing materials for one multisite study now diverge from the approved master consent in ways that may affect risk wording, withdrawal instructions, and compensation language. Agents help reconcile source consent versions, translator notes, site objections, and approved clarification wording into the shared packet while preserving which concerns remain contested and which edits the human artifact owner accepted. The workflow ends only when the named research release owner approves that exact packet revision for one bounded human-subjects ethics pre-review intake lane, where downstream reviewers may decide whether the variance is acceptable, needs an amendment, or requires narrower participant language. It does not decide ethics disposition, contact participants, or submit an amendment package.

## Target systems / source systems

- Governed research collaboration workspace holding the consent-variance clarification packet, revision history, objection ledger, and release-manifest state
- Protocol repository, master consent library, translated consent files, and site implementation trackers providing authoritative wording sources and current divergence evidence
- Translation vendor notes, participant-support issue logs, and study operations comments supplying disputed phrasing, locale-specific constraints, and unresolved site concerns
- Human-subjects governance policy, pre-review intake rules, and privacy controls defining required signers, allowed packet audience, and the bounded ethics intake lane
- Approval-routing, audit, and retention systems preserving superseded packet versions, held-release reasons, accepted residual disagreement, and downstream handoff traceability

## Why this instance matters

This grounds the pattern in research governance work outside benchmark-publication review. The reusable challenge is collaborative ownership of one sensitive clarification artifact whose exact revision must be approved before it can cross into a bounded ethics pre-review lane. The example stays inside the pattern boundary because the downstream ethics determination, participant communications, and protocol-amendment execution remain separate workflows.

## Likely architecture choices

- Approval-gated execution fits because the clarification packet can be collaboration-ready while still blocked from ethics intake until the human release owner approves the exact revision.
- Human-in-the-loop control is required because only accountable research leaders may accept residual disagreement, confirm participant-safety wording scope, and authorize the packet's release boundary.
- Agents may compare consent variants, refresh evidence links, and maintain the release trace, but they must not decide ethics acceptability, notify sites, or file the amendment.

## Governance notes

- The release manifest should bind one exact packet revision, the named human-subjects ethics pre-review lane, signer identities, and any residual objections the human release owner accepted explicitly.
- Master consent text, translated-language differences, participant-support caveats, and site implementation concerns should remain visible in the packet or boundary ledger rather than being normalized away before release.
- Audience scope should stay limited to the approved ethics pre-review lane; reuse of the packet for site instructions, participant outreach, or amendment submission should require separate downstream approval.
- If the master consent, locale-specific legal wording, or approved reviewer set changes materially during approval review, the workflow should hold release and supersede the prior packet revision rather than letting stale approval carry forward.

## Evaluation considerations

- Rate at which ethics pre-review intake accepts the released packet without discovering hidden wording drift, stale consent evidence, or audience-boundary mistakes
- Time required to keep one collaborative clarification packet synchronized as translation notes, site objections, and signer state evolve
- Reliability of binding between the released artifact revision, accepted residual disagreement, and the bounded ethics pre-review lane
- Frequency with which humans reject agent-assisted edits because they drifted into ethics adjudication, participant communication, or amendment-submission execution
