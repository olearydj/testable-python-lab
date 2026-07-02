# AGENTS.md

This is a small teaching repo for INSY 7970: Modern Software Development Tools and Practices for Data Science.

## Role Of This Repo

The repo supports Lecture 05A, "From Script to Testable Python." It represents a tiny Python data tool after an initial Codex-assisted implementation with functions, type hints, and tests.

The point is not to build a polished package. The point is to help students practice supervising a Codex-generated change:

- inspect the repo with shell commands
- read the generated code
- run the script
- run tests
- import and call small functions
- distinguish the testable core from the script boundary
- ask Codex to explain before editing
- inspect the Git diff before committing

## Collaboration Expectations

When helping in this repo:

- Keep changes small and easy to review.
- Explain what changed and why.
- Preserve the teaching focus on script-to-testable-Python structure.
- Prefer standard-library Python unless the user explicitly asks for dependencies.
- Do not add runtime dependencies.
- If adding development tools, use `uv add --dev ...`.
- Keep `tiny_data_generator.py` understandable to early Python learners.
- Keep tests focused on observable behavior.

## Current Teaching Premise

Assume the student has already asked Codex for a first tiny CSV script and tests. The working files are the artifact to inspect. The next useful Codex behavior is usually explanation, review, or a small targeted improvement, not a broad rewrite.

Assumed first prompt:

```text
Can you build a tiny Python script that prints fake CSV data? I want to be able to choose how many rows it prints. Please include tests.
```

Good first prompts include:

```text
Explain tiny_data_generator.py in terms of core logic, boundary code, type hints, and tests. Do not edit files.
```

```text
Do not edit yet. First tell me which functions are easiest to test, which code is boundary code, and what one small test you would add next.
```

```text
Review the tests and identify one small missing behavior worth testing next. Do not edit files.
```

```text
Explain the current git diff file by file. Focus on behavior changes and risk. Do not edit files.
```
