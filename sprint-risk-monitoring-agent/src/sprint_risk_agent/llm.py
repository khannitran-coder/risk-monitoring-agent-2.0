"""Drafter dùng Claude (TUỲ CHỌN, CHƯA kiểm thử với API thật trong v1.0).

Cài: pip install -e ".[llm]" và đặt ANTHROPIC_API_KEY. Model qua biến SPRINT_RISK_MODEL.
Action plan dùng tool-use ép buộc theo JSON schema của RiskResponsePlan (không free-text);
kết quả vẫn phải qua pydantic validate + validate_grounding như TemplateDrafter."""

import json
import os

from .schemas import RiskResponsePlan
from .state import AgentState

_SYSTEM = (
    "Bạn hỗ trợ PM giám sát rủi ro sprint. CHỈ dùng dữ kiện trong dữ liệu được cung cấp; "
    "chỉ nhắc ticket_id có trong danh sách; không làm nhẹ mức độ nghiêm trọng; "
    "KHÔNG đưa khuyến nghị hay chọn phương án tốt nhất — PM quyết định."
)


def _context(state: AgentState) -> str:
    return json.dumps(
        {"sprint_id": state["sprint_id"], "risk_level": state["risk_level"],
         "ticket_risk": state["ticket_risk"], "signals": state["signals"],
         "pm_notes": state.get("checkpoint_notes")},
        ensure_ascii=False,
    )


class AnthropicDrafter:
    def __init__(self, model: str | None = None, client=None) -> None:
        if client is None:
            import anthropic  # import muộn để lõi không phụ thuộc SDK

            client = anthropic.Anthropic()
        self.client = client
        self.model = model or os.environ.get("SPRINT_RISK_MODEL", "claude-sonnet-5-5")

    def digest(self, state: AgentState) -> str:
        msg = self.client.messages.create(
            model=self.model, max_tokens=800, system=_SYSTEM,
            messages=[{"role": "user", "content": "Viết bản tin ngắn cho team từ dữ liệu sau.\n" + _context(state)}],
        )
        return "".join(b.text for b in msg.content if b.type == "text")

    def action_plan(self, state: AgentState) -> RiskResponsePlan:
        msg = self.client.messages.create(
            model=self.model, max_tokens=1500, system=_SYSTEM,
            tools=[{"name": "submit_plan", "description": "Gửi các phương án ứng phó rủi ro (PMBOK).",
                    "input_schema": RiskResponsePlan.model_json_schema()}],
            tool_choice={"type": "tool", "name": "submit_plan"},
            messages=[{"role": "user", "content": "Lập các phương án ứng phó từ dữ liệu sau.\n" + _context(state)}],
        )
        block = next(b for b in msg.content if b.type == "tool_use")
        return RiskResponsePlan.model_validate(block.input)
