# CL new term request: enterocyte progenitor

*Drafted from `data/hca_ontology_findings.csv` row `069_gut_enterocyte-progenitors` — atlas: Gut, project_id: 1030 (Integrated Human Gut Cell Atlas, labelset hgca_celltype_v1, datasets 3397 "Epithelial Lineage" and 3400 "All Cells").*

**Preferred term label**
enterocyte progenitor

**Synonyms** (add reference(s), please)
- absorptive progenitor (related) — CAP curator synonym, project 1030
- absorptive TA (broad) — CAP curator synonym, project 1030; reflects overlap with the transit-amplifying compartment rather than exact equivalence

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
An early enterocyte of the human small intestine that retains residual proliferative activity, expressing PCNA and HELLS alongside early absorptive markers OLFM4, ADH1C, REG1A and LCN2, without having completed the transition to full early-enterocyte maturation. Many cells in this population are ribosomal-high, making them difficult to cleanly separate from the cycling transit-amplifying compartment on one side and mature early enterocytes on the other. Positioned between the transit-amplifying zone and early enterocyte along the crypt-villus differentiation axis, representing a distinct transitional state rather than either compartment alone.

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
early enterocyte (CL:4047019) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4047019

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
small intestine (UBERON:0002108) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002108

**Your ORCID**
Not provided

**Additional notes or concerns**
class: new-term-requested-by-curators; section_ref: 5a.

CAP's own curator rationale (from the project 1030 OLS report, `data/2026_01_09_ols_report.csv`): "These sit between the TA compartment and early enterocytes, with OLFM4, ADH1C, REG1A and LCN2 still up alongside a bit of leftover proliferation like PCNA and HELLS, and a lot of them are ribosomal-high which makes them hard to pull cleanly apart from cycling TA and early enterocytes so we annotate them as absorptive progenitors where the absorptive markers were coming up but maturation hadn't really kicked in yet." CAP's own ontology assessment: "No specific CL term for enterocyte progenitors - we separate these from early enterocytes to provide more resolution on epithelial subtypes." Confirmed via OLS4 search: no existing CL term for "enterocyte progenitor"; `CL:0009012` (transit amplifying cell of small intestine) exists but is a distinct, broader multipotent compartment rather than this specific absorptive-lineage-biased state.

This closely parallels another NTR from the same project, `colonocyte progenitor` (filed as https://github.com/obophenotype/cell-ontology/issues/3775), which identifies the same intermediate-progenitor pattern on the colon side of the epithelium rather than the small intestine. CL editors reviewing this issue may want to consider both together. CAP's current mapping for this label is the parent `CL:4047019` (early enterocyte); this NTR does not propose changing that mapping, only adding a more specific child term.

---
*Drafted by cap_tracking from `data/hca_ontology_findings.csv#069_gut_enterocyte-progenitors`.*
