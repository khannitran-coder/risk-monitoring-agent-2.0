import pytest
from pydantic import ValidationError

from sprint_risk_agent.schemas import RiskResponseOption, RiskResponsePlan


def opt(strategy="mitigate", **kw):
    base = dict(strategy=strategy, description="làm X", evidence_refs=["PAY-1"], tradeoff="mất Y")
    return RiskResponseOption(**{**base, **kw})


def test_valid_plan():
    plan = RiskResponsePlan(root_cause="Process", options=[opt("mitigate"), opt("accept")])
    assert len(plan.options) == 2


def test_needs_two_options():
    with pytest.raises(ValidationError):
        RiskResponsePlan(root_cause="x", options=[opt()])


def test_needs_two_different_strategies():
    with pytest.raises(ValidationError):
        RiskResponsePlan(root_cause="x", options=[opt("mitigate"), opt("mitigate")])


def test_rejects_unknown_strategy():
    with pytest.raises(ValidationError):
        opt("ignore")


def test_requires_evidence_and_text():
    with pytest.raises(ValidationError):
        opt(evidence_refs=[])
    with pytest.raises(ValidationError):
        opt(description="")


@pytest.mark.parametrize("field", ["recommended_option", "best_choice", "recommendation"])
def test_no_room_for_a_verdict(field):
    """Schema không có chỗ cho 'khuyến nghị tốt nhất' - kể cả khi LLM tự thêm field."""
    assert field not in RiskResponsePlan.model_fields
    with pytest.raises(ValidationError):
        RiskResponsePlan(root_cause="x", options=[opt("mitigate"), opt("accept")], **{field: 0})
