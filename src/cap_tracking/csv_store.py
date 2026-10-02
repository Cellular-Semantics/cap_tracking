"""Load/save the tracker CSV. The CSV is the single source of truth."""

from __future__ import annotations

import csv
import os
import re
from pathlib import Path

from cap_tracking.schema import FIELDNAMES
from cap_tracking.slugify import slug

DEFAULT_CSV_PATH = Path("data/hca_ontology_findings.csv")

_ROW_ID_SEQ_RE = re.compile(r"^(\d+)_")


def load_rows(path: Path = DEFAULT_CSV_PATH) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(rows: list[dict], path: Path = DEFAULT_CSV_PATH) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, path)


def get_row(rows: list[dict], row_id: str) -> dict:
    for row in rows:
        if row["row_id"] == row_id:
            return row
    raise KeyError(f"row_id not found: {row_id!r}")


def update_row(rows: list[dict], row_id: str, **updates: str) -> dict:
    row = get_row(rows, row_id)
    row.update(updates)
    return row


def assign_missing_ids(rows: list[dict]) -> int:
    """Fill blank row_id cells in place. Returns the number of rows newly assigned.

    Existing row_id values are never altered, so filenames already generated
    under reports/ stay valid across repeated runs.
    """
    max_seq = 0
    for row in rows:
        m = _ROW_ID_SEQ_RE.match(row.get("row_id") or "")
        if m:
            max_seq = max(max_seq, int(m.group(1)))

    assigned = 0
    for row in rows:
        if row.get("row_id"):
            continue
        max_seq += 1
        atlas_part = slug(row["atlas"])
        label_part = slug(row["label"])
        row["row_id"] = f"{max_seq:03d}_{atlas_part}_{label_part}"
        assigned += 1
    return assigned
