# Lesson B: Clone locally

Cloning brings the repo to your machine so you can work with Git locally.

Objectives:
- Create a local working copy of your fork.
- Confirm your remotes are set correctly.

Key concepts:
- A clone is a full local copy of the repository, including its history.
- "origin" points to your fork by default.
- You can add "upstream" to track the original repo.

Steps:
1. Copy the HTTPS or SSH URL from your fork on GitHub.
2. Open a terminal in your workspace folder.
3. Run:
   - `git clone <your-fork-url>`
4. Enter the repo folder:
   - `cd github-basics-bootcamp`
5. Check remotes:
   - `git remote -v`
6. Optional (recommended): add upstream:
   - `git remote add upstream <upstream-url>`

Verify:
- `git status` shows you are on the default branch with a clean working tree.
- `git remote -v` shows `origin` (and `upstream` if added).

Common pitfalls:
- Cloning the upstream repo instead of your fork.
- Forgetting to `cd` into the repo before running Git commands.

Checklist mapping:
- B) Clone locally

Tip:
- Use the HTTPS URL if you are new to SSH.
