---
name: draft-github-issue
description: Draft a Cell Ontology (CL) New Term Request from a cap_tracking row whose action_route is github_issue or both. Reads the row's current/proposed mapping and evidence, applies CL's definition and naming conventions, and fills in the NTR stub so it's ready for human review and posting. Posting to the CL repo is a separate gated step this skill never performs.
---

# draft-github-issue

Turns one row of `data/hca_ontology_findings.csv` into a posting-ready Cell
Ontology New Term Request. Mirrors the judgment-call steps of
`~/Documents/GitHub/evidencell/workflows/cl-term-request.md`, sourced from the
CSV instead of a KB YAML graph.

## Run parameters

```
ROW_ID   # required — e.g. 007_optic-nerve_fibro-dura
```

The row must have `action_route` of `github_issue` or `both` — `gen-ntr`
refuses otherwise.

## Step 1 — Generate the stub

```
just gen-ntr {ROW_ID}
```

Writes `reports/{atlas_slug}/cl_term_requests/{ROW_ID}_ntr.md` (mechanical
fields only: current CL mapping as parent, raw `proposed_cl_term`, evidence,
notes) and flips `github_issue_status: not_started -> drafted`. Read the
stub — every `[NEEDS CURATOR INPUT]` placeholder is yours to fill below.

## Step 2 — Resolve the parent term

If the stub shows `[parent term required — no current_cl_id/current_cl_term
on this row ...]`, look up a plausible parent on OLS4
(https://www.ebi.ac.uk/ols4/ontologies/cl, or `mcp__ols4__searchClasses` if
available) before drafting further. Never leave this placeholder in the
version you hand to the curator for posting — either fill it with a found
parent term, or explicitly flag in "Additional notes" that no good parent
was found and the curator needs to pick one.

## Step 3 — Clean the preferred label

The stub quotes the raw `proposed_cl_term` verbatim under "RAW proposed_cl_term
(needs cleanup)" because many of this CSV's values embed commentary, e.g.
`"dura fibroblast (new; CL:1000298 is mesothelial, not fibroblast)"` or
`"split into L (CL:0003048) + M (CL:0003049), or map to parent cone
photoreceptor cell"`. Extract the actual candidate label and write it as the
**Preferred term label**, following CL convention:
- Lowercase except proper nouns.
- Include anatomical/species context only when it distinguishes the term.
- No atlas-specific jargon, cluster IDs, or abbreviations.

## Step 4 — Write the definition (80-120 words, single paragraph)

Same rules as evidencell's CL definition guidelines:
1. Do not name the cell type being defined — start from the parent class and
   describe distinguishing features.
2. Ground every claim in the row's `evidence`/`notes` fields. This CSV's
   evidence is almost always marker-gene lists or CAP's own assessment
   prose, rarely a literature citation — that's fine; cite marker genes and
   `CAP project {project_id}` as provenance. **Never invent a PMID or DOI
   that isn't actually in the row's data.**
3. Mention markers only if defining; specify species when relevant.
4. 80-120 words.

## Step 5 — Synonyms and anatomy

Fill from `label`/`notes` if a synonym is implied, and look up the
anatomical structure (UBERON) via OLS4 if the atlas/notes name one. If
nothing is available, write `[not available]` explicitly rather than
guessing.

## Step 6 — Overwrite and stop

Overwrite the same stub file in place with your filled-in version. Then
print the review summary and stop — do **not** post from this skill:

```
NTR draft ready: reports/{atlas_slug}/cl_term_requests/{ROW_ID}_ntr.md

Review the draft, then:
  just preview-ntr reports/{atlas_slug}/cl_term_requests/{ROW_ID}_ntr.md
  just post-ntr    reports/{atlas_slug}/cl_term_requests/{ROW_ID}_ntr.md
(posting uses CAP_TRACKING_GH_TOKEN; requires the curator's explicit go-ahead)
```

`post-ntr` captures the created issue's URL and writes it back into the CSV
(`github_ticket`, `github_issue_status=filed`) automatically — no manual
bookkeeping step needed after a successful post.

## Quality rules

1. Definition follows the guidelines exactly — parent class first, never
   self-naming, 80-120 words.
2. Every fact is grounded in the row's own `evidence`/`notes`. If something
   needed is missing, say so in the draft rather than inventing it.
3. A missing axiom/synonym/anatomy entry is fine; a wrong one is harmful.
4. The markdown file is the deliverable — no JSON intermediate.
