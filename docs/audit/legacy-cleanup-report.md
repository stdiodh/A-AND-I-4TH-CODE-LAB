# Legacy Cleanup Report

Date: 2026-06-04

## Scope

This audit checked root-level legacy cleanup candidates before and after the Visual Lab hub/detail split.

Commands used:

```bash
find . -maxdepth 3 -type f | sort
find . -name "*.sh" -type f | sort
rg -n "legacy|deprecated|visualizer|docs/index.html|docs/visualizer|answerBranch|sourceAnswerBranch|NN-answer|[0-9]{2}-answer" .
git ls-files .repo-builds .DS_Store docs/.DS_Store '*/.DS_Store'
```

## Deleted

No tracked root legacy files were deleted in this pass.

## Kept

- `.github/workflows/repository-integrity.yml`: required repository integrity automation.
- `.gitmodules`: required submodule mapping.
- `scripts/validate-manifest.py`: required manifest validation.
- `scripts/validate-visual-labs.py`: updated for the new hub/detail Visual Lab structure.
- `scripts/validate-visual-lab-colors.py`: retained as an existing Visual Lab color check.
- `docs/manifest/*`, `docs/curriculum/*`, `docs/sequences/*`, `docs/visual-lab-*.md`, `docs/agent/*`: operational source documents.
- `spring-boot-event-driven-lab/scripts/*.sh` and `spring-boot-refactoring-foundation-lab/scripts/*.sh`: deployment/verification scripts used by deployment and event-driven runtime labs.

## Review Needed

- `.repo-builds/*`: local generated build/reference workspace appears untracked or ignored from the root repo. It was not removed because it is outside tracked source and may contain local working material.
- `.DS_Store` files: local filesystem artifacts appear untracked or ignored. They were not removed because they are not part of the tracked diff.
- Legacy branch/default-branch cleanup remains a manual GitHub operation where documented in README and prior audit notes.

## Visual Lab Rule Check

- Root `docs/index.html` does not exist.
- Root `docs/visualizer/*` does not exist.
- No root `.sh` cleanup target was found.
