# Conflict Exercise

This exercise creates a safe merge conflict so you can practice resolving it.

## Goal

Create conflicting changes to `conflict-exercise/CONFLICT.txt`, resolve them, and merge into the default branch. Then update `conflict-exercise/RESOLUTION.txt` to mark completion.

## Steps

1) Start from the default branch.

```bash
git checkout main
```

2) Create a new branch for the conflict.

```bash
git checkout -b conflict-exercise
```

3) Edit `conflict-exercise/CONFLICT.txt` and change the line:

```
COLOR=BLUE
```

to:

```
COLOR=GREEN
```

Commit and push:

```bash
git add conflict-exercise/CONFLICT.txt
git commit -m "conflict: set color to green"
git push -u origin conflict-exercise
```

4) Switch back to `main` and make a conflicting change.

```bash
git checkout main
```

Change the same line in `conflict-exercise/CONFLICT.txt` to:

```
COLOR=RED
```

Commit and push:

```bash
git add conflict-exercise/CONFLICT.txt
git commit -m "conflict: set color to red"
git push
```

5) Merge the conflict branch and resolve the conflict.

```bash
git merge conflict-exercise
```

Resolve the conflict by choosing one color and keeping the file valid. Then:

```bash
git add conflict-exercise/CONFLICT.txt
git commit -m "conflict: resolve"
git push
```

6) Mark the resolution by editing `conflict-exercise/RESOLUTION.txt`:

```
Status: RESOLVED
```

Commit and push:

```bash
git add conflict-exercise/RESOLUTION.txt
git commit -m "conflict: mark resolved"
git push
```

## Auto-check

`PROGRESS.md` item I is checked when `conflict-exercise/RESOLUTION.txt` contains `Status: RESOLVED` on the default branch.