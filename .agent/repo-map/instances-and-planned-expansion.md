# Instances And Planned Expansion

## Grounded example layout

- `instances/engineering/` — software delivery, incident, release, security-exception, and execution-control examples.
- `instances/finance/` — treasury, close, control, payment, and covenant-governance examples.
- `instances/compliance/` — regulatory filing, sanctions, privacy, pharmacovigilance, and remediation-governance examples.
- `instances/operations/` — cold-chain, maintenance, dispatch, contamination, and rollout-governance examples.
- `instances/research/` — benchmark governance, publication readiness, dataset access, and continuing-review examples.
- `instances/support/` — escalation, outage, entitlement, knowledge-ops, and remediation-credit examples.
- `instances/hr/` — leave, payroll, hiring, accommodation, work-authorization, and workforce-governance examples.

## Representative anchors

- `instances/engineering/approved-payments-tokenization-cutover-staged-execution.md` — staged execution under rollback-aware holds.
- `instances/finance/quarter-close-control-review-scheduling.md` — bounded-delegation finance scheduling under close deadlines.
- `instances/compliance/beneficial-ownership-registry-update-submission.md` — approval-gated regulated submission.
- `instances/operations/suspected-contamination-lot-hold-state-truth-restoration.md` — critical authoritative-state restoration.
- `instances/research/benchmark-study-publication-readiness-review-scheduling.md` — publication-readiness coordination.
- `instances/support/severity-one-service-credit-and-recovery-package-recommendation.md` — governed recommendation support.
- `instances/hr/medical-leave-certification-packet-to-leave-case-record-handoff.md` — privacy-sensitive transform handoff.

## Planned but not yet present

- `docs/domains/`
- `docs/architectures/`

## Where to look for more detail

- Use `.agent/ontology-status.yaml` for current instance counts by domain.
- Use `.agent/coverage-matrix.yaml` for coverage state across families, domains, architectures, and risk levels.
- Open specific `instances/<domain>/` files only when the task needs grounded scenario detail.
