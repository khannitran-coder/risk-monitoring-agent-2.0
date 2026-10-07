"""Client GitHub qua MCP - CHƯA NỐI (v1.0 chỉ định nghĩa điểm cắm)."""


class McpGitHubClient:
    def __init__(self, session) -> None:
        self.session = session

    def list_open_pull_requests(self) -> list[dict]:
        raise NotImplementedError("Chưa nối MCP GitHub. Dùng mcp_clients.fake.demo_clients().")
