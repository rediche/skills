---
name: changelog
description: Generate a concise, user-facing changelog from meaningful changes in the current repository and branch. Use when the user asks for a changelog, release notes, recent changes, or a summary of work over a date range or contributor scope.
---

# Changelog

## Quick start

Generate changelog text only. Do not create or edit a changelog file.

Before inspecting history, ask the user what the changelog should cover:

- Date range, defaulting to the past 7 days.
- Contributor scope, defaulting to the current GitHub user.

Use the user's explicit date range and contributor scope when provided. Keep the
default repository and branch as the current repository and current branch.

## Workflow

1. Identify the current GitHub user with `gh api user --jq .login`.
2. Identify the current repository and branch from the local git checkout.
3. Inspect matching local history with `git log` and `git show`, including both
   regular commits and merge commits. Restrict results to the selected dates,
   branch, and contributor scope.
4. When the default GitHub-user filter cannot be reliably matched to local
   author names or emails, use the repository commit API to resolve that
   GitHub login to commit SHAs, then inspect those commits with local git.
5. Read relevant diffs and group duplicate or related commits into one change.
6. Translate implementation details into meaningful outcomes a layman can
   understand. Include internal work only when it has a clear user, maintainer,
   documentation, reliability, or future-feature impact.

## Output rules

- Return only a simple bullet list, with no preamble, table, or commit log.
- Start each bullet with one of: `- Added`, `- Improved`, or `- Fixed`.
- Write one meaningful change per bullet in plain language.
- Explain the result or benefit rather than copying commit messages.
- Combine commits that implement the same outcome.
- Omit routine formatting, mechanical refactors, tests, and dependency changes
  unless their impact is relevant enough to explain to others.
- Do not invent benefits or details that are not supported by the history.
- If no meaningful changes match, return `- No meaningful changes found.`

Example output:

```text
- Added clearer error messages when a saved report cannot be loaded.
- Improved the setup documentation for configuring GitHub authentication.
- Fixed an issue that could hide newly created projects from the project list.
```
