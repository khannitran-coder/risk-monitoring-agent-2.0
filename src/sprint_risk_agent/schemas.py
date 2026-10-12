"""Spec bắt buộc cho đề xuất xử lý rủi ro (nhánh HIGH/CRITICAL).

Cố tình KHÔNG có field `recommended_option` / `best_choice`: PM là người duy nhất chọn
(nguyên tắc Augmentation, SOP Giai đoạn 2 & 10). `extra="forbid"` làm cho việc LLM
tự thêm field kiểu đó bị từ chối ngay khi validate, thay vì chỉ dặn trong prompt.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

RiskResponseStrategy = Literal["avoid", "mitigate", "transfer", "accept"]  # 4 chiến lược PMBOK


class RiskResponseOption(BaseModel):
    model_config = ConfigDict(extra="forbid")

    strategy: RiskResponseStrategy
    description: str = Field(..., min_length=1, description="Hành động cụ thể, không chung chung")
    evidence_refs: list[str] = Field(
        ..., min_length=1, description="ticket_id làm căn cứ - phải khớp signals đã thu thập"
    )
    tradeoff: str = Field(..., min_length=1, description="Cái phải đánh đổi nếu chọn phương án này")


class RiskResponsePlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    root_cause: str = Field(..., min_length=1)  # khung fishbone People/Process/Tools/Environment (PP-27)
    options: list[RiskResponseOption] = Field(..., min_length=2)

    @model_validator(mode="after")
    def _strategies_must_differ(self) -> "RiskResponsePlan":
        strategies = [o.strategy for o in self.options]
        if len(set(strategies)) < 2:
            raise ValueError("options phải gồm ít nhất 2 chiến lược KHÁC NHAU")
        return self
