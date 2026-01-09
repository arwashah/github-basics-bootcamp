import base64
import json
import os
import re
import sys
import urllib.request


def api_request(method, url, token, data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", str(len(body)))
    else:
        body = None
    with urllib.request.urlopen(req, data=body) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_tasks(arg):
    tasks = []
    for part in arg.split(","):
        t = part.strip().upper()
        if t:
            tasks.append(t)
    return tasks


def update_progress(content, tasks):
    changed = False
    for task in tasks:
        pattern = rf"^- \[( |x)\] {re.escape(task)}\."
        def repl(match):
            nonlocal changed
            if match.group(1) != "x":
                changed = True
            return f"- [x] {task}."
        content, _ = re.subn(pattern, repl, content, flags=re.MULTILINE)
    return content, changed


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Missing GITHUB_TOKEN or GITHUB_REPOSITORY", file=sys.stderr)
        sys.exit(1)

    tasks_arg = None
    branch = None
    for i, arg in enumerate(sys.argv):
        if arg == "--tasks" and i + 1 < len(sys.argv):
            tasks_arg = sys.argv[i + 1]
        if arg == "--branch" and i + 1 < len(sys.argv):
            branch = sys.argv[i + 1]

    if not tasks_arg:
        print("--tasks is required", file=sys.stderr)
        sys.exit(1)

    tasks = parse_tasks(tasks_arg)
    if not tasks:
        print("No tasks provided", file=sys.stderr)
        sys.exit(1)

    if not branch:
        branch = "main"

    owner, name = repo.split("/")
    api_base = f"https://api.github.com/repos/{owner}/{name}"

    file_info = api_request(
        "GET",
        f"{api_base}/contents/PROGRESS.md?ref={branch}",
        token,
    )

    raw = base64.b64decode(file_info["content"]).decode("utf-8")
    updated, changed = update_progress(raw, tasks)

    if not changed:
        print("No changes needed")
        return

    message = f"chore: update PROGRESS ({', '.join(tasks)})"

    payload = {
        "message": message,
        "content": base64.b64encode(updated.encode("utf-8")).decode("utf-8"),
        "sha": file_info["sha"],
        "branch": branch,
    }

    api_request(
        "PUT",
        f"{api_base}/contents/PROGRESS.md",
        token,
        payload,
    )

    print("Updated PROGRESS.md")


if __name__ == "__main__":
    main()