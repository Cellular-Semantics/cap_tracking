# CAP edit: Mid Villus Enterocytes

- row_id: 070_gut_mid-villus-enterocytes
- atlas: Gut
- project_id: 1030
- dataset_ids: (not recorded)

## Current CL mapping
enterocyte (CL:0000584)

## Proposed CL mapping
enterocyte of epithelium of intestinal villus (CL:1000335)

## Why
- class: new-term-requested-by-curators; interim-mapping-available
- evidence: no mid-villus/zonation term exists, but a strictly-more-specific term than enterocyte is usable today without asserting zonation
- notes: curator claim correct; §5c gives sharper interim mapping
- section_ref: 5a;5c

## Manual action checklist
1. Log into the CAP website.
2. Locate dataset(s) (see above) for project 1030.
3. Locate the label(s) described above.
4. Change the ontology mapping from the current term to the proposed term (or
   apply whatever fix the notes/evidence describe, if this isn't a simple
   relabel).
5. Optionally add the evidence above as a curator comment on CAP.
6. Come back here and run: `just mark-cap-done 070_gut_mid-villus-enterocytes`

**Note:** CL:1000335 is an interim fix only — it's more specific than plain
`enterocyte` but doesn't assert the mid-villus zonation this label actually
represents, because no CL term for that exists yet. A separate NTR for
`mid villus enterocyte` (parented under CL:1000335) is being filed alongside
this edit — see `reports/gut/cl_term_requests/070_gut_mid-villus-enterocytes_ntr.md`.
If/when that term is accepted into CL, this mapping should be revisited.
