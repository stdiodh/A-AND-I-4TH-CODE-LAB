---
name: aandi-visual-lab-design
description: Design, implement, review, or revise A&I Backend Visual Lab interfaces. Use for any change to */docs/visual-lab/**/*.html, CSS, rendering or interaction JavaScript, Visual Lab UI copy, accessibility, responsive behavior, screenshots, or the central docs/visual-lab-*.md design rules. Do not use to change curriculum scope, technical facts without sources, student or answer branch contents, sequence status, or unrelated repositories.
---

# A&I Visual Lab Design

Create a subject-specific learning workspace, not a generic card dashboard. Preserve the A&I light educational identity while making each sequence's real system behavior the primary visual structure.

## Required references

Read these before planning or editing:

1. Repository `AGENTS.md`, root `README.md`, and `docs/visual-lab-sequence-workflow.md`.
2. Central `docs/visual-lab-design-guide.md`, `docs/visual-lab-content-spec.md`, `docs/visual-lab-implementation-plan.md`, and the target `docs/sequences/NN-*.md`.
3. Target topic repository theory, implementation, checklist, and current `docs/visual-lab` files.
4. [Anthropic frontend-design source](references/anthropic-frontend-design-SKILL.md).

Keep [LICENSE.txt](references/LICENSE.txt) and [SOURCE.md](references/SOURCE.md) with the source reference.

## Before implementation

1. Run repository, remote, branch, status, and submodule checks. Preserve unrelated user changes.
2. Audit the current hub, detailed sequence, interactions, empty/error/disabled states, focus, mobile, and motion.
3. Write a compact plan that defines subject, audience, single job, 4–6 core colors, Display/Body/Utility typography, two ASCII layout options, one signature element, and one motion moment.
4. Critique the plan for generic dashboard patterns. Revise it before writing CSS or rendering code.
5. Establish a browser baseline when the environment supports it.

## Experience model

Use this shared learning grammar:

```text
Current question
-> required premise and first-term definitions
-> input condition without the outcome
-> learner prediction
-> one observed transition
-> adjacent reason and scoped evidence
-> opposite-condition comparison
-> learner's revised causal rule
-> next question
```

Use `Learning Signal Trace` as the single shared signature: keep the real topology visible, expand one current transition, and update the real request, object, token, cache, artifact, test, or event path after a prediction. Do not unfold every transition, repeat the same actor per row, or add decorative numbered steps, terminal chrome, metrics, or diagrams.

Keep the shell consistent, but choose a topic-specific primary workbench. Examples include request packet trace, persistence boundary, failure gate, authentication boundary, cache state inspector, connection/broadcast console, runtime boundary, pipeline gate, behavior invariant map, and event delivery trace.

## Implementation rules

- Use only repository-local HTML, CSS, and Vanilla JavaScript with relative paths.
- Preserve existing IDs, links, hash behavior, and the canonical `window.visualLabData` contract unless the central spec and validator are updated together.
- Extend semantic tokens before adding component-specific values. Keep the established A&I light palette unless the central design policy is explicitly changed.
- Use system sans for Display and Body roles and system mono for paths, commands, code, status, and data. Never import external fonts.
- Prefer one primary interactive surface over repeated cards that restate the same flow.
- Require `workbench.visual`, `workbench.terms`, and a `prediction` for every scenario. Do not reveal path, snapshot, or outcome before the prediction.
- Render node icons from local `assets/icons/{icon}.svg` and one topic explanation from `assets/diagrams`. Keep `system-icons.svg` only as source/backward compatibility, not the primary runtime path.
- Give informative SVGs alt text and visible captions; retain visible text fallback when an image fails. Keep `assets/SOURCE.md` and `assets/LICENSES.md`.
- Simplify each topic SVG so its smallest visible text remains at least 10.5px in the roughly 320px-wide image area of a 390px viewport; do not make students zoom a full desktop flowchart to read it.
- Use manual previous/next navigation only. Do not add autoplay or speed controls.
- Connect every structural element to real actors, states, responsibilities, code points, checks, or next questions.
- Keep copy concise, active, learner-facing, and technically accurate. Never expose answer branch names, secrets, or long completed code.
- Do not use hover movement that shifts layout, decorative glow, blanket gradients, or scattered animation.

## Accessibility and responsive completion

- Use semantic headings, nav, lists, buttons, links, labels, and progress semantics.
- Preserve visible `:focus-visible`; keep touch targets at least 44px where practical.
- Keep state understandable without color through labels, icons, routes, or text.
- Avoid broad or repeatedly changing `aria-live` regions.
- At 390px, prevent page-level horizontal overflow; constrain only genuinely wide code or diagrams locally.
- Support long Korean text, paths, commands, and zoom without overlap.
- Limit motion to the selected signal transition. Under `prefers-reduced-motion: reduce`, remove smooth scrolling and transitions and show the same state statically.

## Verification and repository workflow

1. Run `node --check` for every Visual Lab JavaScript file.
2. Run the central manifest and Visual Lab validators and `git diff --check`.
3. Check all implemented sequences in any repository whose shared CSS or JavaScript changed.
4. Browser-test desktop, tablet, and 390px mobile; inspect console, keyboard focus, reduced motion, long content, and page overflow.
5. Confirm every informative image has `complete === true`, `naturalWidth > 0`, a visible bounding box, no 404, and a text fallback. Check 200% zoom.
6. Record before/after findings and unresolved issues.
7. Commit and push the topic repository first. Update and commit only its central submodule pointer afterward.

Do not declare completion without browser inspection.
