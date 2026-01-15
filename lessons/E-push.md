# Lesson E: Push the branch

Pushing sends your commits to GitHub so others can see them.

Objectives:
- Publish your local branch to your fork.
- Set the upstream branch for easy future pushes.

Key concepts:
- A push updates the remote branch with your local commits.
- "Upstream" tells Git which remote branch to track.

Steps:
1. Confirm your branch:
   - `git status`
2. Push the branch to your fork:
   - `git push -u origin feature/short-name`
3. On later pushes, you can use:
   - `git push`

Verify:
- The branch appears on GitHub under your fork.
- GitHub shows a banner suggesting you open a pull request.

Common pitfalls:
- Pushing to the wrong remote (check `git remote -v`).
- Forgetting `-u` the first time, which causes extra typing later.

Checklist mapping:
- E) Push the branch

Tip:
- The first push should use `-u` to set the upstream branch.
