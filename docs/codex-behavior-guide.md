# Codex Behavior Guide

## 1. Purpose

This guide defines how Codex should behave in this repository.

The goal is not to make Codex faster.
The goal is to make Codex predictable, cautious, and easy to review.

## 2. Working Posture

Codex should act like a careful maintainer.

Default posture:

- Read the existing structure first.
- Prefer the repository's existing patterns.
- Make the smallest change that satisfies the request.
- Preserve central hub boundaries.
- Verify before reporting completion.

Avoid:

- Broad rewrites
- Speculative features
- Unrequested formatting churn
- Moving files just to make the structure look cleaner
- Changing sequence status without direct instruction

## 3. Assumptions

If an assumption affects correctness, write it down before acting.

Good assumptions:

- "I will treat this as a central hub documentation change, not a topic repo sequence change."
- "I will use `02-answer` as the first Visual Lab reference case, but keep the data model sequence-agnostic."

Bad assumptions:

- Silently choosing a sequence
- Silently changing the target branch model
- Silently adding a new topic repo

If the assumption would change scope, ask first.

## 4. Plan Before Implementation

For non-trivial tasks, produce a short plan before editing.

Use this shape:

```text
Goal:
- ...

Scope:
- Change:
- Do not change:

Plan:
1. ...
2. ...
3. ...

Verification:
- ...
```

Do not over-plan small edits.
For a one-line typo fix or a simple command output request, act directly.

## 5. Surgical Editing Rules

Every changed line must serve the task.

When editing:

- Use `apply_patch` for manual edits.
- Keep unrelated changes intact.
- Do not revert user changes.
- Match local naming, tone, and document structure.
- Keep Markdown code fences balanced.
- Prefer ASCII arrows (`->`) in docs unless the file already uses another convention.

## 6. Documentation Rules

This repository has two document types:

1. Central operating documents
2. Topic repository learning documents

Central documents may define:

- Sequence order
- Scope
- Rules
- Branch model
- Generation criteria
- Links and entry points

Central documents should not contain:

- Full theory lessons
- Full answer code
- Full implementation tutorials copied from topic repos

Topic repository documents may contain detailed theory and implementation steps.

## 7. Visual Lab Behavior

When working on Visual Lab:

- Treat it as a visual entry point, not a theory replacement.
- Use the Visual Lab planning documents as source of truth.
- Implement actual web files inside the target sequence submodule under `docs/visual-lab`.
- Do not put implementation files in the root repo's `docs/index.html` or `docs/visualizer/*`.
- Keep topic descriptions short.
- Link to source docs and source code instead of copying them.
- Make `NN-implementation` and `NN-answer` branch context visible.
- Use `spring-boot-db-access-lab` `02-answer` as the first reference case, not the only supported sequence.

## 8. Verification Before Final Response

Before finishing, check:

- Did the changed files match the user's requested scope?
- Did any unrelated file change?
- Did Markdown fences stay balanced?
- Did `git diff --check` pass?
- If code was changed, were relevant tests or local checks run?

If something was not verified, say so plainly.
