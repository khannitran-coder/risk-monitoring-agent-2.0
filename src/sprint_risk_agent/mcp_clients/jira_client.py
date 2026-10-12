"""Client Jira qua MCP Atlassian - CHƯA NỐI (v1.0 chỉ định nghĩa điểm cắm)."""

_MSG = "Chưa nối MCP Atlassian. Dùng mcp_clients.fake.demo_clients() để chạy demo/test."


class McpJiraClient:
    def __init__(self, session) -> None:
        self.session = session

    def search_open_tickets(self, sprint_id: str) -> list[dict]:
        raise NotImplementedError(_MSG)

    def find_issue(self, idempotency_key: str) -> str | None:
        raise NotImplementedError(_MSG)

    def create_issue(self, summary: str, description: str, idempotency_key: str) -> str:
        raise NotImplementedError(_MSG)
