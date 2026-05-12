# Rediche's Workflow Skills

[![skills.sh](https://skills.sh/b/rediche/skills)](https://skills.sh/rediche/skills)

Simple, focused agent skills for planning, implementation flow, and QA.
Inspired by Matt Pocock's skills workflow, kept intentionally simple and condensed.

## Install

Install from [skills.sh](https://skills.sh/docs) with:

```bash
npx skills@latest add rediche/skills
```

Then run the setup flow in your agent (if prompted) and use the installed skills via slash commands.

## Skills

- [`do-subtasks`](./do-subtasks/SKILL.md): Executes exactly one approved subtask at a time, then returns a conventional commit message suggestion for human review and commit.
- [`qa`](./qa/SKILL.md): Generates a practical QA checklist from conversation goals.
- [`to-subtasks`](./to-subtasks/SKILL.md): Converts finalized planning context into an implementation-ready, dependency-ordered subtask list with optional per-subtask test pairing.

## Recommended workflow

When starting a new idea, use this flow:

1. Run [mattpocock's `/grill-me`](https://skills.sh/mattpocock/skills/grill-me) to pressure-test and refine the idea.
2. Run `/to-subtasks` to produce an ordered implementation plan.
3. Run `/do-subtasks`.
4. Implement the generated subtasks with Agent 1, one subtask at a time.
5. Run `/qa` to generate a manual QA plan and test the result.
