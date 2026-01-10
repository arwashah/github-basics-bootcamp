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
3) Set the fork visibility to **Public** (this is required for the bootcamp).
4) Open the fork, then go to **Actions** and enable workflows if prompted.
5) Go to **Settings > Actions > General** and set **Workflow permissions** to **Read and write**.

### Option 2: Fork to an organization

1) Click **Fork** and choose your organization.
2) Set the fork visibility to **Public** (this is required for the bootcamp).
3) Ask an org owner to allow forking if required.
4) In the org fork, go to **Actions** and enable workflows if prompted.
5) In the org fork, go to **Settings > Actions > General**:
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

## Folder guide

Use this as a map while you work through the tasks.

- `lessons/` — Short explanations for each task (A–L). Open the matching lesson right before you do that step.
- `conflict-exercise/` — Files used only for the merge conflict practice (task I). Open this folder when you reach the conflict step.
- `scripts/` — Automation used by the bootcamp to detect progress. You do not need to edit or run these.
- `.github/` — GitHub Actions workflows that update `PROGRESS.md`. You do not need to edit these.
- `PROGRESS.md` — Your checklist. Check this after each task to confirm it was recorded.

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

GitHub Desktop:
- On your fork, click **Code** > **Open with GitHub Desktop** (or use **File > Clone repository** in the app)
- Choose a local path and click **Clone**

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

GitHub Desktop:
- Click **Current Branch** > **New Branch**
- Name it `feature/first-change` and create it

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

GitHub Desktop:
- Edit a file (for example `lessons/C-branch.md`)
- In GitHub Desktop, select the change, add a commit message, and click **Commit to feature/first-change**

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

GitHub Desktop:
- Click **Push origin** in the top bar

GitHub UI:
- Go to your fork and you should see a banner suggesting a PR

Observe:
- The branch appears on GitHub

Auto-check:
- `PROGRESS.md` item E is checked on push

---

### F) Change your first and last name in certificate section

Update the certificate profile so your name appears on the final PDF.

Commands:
```bash
# Edit certificate/profile.json and replace FIRST/LAST with your name
git add certificate/profile.json
git commit -m "docs: add certificate name"
git push
```

GitHub Desktop:
- Edit `certificate/profile.json` and replace `FIRST` and `LAST`
- In GitHub Desktop, add a commit message and click **Commit to feature/first-change**
- Click **Push origin**

GitHub UI:
- No UI action required

Observe:
- Your changes to `certificate/profile.json` are pushed to the branch

Auto-check:
- `PROGRESS.md` item F is checked when the change is pushed

---

### G) Open a Pull Request

Commands:
- None

GitHub UI:
1) Click **Compare & pull request** on your fork
2) Ensure the base branch is your default branch (usually `main`)
3) Create the PR

Observe:
- The PR is open

Auto-check:
- `PROGRESS.md` item G is checked when the PR opens

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

GitHub Desktop:
- Follow `conflict-exercise/README.md` for the edits
- When GitHub Desktop shows a conflict, open in your editor, fix it, mark as resolved, then commit and push

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

## Certificate (auto-generated)

After all tasks A-L are complete, a GitHub Action generates a PDF certificate
and commits it to your fork.

Setup (one time):
1) Open `certificate/profile.json`
2) Replace `FIRST` and `LAST` with your real name
3) Commit and push the change

Notes:
- The certificate includes your GitHub username, your name, and the completion date (UTC).
- You can re-run the **Generate Certificate** workflow from Actions to regenerate it.

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
