---
name: draft-cap-comment
description: Draft a manual CAP-website edit note from a cap_tracking row whose action_route is cap_comment or both. There is no API for posting CAP ontology-mapping edits, so this produces a human checklist the curator follows by hand, then marks the row done.
---

# draft-cap-comment

Turns one row of `data/hca_ontology_findings.csv` into a checklist for a
manual edit on the CAP website. Confirmed: the `cap-client` package in the
sibling `cap_skills` repo is read-only (datasets/expression/DEGs/labelsets
queries only) — there is no API path for posting an ontology-mapping edit, so
this is deliberately a manual, human-in-the-loop step, not an automation gap
to close.

## Run parameters

```
ROW_ID   # required — e.g. 001_trabecular-meshwork_beama
```

The row must have `action_route` of `cap_comment` or `both` — `gen-cap-note`
refuses otherwise.

## Step 1 — Generate the note

```
just gen-cap-note {ROW_ID}
```

Writes `reports/{atlas_slug}/cap_edit_notes/{ROW_ID}_cap_note.md` (current ->
proposed mapping, evidence, notes, a manual action checklist) and flips
`comment_status: not_started -> drafted`.

## Step 2 — Light polish only

The note is already mechanical — current/proposed mapping, evidence, and
notes are pulled straight from the CSV. Polish prose for clarity if useful,
but introduce no new facts beyond what's in the row. If the row's `label`
describes a group (e.g. `"5 RPE labels"`, `"11 fibroblast labels..."`), the
generated note already carries an explicit warning with the label count —
don't remove it.

## Step 3 — Remind the curator this is manual

There is no CAP API to verify against. The curator needs to:
1. Log into CAP.
2. Find the dataset(s)/label(s) described in the note.
3. Apply the mapping change (or whatever fix the evidence/notes describe).
4. Optionally leave the evidence as a CAP curator comment.

## Step 4 — After the edit is made

The curator runs `just mark-cap-done {ROW_ID}` themselves once the CAP edit
is actually done — this skill does not call that command on their behalf,
since only the curator can confirm the website edit actually happened.
