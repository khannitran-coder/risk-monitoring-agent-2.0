"""Client Slack qua MCP - CHƯA NỐI (v1.0 chỉ định nghĩa điểm cắm)."""

_MSG = "Chưa nối MCP Slack. Dùng mcp_clients.fake.demo_clients()."


class McpSlackClient:
    def __init__(self, session) -> None:
        self.session = session

    def search_messages(self, sprint_id: str) -> list[dict]:
        raise NotImplementedError(_MSG)

    def post_message(self, channel: str, text: str) -> None:
        raise NotImplementedError(_MSG)
