---
name: audit-project-rules
description: Audit the application for inconsistencies with its Laravel Boost and project rules. Use when asked to find, audit, or identify a rule violation or inconsistency in the codebase.
---

# Audit Project Rules

Find one concrete inconsistency between the application and its established rules, then stop.

## Workflow

1. Read `.ai/rules/index.md`.
2. Identify every rule file matching the paths being inspected.
3. Read those matching rule files before reviewing code.
4. Search the relevant application files using repository search tools.
5. Confirm the suspected violation by reading the surrounding implementation and existing conventions.
6. Report only the first confirmed inconsistency.
7. Do not modify files unless the user explicitly asks for implementation.

## Report

Include:

- The affected file and line number.
- The exact project or Laravel Boost rule being violated.
- Why the implementation is inconsistent.
- A concise, concrete solution.
- Whether any files were modified.

## Guardrails

- Do not report speculative findings.
- Do not report multiple findings in one run.
- Do not treat unrelated dirty-worktree changes as violations.
- Prefer the smallest compliant solution.
- Include focused test coverage in the proposed solution when implementation would change behavior.
