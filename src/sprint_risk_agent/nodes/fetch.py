"""3 node fetch chạy song song. Redact NGAY tại đây - dữ liệu gốc không bao giờ vào state.

Nếu 1 nguồn lỗi: ghi vào fetch_errors và tiếp tục với dữ liệu rỗng cho nguồn đó
(rule >=2/3 nguồn vẫn đúng; bản nháp sẽ có cảnh báo 'dữ liệu không đầy đủ')."""

from ..guardrails import sanitize_raw_items
from ..mcp_clients.base import Clients
from ..state import AgentState


def make_fetch_nodes(clients: Clients):
    def fetch_jira(state: AgentState) -> dict:
        try:
            raw = clients.jira.search_open_tickets(state["sprint_id"])
        except Exception as e:  # noqa: BLE001 - nguồn lỗi không được làm sập cả lượt chạy
            return {"jira_raw": [], "fetch_errors": [f"jira: {type(e).__name__}"]}
        return {"jira_raw": sanitize_raw_items(raw, ("title", "description", "comment"))}

    def fetch_github(state: AgentState) -> dict:
        try:
            raw = clients.github.list_open_pull_requests()
        except Exception as e:  # noqa: BLE001
            return {"github_raw": [], "fetch_errors": [f"github: {type(e).__name__}"]}
        return {"github_raw": sanitize_raw_items(raw, ("title", "body", "branch"))}

    def fetch_slack(state: AgentState) -> dict:
        try:
            raw = clients.slack.search_messages(state["sprint_id"])
        except Exception as e:  # noqa: BLE001
            return {"slack_raw": [], "fetch_errors": [f"slack: {type(e).__name__}"]}
        return {"slack_raw": sanitize_raw_items(raw, ("text",))}

    return fetch_jira, fetch_github, fetch_slack
