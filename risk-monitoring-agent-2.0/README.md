# Sprint Risk Monitoring Agent

[![CI](https://github.com/khannitran-coder/risk-monitoring-agent-2.0/actions/workflows/ci.yml/badge.svg)](https://github.com/khannitran-coder/risk-monitoring-agent-2.0/actions/workflows/ci.yml)

Agent LangGraph giám sát rủi ro sprint từ 3 nguồn độc lập (Jira, GitHub, Slack). **Quy tắc xác định mức rủi ro, LLM chỉ soạn nháp, con người luôn duyệt trước khi gửi bất cứ thứ gì ra ngoài.**

## Trạng thái

| Hạng mục | Trạng thái |
|---|---|
| Luồng LangGraph, rule correlate, 2 tầng checkpoint, guardrail, circuit breaker, audit log | Đã triển khai, 67 test pass (client giả, dữ liệu synthetic) |
| Kết nối Jira / GitHub / Slack thật | Chưa nối |
| Drafter dùng LLM | Có code, chưa kiểm thử với API thật |
| Số liệu đo trên sprint thật | Chưa có |

## Bắt đầu

```bash
cd sprint-risk-monitoring-agent
pip install -e ".[dev]"
pytest -q
python scripts/run_weekly.py --demo     # agent dừng chờ bạn gõ approve / edit / reject
```

Chi tiết thiết kế, rule gán mức rủi ro, guardrail và giới hạn đã biết: [`sprint-risk-monitoring-agent/README.md`](sprint-risk-monitoring-agent/README.md).

## Liên quan

[AI-PM Harness](https://github.com/khannitran-coder/ai-pm-harness-starter): cùng nguyên tắc "quy tắc quyết định, mô hình soạn nháp, con người duyệt", áp dụng cho phân tích RAID, báo cáo trạng thái và biên bản họp, kèm bộ benchmark 90 test case.
