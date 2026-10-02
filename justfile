# cap_tracking — ontology-edit tracker
# Recipe style mirrors ~/Documents/GitHub/evidencell/justfile's preview/post gate.

# Setup / data hygiene
assign-ids:
    uv run python -m cap_tracking assign-ids

# GitHub NTR pipeline (github_issue / both rows)
gen-ntr ROW_ID:
    uv run python -m cap_tracking gen-ntr {{ROW_ID}}

preview-ntr NTR_FILE:
    uv run python -m cap_tracking preview-ntr {{NTR_FILE}}

# Post a drafted CL new term request as a GitHub issue against
# obophenotype/cell-ontology. Requires CAP_TRACKING_GH_TOKEN in the environment.
# Always preview with `just preview-ntr` first.
post-ntr NTR_FILE:
    uv run python -m cap_tracking post-ntr {{NTR_FILE}}

# CAP manual-edit pipeline (cap_comment / both rows)
gen-cap-note ROW_ID:
    uv run python -m cap_tracking gen-cap-note {{ROW_ID}}

mark-cap-done ROW_ID:
    uv run python -m cap_tracking mark-cap-done {{ROW_ID}}

# Check filed issues' real GitHub state (open/closed) and any closing PR.
# Read-only. Omit ROW_ID to check every row with a github_ticket set.
sync-tickets ROW_ID="":
    uv run python -m cap_tracking sync-tickets {{ROW_ID}}

# Generate a formatted .xlsx review copy: Excel Table, bold frozen header,
# columns sized to content, rows font-colored by completion status
# (green=done, amber=in progress, red=untouched, grey=skip/blocked).
export-xlsx OUT="data/hca_ontology_findings_review.xlsx":
    uv run python -m cap_tracking export-xlsx {{OUT}}

# Audit
status:
    uv run python -m cap_tracking status

status-outstanding:
    uv run python -m cap_tracking status --outstanding-only
