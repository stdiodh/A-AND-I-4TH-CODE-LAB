# AGENTS.md

This repository uses `AGENTS.md` as the Codex project instruction file.
Follow these instructions before making code or document changes.

## Core Principle

Bias toward caution over speed.
Prefer small, verifiable, surgical changes over broad rewrites.

This repository is the A&I 4th Backend Code Lab Central Hub.
The central `docs` directory is not a detailed theory store.
Detailed theory, implementation guides, checklists, and answers live in each topic repository.

## 1. Read Before Working

Before implementation, read the root `README.md`.
For sequence work, also read the curriculum, guides, sequence document, and topic repository documents listed in `README.md`.

When relevant, read these project-specific documents:

- `docs/codex-behavior-guide.md`
- `docs/code-review.md`
- `docs/implementation-plan-template.md`
- `docs/visual-lab-sequence-workflow.md`
- `docs/visual-lab-design-guide.md`
- `docs/visual-lab-content-spec.md`
- `docs/visual-lab-implementation-plan.md`
- `docs/visual-lab-codex-prompt.md`

If these documents conflict, prefer the more specific document for the current task.
If a local task has a nearer `AGENTS.md`, that nearer instruction takes priority for files under that directory.

## 2. Think Before Coding

Before implementing, do the following:

- State assumptions explicitly when they affect correctness.
- Do not silently choose between multiple meaningful interpretations.
- If the request is ambiguous and the ambiguity affects correctness, ask before coding.
- If a simpler approach exists, mention it.
- Push back when the requested solution seems overcomplicated or risky.

For non-trivial tasks, start with a short plan:

1. Step -> verify: check
2. Step -> verify: check
3. Step -> verify: check

Do not write code until the goal and verification method are clear.

## 3. Simplicity First

Write the minimum code or documentation that solves the requested problem.

Do not add:

- Unrequested features
- Single-use abstractions
- Speculative flexibility
- Extra configuration
- Defensive handling for impossible scenarios

If the implementation becomes much larger than necessary, simplify it before finalizing.

## 4. Surgical Changes

Touch only files and lines required by the task.

When editing existing files:

- Do not refactor unrelated code.
- Do not improve adjacent comments, formatting, or style unless required.
- Match the existing project style.
- Remove only unused imports, variables, or functions introduced by your own change.
- If unrelated dead code is found, mention it in the final response instead of deleting it.

Every changed line must directly support the user request.

## 5. Central Hub Rules

For this repository:

- Do not turn central `docs` into a detailed theory repository.
- Do not change `docs/sequences/*` scope or status without explicit user request.
- Do not start the next sequence without user approval.
- Keep `1 sequence = 1 branch = 1 PR` as the operating model.
- Use `NN-implementation` for student starter branches.
- Use `NN-answer` for instructor comparison or answer branches.
- Keep topic repository `main` branches as guide branches, not student starter branches.

## 6. Visual Lab Rules

For A&I Backend Visual Lab work:

- Treat `docs/visual-lab-sequence-workflow.md` as the execution protocol.
- Read the four Visual Lab planning documents before implementation.
- Implement the web files inside the target sequence submodule, under `docs/visual-lab`.
- Do not create root-level `docs/index.html` or `docs/visualizer/*` implementation files.
- Use `docs/visual-lab/index.html` inside the target submodule as the static entry point.
- Use only HTML, CSS, and Vanilla JavaScript.
- Do not use external JS libraries, React, Vue, Next.js, Bootstrap, or Tailwind CDN.
- Use relative paths so GitHub Pages can open the page.
- Do not paste long theory text or full answer code into central HTML.
- Connect every sequence through `NN-implementation` and `NN-answer` when possible.
- After each sequence is complete, commit/push the submodule first, then commit/push the root submodule pointer.
- Do not start the next sequence until the previous sequence's submodule and root pointer updates are complete or the user explicitly redirects.

## 7. Goal-Driven Execution

Convert tasks into verifiable goals.

Examples:

- "Fix a bug" -> reproduce the bug, fix it, then verify it no longer occurs.
- "Add validation" -> add or identify invalid-input checks, then verify passing behavior.
- "Refactor" -> preserve behavior and run the relevant checks before and after.
- "Add a document" -> verify links, required sections, and Markdown rendering boundaries.

Before finishing:

- Run the most relevant tests or checks available.
- If tests cannot be run, explain why.
- Summarize what changed and how it was verified.

## 8. Review Before Final Response

Before responding to the user:

- Review the diff.
- Check for unnecessary changes.
- Check for overengineering.
- Check whether the result matches the original request.
- Mention any assumptions, limitations, or unverified parts.

## 9. Useful Verification Commands

Use the relevant command for the task:

```bash
git diff --check
git status --short
python3 -m http.server 8080 -d docs/visual-lab
```

For Visual Lab verification, open:

```text
http://localhost:8080
```
