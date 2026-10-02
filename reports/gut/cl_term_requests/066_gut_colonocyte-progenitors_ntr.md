# CL new term request: colonocyte progenitor

*Drafted from `data/hca_ontology_findings.csv` row `066_gut_colonocyte-progenitors` — atlas: Gut, project_id: 1030 (Integrated Human Gut Cell Atlas, labelset hgca_celltype_v1, datasets 3397 "Epithelial Lineage" and 3400 "All Cells").*

**Preferred term label**
colonocyte progenitor

**Synonyms** (add reference(s), please)
- absorptive progenitor (related) — CAP curator synonym, project 1030
- colonocyte early progenitor (related) — CAP curator synonym, project 1030

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
An early colonocyte of the human colon that retains residual proliferative
activity and has not yet acquired the surface maturation markers (e.g.
AQP8) characteristic of fully differentiated colonocytes. These cells are
committed to the absorptive colonocyte lineage rather than being
multipotent transit-amplifying cells, and are marked by expression of
NOTCH1 and EDN1. Identified as a distinct transcriptomic cluster in the
Human Gut Cell Atlas (CAP project 1030).

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
early colonocyte (CL:4047018) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_4047018

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
colon (UBERON:0001155) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001155

**Your ORCID**
Not provided

**Additional notes or concerns**
class: new-term-requested-by-curators; section_ref: 5a.

CAP's own curator rationale (from the project 1030 OLS report,
`data/2026_01_09_ols_report.csv`): "Absorptive colonic progenitors, NOTCH1
and EDN1 with some residual cycling, committed towards the colonocyte
lineage but not yet showing surface maturation like AQP8. There isn't a
colonocyte progenitor term so these map to early colonocyte." CAP's current
interim mapping for this label is CL:4047018 (early colonocyte) — this NTR
requests a more specific child term for the distinct progenitor/cycling
state, it does not propose changing that interim mapping.

We considered CL:0009011 "transit amplifying cell of colon" as an
alternative parent, but rejected it: that term describes a multipotent
proliferative precursor (colonocyte/goblet/enteroendocrine/tuft), whereas
this label's own rationale describes a population already committed
specifically to the colonocyte lineage with only *residual* cycling —
closer to CL:4047018's lineage-committed, differentiating character than to
the multipotent transit-amplifying compartment.

---
*Drafted by cap_tracking from `data/hca_ontology_findings.csv#066_gut_colonocyte-progenitors`. Review before posting — in particular, add your ORCID.*
