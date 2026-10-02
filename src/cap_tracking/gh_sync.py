"""Read-only sync of a filed issue's actual GitHub state (open/closed) and,
once resolved, the PR that closed it. Never posts or modifies anything on
GitHub — only `gh api graphql` reads.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys

_ISSUE_URL_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/issues/(?P<number>\d+)$"
)

_QUERY = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    issue(number: $number) {
      state
      closedByPullRequestsReferences(first: 5) {
        nodes { number url state merged }
      }
    }
  }
}
"""


def parse_issue_url(url: str) -> tuple[str, str, int]:
    m = _ISSUE_URL_RE.match(url.strip())
    if not m:
        raise ValueError(f"Not a recognizable GitHub issue URL: {url!r}")
    return m["owner"], m["repo"], int(m["number"])


def fetch_issue_state(github_ticket: str) -> dict:
    """Returns {"github_issue_state": "open"|"closed", "closing_pr": url-or-""}."""
    owner, repo, number = parse_issue_url(github_ticket)

    token = os.environ.get("CAP_TRACKING_GH_TOKEN")
    env = os.environ.copy()
    if token:
        env["GH_TOKEN"] = token

    cmd = [
        "gh", "api", "graphql",
        "-f", f"query={_QUERY}",
        "-f", f"owner={owner}",
        "-f", f"name={repo}",
        "-F", f"number={number}",
    ]
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR checking {github_ticket}: {result.stderr.strip()}", file=sys.stderr)
        return {}

    data = json.loads(result.stdout)
    issue = data["data"]["repository"]["issue"]
    state = issue["state"].lower()  # "OPEN" / "CLOSED" -> "open" / "closed"

    closing_pr = ""
    for pr in issue["closedByPullRequestsReferences"]["nodes"]:
        if pr.get("merged"):
            closing_pr = pr["url"]
            break
    else:
        nodes = issue["closedByPullRequestsReferences"]["nodes"]
        if nodes:
            closing_pr = nodes[0]["url"]

    return {"github_issue_state": state, "closing_pr": closing_pr}
