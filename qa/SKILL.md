---
name: qa
description: Generates a practical QA checklist from the current conversation and goals. Use when the user asks for QA tasks, test checklists, validation steps, or simple step-by-step testing guidance.
---

# QA

## Workflow

1. Review the current conversation and identify the primary goals to verify.
2. Convert each goal into one QA task with a clear, action-oriented title.
3. For each QA task, provide a short step-by-step list of simple test actions.
4. Keep steps explicit and easy to follow; avoid technical jargon unless required.
5. Focus on practical verification outcomes (what to check and what should happen).
6. Keep tasks small and independent so they can be completed one by one.

## Output Rules

- Base all QA tasks on the conversation context.
- Prefer concise tasks over broad, combined tasks.
- Use plain language and short steps.
- Include expected result wording where useful.
- Do not invent unrelated requirements.
