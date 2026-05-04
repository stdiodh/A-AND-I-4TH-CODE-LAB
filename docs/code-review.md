# Code Review Guide

## 1. Purpose

This guide defines how to review changes in this repository.

Review should focus on correctness, scope control, maintainability, and whether the change respects the Central Hub role.

## 2. Review Priorities

Review findings should be ordered by severity.

Prioritize:

1. Behavior regressions
2. Broken links or missing required references
3. Incorrect sequence or branch assumptions
4. Scope creep into unrelated sequences or topic repos
5. Missing verification
6. Accessibility or responsive layout issues for frontend work
7. Overengineering or unnecessary abstractions

## 3. Central Hub Review Checklist

Check:

- Does the change preserve the rule that central `docs` is not a detailed theory store?
- Did the change avoid modifying sequence status without explicit instruction?
- Are `docs/curriculum/*`, `docs/guides/*`, and `docs/sequences/*` respected?
- Are topic repos referenced rather than copied in full?
- Are `NN-implementation` and `NN-answer` branch meanings clear when sequence work is discussed?

## 4. Visual Lab Review Checklist

Check:

- Is the implementation inside the target sequence submodule, under `docs/visual-lab`?
- Does `docs/visual-lab/index.html` use relative paths?
- Did the root repo avoid `docs/index.html` and `docs/visualizer/*` implementation files?
- Are external JS libraries avoided?
- Does the implementation use HTML, CSS, and Vanilla JavaScript only?
- Is detailed theory kept out of central HTML?
- Are source docs and source code linked?
- Does the first DB Access flow match the expected path?

Expected first flow:

```text
Client
-> POST /posts
-> PostController
-> PostCreateRequest
-> PostService
-> PostEntity
-> PostRepository
-> MySQL
-> PostResponse
-> JSON Response
```

## 5. Frontend Review Checklist

For Visual Lab frontend work, check:

- The page opens from the target submodule's `docs/visual-lab/index.html`.
- The topic cards render.
- The first card is selected by default.
- Card click changes the detail view.
- Selected card state is visible and uses `aria-pressed="true"`.
- Flow timeline is readable on desktop and mobile.
- Text does not overlap or clip.
- Colors follow the Visual Lab design guide.

## 6. Markdown Review Checklist

For documentation work, check:

- Code fences are balanced.
- Links are correct.
- Headings match the document purpose.
- Examples do not accidentally become instructions for a different scope.
- Long code or theory from topic repos is linked instead of copied.

## 7. Review Response Format

When the user asks for a review, lead with findings.

Use this order:

1. Findings, highest severity first
2. Open questions or assumptions
3. Brief summary
4. Verification notes

If there are no issues, say that clearly and mention any remaining test gaps or residual risk.
