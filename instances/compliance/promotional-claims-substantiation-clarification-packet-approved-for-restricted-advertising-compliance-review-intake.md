# Promotional claims substantiation clarification packet approved for restricted advertising-compliance review intake

## Linked pattern(s)

- `approval-gated-collaborative-artifact-release`

## Domain

Compliance.

## Scenario summary

A promotional compliance lead, a medical affairs reviewer, and a brand-governance partner are co-producing one governed claims substantiation clarification packet because a disease-awareness campaign draft now depends on comparative outcome language, citation excerpts, and audience-limitation notes that remain partially contested across internal reviewers. Agents help reconcile approved label references, evidence-table excerpts, fair-balance caveats, market-specific restrictions, and unresolved reviewer objections into the shared packet while preserving which concerns remain open and which residual caveats the human artifact owner accepted explicitly. The workflow ends only when the named compliance release owner approves that exact packet revision for one bounded advertising-compliance review intake lane, where downstream reviewers may decide whether the packet is sufficient for formal promotional review or needs narrower wording and fresher support. It does not approve campaign launch, choose a regulatory posture, contact authorities, or publish or remediate the customer-facing materials.

## Target systems / source systems

- Governed promotional-compliance collaboration workspace holding the claims substantiation clarification packet, revision history, objection ledger, and release-manifest state
- Labeling, medical-legal-reference, and claims-library systems providing approved indication language, evidence citations, usage constraints, and prior claim-treatment history
- Campaign asset inventory, market-routing notes, reviewer comment threads, and fair-balance checklists supplying contested wording, audience-scope caveats, and unresolved restriction gaps
- Advertising-compliance policy, restricted review-intake controls, and approval-routing tools defining required signers, approved packet audience, and the single downstream intake lane
- Audit, retention, and access-governance systems preserving superseded packet revisions, accepted residual disagreement, blocked-release causes, and downstream handoff traceability

## Why this instance matters

This grounds the pattern in compliance work focused on collaborative stewardship of one governed claims substantiation artifact rather than recommendation drafting, content publication, or exception adjudication. The reusable challenge is keeping one clarification packet current while comparative-claim wording, evidence freshness, and market-bound restrictions remain visibly disputed, then approving release of that exact revision into one restricted advertising-compliance intake lane only. The example stays inside the pattern boundary because promotional adjudication, regulator engagement, asset revision, and launch execution remain separate downstream workflows.

## Likely architecture choices

- Approval-gated execution fits because the clarification packet can be collaboration-ready while still blocked from advertising-compliance intake until the human release owner approves the exact revision.
- Human-in-the-loop control is required because only accountable compliance leaders may accept residual wording disagreement, confirm audience scope, and authorize the packet's release boundary.
- Agents may crosswalk citations, refresh evidence references, normalize objection wording, and maintain the release trace, but they must not decide claim acceptability, approve campaign use, or trigger external dissemination.

## Governance notes

- The release manifest should bind one exact packet revision, the named advertising-compliance review-intake lane, signer identities, the covered campaign-asset scope, and any residual objections the human release owner accepted explicitly.
- Comparative-claim disputes, outdated study excerpts, fair-balance caveats, and market-specific indication restrictions should remain visible in the packet or boundary ledger rather than being normalized away before release.
- Audience scope should stay limited to the approved advertising-compliance intake lane; reuse of the packet for regulator submission, agency outreach, brand launch approval, or field-distribution instructions should require separate downstream approval.
- If new study results, label changes, or reviewer-scope changes alter the substantiation picture materially during approval review, the workflow should hold release and supersede the prior packet revision rather than letting stale approval carry forward.

## Evaluation considerations

- Rate at which advertising-compliance intake accepts the released packet without discovering hidden claim-scope drift, stale substantiation evidence, or audience-boundary mistakes
- Time required to keep one collaborative clarification packet synchronized as citations, reviewer objections, and signer state evolve
- Reliability of binding between the released artifact revision, accepted residual disagreement, campaign-asset scope, and the bounded advertising-compliance review-intake lane
- Frequency with which humans reject agent-assisted edits because they drifted into claim adjudication, regulator communication, asset publication, or downstream remediation execution
