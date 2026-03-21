# Service mesh migration readiness evidence synthesis for architecture review

## Linked pattern(s)

- `research-synthesis-with-citation-verification`

## Domain

Engineering.

## Scenario summary

A platform engineering architecture review board is preparing a gate review for migrating customer-facing microservices from legacy sidecar proxies to a managed service mesh control plane. Before anyone approves migration waves, updates production standards, or schedules cutovers, the workflow needs a cited readiness brief showing which reliability assumptions, dependency constraints, rollback prerequisites, security-control requirements, performance baselines, and unresolved adoption risks are actually supported by the current source set. The useful output is an evidence-backed synthesis that separates verified readiness facts from stale design assumptions, conflicting operational signals, and open questions that still require service-owner or security review.

## Target systems / source systems

- Architecture decision record archive, platform RFC repository, and mesh adoption design docs
- Service catalog with ownership metadata, dependency maps, and ingress or egress policy inventories
- SLO dashboards, latency and error-budget reports, and production capacity review artifacts for candidate services
- Load-test results, canary evaluation notes, rollback drill records, and release-readiness checklists
- Incident postmortems, exception register entries, and known-issue trackers related to proxying, certificate rotation, or traffic policy failures
- Security standards repository, approved control baselines, and policy-as-code results for mTLS, identity, and network segmentation

## Why this instance matters

This grounds the gather/synthesize pattern in an engineering workflow where the key need is a traceable readiness brief rather than a migration recommendation or an execution plan. Platform migrations often accumulate partial evidence across RFCs, benchmark notes, postmortems, and service-owner exceptions that do not carry equal authority or recency. The value comes from assembling a source-ranked synthesis that lets reviewers inspect what is verified, what is merely proposed, and which readiness claims are still unsupported before any production migration decision moves downstream.

## Likely architecture choices

- A tool-using single agent can retrieve approved architecture records, operational evidence, test artifacts, and policy results, then draft a structured synthesis with claim-to-source mappings.
- Human-in-the-loop review should remain mandatory for source-boundary decisions, interpretation of conflicting readiness signals, and any conclusion that could influence production migration approval.
- The workflow should preserve an evidence trace that distinguishes binding platform standards, observed production behavior, controlled test evidence, and lower-authority planning assumptions.
- Retrieval should stay within approved engineering, security, and reliability repositories; unsupported inference about migration safety, team capacity, or rollback sufficiency should be blocked.

## Governance notes

- Current platform standards, approved RFC decisions, and production telemetry should outrank slide decks, chat summaries, or stale planning notes when sources disagree.
- The brief should clearly separate verified prerequisites, observed service readiness evidence, temporary exceptions, and open questions instead of flattening them into one migration narrative.
- Source timestamps and environment scope should be explicit because superseded load tests or outdated dependency maps can make readiness look stronger than it is.
- Open questions should remain visible for items such as missing rollback drill evidence, incomplete certificate-rotation coverage, or unresolved east-west traffic-policy dependencies.
- Access to incident artifacts, topology data, and security findings should follow least-privilege rules, with copied excerpts minimized to what reviewers need to inspect each cited claim.

## Evaluation considerations

- Percentage of material readiness, rollback, security-control, and performance-baseline claims backed by inspectable citations to the current approved source set
- Reviewer correction rate for source precedence, recency handling, dependency scoping, or citation mismatch during architecture review
- Rate at which stale benchmarks, undocumented service exceptions, or conflicting operational evidence are surfaced explicitly before migration-wave approval
- Usefulness of the open-questions section for helping platform, service-owner, and security reviewers close readiness gaps without reconstructing the source corpus from scratch
