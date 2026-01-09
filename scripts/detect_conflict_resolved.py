import base64
import json
import os
import sys
import urllib.request


def api_request(url, token):
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    branch = os.environ.get("DEFAULT_BRANCH")

    if not token or not repo or not branch:
        print("false")
        return

    owner, name = repo.split("/")
    url = (
        f"https://api.github.com/repos/{owner}/{name}"
        f"/contents/conflict-exercise/RESOLUTION.txt?ref={branch}"
    )

    try:
        file_info = api_request(url, token)
    except Exception:
        print("false")
        return

    raw = base64.b64decode(file_info["content"]).decode("utf-8")
    if "Status: RESOLVED" in raw:
        print("true")
        return

    print("false")


if __name__ == "__main__":
    main()