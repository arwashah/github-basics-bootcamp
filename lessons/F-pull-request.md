# Lesson F: Update your certificate name

Your certificate uses the name in `certificate/profile.json`.

Objectives:
- Edit the certificate profile data.
- Practice a small change that will be committed and pushed.

Key concepts:
- `certificate/profile.json` stores your display name.
- JSON requires double quotes and commas between fields.

Steps:
1. Open `certificate/profile.json` in your editor.
2. Find the first and last name fields.
3. Replace them with your real name.
4. Save the file.
5. Check the diff:
   - `git status`
   - `git diff`
6. Commit the change:
   - `git add certificate/profile.json`
   - `git commit -m "Update certificate name"`

Verify:
- The JSON remains valid (no missing quotes or commas).
- `git log -1` shows your commit.

Common pitfalls:
- Editing the wrong file.
- Breaking JSON formatting.

Checklist mapping:
- F) Change your first and last name in certificate section

Tip:
- Use your real name so the certificate matches your profile.
