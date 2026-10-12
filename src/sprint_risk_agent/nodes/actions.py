"""Hành động ra ngoài - chỉ chạy SAU checkpoint approve.

Phân loại (SOP 3.3 Bước 2b): tạo Jira issue = hoàn tác được (đóng issue); gửi Slack cho
Ban giám đốc = KHÔNG hoàn tác. Vì vậy Jira tạo trước, Slack gửi sau, và Jira idempotent."""

from ..config import Settings
from ..mcp_clients.base import Clients
from ..state import AgentState


def idempotency_key(sprint_id: str, ticket_id: str) -> str:
    # Theo sprint+ticket (không theo run_id) để các lượt chạy tuần sau không tạo trùng.
    return f"{sprint_id}:{ticket_id}"


def make_action_nodes(clients: Clients, settings: Settings):
    def send_digest(state: AgentState) -> dict:
        clients.slack.post_message(settings.team_channel, state["draft_text"])
        return {"status": "COMPLETED"}

    def escalate(state: AgentState) -> dict:
        issue_ids: dict[str, str] = {}
        for tid, level in sorted(state["ticket_risk"].items()):
            if level not in ("HIGH", "CRITICAL"):
                continue
            key = idempotency_key(state["sprint_id"], tid)
            existing = clients.jira.find_issue(key)
            if existing:
                issue_ids[tid] = existing
                continue
            evidence = "\n".join(
                f"- [{s['source']}] {s['evidence']}" for s in state["signals"] if s["ticket_id"] == tid
            )
            issue_ids[tid] = clients.jira.create_issue(
                summary=f"[{level}] {tid}: rủi ro sprint {state['sprint_id']}",
                description=f"Được PM duyệt (run {state['run_id']}).\n{evidence}",
                idempotency_key=key,
            )
        text = state["draft_text"]
        if issue_ids:
            text += "\n\nJira: " + ", ".join(f"{t} → {k}" for t, k in issue_ids.items())
        clients.slack.post_message(settings.leadership_channel, text)
        return {"jira_issue_ids": issue_ids, "status": "COMPLETED"}

    return send_digest, escalate
