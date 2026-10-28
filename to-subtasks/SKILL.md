---
name: to-subtasks
description: Converts the current conversation context into an implementation-ready subtask plan with atomic, dependency-ordered steps and optional test pairing. Use when a planning/discovery conversation (including grill-me sessions) is complete and the next step is to break decisions into actionable subtasks for sequential implementation.
---

# To Subtasks

## Quick start

When the user asks to move from discussion to execution planning:

1. Read the current conversation context.
2. Extract decisions, constraints, assumptions, and open questions.
3. Resolve implementation-relevant uncertainties, then produce code-changing subtasks that can be implemented one by one.
4. If tests are agreed upon, pair test work with each relevant subtask.
5. Present the subtasks to the human for confirmation before execution.

## Workflow

### 1) Context digestion
- Identify final decisions from the conversation.
- Capture constraints (tech, scope, style, deadlines, dependencies).
- Detect whether a grill-me session has already been completed.
- If context came from a grill-me session, treat resolved branches as requirements.

### 2) Readiness gate
- Resolve implementation-relevant uncertainties before generating subtasks.
- Investigate factual questions through available code, documentation, and conversation context.
- Ask the user about unresolved requirements or tradeoffs. Recommend a grill-me session when substantial decisions remain.
- A completed grill-me session does not bypass this gate if new uncertainties appear.
- Do not turn investigation, clarification, or decision-making into subtasks.
- Generate subtasks only when the intended changes and their prerequisites are clear.

### What counts as a subtask?

A subtask is a focused implementation change that produces a concrete, reviewable code diff.

- State what will change, not merely what someone will investigate or verify.
- Include relevant test changes and validation within the implementation subtask.
- Test-only changes qualify when they deliver requested coverage or regression protection.
- Reading code, exploring options, choosing an approach, running tests, and reviewing results do not qualify on their own.
- Do not invent code changes merely to make an activity qualify.

Examples:
- Not a subtask: “Investigate how authentication works.”
- Valid subtask: “Reject expired authentication tokens and add regression coverage.”
- Not a subtask: “Run the full test suite and validate the implementation.”
- Instead: Include the relevant test commands and acceptance checks in each implementation subtask.

### 3) Subtask generation
Create subtasks that are:
- Atomic: each can be implemented in one focused change set.
- Ordered: each step depends only on prior completed steps.
- Dependency-safe: every subtask appears only after all of its prerequisites are resolved.
- Reviewable: each step is scoped for clear implementation and validation.
- Traceable: each subtask maps back to one or more conversation decisions.

### 4) Test pairing (conditional)
If testing is requested or agreed:
- Attach test updates to each implementation subtask, not as one final bulk step.
- Specify test type per subtask (unit/feature/integration/e2e as appropriate).
- Define acceptance checks per subtask.
- Running existing tests is a validation check, not a separate subtask.
- If a full-suite run is required, attach it to the final implementation subtask's validation checks.
- Never append a standalone testing, validation, or review subtask.

If testing is explicitly not desired:
- Note that in assumptions and proceed without test subtasks.

### 5) Human-ready presentation
Present subtasks as a structured numbered list only.
- If grill-me has already been run, output only the subtask list and nothing after it.
- Do not append sections after the list.

## Output format

Use this format when presenting to the human:

1. **Subtask N: <title>**
   - Goal:
   - Scope:
   - Deliverables:
   - Tests:

## Guardrails

- Do not start implementation; planning only.
- Do not combine unrelated concerns in one subtask.
- Prefer smaller implementation changes, but never split investigation or validation into standalone subtasks.
- Resolve assumptions that affect scope or implementation before planning; label only non-blocking assumptions within the relevant subtask.
- Before presenting the list, verify that every subtask names a concrete code change. Resolve or remove any item that does not.
- Keep language concrete and execution-oriented.
- Always order subtasks so all dependencies are resolved before dependent work begins.
