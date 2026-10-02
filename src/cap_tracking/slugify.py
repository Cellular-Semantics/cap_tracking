"""Deterministic, filesystem-safe slugs for row_id and atlas directory names."""

from __future__ import annotations

import re


def slug(text: str, max_len: int = 40) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"
