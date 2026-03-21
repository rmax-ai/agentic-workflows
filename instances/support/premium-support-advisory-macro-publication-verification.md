# Premium support advisory macro publication verification

## Linked pattern(s)

- `claimed-state-verification`

## Domain

Support.

## Scenario summary

Knowledge operations marks an internal premium-support advisory macro as published after the macro source repository, agent-assist macro library, and support-console suggestion service report a successful release for a recurring but low-risk product guidance scenario. Premium-support teams still need to know whether that claimed publication state is actually true across the approved internal support surfaces before they rely on the macro in routine case handling. The workflow verifies the claim against authoritative evidence and emits a bounded confirmed, disproved, or inconclusive verdict; it must not edit the macro, republish content, contact customers, escalate the case, or trigger downstream workflow changes.

## Target systems / source systems

- Macro source repository containing the approved advisory macro revision, publication metadata, and internal visibility settings
- Agent-assist macro library used to distribute approved internal premium-support response macros to support tooling
- Support-console suggestion service showing which macro revision is currently eligible for advisor prompts and case-side recommendations
- Knowledge-operations workflow tracker or event feed that records the original publication-complete claim and any replayed propagation events
- Verification audit log preserving evidence checks, observed revision identifiers, verdicts, lag handling, and bounded follow-up records

## Why this instance matters

This grounds the pattern in a support workflow where a published-state claim can look trustworthy even though one approved internal support surface still exposes an older macro revision or the support-console suggestion layer has not yet propagated the approved macro. The value is not rewriting the advisory macro and not deciding how agents should communicate with customers. It is bounded, evidence-backed confirmation of whether the already-approved internal guidance is actually available where premium-support teams expect to find it before they rely on the claimed publication state.

## Likely architecture choices

- Event-driven monitoring fits because the verification run should begin when the macro publication-complete claim is recorded rather than only after agents notice a stale suggestion.
- A tool-using single agent can compare macro ids, revision markers, visibility flags, and freshness timestamps across the approved internal support systems while applying allowed propagation tolerances.
- Bounded delegation is appropriate because support governance owners can predefine the authoritative macro surfaces, required corroborating fields, and acceptable lag windows while humans retain authority over any macro edits, republish actions, or customer communication.
- Durable verification state should preserve duplicate publication claims and prior inconclusive checks so repeated runs do not create contradictory verdicts for the same macro revision.

## Governance notes

- Only the approved macro repository, agent-assist library, support-console suggestion service, and workflow event records should count as authoritative evidence; screenshots, copied macro text, or chat confirmations should not confirm publication.
- Verification records should stay privacy-minimized by preserving macro identifiers, revision markers, timestamps, visibility state, and propagation status rather than customer case content or advisor notes.
- If one approved internal support surface remains stale within an allowed propagation window, the workflow should keep the result explicitly inconclusive instead of overstating either success or failure.
- Editing the macro, changing approval metadata, telling agents to use the content anyway, or opening escalation work remains outside this verification workflow and under human control.

## Evaluation considerations

- Percentage of premium-support advisory macro publication claims that receive a verdict with complete repository, macro-library, and suggestion-service traceability
- Rate at which stale or partially propagated macro revisions are detected before support teams rely on the claimed published state
- Reviewer agreement that the workflow applied the correct revision-match, visibility, and lag-tolerance rules
- Clarity of follow-up records when one approved internal support surface remains out of date beyond the allowed publication window
