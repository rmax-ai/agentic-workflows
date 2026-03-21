# Deprecated message broker client migration exception copilot loop

## Linked pattern(s)

- `analyst-copilot-loop`

## Domain

Engineering.

## Scenario summary

A principal engineer is preparing a time-bounded exception packet for an architecture review board because a high-throughput order-routing service cannot yet migrate off a deprecated message-broker client before the platform team's retirement deadline. The engineer uses a copilot inside a shared engineering workspace to iteratively pull compatibility-test evidence, compare dependency constraints across services, rewrite the exception memo for reliability and security reviewers, and maintain an open-questions and owners list as reviewers tighten the ask. The human engineer remains responsible for deciding whether the incompatibilities actually justify the exception, choosing which mitigation and rollback commitments are credible, and approving the final packet before anything is submitted to the review board or recorded in the engineering system of record.

## Target systems / source systems

- Shared engineering workbench with the draft exception memo, reviewer comments, and explicit section ownership
- Service catalog and dependency graph showing affected services, upstream libraries, and planned migration waves
- CI and compatibility-test records covering client-library upgrade failures, benchmark regressions, and reproducibility notes
- Incident archive, SLO dashboards, and postmortem records for recent reliability issues involving the current broker integration
- Platform standards repository with deprecation notices, approved migration guidance, and required exception-review criteria
- Architecture review backlog or change-governance queue where the final human-approved packet, expiration date, and follow-up owners are tracked

## Why this instance matters

This grounds the collaboration pattern in engineering governance work where the shared artifact is a living exception packet rather than a one-shot summary or an autonomous approval flow. The hard part is sustaining disciplined mixed-initiative editing while the engineer and copilot move between test evidence, operational history, reviewer questions, and narrowed mitigation language. A polished but weakly governed draft could make unsupported technical claims, hide unresolved migration blockers, or imply remediation commitments the service team never approved, so the collaboration loop has to keep provenance, ownership, and handoff state visible throughout the work.

## Likely architecture choices

- Human-in-the-loop collaboration should remain primary because exception scope, risk acceptance, and deadline commitments require accountable engineering judgment.
- A tool-using single agent can retrieve dependency evidence, refresh the memo's facts and citations, propose reviewer-specific rewrites, and track unresolved questions inside one shared workspace.
- The copilot may update the draft packet and evidence matrix, but submitting the exception, changing the proposed expiration date, or recording platform-standard waivers should remain explicitly human-approved.

## Governance notes

- The shared artifact should clearly distinguish observed test results, quoted platform standards, agent-drafted paraphrases, and human-approved commitments so reviewers can see where interpretation entered the packet.
- Every material claim should link to inspectable evidence such as CI run ids, benchmark results, incident references, dependency snapshots, or platform-policy sections; unsupported narrative should not survive into the final memo.
- The human owner must approve exception duration, rollback language, mitigation milestones, and any statement about customer-impact risk because those claims can create downstream operational commitments.
- Service names, incident excerpts, and dependency data should be limited to what reviewers need, and copied evidence should avoid unnecessary customer identifiers or sensitive payload details.
- If the evidence suggests the deprecated client is causing an active production safety issue, the workflow should branch into formal incident or change-control handling instead of letting the copilot finalize a routine exception packet.

## Evaluation considerations

- Time to produce an internal-review-ready exception packet that preserves claim-to-evidence traceability after multiple rewrite and reviewer-feedback turns
- Reviewer correction rate for memo sections where the copilot misstated deprecation deadlines, exaggerated incompatibility scope, or implied unapproved mitigation promises
- Completeness of the open-questions and handoff state, including whether ownership of follow-up tests, migration milestones, and approval checkpoints is explicit
- Reliability of governance checkpoints that prevent agent-authored drafts from being submitted to the architecture review board without human approval and visible audit history
