# CAP edit: BeamA

- row_id: 001_trabecular-meshwork_beama
- atlas: Trabecular meshwork
- project_id: 574
- dataset_ids: 12,411,242

## Current CL mapping
fibroblast (CL:0000057)

## Proposed CL mapping
beam A cell (CL:7770003)

## Why
- class: under-specific
- evidence: BMP5, FABP4, EDN3; CL def specifies FABP4 in humans
- notes: (none)
- section_ref: 1;3;6a

## Manual action checklist
1. Log into the CAP website.
2. Locate dataset(s) 12,411,242 for project 574.
3. Locate the label(s) described above.
4. Change the ontology mapping from the current term to the proposed term (or
   apply whatever fix the notes/evidence describe, if this isn't a simple
   relabel).
5. Optionally add the evidence above as a curator comment on CAP.
6. Come back here and run: `just mark-cap-done 001_trabecular-meshwork_beama`
