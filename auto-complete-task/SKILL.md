---
name: auto-complete-task
description: Completes requested work autonomously through investigation, subtask planning, implementation, testing, and GitHub PR creation. Use when the user explicitly invokes auto-complete-task to complete a feature, bug fix, optimization, GitHub issue, or plain-text request.
metadata:
  opencode/autoinvoke: false
---

# Auto Complete Task

## Quick start

Example: `Auto-complete-task: fix the search timeout described in #123.`

1. Accept the work request.
2. Delegate investigation to a subagent using `investigate-issue`.
3. Load `to-subtasks` and generate implementation subtasks.
4. Load `to-pr` and execute the subtasks without separate approval.
5. Return the PR URL and validation results.

## Authorization

- Run this skill only when the user explicitly invokes it.
- Do not invoke this skill automatically from another skill or agent.
- Treat invocation as authorization to implement, test, commit, push, and create a PR for the request.
- Do not merge the PR.
- Follow repository instructions, tool permissions, and higher-priority restrictions.

## Workflow

### 1) Intake and preflight

- Accept a GitHub issue URL, issue number, or plain-text work request.
- Treat features, bugs, and optimizations as valid requests.
- Ask what to work on only when no request was supplied.
- Read applicable repository instructions.
- Check the working tree with `git status --short`.
- Preserve the dirty-file safeguards from `to-pr`.
- Stop on dirty files unless the user explicitly authorized continuing despite them.
- Never modify, revert, or stage unrelated changes.
- Stay in the current directory, including when it is already a worktree.
- Never create another worktree.

### 2) Resolve the target

- Default the target branch to `main` on `origin`.
- Use another target branch or remote when the user explicitly specifies one.
- Fetch the selected target before investigation.
- For the default, run `git fetch origin main`.
- Resolve the fetched target commit with `git rev-parse FETCH_HEAD`.
- Record the target branch name, remote, and fetched commit separately.
- Stop if the target is missing or fetching fails.
- Never substitute stale local branches or the current branch for the selected target.

### 3) Investigate in a subagent

- Start a read-only subagent and instruct it to load `investigate-issue`.
- Supply the request, repository path, target commit, constraints, and relevant conversation context.
- Require investigation against the fetched target commit.
- Use read-only Git commands to inspect target files when the current checkout differs.
- Require evidence, acceptance criteria, proposed changes, validation options, and blockers.
- Do not authorize file edits or implementation in the investigation subagent.
- Continue factual investigation when findings are insufficient.

### 4) Plan autonomously

- Resolve routine uncertainty from repository evidence and established project conventions.
- Choose the smallest supported change that satisfies the request.
- Record reasonable, non-blocking assumptions.
- Ask only when missing access, conflicting requirements, or consequential ambiguity prevents safe progress.
- Do not invent requirements to avoid asking a necessary question.
- Load `to-subtasks` with the request, investigation findings, acceptance criteria, and constraints.
- Identify this as an explicitly user-invoked `auto-complete-task` workflow.
- Use its autonomous handoff instead of requesting subtask approval.
- Include relevant regression coverage and validation checks in the implementation subtasks.

### 5) Implement and open the PR

- Load `to-pr` with the authorized subtasks.
- Explicitly supply the fetched commit as the work branch starting point.
- Explicitly supply the selected branch name as the PR base, such as `main`, not `origin/main`.
- Supply the selected remote and original GitHub issue reference when applicable.
- Apply these branch instructions only to this run.
- Preserve the standalone current-branch default in `to-pr`.
- Follow its implementation, testing, separate-commit, push, and PR verification rules.
- Preserve its safeguards, including dirty-file, label-selection, and validation blockers.
- Do not push partial work or create a PR before all subtasks and required checks pass.
- Return the PR URL, completed work, validation results, assumptions, and blast-radius rationale.
- If blocked, report completed work and the exact action needed to continue.
