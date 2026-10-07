"""Giao diện (Protocol) cho 3 nguồn dữ liệu. Node chỉ phụ thuộc vào giao diện này,
nên test dùng fake và bản MCP thật cắm vào sau mà không phải sửa node."""

from dataclasses import dataclass
from typing import Protocol


class JiraClient(Protocol):
    def search_open_tickets(self, sprint_id: str) -> list[dict]:
        """Item: ticket_id, title, status, due_date (YYYY-MM-DD), description?, comment?"""

    def find_issue(self, idempotency_key: str) -> str | None:
        """Trả issue key nếu đã tạo với idempotency_key này (vd tra theo label)."""

    def create_issue(self, summary: str, description: str, idempotency_key: str) -> str: ...


class GitHubClient(Protocol):
    def list_open_pull_requests(self) -> list[dict]:
        """Item: title, branch?, ticket_id?, review_wait_hours, ci_status, url?"""


class SlackClient(Protocol):
    def search_messages(self, sprint_id: str) -> list[dict]:
        """Item: text, ts?, channel?"""

    def post_message(self, channel: str, text: str) -> None: ...


@dataclass
class Clients:
    jira: JiraClient
    github: GitHubClient
    slack: SlackClient
