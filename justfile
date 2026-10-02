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

# Audit
status:
    uv run python -m cap_tracking status

status-outstanding:
    uv run python -m cap_tracking status --outstanding-only
