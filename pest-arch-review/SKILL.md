---
name: pest-arch-review
description: Reviews PHP codebases for architectural conventions and proposes missing architecture tests using only built-in Pest assertions. Use when explicitly invoked to review architecture-test coverage, identify testable code patterns, or propose Pest architecture tests.
metadata:
  opencode/autoinvoke: false
---

# Pest Architecture Review

Run only when the user explicitly invokes this skill. Propose architecture tests grounded in the codebase, using only Pest's built-in architecture assertions. Do not modify files unless the user explicitly requests implementation.

## Workflow

1. Read applicable project instructions and architecture documentation. Use the user's requested scope; otherwise review first-party PHP source and architecture tests. Exclude vendor, generated code, and caches unless explicitly relevant.
2. Inspect `composer.json`, `composer.lock`, available installed package metadata, autoload mappings, test configuration, and `tests/Pest.php`. Determine the Pest version and architecture-testing capabilities. Distinguish locked dependencies from installed ones; if availability cannot be verified, report the uncertainty rather than assuming the latest API.
3. Read existing architecture tests, including shared configuration, built-in presets, selectors, and exclusions. Identify rules already enforced so proposals do not duplicate coverage.
4. Search the source for recurring conventions and verify them by reading representative implementations and counterexamples. Consider namespace boundaries, dependency direction, naming, inheritance, interfaces, traits, class modifiers, and strict types. Treat these as discovery prompts, not mandatory rules.
5. Separate documented requirements from inferred patterns. Support inferred conventions with multiple concrete examples where available; do not turn an isolated example or generic best practice into a rule. Check the full proposed target scope for exceptions, and disclose any incomplete inspection.
6. Map each supported coverage gap to built-in architecture assertions and modifiers. Verify exact method names, signatures, selector behavior, and semantics against the installed Pest implementation or official documentation matching the project's version. Start with <https://pestphp.com/docs/arch-testing>, but do not assume current documentation matches older installations. Omit any rule whose built-in support cannot be verified.
7. Choose the narrowest useful, nonempty target scope. Inspect dependency direction carefully: restricting what a namespace uses is different from restricting who may use it. Include only justified exclusions; never hide violations merely to make a proposal pass.
8. Present the strongest nonredundant proposals first. If none qualify, say so. Do not invent tests to fill a quota. Do not create test files, install dependencies, or change application code during the review.

## Report

Start with the reviewed scope, detected Pest version, existing coverage, and inspection limitations. For each proposal include:

- **Rule and value:** The convention protected and why it matters in this project.
- **Evidence:** Source paths and line numbers, relevant documentation, and whether the rule is documented or inferred.
- **Coverage gap:** Why existing tests or presets do not already enforce it.
- **Proposed test:** Concrete PHP code using verified built-in assertions, plus the suggested test-file path following project conventions.
- **Scope and exceptions:** Matched namespaces or classes, justified exclusions, and any uninspected targets.
- **Expected outcome:** Known likely violations with paths, or an explicitly unverified expectation that the test will pass. Never claim an unexecuted test passed.
- **API basis:** Installed source location or version-matched official reference supporting the assertion and modifiers.

## Example

If multiple controllers and project rules establish the suffix convention, and no existing test or preset covers it, propose:

```php
arch('controllers use the Controller suffix')
    ->expect('App\Http\Controllers')
    ->toHaveSuffix('Controller');
```

This is illustrative, not a default recommendation. Verify the namespace exists, all intended targets are included, and the installed Pest version supports the assertion.

## Guardrails

- Use only built-in Pest architecture assertions, selectors, modifiers, and built-in presets available to the project. Prefer focused assertions; propose a preset only after inspecting all its rules and overlap.
- Do not propose custom expectations, custom presets, third-party plugins, Pest extensions, helper-based checks, reflection loops, AST traversal, regex scans, or callbacks as substitutes for unsupported assertions. Search tools may aid discovery, but must not become bespoke test logic.
- Do not propose upgrading Pest or adding packages to make a rule expressible. Report missing prerequisites without making installation part of the review.
- Omit rules that built-in assertions cannot express faithfully. Do not approximate behavioral guarantees with naming or dependency checks.
- Do not impose Laravel, domain-driven design, repository layers, final classes, or other preferences without project evidence.
- Treat existing violations as findings, not automatic permission to refactor or weaken the rule. Distinguish intentional exceptions from uncertain cases.
