"""Render a stub Cell Ontology New Term Request (NTR) markdown file from a CSV row.

Mirrors the field set of obophenotype/cell-ontology's `a_adding_term.md` issue
template and the title convention used by evidencell's cl-term-request workflow
(`# CL new term request: {label}`). This renderer is deliberately mechanical —
it never invents a cleaned-up label, a definition, synonyms, or anatomy; those
are judgment calls left to the draft-github-issue skill, which reads and
overwrites this stub in place.
"""

from __future__ import annotations

from pathlib import Path

from cap_tracking.slugify import slug

NEEDS_INPUT = "[NEEDS CURATOR INPUT]"


def render_ntr_stub(row: dict) -> str:
    if row["current_cl_id"] and row["current_cl_term"]:
        parent_line = f"{row['current_cl_term']} ({row['current_cl_id']})"
    else:
        parent_line = (
            "[parent term required — no current_cl_id/current_cl_term on this row; "
            "look up a plausible parent on OLS4 before drafting further]"
        )

    notes_parts = [
        p
        for p in [
            f"class: {row['class']}" if row.get("class") else "",
            f"section_ref: {row['section_ref']}" if row.get("section_ref") else "",
            row.get("notes") or "",
        ]
        if p
    ]
    notes_block = "\n".join(notes_parts) if notes_parts else NEEDS_INPUT

    return f"""# CL new term request: {row['label']}

*Drafted from `data/hca_ontology_findings.csv` row `{row['row_id']}` — atlas: {row['atlas']}, project_id: {row['project_id']}.*

**Preferred term label**
{NEEDS_INPUT}
RAW proposed_cl_term (needs cleanup): {row.get('proposed_cl_term') or NEEDS_INPUT}

**Synonyms** (add reference(s), please)
{NEEDS_INPUT}

**Definition** (free text, with reference(s), please. PubMed ID format is PMID:XXXXXX)
{NEEDS_INPUT}
Evidence from CAP review: {row.get('evidence') or '(none recorded)'}

**Parent cell type term** (check the hierarchy here https://www.ebi.ac.uk/ols4/ontologies/cl)
{parent_line}

**Anatomical structure where the cell type is found** (check Uberon for anatomical structures: https://www.ebi.ac.uk/ols4/ontologies/uberon)
{NEEDS_INPUT}

**Your ORCID**
{NEEDS_INPUT}

**Additional notes or concerns**
{notes_block}

---
*Drafted by cap_tracking from `data/hca_ontology_findings.csv#{row['row_id']}`. Review and fill in every {NEEDS_INPUT} before posting.*
"""


def ntr_output_path(row: dict, reports_dir: Path = Path("reports")) -> Path:
    atlas_dir = slug(row["atlas"])
    return reports_dir / atlas_dir / "cl_term_requests" / f"{row['row_id']}_ntr.md"


def write_ntr_draft(row: dict, reports_dir: Path = Path("reports")) -> Path:
    out_path = ntr_output_path(row, reports_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_ntr_stub(row), encoding="utf-8")
    return out_path
