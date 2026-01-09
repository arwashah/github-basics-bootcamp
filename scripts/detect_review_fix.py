import json
import os
import sys
import urllib.request
from datetime import datetime, timezone


def api_request(url, token):
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    event_path = os.environ.get("GITHUB_EVENT_PATH")

    if not token or not repo or not event_path:
        print("false")
        return

    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)

    ref = event.get("ref", "")
    if not ref.startswith("refs/heads/"):
        print("false")
        return

    branch = ref.replace("refs/heads/", "")
    owner, name = repo.split("/")

    commits = event.get("commits") or []
    head_commit = event.get("head_commit") or {}
    ts = head_commit.get("timestamp")
    if not ts and commits:
        ts = commits[-1].get("timestamp")
    if not ts:
        print("false")
        return

    push_time = parse_time(ts)

    pulls_url = (
        f"https://api.github.com/repos/{owner}/{name}/pulls"
        f"?head={owner}:{branch}&state=open"
    )
    pulls = api_request(pulls_url, token)
    if not pulls:
        print("false")
        return

    pr_number = pulls[0]["number"]
    reviews_url = f"https://api.github.com/repos/{owner}/{name}/pulls/{pr_number}/reviews"
    reviews = api_request(reviews_url, token)

    for review in reviews:
        if review.get("state") == "CHANGES_REQUESTED":
            submitted = review.get("submitted_at")
            if submitted and parse_time(submitted) < push_time:
                print("true")
                return

    print("false")


if __name__ == "__main__":
    main()