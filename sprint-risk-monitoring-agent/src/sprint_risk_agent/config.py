"""Ngưỡng và cấu hình vận hành. Mọi rule định lượng nằm ở đây, KHÔNG nằm trong prompt."""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    # Vòng lặp reject/edit tối đa bao nhiêu lần trước khi dừng (SOP 3.3 Bước 2a)
    max_revisions: int = 3
    # Circuit breaker: số lần chạy liên tiếp có grounding warning thì chuyển thủ công (SOP 3.3 Bước 2b)
    breaker_threshold: int = 2
    # Ngưỡng tín hiệu
    review_wait_hours_threshold: int = 48   # PR chưa review quá số giờ này
    jira_due_window_days: int = 2           # ticket chưa xong, còn <= số ngày này tới due date
    critical_days_left: int = 1             # 3 nguồn + còn <= số ngày này => CRITICAL
    low_days_left: int = 5                  # 2 nguồn + còn > số ngày này => LOW
    # Kênh gửi
    team_channel: str = "#team-sprint"
    leadership_channel: str = "#leadership-escalation"
    jira_project_key: str = "RISK"


DONE_STATUSES = frozenset({"done", "closed", "resolved", "hoàn thành", "đã xong"})

SLACK_BLOCKER_PATTERN = re.compile(
    r"\b(blocked|stuck|waiting on)\b|bị chặn|kẹt|đang chờ", re.IGNORECASE
)

DEFAULT_SETTINGS = Settings()
