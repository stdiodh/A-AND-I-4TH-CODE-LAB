# Implementation Plan Template

Use this template before non-trivial code or documentation changes.

Do not use it for tiny typo fixes or simple command-output requests.

## 1. Goal

```text
What should be true when this work is complete?
```

## 2. Scope

Change:

- ...

Do not change:

- ...

## 3. Inputs To Read

Required:

- `README.md`
- ...

Task-specific:

- ...

For Visual Lab:

- `docs/visual-lab-design-guide.md`
- `docs/visual-lab-content-spec.md`
- `docs/visual-lab-implementation-plan.md`
- `docs/visual-lab-codex-prompt.md`

## 4. Assumptions

- ...

If any assumption affects correctness or scope, ask before implementing.

## 5. Plan

1. Step:
   Verify:
2. Step:
   Verify:
3. Step:
   Verify:

## 6. Files Expected To Change

- ...

## 7. Verification

Run the most relevant checks:

```bash
git diff --check
```

For static docs pages:

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

Expected browser URL:

```text
http://localhost:8080
```

## 8. Completion Notes

Final response should include:

- What changed
- How it was verified
- Anything not verified
- Any assumptions or follow-up risks
