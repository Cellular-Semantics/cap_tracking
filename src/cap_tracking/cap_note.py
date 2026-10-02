"""Render a manual CAP-website edit checklist from a CSV row.

There is no API for posting CAP ontology-mapping edits (confirmed: the
read-only cap-client package in the sibling cap_skills repo only queries
datasets/expression/DEGs/labelsets). This note is purely a human reference —
the curator edits CAP by hand, then runs `mark-cap-done`.
"""

from __future__ import annotations

import re
from pathlib import Path

from cap_tracking.slugify import slug

# Rows whose `label` describes a group of underlying CAP labels, e.g.
# "11 fibroblast labels (...)" or "5 RPE labels" or "(15 labels)".
_GROUP_COUNT_RE = re.compile(r"(\d+)\s*labels?", re.IGNORECASE)


def _group_warning(row: dict) -> str:
    label = row.get("label") or ""
    m = _GROUP_COUNT_RE.search(label)
    if m:
        return (
            f"\n**This single tracker row covers approximately {m.group(1)} underlying "
            "CAP labels** — verify every one is edited, not just the first match.\n"
        )
    if "," in label or "/" in label:
        return (
            "\n**This row's label lists multiple CAP labels** "
            f"(`{label}`) — verify every one is edited, not just the first match.\n"
        )
    return ""


def render_cap_note(row: dict) -> str:
    current = (
        f"{row['current_cl_term']} ({row['current_cl_id']})"
        if row.get("current_cl_id")
        else "(none mapped)"
    )
    proposed = (
        f"{row['proposed_cl_term']} ({row['proposed_cl_id']})"
        if row.get("proposed_cl_id")
        else (row.get("proposed_cl_term") or "(see notes)")
    )

    return f"""# CAP edit: {row['label']}

- row_id: {row['row_id']}
- atlas: {row['atlas']}
- project_id: {row['project_id']}
- dataset_ids: {row.get('dataset_ids') or '(not recorded)'}
{_group_warning(row)}
## Current CL mapping
{current}

## Proposed CL mapping
{proposed}

## Why
- class: {row.get('class') or '(not recorded)'}
- evidence: {row.get('evidence') or '(not recorded)'}
- notes: {row.get('notes') or '(none)'}
- section_ref: {row.get('section_ref') or '(none)'}

## Manual action checklist
1. Log into the CAP website.
2. Locate dataset(s) {row.get('dataset_ids') or '(see above)'} for project {row['project_id']}.
3. Locate the label(s) described above.
4. Change the ontology mapping from the current term to the proposed term (or
   apply whatever fix the notes/evidence describe, if this isn't a simple
   relabel).
5. Optionally add the evidence above as a curator comment on CAP.
6. Come back here and run: `just mark-cap-done {row['row_id']}`
"""


def cap_note_output_path(row: dict, reports_dir: Path = Path("reports")) -> Path:
    atlas_dir = slug(row["atlas"])
    return reports_dir / atlas_dir / "cap_edit_notes" / f"{row['row_id']}_cap_note.md"


def write_cap_note(row: dict, reports_dir: Path = Path("reports")) -> Path:
    out_path = cap_note_output_path(row, reports_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_cap_note(row), encoding="utf-8")
    return out_path
