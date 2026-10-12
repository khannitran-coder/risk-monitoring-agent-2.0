import pytest

from sprint_risk_agent.guardrails import redact_sensitive, sanitize_raw_items, validate_grounding


@pytest.mark.parametrize(
    "text,must_not_contain",
    [
        ("api_key=sk_live_ABC123", "sk_live_ABC123"),
        ("password: hunter2", "hunter2"),
        ("mật khẩu: abc123", "abc123"),
        ("Authorization: Bearer abc.def-123", "abc.def-123"),
        ("key AKIAABCDEFGHIJKLMNOP end", "AKIAABCDEFGHIJKLMNOP"),
        ("token ghp_" + "a" * 36, "ghp_" + "a" * 36),
        ("liên hệ chi@example.com nhé", "chi@example.com"),
        ("gọi +84 912 345 678", "912 345 678"),
        ("gọi 0912345678", "0912345678"),
        ("thẻ 4111 1111 1111 1111", "4111 1111 1111 1111"),
    ],
)
def test_redacts(text, must_not_contain):
    out = redact_sensitive(text)
    assert must_not_contain not in out
    assert "[REDACTED_" in out


@pytest.mark.parametrize("text", ["PAY-101 bị chặn", "due 2026-10-08", "epoch 1759800000000", "SPRINT-42 còn 3 ngày", ""])
def test_leaves_normal_text_alone(text):
    assert redact_sensitive(text) == text


def test_none_passthrough():
    assert redact_sensitive(None) is None


def test_sanitize_raw_items_copies_and_only_touches_text_fields():
    items = [{"ticket_id": "PAY-1", "title": "token=abc123", "n": 5}]
    out = sanitize_raw_items(items, ("title",))
    assert out[0]["title"] == "[REDACTED_SECRET]"
    assert out[0]["ticket_id"] == "PAY-1" and out[0]["n"] == 5
    assert items[0]["title"] == "token=abc123"  # không sửa object gốc


def test_grounding_flags_fabricated_ticket():
    assert validate_grounding("PAY-101 và PAY-999 bị trễ", {"PAY-101"}) == ["PAY-999"]


def test_grounding_ok_and_ignore():
    assert validate_grounding("PAY-101 ok", {"PAY-101"}) == []
    assert validate_grounding("Sprint SPRINT-42: PAY-101", {"PAY-101"}, ignore={"SPRINT-42"}) == []
    assert validate_grounding("SPRINT-42", set()) == ["SPRINT-42"]
