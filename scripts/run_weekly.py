"""Chạy 1 lượt giám sát rủi ro sprint với CLI duyệt tay.

    python scripts/run_weekly.py --demo --sprint SPRINT-42

Chỉ có chế độ --demo (client giả) vì MCP Jira/GitHub/Slack chưa được nối ở v1.0.
Không có cờ "tự duyệt": mọi bản nháp đều dừng chờ PM.
Lưu ý: checkpointer là MemorySaver nên quyết định phải được trả lời trong cùng tiến trình.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from sprint_risk_agent.audit import AuditLog  # noqa: E402
from sprint_risk_agent.graph import build_graph  # noqa: E402
from sprint_risk_agent.mcp_clients.fake import demo_clients  # noqa: E402
from sprint_risk_agent.runner import pending_interrupt, resume_run, start_run  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprint", default="SPRINT-42")
    ap.add_argument("--demo", action="store_true", help="dùng dữ liệu synthetic (bắt buộc ở v1.0)")
    ap.add_argument("--audit", default="runs/audit.jsonl")
    ap.add_argument("--reset-breaker", action="store_true", help="PM xác nhận lại sau khi circuit breaker bật")
    args = ap.parse_args()

    audit = AuditLog(args.audit)
    if args.reset_breaker:
        audit.reset_breaker(args.sprint)
        print(f"Đã reset circuit breaker cho {args.sprint}")
        return 0
    if not args.demo:
        print("MCP Jira/GitHub/Slack chưa được nối ở v1.0. Chạy với --demo.", file=sys.stderr)
        return 2

    graph = build_graph(demo_clients(date.today()), audit=audit)
    thread_id, result = start_run(graph, args.sprint)
    while (payload := pending_interrupt(result)) is not None:
        print("\n" + "=" * 70)
        print(payload["draft_text"])
        print("-" * 70)
        print(f"Mức: {payload['risk_level']} | Cảnh báo grounding: {payload['grounding_warnings'] or 'không'}"
              f" | Sửa lần {payload['revision_count']}/{payload['max_revisions']}")
        action = input("approve / edit / reject > ").strip().lower()
        notes = input("ghi chú (nếu edit) > ").strip() or None if action == "edit" else None
        result = resume_run(graph, thread_id, action, notes)
    print(f"\nKết thúc: {result.get('status')} | Jira: {result.get('jira_issue_ids') or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
