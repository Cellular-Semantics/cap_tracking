"""
Post a drafted CL new term request markdown file to the obophenotype/cell-ontology
GitHub repo as a new issue. Adapted from evidencell's `cl_post.py`.

Two-stage gate:
  1. Without --confirm, prints title + body preview and exits (the default).
  2. With --confirm, posts via `gh issue create`, using GH_TOKEN sourced from
     the CAP_TRACKING_GH_TOKEN environment variable.

Unlike evidencell's cl_post.py, this module captures the created issue's URL
from `gh issue create`'s stdout and returns it, so the caller can write it
back into the tracker CSV (`github_ticket` + `github_issue_status=filed`).

Usage:
    python -m cap_tracking.gh_post {ntr_md_file}              # preview only
    python -m cap_tracking.gh_post {ntr_md_file} --confirm    # post for real
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CL_REPO = "obophenotype/cell-ontology"
ISSUE_LABEL = "new term request"

_ISSUE_URL_RE = re.compile(
    r"^https://github\.com/obophenotype/cell-ontology/issues/\d+$"
)


_THEMATIC_BREAK_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")


def unwrap_paragraphs(text: str) -> str:
    """Collapse hard-wrapped prose into single flowing lines.

    GitHub renders a bare `\\n` inside an issue body as a literal `<br>`
    (unlike CommonMark's soft-break-as-space), so a paragraph manually
    wrapped across multiple lines for source-file readability renders as a
    choppy column of forced short lines instead of flowing text.

    Only multi-line *prose* bodies get reflowed. Left untouched: blank lines
    (block boundaries), `**bold label**` lines (kept on their own line, same
    as the template's label-then-answer layout), bullet list items (one line
    each), and standalone thematic-break lines (`---`) — joining any of
    these into the surrounding text would change the rendered structure, not
    just the wrapping.
    """
    output: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        if not buffer:
            return
        if all(line.lstrip().startswith("- ") for line in buffer):
            output.extend(buffer)
        else:
            output.append(" ".join(line.strip() for line in buffer))
        buffer.clear()

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            flush()
            output.append("")
        elif _THEMATIC_BREAK_RE.match(stripped):
            flush()
            output.append(line)
        elif stripped.startswith("**"):
            flush()
            output.append(line)
        else:
            buffer.append(line)
    flush()

    return "\n".join(output)


def split_title_body(md_text: str) -> tuple[str, str]:
    """
    First top-level `# Title` line becomes the issue title (without the `# `).
    Everything after that line is the body. Title MUST be on the first
    non-blank line; otherwise the file is rejected as malformed.
    """
    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if not line.startswith("# "):
            raise ValueError(
                f"NTR file must start with a '# Title' heading; first non-blank line was: {line!r}"
            )
        title = line[2:].strip()
        body = "\n".join(lines[i + 1 :]).lstrip("\n")
        return title, body
    raise ValueError("NTR file is empty.")


def post(ntr_path: Path, confirm: bool) -> tuple[int, str | None]:
    if not ntr_path.is_file():
        print(f"ERROR: file not found: {ntr_path}", file=sys.stderr)
        return 2, None

    title, body = split_title_body(ntr_path.read_text())
    body = unwrap_paragraphs(body)

    print(f"Repo:   {CL_REPO}")
    print(f"Label:  {ISSUE_LABEL}")
    print(f"Title:  {title}")
    print("Body preview (first 40 lines):")
    print("─" * 60)
    for line in body.splitlines()[:40]:
        print(line)
    print("─" * 60)

    if not confirm:
        print()
        print("Preview only. To post this issue, run: just post-ntr " + str(ntr_path))
        return 0, None

    if shutil.which("gh") is None:
        print("ERROR: `gh` CLI not found on PATH.", file=sys.stderr)
        return 3, None

    token = os.environ.get("CAP_TRACKING_GH_TOKEN")
    if not token:
        print(
            "ERROR: CAP_TRACKING_GH_TOKEN is not set in the environment. "
            "Configure it via .claude/settings.local.json or your shell.",
            file=sys.stderr,
        )
        return 4, None

    env = os.environ.copy()
    env["GH_TOKEN"] = token

    cmd = [
        "gh", "issue", "create",
        "--repo", CL_REPO,
        "--title", title,
        "--body", body,
        "--label", ISSUE_LABEL,
    ]
    print(f"Posting to {CL_REPO}…")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(result.stdout, end="")
    print(result.stderr, end="", file=sys.stderr)

    if result.returncode != 0:
        return result.returncode, None

    issue_url = None
    for line in reversed(result.stdout.splitlines()):
        line = line.strip()
        if line and _ISSUE_URL_RE.match(line):
            issue_url = line
            break

    if issue_url is None:
        print(
            "ERROR: `gh issue create` exited 0 but no recognizable issue URL was "
            "found in its output. Treating this as a failed post — check the "
            "repo manually before retrying.",
            file=sys.stderr,
        )
        return 5, None

    return 0, issue_url


def row_id_from_ntr_path(ntr_path: Path) -> str:
    name = ntr_path.name
    if not name.endswith("_ntr.md"):
        raise ValueError(f"Expected an NTR filename ending in '_ntr.md', got: {name!r}")
    return name[: -len("_ntr.md")]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ntr_path", type=Path, help="Path to NTR markdown file")
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Actually post the issue. Without this flag, prints a preview only.",
    )
    args = parser.parse_args(argv)
    returncode, issue_url = post(args.ntr_path, args.confirm)
    if issue_url:
        print(f"\nIssue created: {issue_url}")
    return returncode


if __name__ == "__main__":
    sys.exit(main())
