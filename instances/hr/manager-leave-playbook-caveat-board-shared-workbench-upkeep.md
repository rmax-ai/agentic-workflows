# Manager leave playbook caveat board shared workbench upkeep

## Linked pattern(s)

- `shared-workbench-orchestration`

## Domain

HR.

## Scenario summary

A people policy enablement team maintains an internal manager leave playbook caveat board while leave program owners, regional HR partners, absence administrators, and manager-training reviewers continuously refine internal manager-guidance coverage for recurring leave scenarios. Small updates arrive throughout the cycle: one leave specialist links a revised intermittent-leave intake note, a regional partner flags a stale jurisdiction-specific return-to-work example, a training reviewer marks one decision-tree screenshot as outdated, and a policy owner reassigns ownership of an unresolved leave-vendor handoff note. The agent keeps that internal workbench usable by refreshing linked source references, normalizing duplicate caveat notes, updating section ownership and hold markers, and carrying unresolved policy-boundary questions forward in a visible register. Humans remain responsible for deciding what leave policy actually requires, which manager instructions are legally or policy-safe, whether any exception handling is approved, and when any material should move into separate manager communication, approval, case administration, or operational execution workflows.

## Target systems / source systems

- Shared manager leave playbook caveat board with topic sections, owner fields, blocker tags, and revision history
- Internal leave policy repository containing approved leave guidance, jurisdiction notes, and manager playbook source references
- Leave administration knowledge workspace with vendor handoff notes, effective dates, and approved process clarifications
- Screenshot and artifact store referenced by topic-level caveats, decision trees, and reviewer comments
- HR annotation or review surface where leave program owners, regional partners, and training reviewers add small edits, caveats, and hold notes

## Why this instance matters

This grounds the pattern in a low-risk HR collaboration loop where the maintained artifact is an internal manager leave playbook workbench used to keep caveats organized before any manager-facing guidance or leave-case action is updated. The useful work is not interpreting leave law, directing managers, or changing case handling. It is keeping one bounded board current, inspectable, and resumable as many small edits and linked-source changes arrive from different human collaborators.

## Likely architecture choices

- Event-driven monitoring fits because upkeep should react when leave-policy notes, jurisdiction references, screenshots, or board fields change.
- A tool-using single agent can refresh source links, normalize duplicated caveat text, and keep ownership plus hold markers synchronized inside one bounded board.
- Human-in-the-loop review remains necessary when a note changes leave-policy interpretation, sounds ready for manager-facing release, or could remove a caveat that a human owner still considers unresolved.
- Bounded delegation works because the team can predefine allowable field updates, source boundaries, and hold conditions without delegating approval of final manager guidance or downstream leave operations.

## Governance notes

- The board should clearly distinguish approved source excerpts, reviewer proposals, unresolved jurisdiction questions, and manager-facing wording candidates so internal upkeep does not imply final policy guidance.
- Leave-policy citations, jurisdiction tags, screenshot links, and owner assignments should be revalidated before a section is marked current or a blocker is cleared.
- The agent may normalize structure and merge duplicate comments, but it should not decide what leave guidance means, approve a jurisdiction-specific exception, or remove a caveat that a human owner accepted.
- If a requested update would release manager guidance, commit to leave-case handling, trigger leave administration changes, or approve a policy interpretation, the workflow should stop and hand off to the appropriate communication, approval, or execution pattern.

## Evaluation considerations

- Percentage of board refreshes that preserve correct policy links, screenshot references, ownership fields, and unresolved-question state across repeated update cycles
- Reviewer correction rate for merged caveat notes, refreshed source references, or automatically updated blocker markers
- Rate at which manager-facing or interpretation-heavy edits are held for human review instead of being silently folded into the internal board
- Usefulness of the maintained workbench for helping leave program and training reviewers resume internal manager-playbook upkeep without reconstructing stale context by hand
