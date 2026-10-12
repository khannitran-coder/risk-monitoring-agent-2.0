import operator
from typing import Annotated, Literal, TypedDict

RiskLevel = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
RunStatus = Literal["COMPLETED", "REJECTED", "ABORTED_MAX_REVISIONS", "MANUAL_MODE"]
Decision = Literal["approve", "edit", "reject"]
LEVEL_ORDER: tuple[RiskLevel, ...] = ("LOW", "MEDIUM", "HIGH", "CRITICAL")


class RiskSignal(TypedDict):
    ticket_id: str
    source: str        # "jira" | "github" | "slack"
    evidence: str      # đã redact; không diễn giải lại
    detected_at: str   # ISO date (as_of)


class AgentState(TypedDict, total=False):
    sprint_id: str
    as_of: str                      # ISO date, mốc tính "còn bao nhiêu ngày"
    run_id: str
    session_started_at: str
    manual_mode: bool               # circuit breaker đang bật
    jira_raw: list[dict]
    github_raw: list[dict]
    slack_raw: list[dict]
    fetch_errors: Annotated[list[str], operator.add]   # 3 node fetch ghi song song
    signals: list[RiskSignal]
    ticket_risk: dict[str, RiskLevel]
    unconfirmed_tickets: list[str]  # chỉ 1 nguồn - không gán risk, chỉ để PM biết
    risk_level: RiskLevel
    draft_text: str
    action_plan: dict | None        # RiskResponsePlan.model_dump() (nhánh HIGH/CRITICAL)
    grounding_warnings: list[str]
    checkpoint_decision: Decision | None
    checkpoint_notes: str | None
    revision_count: int
    jira_issue_ids: dict[str, str]  # ticket_id -> issue key
    status: RunStatus
