"""Tương quan 3 nguồn và gán risk_level bằng RULE TƯỜNG MINH (không để LLM chấm).

Bảng rule (số nguồn độc lập xác nhận cùng 1 ticket):
  1 nguồn                                   -> bỏ qua (chưa đủ bằng chứng)
  2 nguồn, còn > low_days_left ngày         -> LOW
  2 nguồn, các trường hợp còn lại           -> MEDIUM
  3 nguồn                                   -> HIGH
  3 nguồn và còn <= critical_days_left ngày -> CRITICAL (quá hạn cũng tính)
Evidence giữ nguyên dữ kiện gốc (đã redact), không diễn giải/làm nhẹ (Severity Distortion Test).
"""

from datetime import date

from ..config import DONE_STATUSES, SLACK_BLOCKER_PATTERN, Settings
from ..guardrails import extract_ticket_ids
from ..state import LEVEL_ORDER, AgentState, RiskLevel, RiskSignal


def _parse_date(value) -> date | None:
    try:
        return date.fromisoformat(str(value)[:10])
    except (TypeError, ValueError):
        return None


def jira_days_left(jira_raw: list[dict], as_of: date) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in jira_raw:
        due = _parse_date(item.get("due_date"))
        tid = item.get("ticket_id")
        if tid and due and str(item.get("status", "")).lower() not in DONE_STATUSES:
            out[tid] = (due - as_of).days
    return out


def build_signals(state: AgentState, settings: Settings) -> list[RiskSignal]:
    as_of = _parse_date(state["as_of"]) or date.today()
    stamp = as_of.isoformat()
    signals: list[RiskSignal] = []

    for item in state.get("jira_raw", []):
        tid, due = item.get("ticket_id"), _parse_date(item.get("due_date"))
        if not tid or not due or str(item.get("status", "")).lower() in DONE_STATUSES:
            continue
        left = (due - as_of).days
        if left <= settings.jira_due_window_days:
            signals.append(
                {"ticket_id": tid, "source": "jira", "detected_at": stamp,
                 "evidence": f"Jira: chưa hoàn thành, due {due.isoformat()} (còn {left} ngày)"}
            )

    for pr in state.get("github_raw", []):
        ids = [pr["ticket_id"]] if pr.get("ticket_id") else extract_ticket_ids(
            f"{pr.get('title', '')} {pr.get('branch', '')}"
        )[:1]
        reasons = []
        if (pr.get("review_wait_hours") or 0) > settings.review_wait_hours_threshold:
            reasons.append(f"PR chờ review {pr['review_wait_hours']}h")
        if str(pr.get("ci_status", "")).lower() == "failed":
            reasons.append("CI failed")
        for tid in ids:
            if reasons:
                signals.append(
                    {"ticket_id": tid, "source": "github", "detected_at": stamp,
                     "evidence": f"GitHub '{pr.get('title', '')}': " + "; ".join(reasons)}
                )

    for msg in state.get("slack_raw", []):
        text = msg.get("text") or ""
        if SLACK_BLOCKER_PATTERN.search(text):
            for tid in dict.fromkeys(extract_ticket_ids(text)):  # chỉ khớp chính xác ticket_id ở v1
                signals.append(
                    {"ticket_id": tid, "source": "slack", "detected_at": stamp, "evidence": f"Slack: {text}"}
                )
    return signals


def classify(n_sources: int, days_left: int | None, settings: Settings) -> RiskLevel | None:
    if n_sources <= 1:
        return None
    if n_sources == 2:
        return "LOW" if days_left is not None and days_left > settings.low_days_left else "MEDIUM"
    if days_left is not None and days_left <= settings.critical_days_left:
        return "CRITICAL"
    return "HIGH"


def make_correlate_node(settings: Settings):
    def correlate_signals(state: AgentState) -> dict:
        signals = build_signals(state, settings)
        sources: dict[str, set[str]] = {}
        for s in signals:
            sources.setdefault(s["ticket_id"], set()).add(s["source"])

        as_of = _parse_date(state["as_of"]) or date.today()
        left = jira_days_left(state.get("jira_raw", []), as_of)

        ticket_risk: dict[str, RiskLevel] = {}
        unconfirmed: list[str] = []
        for tid, srcs in sorted(sources.items()):
            level = classify(len(srcs), left.get(tid), settings)
            if level is None:
                unconfirmed.append(tid)
            else:
                ticket_risk[tid] = level

        overall: RiskLevel = "LOW"
        for lvl in ticket_risk.values():
            if LEVEL_ORDER.index(lvl) > LEVEL_ORDER.index(overall):
                overall = lvl
        return {"signals": signals, "ticket_risk": ticket_risk,
                "unconfirmed_tickets": unconfirmed, "risk_level": overall}

    def route_after_correlate(state: AgentState) -> str:
        return "draft_action_plan" if state["risk_level"] in ("HIGH", "CRITICAL") else "draft_digest"

    return correlate_signals, route_after_correlate
