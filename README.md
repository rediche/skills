# Rediche's Workflow Skills

[![skills.sh](https://skills.sh/b/rediche/skills)](https://skills.sh/rediche/skills)

Simple, focused agent skills for planning, implementation flow, and QA.
Inspired by [Matt Pocock's skills workflow](https://github.com/mattpocock/skills), kept intentionally simple and condensed.

## Install

Install from [skills.sh](https://skills.sh/docs) with:

```bash
npx skills@latest add rediche/skills
```

Then run the setup flow in your agent (if prompted) and use the installed skills via slash commands.

## Skills

- [`investigate-issue`](./investigate-issue/SKILL.md): Investigates an issue or work request and returns evidence-based implementation guidance without changing files.
- [`to-subtasks`](./to-subtasks/SKILL.md): Converts finalized planning context into an implementation-ready, dependency-ordered subtask list with optional per-subtask test pairing.
- [`do-subtasks`](./do-subtasks/SKILL.md): Executes exactly one approved subtask at a time, then returns a conventional commit message suggestion for human review and commit.
- [`to-pr`](./to-pr/SKILL.md): Implements agreed subtasks into a new branch, commits each subtask, pushes when complete, and opens a GitHub PR.
- [`auto-complete-task`](./auto-complete-task/SKILL.md): When explicitly invoked, coordinates investigation, planning, implementation, testing, commits, push, and PR creation without separate approval. Never merges the PR.
- [`qa`](./qa/SKILL.md): Generates a practical QA checklist from conversation goals.
- [`clear-writing`](./clear-writing/SKILL.md): Drafts or revises technical documentation with clear language while preserving requirements and technical meaning.
- [`simplify-agent-instructions`](./simplify-agent-instructions/SKILL.md): Reviews agent instructions and suggests clearer wording without editing files.
- [`pest-arch-review`](./pest-arch-review/SKILL.md): When explicitly invoked, reviews PHP architecture coverage and proposes tests using verified built-in Pest assertions. Does not edit files unless implementation is requested.
- [`retro`](./retro/SKILL.md): Reviews OpenCode session history and proposes evidence-based improvements to the AI setup.
- [`changelog`](./changelog/SKILL.md): Generates a concise, user-facing changelog from meaningful repository changes.
- [`audit-project-rules`](./audit-project-rules/SKILL.md): Audits application code for inconsistencies with Laravel Boost and project rules.

## Recommended workflow

### Planning and implementation

1. For a new idea, use [mattpocock's `/grill-me`](https://skills.sh/mattpocock/skills/grill-me) to pressure-test and refine it. This skill comes from a separate collection.
2. Use `/investigate-issue` when an issue or work request needs repository evidence before planning. It returns findings without changing files.
3. Run `/to-subtasks` to produce an ordered implementation plan.
4. Choose an execution path:
   - Use `/do-subtasks` for one approved subtask at a time. Review and commit each change yourself.
   - Use `/to-pr` to implement all agreed subtasks, commit each separately, push, and open a GitHub PR on a new branch.
5. Run `/qa` to generate a manual QA checklist, then perform the checks. The skill does not run them for you.

### Autonomous alternative

Explicitly invoke `/auto-complete-task` with an issue or work request to coordinate investigation through PR creation.
It delegates read-only investigation, plans with `/to-subtasks`, and executes through `/to-pr` without separate subtask approval.
Invocation authorizes implementation, testing, commits, push, and PR creation, but not merging.
This is an opt-in alternative to the planning and execution steps above, not an automatic follow-up.

### Supporting skills

Use these when relevant; they are not required pipeline steps:

- **Documentation:** Use `/clear-writing` to draft or revise documentation throughout the workflow.
- **Agent instructions:** Use `/simplify-agent-instructions` during setup or maintenance to get review-only suggestions. It uses `/clear-writing` for wording.
- **Project rules:** Use `/audit-project-rules` to report one confirmed project-rule inconsistency per run. It changes files only when implementation is explicitly requested.
- **Architecture coverage:** Explicitly invoke `/pest-arch-review` to propose PHP architecture tests before requesting implementation.
- **Release notes:** Use `/changelog` to summarize meaningful changes for users.
- **Workflow improvement:** Use `/retro` after work to review prior OpenCode sessions and propose evidence-based setup improvements.
