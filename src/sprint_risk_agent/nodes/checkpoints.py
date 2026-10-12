"""Checkpoint người: interrupt() dừng graph thật sự (cần checkpointer). Không có nhánh nào
tự gửi thẳng. Quyết định không hợp lệ được coi là reject (fail-safe: không gửi gì)."""

from langgraph.types import Command, interrupt

from ..config import Settings
from ..guardrails import redact_sensitive
from ..state import AgentState


def _payload(state: AgentState, ask: str, settings: Settings) -> dict:
    return {
        "draft_text": state["draft_text"],
        "risk_level": state["risk_level"],
        "ticket_risk": state.get("ticket_risk", {}),
        "grounding_warnings": state.get("grounding_warnings", []),  # luôn hiển thị, kể cả rỗng
        "fetch_errors": state.get("fetch_errors", []),
        "action_plan": state.get("action_plan"),
        "revision_count": state.get("revision_count", 0),
        "max_revisions": settings.max_revisions,
        "ask": ask,
    }


def _decide(state: AgentState, ask: str, on_approve: str, redraft: str, settings: Settings) -> Command:
    decision = interrupt(_payload(state, ask, settings))
    action = decision.get("action") if isinstance(decision, dict) else None
    notes = redact_sensitive((decision or {}).get("notes")) if isinstance(decision, dict) else None

    if action == "approve":
        return Command(update={"checkpoint_decision": "approve", "checkpoint_notes": notes}, goto=on_approve)

    if action == "edit":
        n = state.get("revision_count", 0) + 1
        if n > settings.max_revisions:
            return Command(
                update={"checkpoint_decision": "edit", "checkpoint_notes": notes,
                        "revision_count": n - 1, "status": "ABORTED_MAX_REVISIONS"},
                goto="cleanup_session",
            )
        return Command(
            update={"checkpoint_decision": "edit", "checkpoint_notes": notes, "revision_count": n},
            goto=redraft,
        )

    return Command(  # reject hoặc quyết định không hợp lệ
        update={"checkpoint_decision": "reject", "checkpoint_notes": notes, "status": "REJECTED"},
        goto="cleanup_session",
    )


def make_checkpoint_nodes(settings: Settings):
    def spot_check(state: AgentState) -> Command:
        """Checkpoint NHẸ (SOP 5.2 cấp Cơ bản/Trung cấp) cho nhánh LOW/MEDIUM."""
        return _decide(state, "approve / edit (kèm ghi chú) / reject — spot-check nhanh",
                       "send_digest", "draft_digest", settings)

    def human_approval(state: AgentState) -> Command:
        """Checkpoint ĐẦY ĐỦ (SOP 5.2 cấp Nâng cao) cho nhánh HIGH/CRITICAL."""
        return _decide(state, "approve / edit (kèm ghi chú) / reject — cần xem xét đầy đủ",
                       "escalate", "draft_action_plan", settings)

    return spot_check, human_approval
