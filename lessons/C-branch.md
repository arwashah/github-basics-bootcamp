# Lesson C: Create a new branch

Branches let you work on changes without touching the default branch.

Objectives:
- Create a feature branch from the default branch.
- Keep work isolated and easy to review.

Key concepts:
- A branch is a named pointer to a line of commits.
- The default branch is usually `main`.
- New work should start from an up-to-date default branch.

Steps:
1. Make sure your default branch is current:
   - `git checkout main`
   - `git pull origin main`
2. Create and switch to a new branch:
   - `git checkout -b feature/short-name`
   - or `git switch -c feature/short-name`
3. Confirm the active branch:
   - `git status` (look for the branch name)

Verify:
- `git branch` lists your new branch with a `*` next to it.

Common pitfalls:
- Creating a branch while still on an outdated `main`.
- Using long or unclear branch names.

Checklist mapping:
- C) Create a new branch

Tip:
- Use short, descriptive branch names like `feature/short-name`.
