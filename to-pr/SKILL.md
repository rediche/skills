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
- Run `git status --short` to check the working tree. If it prints any files, stop and list the dirty files.
- If the user explicitly says to continue despite a dirty tree, ignore unrelated dirty files and proceed without modifying or reverting them.
- Determine the base branch with `git branch --show-current`, unless the user specifies another base branch.

### 2) Do-subtasks routing
- If `do-subtasks` has not already run for these subtasks, automatically enter its subtask execution model without asking the user.
- After that routing step, ignore the `do-subtasks` requirement to stop after one task.
- Continue through all agreed subtasks, but keep each commit limited to the current subtask.

### 3) Branch setup
- Create the work branch from the base branch with `git switch -c <work-branch> <base-branch>` before implementation.
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

Use this format for the PR body. Keep prose brief and use the project's domain language:

```md
## Summary

<diagram, diff sketch, or tree that makes the key change clear>

## Evidence

- **Before:** <screenshot, output, or failing test>
- **After:** <screenshot, output, or passing test>
- **Manual QA:** <practical step-by-step checks, when hands-on verification is useful>

## Merge Danger

**Door:** <one-way or two-way>

<Brief explanation, if useful>

**Blast Radius:** <one-word description>

<Potential impact of merging, if useful>
```

Choose the smallest representation that explains the change:

- Pseudocode for logic or algorithms.
- A call tree for runtime control flow.
- A component tree for UI structure.
- A shallow file tree for file responsibility or broad refactors.
- Mermaid for interactions or data flow.
- A focused diff sketch when the key point is what changed.

Use visuals only when they help explain the change. Include concrete before-and-after evidence; prefer screenshots for visual changes and test or command output for behavior changes. Write manual QA steps in the style of `qa` when hands-on verification is useful.

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
