# cap_tracking

Tracks the edits needed to fix cell-type ontology mappings across HCA (Human
Cell Atlas) datasets reviewed on CAP (Cell Annotation Platform), and makes
sure none of them get missed.

Each finding needs exactly one of:
- a **manual edit on the CAP website** (no API exists for this — tracked by
  hand), or
- a **New Term Request (NTR) issue** filed against
  [obophenotype/cell-ontology](https://github.com/obophenotype/cell-ontology), or
- **both**, or
- **no action** (already correct, or blocked pending a decision).

`data/hca_ontology_findings.csv` is the single source of truth. Everything
else in this repo is tooling around it: a CLI for the mechanical parts
(drafting, posting, status), and Claude Code skills for the judgment-call
parts (writing a CL-style definition, cleaning up a proposed label).

**Note:** `data/hca_ontology_findings.csv`, `data/hca_ontology_findings.md`,
and `data/2026_01_09_ols_report.csv` are gitignored — they live locally and
are not pushed to this repo's remote. The CLI/skills all still work against
them unchanged; only their presence in the hosted repo is removed.

## Quickstart

```sh
uv run python -m cap_tracking status      # or: just status
```

Prints every row in exactly one bucket — DONE, OUTSTANDING, NO ACTION
(skip), or NEEDS DECISION (blocked) — so nothing silently falls through the
cracks.

[`just`](https://github.com/casey/just) is optional — it's only a thin
wrapper. Every `just X` recipe below is one line of
`uv run python -m cap_tracking X`; if you don't have `just` installed, call
the `uv run` form directly.

## The CSV

21 original columns, plus one added by this repo:

- **`row_id`** — stable per-row id, `{seq}_{atlas-slug}_{label-slug}` (e.g.
  `001_trabecular-meshwork_beama`). Assigned once by `assign-ids` and never
  reassigned, so generated filenames under `reports/` never go stale. Run
  `just assign-ids` any time new rows are appended — it only fills blank
  `row_id` cells.
- **`action_route`** — one of `cap_comment`, `github_issue`, `both`, `skip`,
  `blocked`. Drives everything else.
- **`github_issue_status`** — `""` → `not_started` → `drafted` → `filed`
  (only meaningful for `github_issue`/`both` rows).
- **`comment_status`** — `""` → `not_started` → `drafted` → `done` (only
  meaningful for `cap_comment`/`both` rows).
- **`github_ticket`** — filled automatically with the created issue's URL
  once `post-ntr` succeeds.
- **`github_issue_state`** / **`closing_pr`** — GitHub's own issue state
  (`open`/`closed`) and, once resolved, the PR that closed it. Kept up to
  date by `just sync-tickets` (read-only — never posts anything).

`dataset_ids`, `n_cells`, and `label` are always treated as opaque display
strings — several rows have irregular delimiters or describe a group of
underlying CAP labels (e.g. `"11 fibroblast labels (...)"`) — never parse or
split them.

`feedback_filed` / `feedback_scope` are read-only historical context from a
separate, pre-existing feedback channel. They're surfaced in `status` output
but never drive the `comment_status`/`github_issue_status` lifecycle.

## Workflows

### GitHub NTR issues (`github_issue` / `both` rows)

```sh
just gen-ntr ROW_ID        # draft a stub under reports/{atlas}/cl_term_requests/
# → fill in the draft (see the draft-github-issue skill below) →
just preview-ntr PATH      # renders title/body, no network call
just post-ntr PATH         # posts via `gh issue create`, requires CAP_TRACKING_GH_TOKEN
                            # → writes the issue URL back into github_ticket automatically
```

Both `preview-ntr` and `post-ntr` run the draft body through
`gh_post.unwrap_paragraphs()` first — GitHub renders a bare `\n` inside an
issue as a literal `<br>`, so a paragraph hard-wrapped across multiple lines
in the source `.md` (for editor readability) would otherwise render as a
choppy forced-line-break column instead of flowing text. This reflows prose
back into one line per paragraph while leaving bold field labels, bullet
lists, and the closing `---` rule on their own lines. What you see in
`preview-ntr`'s terminal output is exactly what gets posted.

### CAP website edits (`cap_comment` / `both` rows)

```sh
just gen-cap-note ROW_ID   # draft a checklist under reports/{atlas}/cap_edit_notes/
# → edit CAP by hand →
just mark-cap-done ROW_ID  # comment_status -> done
```

### Everything else

```sh
just status                # full audit, all rows accounted for
just status-outstanding    # only what's still actionable
just sync-tickets [ROW_ID] # check filed issues' real GitHub state + closing PR
```

## Claude Code skills (`.claude/skills/`)

- **`process-findings`** — run first each session: assigns ids, validates the
  CSV, shows current status.
- **`draft-github-issue`** — turns a `gen-ntr` stub into a posting-ready NTR
  (resolves the parent term, cleans the label, writes an 80–120 word
  definition grounded only in the row's own evidence). Never posts — that
  stays a separate, explicit human step.
- **`draft-cap-comment`** — polishes a `gen-cap-note` checklist. Never marks
  it done itself — only the curator can confirm the CAP edit actually
  happened.

## GitHub token setup

`post-ntr` needs a token to authenticate `gh issue create`. One-time setup:

1. Generate a token at https://github.com/settings/tokens (classic —
   `public_repo` scope is enough, since `cell-ontology` is public) or
   https://github.com/settings/personal-access-tokens/new (fine-grained —
   scope to `obophenotype/cell-ontology`, Issues: Read and write).
2. Set it as `CAP_TRACKING_GH_TOKEN` — either in
   `.claude/settings.local.json` (already gitignored, never committed):
   ```json
   { "env": { "CAP_TRACKING_GH_TOKEN": "ghp_..." } }
   ```
   or as an ambient shell env var for the session, if you'd rather it never
   touch disk.

No `gh auth login` needed — the token is passed into the `gh` subprocess's
environment per-invocation, scoped to this one action.

**Fine-grained tokens can fail here with `Resource not accessible by
personal access token (createIssue)`** — this isn't a config mistake on your
end; organizations (including `obophenotype`) can block fine-grained-PAT
access entirely regardless of the permissions you grant, and as a
non-member you can't approve it yourself. If you hit this, switch to a
classic token with the `public_repo` scope instead — that's the mechanism
this repo's own token actually uses.

**Always `preview-ntr` before `post-ntr`.** Posting is a one-way action
against a public, third-party repo.

## Where this pattern comes from

The GitHub-issue-filing mechanism (`src/cap_tracking/gh_post.py`) is adapted
from the sibling repo `evidencell`'s `cl_post.py` + `cl-term-request.md`
workflow, which uses the same two-stage preview/confirm gate against the
same `obophenotype/cell-ontology` repo. The one deliberate difference: this
repo's `post-ntr` captures the created issue's URL and writes it back into
`github_ticket` automatically, which evidencell's version doesn't do.

## Layout

```
data/hca_ontology_findings.csv   # source of truth (gitignored, local-only)
src/cap_tracking/                # CLI + renderers (see cli.py for commands)
  gh_post.py                       # drafts -> gh issue create, URL capture, paragraph reflow
  gh_sync.py                       # read-only: real issue state + closing PR, via gh api graphql
reports/{atlas}/
  cl_term_requests/{row_id}_ntr.md       # generated NTR drafts
  cap_edit_notes/{row_id}_cap_note.md    # generated CAP edit checklists
.claude/skills/                  # the three skills above
justfile                         # thin wrapper over `uv run python -m cap_tracking ...`
```
