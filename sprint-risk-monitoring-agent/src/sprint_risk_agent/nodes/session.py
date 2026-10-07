import uuid
from datetime import date, datetime, timezone

from ..audit import AuditLog
from ..config import Settings
from ..state import AgentState


def make_session_nodes(audit: AuditLog, settings: Settings):
    def init_session(state: AgentState) -> dict:
        """Gán run_id/timestamp, kiểm tra circuit breaker. Là chỗ duy nhất khởi tạo state."""
        update: dict = {
            "run_id": str(uuid.uuid4()),
            "session_started_at": datetime.now(timezone.utc).isoformat(),
            "as_of": state.get("as_of") or date.today().isoformat(),
            "revision_count": 0,
        }
        if audit.breaker_tripped(state["sprint_id"], settings.breaker_threshold):
            update.update(manual_mode=True, status="MANUAL_MODE")
        return update

    def route_after_init(state: AgentState) -> list[str]:
        if state.get("manual_mode"):
            return ["cleanup_session"]
        return ["fetch_jira", "fetch_github", "fetch_slack"]

    def cleanup_session(state: AgentState) -> dict:
        audit.append(
            {
                "event": "run_end",
                "sprint_id": state.get("sprint_id"),
                "run_id": state.get("run_id"),
                "started_at": state.get("session_started_at"),
                "ended_at": datetime.now(timezone.utc).isoformat(),
                "risk_level": state.get("risk_level"),
                "status": state.get("status", "UNKNOWN"),
                "decision": state.get("checkpoint_decision"),
                "revision_count": state.get("revision_count", 0),
                "grounding_warnings_count": len(state.get("grounding_warnings") or []),
                "fetch_errors": state.get("fetch_errors") or [],
                "jira_issue_ids": state.get("jira_issue_ids") or {},
            }
        )
        return {}

    return init_session, route_after_init, cleanup_session
