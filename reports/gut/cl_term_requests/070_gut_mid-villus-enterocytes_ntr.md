# CL new term request: mid villus enterocyte

*Drafted from `data/hca_ontology_findings.csv` row `070_gut_mid-villus-enterocytes` — atlas: Gut, project_id: 1030 (Integrated Human Gut Cell Atlas, labelset hgca_celltype_v1, datasets 3397 "Epithelial Lineage" and 3400 "All Cells").*

**Preferred term label**
mid villus enterocyte

**Synonyms** (add reference(s), please)
- enterocyte, mid villus (related) — CAP curator synonym, project 1030

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
An enterocyte of the epithelium of the intestinal villus representing an intermediate stage along the enterocyte maturation trajectory, positioned partway up the villus. Marked by co-expression of early and late absorptive markers, including APOA1, APOC3 and ALDOB alongside ANPEP, rather than the marker profile of either extreme alone. This mixed-marker signature places it clearly in the middle of the maturation continuum, distinguishing it as a distinct intermediate state rather than a transitional artifact. Identified as a distinct transcriptomic cluster in the Human Gut Cell Atlas (CAP project 1030).

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
enterocyte of epithelium of intestinal villus (CL:1000335) — https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_1000335

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
intestinal villus (UBERON:0001213) — https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001213

**Your ORCID**
Not provided

**Additional notes or concerns**
class: new-term-requested-by-curators; interim-mapping-available; section_ref: 5a;5c.

CAP's own curator rationale (from the project 1030 OLS report, `data/2026_01_09_ols_report.csv`): "Enterocytes partway up the crypt, these display ANPEP and ALDOB alongside APOA1 and APOC3. They are placed clearly in the middle of the enterocyte maturation trajectory." CAP's own ontology assessment: "GCA supports an intermediate between early and late absorptive colonocytes and enterocytes, based on coexpression of early and late markers and middling positioning on the continuum of epithelia." Confirmed via OLS4: no existing CL term for "mid villus enterocyte"; `CL:1000335` (the proposed parent) currently has only one child, `CL:4033092` (CD57-positive enterocyte), unrelated to maturation staging.

This closely parallels another NTR from the same project, `mid crypt colonocyte` (filed as https://github.com/obophenotype/cell-ontology/issues/3778), which identifies the same intermediate-maturation pattern on the colon side rather than the small intestine. CL editors reviewing this issue may want to consider both together.

This row is one of a linked pair of actions: alongside this NTR, CAP's own mapping for this label is separately being updated from the generic parent `CL:0000584` (enterocyte) to this NTR's proposed parent `CL:1000335` (enterocyte of epithelium of intestinal villus) as a sharper interim fix, pending this new term's acceptance.

---
*Drafted by cap_tracking from `data/hca_ontology_findings.csv#070_gut_mid-villus-enterocytes`.*
