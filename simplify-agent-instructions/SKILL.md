---
name: simplify-agent-instructions
description: Reviews agent instructions and suggests clearer language using practical ASD-STE100 principles. Use when simplifying AGENTS.md, CLAUDE.md, .ai/ files, editor rules, or other codebase instructions for agents.
---

# Simplify Agent Instructions

Find agent instructions throughout the codebase, including nested files, rule directories, and referenced instruction sources. For Laravel projects using Laravel Boost, prioritize `.ai/` source instructions over generated files such as `AGENTS.md` or `CLAUDE.md`.

Load and follow the `clear-writing` skill for language rules and meaning preservation. For agent instructions, use one instruction per sentence. Keep code, commands, paths, and identifiers unchanged.

Report suggestions only. For each suggestion, include:
- File path and line number.
- Original text.
- Suggested replacement.
- Brief reason.

Skip changes that do not improve clarity. Identify source files when generated instructions duplicate them.
