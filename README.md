# Sprint Risk Monitoring Agent

[![CI](https://github.com/khannitran-coder/risk-monitoring-agent-2.0/actions/workflows/main.yml/badge.svg)](https://github.com/khannitran-coder/risk-monitoring-agent-2.0/actions/workflows/main.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **In short:** a human-in-the-loop agent that monitors sprint risk across Jira, GitHub and Slack. A ticket gets a risk level only when **at least 2 of the 3 independent sources confirm it**; the level is set by deterministic rules (never by an LLM), sensitive data is redacted before it enters state, every draft is grounding-checked against the collected signals, and **nothing leaves the system without the PM's approval**.
>
> Built with LangGraph and Pydantic to put my own AI-in-project-management SOP into practice ([SOP-AI-PM](./docs/SOP-AI-PM.md), aligned with PMBOK® Guide 8th ed., Appendix X3). 67 tests pass against fake MCP clients; real Jira/GitHub/Slack connectors and a live-sprint pilot are **not done yet** — see [Status](#trạng-thái).

Agent giám sát rủi ro sprint từ 3 nguồn độc lập (Jira, GitHub, Slack): chỉ gán mức rủi ro khi **≥2/3 nguồn cùng xác nhận**, định tuyến theo mức độ, và **luôn dừng chờ PM duyệt** trước khi gửi bất cứ thứ gì ra ngoài.

## Vì sao có dự án này

Mỗi tuần PM phải tự rà Jira, GitHub và Slack để tìm ticket đang tắc. Làm thủ công thì chậm và dễ sót; AI tích hợp sẵn trong từng công cụ lại chỉ thấy dữ liệu của chính nó. Dự án này tương quan 3 nguồn bằng rule rõ ràng, để AI **hỗ trợ** phát hiện và soạn nháp còn **quyết định luôn thuộc về PM**.

## Trạng thái

| Hạng mục | Trạng thái |
|---|---|
| Luồng LangGraph, rule correlate, 2 tầng checkpoint, guardrail redact/grounding, schema PMBOK, circuit breaker, audit log, idempotency Jira | **Đã triển khai, 67 test pass** (chạy với client giả) |
| Kết nối MCP Jira / GitHub / Slack | **Chưa nối** — `mcp_clients/*_client.py` là điểm cắm, ném `NotImplementedError` |
| Drafter dùng Claude (`llm.py`) | Có code, **chưa kiểm thử với API thật** — mặc định dùng `TemplateDrafter` (không LLM) |
| Checkpointer | `MemorySaver` (dev/test, mất state khi restart) |
| Pilot trên sprint thật / số liệu đo | **Chưa thực hiện — chưa có số liệu** |
| P×I reference score, RAG, Postgres, tracing, Slack approval | **Chỉ là thiết kế** — [roadmap v2](./docs/roadmap-v2.md) |

Không có thành phần nào trong repo được triển khai production.

## Chạy thử (dữ liệu synthetic)

```bash
pip install -e ".[dev]"
pytest -q                              # 67 test
python scripts/run_weekly.py --demo    # agent dừng chờ bạn gõ approve / edit / reject
```

Kết quả mẫu (rút gọn). Lưu ý secret trong tin nhắn Slack đã bị che trước khi vào state:

```text
Sprint SPRINT-42 — rủi ro cao nhất: CRITICAL
- PAY-101 — CRITICAL
    • [jira]   chưa hoàn thành, due 2026-10-13 (còn 1 ngày)
    • [github] PR chờ review 72h; CI failed
    • [slack]  PAY-101 đang bị chặn vì sandbox lỗi, [REDACTED_SECRET] vẫn chưa đổi

Phương án 1 [MITIGATE]: Dồn nguồn lực/gỡ blocker cho PAY-101 trước các việc khác.
    Căn cứ: PAY-101 · Đánh đổi: Các ticket khác trong sprint có thể trễ.
Phương án 2 [AVOID]: Cắt hoặc hoãn phần phạm vi của PAY-101 ra khỏi sprint.
Phương án 3 [ACCEPT]: Giữ nguyên kế hoạch và theo dõi hằng ngày.

(Agent không đưa khuyến nghị — PM chọn phương án.)
approve / edit / reject >
```

## Luồng v1.0

![Luồng v1.0](./docs/diagrams/agent-flow-v1.svg)

```
init_session ─► fetch_jira | fetch_github | fetch_slack (song song, redact ngay tại đây)
             ─► correlate_signals (rule, không LLM)
   LOW/MEDIUM  ─► draft_digest      ─► spot_check (nhẹ)        ─► send_digest ─► cleanup
   HIGH/CRIT   ─► draft_action_plan ─► human_approval (đầy đủ) ─► escalate    ─► cleanup
   edit → soạn lại (tối đa 3 lần) · reject / quyết định lạ → cleanup, không gửi gì
```

### Rule gán mức rủi ro (`nodes/correlate.py`, ngưỡng ở `config.py`)

| Số nguồn xác nhận 1 ticket | Điều kiện | Mức |
|---|---|---|
| 1 | — | bỏ qua (chỉ ghi vào `unconfirmed_tickets`) |
| 2 | còn > 5 ngày | LOW |
| 2 | còn lại | MEDIUM |
| 3 | — | HIGH |
| 3 | còn ≤ 1 ngày (kể cả quá hạn) | CRITICAL |

Tín hiệu: Jira (chưa xong, còn ≤ 2 ngày tới due) · GitHub (PR chờ review > 48h hoặc CI fail) · Slack (từ khóa blocked/stuck/waiting on/bị chặn/kẹt/đang chờ **và** có ticket_id khớp chính xác).

## Guardrail

- **Chống Severity Distortion:** `risk_level` do rule quyết định; LLM (nếu dùng) không được chấm mức.
- **Redact tại nguồn:** email, SĐT, thẻ (Luhn), token/secret (kể cả "mật khẩu:") bị che ngay ở fetch node, trước khi vào state hoặc prompt. Regex chỉ là baseline — môi trường thật nên dùng Presidio.
- **Chống bịa:** `validate_grounding` so mọi ticket_id trong bản nháp (và `evidence_refs`) với signals đã thu thập; cảnh báo luôn nằm trong payload checkpoint, kể cả khi rỗng.
- **Ranh giới Augmentation:** `RiskResponsePlan` có ≥2 phương án khác chiến lược (Avoid/Mitigate/Transfer/Accept), mỗi phương án có căn cứ và đánh đổi, **không có field "khuyến nghị"** (`extra="forbid"` từ chối nếu LLM tự thêm).
- **Human-in-the-loop không có đường tắt:** không có cờ tự duyệt; quyết định không hợp lệ = reject.
- **Vận hành an toàn:** giới hạn vòng edit; circuit breaker (2 lượt chạy liên tiếp có cảnh báo grounding → `MANUAL_MODE` tới khi PM `--reset-breaker`); Jira idempotent theo `sprint_id:ticket_id`; nguồn lỗi → chạy tiếp với cảnh báo "dữ liệu không đầy đủ".

Giới hạn đã biết: Slack gửi Ban giám đốc không hoàn tác được và không idempotent; regex ticket_id có thể báo nhầm với chuỗi dạng `CVE-2024-1`; Slack chỉ khớp chính xác ticket_id.

## Cấu trúc

```text
src/sprint_risk_agent/   graph · state · schemas · guardrails · config · audit · runner · llm
  nodes/                 session · fetch · correlate · draft · checkpoints · actions
  mcp_clients/           base (Protocol) · fake (test/demo) · jira/github/slack (chưa nối)
tests/                   guardrails · schemas · correlate · graph flow
scripts/                 run_weekly.py (CLI demo duyệt tay) · verify_demo.py (chạy trong CI)
docs/                    SOP · design-notes · case-study · roadmap-v2 · rag-data-governance · diagrams/
```

## Tài liệu

- [SOP cá nhân — Ứng dụng AI vào quản lý dự án](./docs/SOP-AI-PM.md): khung phương pháp mà dự án này hiện thực hoá
- [Ghi chú thiết kế](./docs/design-notes.md): vì sao LangGraph, vì sao `risk_level` không do LLM chấm
- [Case study](./docs/case-study.md): quá trình xây dựng, lỗi đã phát hiện, phần chưa làm
- [Roadmap v2.0](./docs/roadmap-v2.md) · [RAG data governance](./docs/rag-data-governance.md): thiết kế, chưa triển khai

## Kết quả đo được

*Chưa có.* Chỉ số dự kiến (planned, not yet measured): tỉ lệ báo động giả; % bản nháp bị edit/reject; thời gian chờ duyệt; số ticket Jira trùng; thời gian tiết kiệm so với baseline Time Audit của SOP.

## License

MIT — xem [LICENSE](./LICENSE).
