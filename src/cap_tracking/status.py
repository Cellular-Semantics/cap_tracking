"""The audit report: every row lands in exactly one of four buckets, every run."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StatusReport:
    done: list[dict] = field(default_factory=list)
    outstanding: list[dict] = field(default_factory=list)
    no_action: list[dict] = field(default_factory=list)
    needs_decision: list[dict] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _github_complete(row: dict) -> bool:
    return row.get("github_issue_status") == "filed" and bool(row.get("github_ticket"))


def _cap_complete(row: dict) -> bool:
    return row.get("comment_status") == "done"


def classify(row: dict, warnings: list[str]) -> str:
    route = row.get("action_route")
    row_id = row.get("row_id") or "(no row_id)"

    if row.get("github_issue_status") == "filed" and not row.get("github_ticket"):
        warnings.append(
            f"{row_id}: github_issue_status=filed but github_ticket is empty (data integrity)"
        )

    if route == "skip":
        return "no_action"
    if route == "blocked":
        return "needs_decision"
    if route == "cap_comment":
        return "done" if _cap_complete(row) else "outstanding"
    if route == "github_issue":
        return "done" if _github_complete(row) else "outstanding"
    if route == "both":
        return "done" if (_cap_complete(row) and _github_complete(row)) else "outstanding"

    warnings.append(f"{row_id}: unrecognized action_route {route!r}")
    return "outstanding"


def build_status_report(rows: list[dict]) -> StatusReport:
    report = StatusReport()
    for row in rows:
        bucket = classify(row, report.warnings)
        getattr(report, bucket).append(row)
    return report


def _route_state(row: dict) -> str:
    route = row.get("action_route")
    if route == "both":
        gh = "filed" if _github_complete(row) else (row.get("github_issue_status") or "not_started")
        cap = "done" if _cap_complete(row) else (row.get("comment_status") or "not_started")
        return f"both: github={gh}, cap={cap}"
    if route == "github_issue":
        status = row.get("github_issue_status") or "not_started"
        ticket = row.get("github_ticket") or "(none)"
        return f"github_issue  status={status}  ticket={ticket}"
    if route == "cap_comment":
        status = row.get("comment_status") or "not_started"
        return f"cap_comment   status={status}"
    return route or "(no action_route)"


def format_report(report: StatusReport, total: int) -> str:
    lines: list[str] = []
    lines.append(f"=== cap_tracking status ({total} rows) ===\n")
    lines.append(f"DONE                         : {len(report.done)} / {total}")
    lines.append(f"OUTSTANDING (action pending) : {len(report.outstanding)} / {total}")
    lines.append(f"NO ACTION (skip)             : {len(report.no_action)} / {total}")
    lines.append(f"NEEDS DECISION (blocked)     : {len(report.needs_decision)} / {total}")

    if report.outstanding:
        lines.append("\n--- OUTSTANDING ---")
        for row in report.outstanding:
            feedback_note = ""
            if row.get("feedback_filed") in ("partial", "yes"):
                feedback_note = f"   (prior feedback: {row['feedback_filed']} — {row.get('feedback_scope', '')})"
            lines.append(f"[{row.get('row_id')}] {_route_state(row)}{feedback_note}")

    if report.no_action:
        lines.append("\n--- NO ACTION (skip) ---")
        for row in report.no_action:
            extra = ""
            if row.get("feedback_filed") in ("partial", "yes"):
                extra = f"  (historical: filed via feedback channel, feedback_filed={row['feedback_filed']})"
            lines.append(f"[{row.get('row_id')}] class={row.get('class')}{extra}")

    if report.needs_decision:
        lines.append("\n--- NEEDS DECISION (blocked) ---")
        for row in report.needs_decision:
            lines.append(
                f"[{row.get('row_id')}] class={row.get('class')}  notes=\"{row.get('notes', '')}\""
            )

    if report.warnings:
        lines.append("\n--- DATA INTEGRITY WARNINGS ---")
        for w in report.warnings:
            lines.append(w)

    return "\n".join(lines) + "\n"
