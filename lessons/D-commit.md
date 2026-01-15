# Lesson D: Make a commit

A commit records a snapshot of your work.

Objectives:
- Stage the right files.
- Create a clear, descriptive commit.

Key concepts:
- A commit is a saved change with a message and author.
- "Staging" lets you pick exactly what goes into the commit.
- Small, focused commits are easier to review.

Steps:
1. Check your working tree:
   - `git status`
2. Stage your changes:
   - `git add <file>` for specific files
   - or `git add .` for all changes in the repo
3. Review what is staged:
   - `git diff --staged`
4. Create the commit:
   - `git commit -m "Describe the change"`
5. Confirm the commit exists:
   - `git log -1`

Verify:
- `git status` shows a clean working tree.
- `git log -1` shows your new commit message.

Common pitfalls:
- Committing unrelated changes together.
- Writing vague messages like "update".

Checklist mapping:
- D) Make a commit

Tip:
- Write clear commit messages that explain the change.
