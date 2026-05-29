---
name: to-pr
description: Implements agreed subtasks into a new branch, commits each subtask, pushes when complete, and opens a GitHub PR. Use when subtasks from to-subtasks should be implemented end-to-end as a pull request, or when the user mentions to-pr, PR automation, branch-to-PR workflow, or implementing all subtasks into a GitHub pull request.
---

# To PR

## Quick start

When the user asks to turn agreed subtasks into a PR:

1. Use the existing subtasks from `to-subtasks`.
2. Route through `do-subtasks` behavior automatically if it has not already run.
3. Create a new branch from the current branch, unless the user specifies another base.
4. Implement each subtask, test it, and commit it separately.
5. Push only after all subtasks are complete and tests pass.
6. Create the PR with `gh` and return the PR URL.

## Workflow

### 1) Preconditions
- If no agreed subtasks exist, stop and instruct the user to run `to-subtasks` first.
- If the working tree is dirty, stop and list the dirty files.
- If the user explicitly says to continue despite a dirty tree, ignore unrelated dirty files and proceed without modifying or reverting them.
- Determine the base branch: use the current branch by default, or the user-specified base branch if provided.

### 2) Do-subtasks routing
- If `do-subtasks` has not already run for these subtasks, automatically enter its subtask execution model without asking the user.
- After that routing step, ignore the `do-subtasks` requirement to stop after one task.
- Continue through all agreed subtasks, but keep each commit limited to the current subtask.

### 3) Branch setup
- Create a new branch from the base branch before implementation.
- Infer the branch prefix from the goal and work type, using conventional prefixes such as `feat/`, `fix/`, `chore/`, `ci/`, `docs/`, `refactor/`, or `test/`.
- Infer a short kebab-case branch name from the project goal.
- Do not push the branch until all subtasks are complete and tests pass.

### 4) Implementation loop
For each agreed subtask, in order:

1. Implement only the current subtask.
2. Run the relevant tests or checks for that subtask.
3. Treat the subtask as incomplete until tests pass.
4. Commit only the changes for that subtask.
5. Use a conventional commit message with no scope and no body: `<type>: <short description>`.

### 5) Push and PR
- After all subtasks are committed and the full relevant test suite passes, push the branch.
- Create the PR with the GitHub CLI using `gh`.
- Target the same branch used as the base branch.
- Use a human-readable PR title based on the project goal, such as `Add comments to blog posts`.
- Do not use conventional commit style for the PR title.
- If the PR resolves an open GitHub issue, include a closing keyword in the PR body (for example, `Closes #123`) so the issue closes automatically when the PR is merged.

## PR description

Include these sections in the PR body:

- Goal: what the PR is meant to achieve.
- Implemented: concise summary of completed subtasks.
- Manual QA: practical step-by-step checks written in the style of `qa`.

## Output rules

- Return the GitHub PR URL when finished.
- Include a concise recap of implemented subtasks.
- If blocked, explain the blocker and the exact next action needed.

## Guardrails

- Stick exactly to the agreed subtasks.
- Do not add opportunistic refactors or unrelated fixes.
- Do not modify, revert, or stage unrelated dirty files.
- Do not push partial work.
- Do not create a PR until all subtasks are complete and tests pass.
