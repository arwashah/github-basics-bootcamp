# GitHub Basics Bootcamp

Welcome to the GitHub Basics Bootcamp. This repo teaches GitHub fundamentals through hands-on tasks that you complete in your own fork. Track completion by checking off items manually in `PROGRESS.md`.

## How this works

- You fork this repo to your personal account or an organization.
- You complete tasks in order (A through L).
- You manually check off each task in `PROGRESS.md`.

## Quick start: fork + setup

### Option 1: Fork to personal account

1) Click **Fork** on the top right of this repo.
2) Select your personal account as the destination.
3) Set the fork visibility to **Public** (this is required for the bootcamp).

### Option 2: Fork to an organization

1) Click **Fork** and choose your organization.
2) Set the fork visibility to **Public** (this is required for the bootcamp).
3) Ask an org owner to allow forking if required.

## Lessons

Each task has a short lesson in the `lessons/` folder. Read them as you go.

## Folder guide

Use this as a map while you work through the tasks.

- `lessons/` - Short explanations for each task (A-L). Open the matching lesson right before you do that step.
- `conflict-exercise/` - Files used only for the merge conflict practice (task I). Open this folder when you reach the conflict step.
- `PROGRESS.md` - Your checklist. Check this after each task to record completion.

## The bootcamp tasks (A to L)

Complete these in order. Each step includes:
- Commands to run
- What to click in GitHub
- What you should observe
- Which checkbox to check manually

---

### A) Fork the upstream repo

Commands:
- None

GitHub UI:
- Click **Fork** on the upstream repo

Observe:
- You now own a fork under your account or organization

Manual check:
- Check off item A in `PROGRESS.md`

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

Manual check:
- Check off item B in `PROGRESS.md`

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

Manual check:
- Check off item C in `PROGRESS.md`

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

Manual check:
- Check off item D in `PROGRESS.md`

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

Manual check:
- Check off item E in `PROGRESS.md`

---

### F) Change your first and last name in certificate section

Update the certificate profile so your name appears in the certificate assets.

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

Manual check:
- Check off item F in `PROGRESS.md`

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

Manual check:
- Check off item G in `PROGRESS.md`

---

### H) Merge the PR

Commands:
- None

GitHub UI:
1) On the PR page, click **Merge pull request**
2) Confirm the merge

Observe:
- The PR shows as **Merged**

Manual check:
- Check off item H in `PROGRESS.md`

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

Manual check:
- Check off item I in `PROGRESS.md`

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

Manual check:
- Check off item J in `PROGRESS.md`

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

Manual check:
- Check off item K in `PROGRESS.md`

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

Manual check:
- Check off item L in `PROGRESS.md`

---

## Certificate (manual)

This repo includes certificate assets, but it does not auto-generate a PDF.
If you want to personalize the certificate data:
1) Open `certificate/profile.json`
2) Replace `FIRST` and `LAST` with your real name
3) Commit and push the change

## What to do next

- Check off your progress in `PROGRESS.md`.
- Use the lessons in `lessons/` if you get stuck.
- When finished, keep this fork as your personal GitHub practice repo.
