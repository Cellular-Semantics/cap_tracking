---
name: process-findings
description: Data-quality gate and status check for the cap_tracking CSV. Assigns row_id to any new rows, validates action_route and status columns against the controlled vocabulary, and prints the current status report. Run this first at the start of any curation session, and whenever rows are added to data/hca_ontology_findings.csv.
---

# process-findings

Run this before touching individual rows. It makes sure the tracker CSV is in
a state the other two skills (`draft-github-issue`, `draft-cap-comment`) can
trust, and gives the curator a current picture.

## Steps

1. Run `just assign-ids`. Idempotent — only fills blank `row_id` cells, never
   touches existing ones (so filenames already generated under `reports/`
   never go stale).
2. Run `just sync-tickets`. Read-only — refreshes `github_issue_state` and
   `closing_pr` for every already-filed issue, so `status` reflects whether
   CL maintainers have actually resolved it, not just that we filed it.
3. Load `data/hca_ontology_findings.csv` and validate:
   - Every `action_route` is one of `cap_comment`, `skip`, `github_issue`,
     `blocked`, `both` (see `src/cap_tracking/schema.py:ACTION_ROUTES`).
   - Every `github_issue_status` is one of `""`, `not_started`, `drafted`,
     `filed`; every `comment_status` is one of `""`, `not_started`,
     `drafted`, `done`.
   - A status column is populated only when its route expects it:
     `comment_status` should be blank on `skip`/`blocked`/`github_issue`-only
     rows; `github_issue_status` should be blank on `skip`/`blocked`/
     `cap_comment`-only rows. Flag (don't silently fix) any row that breaks
     this — it likely means `action_route` was hand-edited without updating
     the status columns.
4. Run `just status` and show the curator the full report — this is also
   exactly what `just status` prints on its own, so this step is mostly
   "run it and make sure nothing in the DATA INTEGRITY WARNINGS section is
   new since last time."

## Do not

- Do not invent a `row_id` scheme of your own — always go through
  `just assign-ids` (`src/cap_tracking/csv_store.py:assign_missing_ids`).
- Do not reassign or renumber an existing `row_id` — it's load-bearing for
  already-generated files under `reports/`.
- Do not "fix" a data integrity warning by editing the CSV directly unless
  the curator confirms that's the right fix — report it and ask first.
