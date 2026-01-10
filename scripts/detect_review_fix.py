import json
import os
import sys

TARGET_PATH = "certificate/profile.json"


def has_profile_change(event):
    commits = event.get("commits") or []
    for commit in commits:
        for key in ("added", "modified", "removed"):
            for path in commit.get(key, []):
                if path == TARGET_PATH:
                    return True
    return False


def main():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("false")
        return

    try:
        with open(event_path, "r", encoding="utf-8") as handle:
            event = json.load(handle)
    except OSError:
        print("false")
        return

    print("true" if has_profile_change(event) else "false")


if __name__ == "__main__":
    main()