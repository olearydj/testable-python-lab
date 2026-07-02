# Testable Python Lab

This repo is the working context for INSY 7970 Lecture 05A: From Script to Testable Python.

The lecture slides provide the clone command and Jupyter startup command. The notebook adds the development tools and walks through the review. This repo represents the state after asking Codex for a tiny CSV-generating Python script with tests. The notebook is the inspection and review surface for that result.

## Files

```text
tiny_data_generator.py
tests/
  test_tiny_data_generator.py
notebooks/
AGENTS.md
pyproject.toml
```

## Assumed Codex Prompt

```text
Can you build a tiny Python script that prints fake CSV data? I want to be able to choose how many rows it prints. Please include tests.
```

## Your Job

Treat the files in this repo as Codex output that needs review.

Use the notebook to inspect the project, run the tool, import selected functions, run tests, and decide whether the result is understandable enough to commit.

The point is not to memorize every Python detail. The point is to practice supervising a code change:

1. inspect the files
2. run the program
3. install and run review tools
4. run the tests
5. probe small functions directly
6. understand the testable core and script boundary
7. inspect the Git diff before committing
