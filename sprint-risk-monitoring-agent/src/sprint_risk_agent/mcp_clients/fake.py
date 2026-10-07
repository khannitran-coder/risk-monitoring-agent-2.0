"""Client giả (in-memory) cho test và demo. Ghi lại mọi hành động ra ngoài để test kiểm tra."""

from datetime import date, timedelta

from .base import Clients


class FakeJira:
    def __init__(self, tickets: list[dict] | None = None, fail: bool = False) -> None:
        self.tickets = tickets or []
        self.fail = fail
        self.issues: dict[str, dict] = {}       # idempotency_key -> issue
        self.create_calls = 0

    def search_open_tickets(self, sprint_id: str) -> list[dict]:
        if self.fail:
            raise ConnectionError("jira down")
        return [dict(t) for t in self.tickets]

    def find_issue(self, idempotency_key: str) -> str | None:
        issue = self.issues.get(idempotency_key)
        return issue["key"] if issue else None

    def create_issue(self, summary: str, description: str, idempotency_key: str) -> str:
        self.create_calls += 1
        key = f"RISK-{len(self.issues) + 1}"
        self.issues[idempotency_key] = {"key": key, "summary": summary, "description": description}
        return key


class FakeGitHub:
    def __init__(self, prs: list[dict] | None = None, fail: bool = False) -> None:
        self.prs = prs or []
        self.fail = fail

    def list_open_pull_requests(self) -> list[dict]:
        if self.fail:
            raise ConnectionError("github down")
        return [dict(p) for p in self.prs]


class FakeSlack:
    def __init__(self, messages: list[dict] | None = None, fail: bool = False) -> None:
        self.messages = messages or []
        self.fail = fail
        self.sent: list[tuple[str, str]] = []   # (channel, text)

    def search_messages(self, sprint_id: str) -> list[dict]:
        if self.fail:
            raise ConnectionError("slack down")
        return [dict(m) for m in self.messages]

    def post_message(self, channel: str, text: str) -> None:
        self.sent.append((channel, text))


def demo_clients(as_of: date) -> Clients:
    """Dữ liệu synthetic: PAY-101 (3 nguồn, sát hạn -> CRITICAL), PAY-102 (2 nguồn -> MEDIUM),
    PAY-103 (1 nguồn -> bỏ qua). Có 1 secret trong Slack để minh họa redact."""
    d = lambda n: (as_of + timedelta(days=n)).isoformat()  # noqa: E731
    jira = FakeJira(
        [
            {"ticket_id": "PAY-101", "title": "Tích hợp cổng thanh toán", "status": "In Progress", "due_date": d(1)},
            {"ticket_id": "PAY-102", "title": "Đối soát giao dịch", "status": "In Progress", "due_date": d(2)},
            {"ticket_id": "PAY-103", "title": "Báo cáo cuối ngày", "status": "To Do", "due_date": d(10)},
        ]
    )
    github = FakeGitHub(
        [
            {"title": "PAY-101: gateway adapter", "review_wait_hours": 72, "ci_status": "failed"},
            {"title": "PAY-102: reconcile job", "review_wait_hours": 60, "ci_status": "passed"},
        ]
    )
    slack = FakeSlack(
        [
            {"text": "PAY-101 đang bị chặn vì sandbox lỗi, api_key=sk_live_ABC123 vẫn chưa đổi"},
            {"text": "PAY-103 hơi stuck nhưng chắc không sao"},
        ]
    )
    return Clients(jira=jira, github=github, slack=slack)
