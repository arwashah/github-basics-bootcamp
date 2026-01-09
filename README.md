# GitHub Basics Bootcamp

Welcome to the GitHub Basics Bootcamp. This repo teaches GitHub fundamentals through hands-on tasks that you complete in your own fork. Each task automatically checks off in `PROGRESS.md` when detected by GitHub Actions.

## How this works

- You fork this repo to your personal account or an organization.
- You complete tasks in order (A through L).
- GitHub Actions detects the activity and updates `PROGRESS.md` in your fork.
- All progress is stored only in `PROGRESS.md`.

## Quick start: fork + setup

### Option 1: Fork to personal account

1) Click **Fork** on the top right of this repo.
2) Select your personal account as the destination.
3) Open the fork, then go to **Actions** and enable workflows if prompted.
4) Go to **Settings > Actions > General** and set **Workflow permissions** to **Read and write**.

### Option 2: Fork to an organization

1) Click **Fork** and choose your organization.
2) Ask an org owner to allow forking if required.
3) In the org fork, go to **Actions** and enable workflows if prompted.
4) In the org fork, go to **Settings > Actions > General**:
   - Set **Workflow permissions** to **Read and write**.
   - If the org enforces branch protection, temporarily relax it for this repo so the bot can update `PROGRESS.md` on the default branch.

### Starter Workflow

After your fork is ready, run the starter workflow to verify setup and mark the first two tasks.

1) Go to **Actions**.
2) Select **Bootcamp Starter**.
3) Click **Run workflow**.

This marks:
- A) Fork the upstream repo
- B) Clone locally (you will do this next)

## Lessons

Each task has a short lesson in the `lessons/` folder. Read them as you go.

## The bootcamp tasks (A to L)

Complete these in order. Each step includes:
- Commands to run
- What to click in GitHub
- What you should observe
- Which checkbox will be checked

---

### A) Fork the upstream repo

Commands:
- None

GitHub UI:
- Click **Fork** on the upstream repo

Observe:
- You now own a fork under your account or organization

Auto-check:
- `PROGRESS.md` item A is checked by running **Bootcamp Starter**

---

### B) Clone locally

Commands:
```bash
# Replace URL with your fork URL
git clone https://github.com/YOUR-USER-OR-ORG/github-basics-bootcamp.git
cd github-basics-bootcamp
```

GitHub UI:
- Click the **Code** button and copy the HTTPS URL

Observe:
- A new `github-basics-bootcamp` folder exists locally

Auto-check:
- `PROGRESS.md` item B is checked by running **Bootcamp Starter**

---

### C) Create a new branch

Commands:
```bash
git checkout -b feature/first-change
```

GitHub UI:
- No UI action required

Observe:
- `git status` shows you are on `feature/first-change`

Auto-check:
- `PROGRESS.md` item C is checked on the next push

---

### D) Make a commit

Commands:
```bash
# Edit any file, for example lessons/C-branch.md
# Then commit
git add lessons/C-branch.md
git commit -m "docs: update lesson C"
```

GitHub UI:
- No UI action required

Observe:
- `git log -1` shows your new commit

Auto-check:
- `PROGRESS.md` item D is checked on the next push

---

### E) Push the branch

Commands:
```bash
git push -u origin feature/first-change
```

GitHub UI:
- Go to your fork and you should see a banner suggesting a PR

Observe:
- The branch appears on GitHub

Auto-check:
- `PROGRESS.md` item E is checked on push

---

### F) Open a Pull Request

Commands:
- None

GitHub UI:
1) Click **Compare & pull request** on your fork
2) Ensure the base branch is your default branch (usually `main`)
3) Create the PR

Observe:
- The PR is open

Auto-check:
- `PROGRESS.md` item F is checked when the PR opens

---

### G) Address a review comment (simulate review)

This step requires a review from another GitHub account. Ask a friend, classmate, or use a second account to add a review with **Request changes** on your PR.

Commands:
```bash
# Make a small fix in response to the review
git add lessons/D-commit.md
git commit -m "fix: respond to review"
git push
```

GitHub UI:
1) Reviewer adds a review with **Request changes**
2) You push a follow-up commit to address it

Observe:
- The PR shows your new commit after the review

Auto-check:
- `PROGRESS.md` item G is checked when you push after a changes-requested review exists

---

### H) Merge the PR

Commands:
- None

GitHub UI:
1) On the PR page, click **Merge pull request**
2) Confirm the merge

Observe:
- The PR shows as **Merged**

Auto-check:
- `PROGRESS.md` item H is checked when the PR merges

---

### I) Resolve a merge conflict

Follow the instructions in `conflict-exercise/README.md` to create and resolve a conflict.

Commands:
- See `conflict-exercise/README.md`

GitHub UI:
- You may resolve locally or in the GitHub conflict editor

Observe:
- The conflict is resolved and merged to the default branch

Auto-check:
- `PROGRESS.md` item I is checked when `conflict-exercise/RESOLUTION.txt` is updated to `Status: RESOLVED`

---

### J) Open an Issue

Commands:
- None

GitHub UI:
1) Go to **Issues**
2) Click **New issue**
3) Add a title and description

Observe:
- The issue appears in the list

Auto-check:
- `PROGRESS.md` item J is checked when the issue opens

---

### K) Add a label to the Issue

Commands:
- None

GitHub UI:
1) Open your issue
2) In the right sidebar, click **Labels**
3) Add any label (create one if needed)

Observe:
- The label appears on the issue

Auto-check:
- `PROGRESS.md` item K is checked when the issue is labeled

---

### L) Create a release + tag

Commands:
- None

GitHub UI:
1) Go to **Releases**
2) Click **Draft a new release**
3) Create a new tag (for example `v1.0.0`)
4) Publish the release

Observe:
- The release appears in the list

Auto-check:
- `PROGRESS.md` item L is checked when the release is published

---

## Troubleshooting

Actions disabled in fork:
- Go to **Actions** and click **Enable**.

Workflow permissions insufficient:
- Go to **Settings > Actions > General** and set **Workflow permissions** to **Read and write**.

Protected branches or required reviews in org forks:
- Temporarily relax branch protection so the bot can update `PROGRESS.md` on the default branch.

Re-run workflow_dispatch:
- Go to **Actions**, select the workflow, and click **Run workflow**.

## What to do next

- Check your progress in `PROGRESS.md`.
- Use the lessons in `lessons/` if you get stuck.
- When finished, keep this fork as your personal GitHub practice repo.