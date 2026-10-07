"""Guardrail 1: redact PII/secret tại nguồn. Guardrail 2: kiểm tra grounding (chống bịa ticket).

Lưu ý: regex dưới đây là baseline tối thiểu, KHÔNG toàn diện. Môi trường thật nên dùng
thư viện chuyên dụng (vd Microsoft Presidio).
"""

import re

_REPLACEMENTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bBearer\s+[A-Za-z0-9\-_.]+"), "[REDACTED_TOKEN]"),
    (re.compile(r"(?i)\b(api[_-]?key|token|secret|password|mật khẩu|mat khau)\s*[:=]\s*\S+"), "[REDACTED_SECRET]"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "[REDACTED_AWS_KEY]"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"), "[REDACTED_SLACK_TOKEN]"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED_EMAIL]"),
]
_CARD = re.compile(r"\b(?:\d[ -]?){12,15}\d\b")
_PHONE = re.compile(r"(?<!\w)(?:\+?84|0)(?:[\s.-]?\d){9}(?!\d)")


def _luhn_ok(digits: str) -> bool:
    total, flip = 0, False
    for ch in reversed(digits):
        d = int(ch)
        if flip:
            d = d * 2 - 9 if d * 2 > 9 else d * 2
        total += d
        flip = not flip
    return total % 10 == 0


def _redact_card(match: re.Match[str]) -> str:
    digits = re.sub(r"\D", "", match.group(0))
    return "[REDACTED_CARD]" if 13 <= len(digits) <= 16 and _luhn_ok(digits) else match.group(0)


def redact_sensitive(text: str | None) -> str | None:
    """Áp dụng ngay tại fetch node, TRƯỚC khi text vào state hoặc prompt LLM."""
    if not text:
        return text
    out = text
    for pattern, placeholder in _REPLACEMENTS:
        out = pattern.sub(placeholder, out)
    out = _CARD.sub(_redact_card, out)
    out = _PHONE.sub("[REDACTED_PHONE]", out)
    return out


def sanitize_raw_items(items: list[dict], text_fields: tuple[str, ...]) -> list[dict]:
    """Redact các field text của từng item lấy về từ MCP (trả về bản sao)."""
    cleaned = []
    for item in items:
        item = dict(item)
        for field in text_fields:
            if isinstance(item.get(field), str):
                item[field] = redact_sensitive(item[field])
        cleaned.append(item)
    return cleaned


TICKET_ID_PATTERN = re.compile(r"\b[A-Z][A-Z0-9]+-\d+\b")  # vd PROJ-123


def extract_ticket_ids(text: str) -> list[str]:
    return TICKET_ID_PATTERN.findall(text or "")


def validate_grounding(
    draft_text: str, known_ticket_ids: set[str], ignore: set[str] | None = None
) -> list[str]:
    """Trả về các ticket_id có trong draft nhưng KHÔNG có trong signals đã thu thập.

    Không tự chặn (agent không tự quyết định điều đó) - chỉ trả cảnh báo để gắn vào
    payload checkpoint cho PM. `ignore` dùng cho id hợp lệ không phải ticket (vd SPRINT-42).
    """
    mentioned = set(extract_ticket_ids(draft_text)) - (ignore or set())
    return sorted(mentioned - known_ticket_ids)
