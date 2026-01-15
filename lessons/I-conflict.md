# Lesson I: Resolve a merge conflict

Conflicts happen when two branches change the same lines.

Objectives:
- Understand conflict markers.
- Resolve conflicts safely and commit the result.

Key concepts:
- A merge conflict means Git cannot auto-combine changes.
- Conflict markers show the competing changes:
  - `<<<<<<<` your branch
  - `=======` separator
  - `>>>>>>>` other branch

Steps:
1. Start a merge or rebase that causes a conflict.
2. Open the conflicted file and find the markers.
3. Decide the final content (keep one side or combine both).
4. Remove the conflict markers and save the file.
5. Stage the resolved file:
   - `git add <file>`
6. Continue and finalize:
   - For merge: `git commit`
   - For rebase: `git rebase --continue`

Verify:
- `git status` shows no conflicts.
- The resolved file reads correctly.

Common pitfalls:
- Leaving conflict markers in the file.
- Choosing the wrong content without checking context.

Checklist mapping:
- I) Resolve a merge conflict

Tip:
- Follow `conflict-exercise/README.md` for a safe practice conflict.
