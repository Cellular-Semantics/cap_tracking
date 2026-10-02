# CL new term request: mid crypt colonocyte

*Drafted from `data/hca_ontology_findings.csv` row `068_gut_mid-crypt-colonocytes` — atlas: Gut, project_id: 1030 (Integrated Human Gut Cell Atlas, labelset hgca_celltype_v1, datasets 3397 "Epithelial Lineage" and 3400 "All Cells").*

**Preferred term label**
mid crypt colonocyte

**Synonyms** (add reference(s), please)
- colonocyte, mid crypt (related) — CAP curator synonym, project 1030
- intermediate colonocyte (related) — from CAP's ontology assessment wording

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
A colonocyte of the human colon representing an intermediate stage along the crypt-to-surface maturation trajectory, positioned partway up the crypt between early colonocyte (CL:4047018) and the most differentiated crypt-top colonocytes. Marked by co-expression of early and late colonocyte markers, including CEACAM5, LEFTY1, ADH1C, SPINK5 and AQP8 alongside PIGR, MUC1 and MUC4, rather than the marker profile of either extreme alone. This mixed-marker signature distinguishes it as a distinct maturation state rather than a transitional artifact. Identified as a distinct transcriptomic cluster in the Human Gut Cell Atlas (CAP project 1030).

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
colonocyte (CL:1000347) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_1000347

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
colon (UBERON:0001155) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001155

**Your ORCID**
Not provided

**Additional notes or concerns**
class: new-term-requested-by-curators; section_ref: 5a.

CAP's own curator rationale (from the project 1030 OLS report, `data/2026_01_09_ols_report.csv`): "Colonocytes partway up the crypt, these display CEACAM5, CA2 and AQP8 alongside PIGR, MUC1 and MUC4. They are placed clearly in the middle of the colonocyte maturation trajectory." CAP's own ontology assessment: "GCA supports an intermediate between early and late absorptive colonocytes and enterocytes, based on coexpression of early and late markers and middling positioning on the continuum of epithelia." Confirmed via OLS4 search: no existing CL term for "mid crypt colonocyte" or "intermediate colonocyte".

This request is closely related to two other NTRs from the same project: `early colonocyte` (CL:4047018, already in CL) marks the start of this maturation axis, and a request for `crypt top colonocyte` (the opposite, most-mature end) was filed separately as https://github.com/obophenotype/cell-ontology/issues/3776 — CL editors reviewing this issue may want to consider all three as a set. CAP's current mapping for this label is the general parent `CL:1000347` (colonocyte); this NTR does not propose changing that mapping, only adding a more specific child term.

---
*Drafted by cap_tracking from `data/hca_ontology_findings.csv#068_gut_mid-crypt-colonocytes`.*
