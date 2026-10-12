"""Soạn digest / action plan. Drafter là điểm cắm: mặc định TemplateDrafter (xác định, offline);
AnthropicDrafter (llm.py) là tuỳ chọn. Mọi output đều đi qua redact + validate_grounding."""

from typing import Protocol

from ..guardrails import redact_sensitive, validate_grounding
from ..schemas import RiskResponseOption, RiskResponsePlan
from ..state import AgentState


class Drafter(Protocol):
    def digest(self, state: AgentState) -> str: ...
    def action_plan(self, state: AgentState) -> RiskResponsePlan: ...


def _risk_lines(state: AgentState) -> list[str]:
    by_ticket: dict[str, list[str]] = {}
    for s in state.get("signals", []):
        by_ticket.setdefault(s["ticket_id"], []).append(f"[{s['source']}] {s['evidence']}")
    lines = []
    for tid, level in sorted(state.get("ticket_risk", {}).items()):
        lines.append(f"- {tid} — {level}")
        lines.extend(f"    • {e}" for e in by_ticket.get(tid, []))
    return lines


class TemplateDrafter:
    """Không dùng LLM: chỉ trình bày lại dữ kiện đã có. Không suy luận nguyên nhân gốc."""

    def digest(self, state: AgentState) -> str:
        lines = [f"Sprint {state['sprint_id']} — rủi ro cao nhất: {state['risk_level']}"]
        risks = _risk_lines(state)
        lines += risks or ["Không có ticket nào được >=2 nguồn xác nhận rủi ro."]
        if state.get("unconfirmed_tickets"):
            lines.append(f"({len(state['unconfirmed_tickets'])} ticket chỉ có 1 nguồn — chưa gán mức rủi ro)")
        return "\n".join(lines)

    def action_plan(self, state: AgentState) -> RiskResponsePlan:
        refs = [t for t, lvl in sorted(state["ticket_risk"].items()) if lvl in ("HIGH", "CRITICAL")]
        ids = ", ".join(refs)
        return RiskResponsePlan(
            root_cause=(
                "Chưa phân tích (template mặc định không suy luận nguyên nhân gốc). PM bổ sung theo "
                "fishbone People/Process/Tools/Environment."
            ),
            options=[
                RiskResponseOption(strategy="mitigate", evidence_refs=refs,
                                   description=f"Dồn nguồn lực/gỡ blocker cho {ids} trước các việc khác trong sprint.",
                                   tradeoff="Các ticket khác trong sprint có thể trễ."),
                RiskResponseOption(strategy="avoid", evidence_refs=refs,
                                   description=f"Cắt hoặc hoãn phần phạm vi của {ids} ra khỏi sprint hiện tại.",
                                   tradeoff="Giảm scope đã cam kết; cần thống nhất với stakeholder."),
                RiskResponseOption(strategy="accept", evidence_refs=refs,
                                   description=f"Giữ nguyên kế hoạch cho {ids} và theo dõi hằng ngày.",
                                   tradeoff="Giữ nguyên khả năng trễ deadline."),
            ],
        )


def format_plan(plan: RiskResponsePlan, state: AgentState) -> str:
    lines = [f"Sprint {state['sprint_id']} — rủi ro cao nhất: {state['risk_level']}", *_risk_lines(state),
             "", f"Nguyên nhân gốc: {plan.root_cause}", ""]
    for i, o in enumerate(plan.options, 1):
        lines += [f"Phương án {i} [{o.strategy.upper()}]: {o.description}",
                  f"    Căn cứ: {', '.join(o.evidence_refs)}", f"    Đánh đổi: {o.tradeoff}"]
    lines += ["", "(Agent không đưa khuyến nghị — PM chọn phương án.)"]
    return "\n".join(lines)


def _degraded_prefix(state: AgentState) -> str:
    errs = state.get("fetch_errors") or []
    return f"⚠ Dữ liệu không đầy đủ, thiếu nguồn: {', '.join(errs)}\n" if errs else ""


def _grounding(text: str, state: AgentState, extra_refs: list[str] = ()) -> list[str]:
    known = {s["ticket_id"] for s in state.get("signals", [])}
    bad = set(validate_grounding(text, known, ignore={state["sprint_id"]}))
    bad |= {r for r in extra_refs if r not in known}
    return sorted(bad)


def make_draft_nodes(drafter: Drafter):
    def draft_digest(state: AgentState) -> dict:
        text = _degraded_prefix(state) + (redact_sensitive(drafter.digest(state)) or "")
        return {"draft_text": text, "action_plan": None, "grounding_warnings": _grounding(text, state)}

    def draft_action_plan(state: AgentState) -> dict:
        plan = drafter.action_plan(state)  # đã validate bởi pydantic (>=2 option, khác strategy, có evidence)
        text = _degraded_prefix(state) + (redact_sensitive(format_plan(plan, state)) or "")
        refs = [r for o in plan.options for r in o.evidence_refs]
        return {"draft_text": text, "action_plan": plan.model_dump(),
                "grounding_warnings": _grounding(text, state, refs)}

    return draft_digest, draft_action_plan
