"""cap_tracking CLI entrypoint: `python -m cap_tracking <command> ...`"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cap_tracking import cap_note, csv_store, gh_post, gh_sync, ntr_render, xlsx_export
from cap_tracking.schema import CAP_ROUTES, GITHUB_ROUTES
from cap_tracking.status import StatusReport, build_status_report, format_report


def cmd_assign_ids(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    assigned = csv_store.assign_missing_ids(rows)
    csv_store.save_rows(rows)
    print(f"Assigned row_id to {assigned} row(s). Total rows: {len(rows)}.")
    return 0


def cmd_gen_ntr(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    row = csv_store.get_row(rows, args.row_id)
    if row["action_route"] not in GITHUB_ROUTES:
        print(
            f"ERROR: row {args.row_id} has action_route={row['action_route']!r}, "
            f"not one of {sorted(GITHUB_ROUTES)}.",
            file=sys.stderr,
        )
        return 1
    out_path = ntr_render.write_ntr_draft(row)
    if row.get("github_issue_status") == "not_started":
        csv_store.update_row(rows, args.row_id, github_issue_status="drafted")
        csv_store.save_rows(rows)
    print(f"NTR draft written: {out_path}")
    print(f"Next: just preview-ntr {out_path}")
    return 0


def cmd_preview_ntr(args: argparse.Namespace) -> int:
    returncode, _ = gh_post.post(args.ntr_file, confirm=False)
    return returncode


def cmd_post_ntr(args: argparse.Namespace) -> int:
    returncode, issue_url = gh_post.post(args.ntr_file, confirm=True)
    if returncode != 0 or not issue_url:
        return returncode

    row_id = gh_post.row_id_from_ntr_path(args.ntr_file)
    rows = csv_store.load_rows()
    csv_store.update_row(rows, row_id, github_ticket=issue_url, github_issue_status="filed")
    csv_store.save_rows(rows)
    print(f"Tracker updated: {row_id} -> github_ticket={issue_url}, github_issue_status=filed")
    return 0


def cmd_gen_cap_note(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    row = csv_store.get_row(rows, args.row_id)
    if row["action_route"] not in CAP_ROUTES:
        print(
            f"ERROR: row {args.row_id} has action_route={row['action_route']!r}, "
            f"not one of {sorted(CAP_ROUTES)}.",
            file=sys.stderr,
        )
        return 1
    out_path = cap_note.write_cap_note(row)
    if row.get("comment_status") == "not_started":
        csv_store.update_row(rows, args.row_id, comment_status="drafted")
        csv_store.save_rows(rows)
    print(f"CAP edit note written: {out_path}")
    print(f"Next: edit CAP by hand, then run: just mark-cap-done {args.row_id}")
    return 0


def cmd_mark_cap_done(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    row = csv_store.get_row(rows, args.row_id)
    if row["action_route"] not in CAP_ROUTES:
        print(
            f"ERROR: row {args.row_id} has action_route={row['action_route']!r}, "
            f"not one of {sorted(CAP_ROUTES)}.",
            file=sys.stderr,
        )
        return 1
    csv_store.update_row(rows, args.row_id, comment_status="done")
    csv_store.save_rows(rows)
    print(f"{args.row_id}: comment_status -> done")
    return 0


def cmd_sync_tickets(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    targets = [r for r in rows if r.get("github_ticket")]
    if args.row_id:
        targets = [r for r in targets if r["row_id"] == args.row_id]
        if not targets:
            print(f"ERROR: no row with row_id={args.row_id!r} and a github_ticket set.", file=sys.stderr)
            return 1

    changed = 0
    for row in targets:
        result = gh_sync.fetch_issue_state(row["github_ticket"])
        if not result:
            continue
        if (
            row.get("github_issue_state") != result["github_issue_state"]
            or row.get("closing_pr") != result["closing_pr"]
        ):
            csv_store.update_row(rows, row["row_id"], **result)
            changed += 1
        state = result["github_issue_state"]
        pr = f"  closing_pr={result['closing_pr']}" if result["closing_pr"] else ""
        print(f"{row['row_id']}: {state}{pr}")

    if changed:
        csv_store.save_rows(rows)
    print(f"\nChecked {len(targets)} ticket(s), updated {changed}.")
    return 0


def cmd_export_xlsx(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    xlsx_export.export_xlsx(rows, args.out_path)
    print(f"Wrote {args.out_path} ({len(rows)} rows)")
    return 0


_ROUTE_FILTER_ATTR = {
    "done": "done",
    "outstanding": "outstanding",
    "skip": "no_action",
    "blocked": "needs_decision",
}


def cmd_status(args: argparse.Namespace) -> int:
    rows = csv_store.load_rows()
    report = build_status_report(rows)

    if args.outstanding_only:
        filtered = StatusReport(outstanding=report.outstanding, warnings=report.warnings)
        print(format_report(filtered, total=len(rows)))
        return 0

    if args.route != "all":
        route_rows = [r for r in rows if r.get("action_route") == args.route]
        filtered_report = build_status_report(route_rows)
        print(format_report(filtered_report, total=len(route_rows)))
        return 0

    print(format_report(report, total=len(rows)))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cap_tracking")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("assign-ids", help="Fill blank row_id cells in the CSV.").set_defaults(
        func=cmd_assign_ids
    )

    p = sub.add_parser("gen-ntr", help="Draft an NTR markdown stub for a github_issue/both row.")
    p.add_argument("row_id")
    p.set_defaults(func=cmd_gen_ntr)

    p = sub.add_parser("preview-ntr", help="Preview an NTR file (no network call).")
    p.add_argument("ntr_file", type=Path)
    p.set_defaults(func=cmd_preview_ntr)

    p = sub.add_parser("post-ntr", help="Post an NTR file to obophenotype/cell-ontology.")
    p.add_argument("ntr_file", type=Path)
    p.set_defaults(func=cmd_post_ntr)

    p = sub.add_parser("gen-cap-note", help="Draft a CAP edit note for a cap_comment/both row.")
    p.add_argument("row_id")
    p.set_defaults(func=cmd_gen_cap_note)

    p = sub.add_parser("mark-cap-done", help="Mark a row's manual CAP edit as done.")
    p.add_argument("row_id")
    p.set_defaults(func=cmd_mark_cap_done)

    p = sub.add_parser(
        "sync-tickets",
        help="Read-only: check filed issues' real GitHub state and closing PR.",
    )
    p.add_argument("row_id", nargs="?", default=None, help="Sync just this row (default: all filed).")
    p.set_defaults(func=cmd_sync_tickets)

    p = sub.add_parser(
        "export-xlsx",
        help="Generate a formatted .xlsx review copy (table, frozen bold header, color-coded rows).",
    )
    p.add_argument(
        "out_path",
        type=Path,
        nargs="?",
        default=Path("data/hca_ontology_findings_review.xlsx"),
    )
    p.set_defaults(func=cmd_export_xlsx)

    p = sub.add_parser("status", help="Audit report: every row in exactly one bucket.")
    p.add_argument(
        "--route",
        choices=["all", "cap_comment", "skip", "github_issue", "blocked", "both"],
        default="all",
    )
    p.add_argument("--outstanding-only", action="store_true")
    p.set_defaults(func=cmd_status)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
