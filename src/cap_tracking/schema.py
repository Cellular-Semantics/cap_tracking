"""Column list and controlled vocabulary for the tracker CSV."""

from __future__ import annotations

FIELDNAMES = [
    "row_id",
    "atlas",
    "project_id",
    "dataset_ids",
    "label",
    "n_cells",
    "current_cl_id",
    "current_cl_term",
    "proposed_cl_id",
    "proposed_cl_term",
    "class",
    "action_route",
    "issue_template",
    "github_issue_status",
    "comment_status",
    "evidence",
    "source_tags",
    "feedback_filed",
    "feedback_scope",
    "section_ref",
    "notes",
    "github_ticket",
]

ACTION_ROUTES = {"cap_comment", "skip", "github_issue", "blocked", "both"}

GITHUB_ISSUE_STATUS = {"", "not_started", "drafted", "filed"}
COMMENT_STATUS = {"", "not_started", "drafted", "done"}

# action_route values that require a GitHub NTR issue
GITHUB_ROUTES = {"github_issue", "both"}
# action_route values that require a manual CAP-website edit
CAP_ROUTES = {"cap_comment", "both"}
