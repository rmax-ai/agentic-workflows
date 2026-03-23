# Hiring panel interview-guide caveat board shared workbench upkeep

## Linked pattern(s)

- `shared-workbench-orchestration`

## Domain

HR.

## Scenario summary

A talent acquisition enablement team maintains an internal interview-guide caveat board while recruiting operations leads, regional HR partners, interviewer-training reviewers, and hiring-program owners continuously refine interviewer-instruction coverage for a recurring hiring loop. Small updates arrive throughout the cycle: one reviewer links a revised scorecard note, a regional partner flags a stale locale-specific prohibited-question example, a training reviewer marks one screenshot as outdated, and a program owner reassigns section ownership after recruiter rotation. The agent keeps that internal workbench usable by refreshing linked source references, normalizing duplicate caveat notes, updating section ownership and hold markers, and carrying unresolved local-guidance questions forward in a visible register. Humans remain responsible for deciding what interviewing guidance is actually approved, which wording is legally or policy-safe, whether any note changes evaluation criteria, and when any material should move into separate training release, policy review, candidate communication, or hiring execution workflows.

```mermaid
flowchart TD
    A["Recruiting operations leads,<br>regional HR partners, training reviewers,<br>and program owners add small updates"] -->|"triggers upkeep cycle"| B["Agent checks the caveat board,<br>linked sources, and prior hold state"]
    B -->|"tests boundary and source fit"| C{"Update stays inside internal<br>workbench upkeep?"}
    C -->|"yes"| D["Agent refreshes source links,<br>deduplicates caveat notes,<br>and updates owners or hold markers"]
    D -->|"writes bounded board changes"| E["Shared interview-guide caveat board<br>remains current and inspectable"]
    D -->|"carries forward unresolved items"| F["Open local-guidance questions<br>and blockers stay visible"]
    C -->|"no"| G["Hold for named human owner<br>because interpretation, approval,<br>or release work is out of scope"]
    G -->|"stops at internal handoff"| H["Stop before training release,<br>policy review, candidate communication,<br>or hiring execution"]
```

## Target systems / source systems

- Shared interview-guide caveat board with topic sections, owner fields, blocker tags, and revision history
- Internal interviewing standards repository containing approved scorecard guidance, interviewer instructions, and structured interview template notes
- Regional recruiting policy workspace with locale-specific caveats, effective dates, and linked source references
- Screenshot and artifact store referenced by topic-level caveats and reviewer comments
- HR or recruiting annotation surface where enablement owners, regional partners, and training reviewers add small edits, caveats, and hold notes

## Why this instance matters

This grounds the pattern in a low-risk HR collaboration loop where the maintained artifact is an internal interviewer-guidance workbench used to keep caveats organized before any training material or active hiring workflow is updated. The useful work is not approving interview policy, changing evaluation criteria, or messaging candidates. It is keeping one bounded board current, inspectable, and resumable as many small edits and linked-source changes arrive from different human collaborators.

## Likely architecture choices

```mermaid
flowchart LR
    subgraph up["Internal shared-workbench upkeep"]
        ann["HR or recruiting annotation surface<br>small edits, caveats, and hold notes"]
        agt["Bounded single agent<br>refreshes links, normalizes notes,<br>and updates owners plus hold markers"]
        brd["Shared interview-guide caveat board<br>topic sections, owner fields,<br>blocker tags, and revision history"]
        reg["Visible register of unresolved<br>local-guidance questions and hold markers"]
    end
    subgraph src["Linked source systems"]
        std["Internal interviewing standards repository<br>approved scorecard guidance,<br>interviewer instructions, and template notes"]
        pol["Regional recruiting policy workspace<br>locale-specific caveats,<br>effective dates, and source references"]
        art["Screenshot and artifact store<br>topic-level caveat references<br>and reviewer-comment artifacts"]
    end
    subgraph hum["Human review boundary"]
        rev["Recruiting operations leads,<br>regional HR partners,<br>training reviewers, and program owners"]
    end

    ann -->|"small edit events"| agt
    brd -->|"board field changes"| agt
    std -->|"linked source refresh"| agt
    pol -->|"regional caveat refresh"| agt
    art -->|"artifact refresh"| agt
    agt -->|"bounded board updates<br>links, dedupes, owners, and blocker tags"| brd
    agt -->|"carries forward unresolved items<br>and hold markers"| reg
    reg -->|"stays visible on the shared board"| brd
    brd -->|"routes interpretation, approval,<br>or release questions for review"| rev
    rev -->|"reviews held items and named ownership decisions"| brd
```

- Event-driven monitoring fits because upkeep should react when interviewing-standard notes, regional caveats, screenshots, or board fields change.
- A tool-using single agent can refresh source links, normalize duplicated caveat text, and keep ownership plus hold markers synchronized inside one bounded board.
- Human-in-the-loop review remains necessary when a note changes interview-policy interpretation, sounds ready for interviewer-facing release, or could remove a caveat that a human owner still considers unresolved.
- Bounded delegation works because the team can predefine allowable field updates, source boundaries, and hold conditions without delegating approval of final interviewer guidance or downstream hiring actions.

## Governance notes

- The board should clearly distinguish approved source excerpts, reviewer proposals, unresolved local-guidance questions, and interviewer-facing wording candidates so internal upkeep does not imply final policy guidance.
- Scorecard references, locale tags, screenshot links, and owner assignments should be revalidated before a section is marked current or a blocker is cleared.
- The agent may normalize structure and merge duplicate comments, but it should not decide what interviewing guidance means, approve a local exception, or remove a caveat that a human owner accepted.
- If a requested update would release interviewer training, change hiring criteria, send candidate or manager guidance, or trigger active recruiting execution, the workflow should stop and hand off to the appropriate communication, approval, or execution pattern.

## Evaluation considerations

- Percentage of board refreshes that preserve correct guidance links, screenshot references, ownership fields, and unresolved-question state across repeated update cycles
- Reviewer correction rate for merged caveat notes, refreshed source references, or automatically updated blocker markers
- Rate at which interviewer-facing or interpretation-heavy edits are held for human review instead of being silently folded into the internal board
- Usefulness of the maintained workbench for helping recruiting and training reviewers resume internal interview-guide upkeep without reconstructing stale context by hand
