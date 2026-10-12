# Design Notes

## Vì sao LangGraph (và vì sao các pain point khác trong SOP thì không)

Theo khung quyết định SOP 3.3 Bước 1, PP-12 (rà soát rủi ro sprint) thỏa cả hai điều kiện cần state machine:

1. **Có rule định lượng** (≥2/3 nguồn, ngưỡng ngày/giờ) và rủi ro bịa ticket_id cao → code hóa thành hàm kiểm tra, không giao cho prompt.
2. **≥2 nhánh rẽ + vòng lặp tự sửa** (edit → quay lại đúng node soạn thảo) và **bước dừng chờ người** (`interrupt()` giữ state, resume sau hàng giờ/ngày) → cần checkpointer.

Các pain point tuyến tính khác (PP-01…PP-11) không có đặc điểm này nên dùng thẳng Claude Projects/Cowork là đủ.

## Vì sao risk_level không do LLM chấm

`correlate_signals` đếm số nguồn độc lập xác nhận và áp bảng rule cố định. Evidence giữ nguyên dữ kiện gốc (đã redact), không diễn giải lại. Đây là bản code hóa của Severity Distortion Test (SOP 5.1).

## Quyết định thiết kế đáng nhớ

- **Redact trước khi vào state**, không phải "ngay trước khi gọi LLM": nếu không, dữ liệu gốc vẫn nằm trong state/checkpoint/log.
- **reject ≠ edit.** `edit` quay lại soạn thảo (có giới hạn 3 lần); `reject` kết thúc lượt chạy, không gửi gì. Quyết định không hợp lệ được xử lý như reject (fail-safe).
- **Hành động ra ngoài chia theo khả năng hoàn tác** (SOP 3.3 Bước 2b): tạo Jira issue hoàn tác được và idempotent (key `sprint_id:ticket_id`, không dùng `run_id` vì sẽ trùng giữa các tuần); gửi Slack cho Ban giám đốc không hoàn tác được nên chỉ chạy sau full review.
- **Circuit breaker** dựa trên audit log JSONL, không dựa vào state của LangGraph, để sống qua nhiều lượt chạy.
- **Drafter là điểm cắm.** Mặc định `TemplateDrafter` chỉ trình bày lại dữ kiện và không suy luận nguyên nhân gốc (nên `root_cause` ghi rõ "chưa phân tích"). `AnthropicDrafter` dùng tool-use ép theo JSON schema, vẫn đi qua pydantic và grounding.

## Checkpointer

`interrupt()` bắt buộc có checkpointer. v1.0 dùng `MemorySaver` (mất state khi restart process nên CLI demo phải trả lời trong cùng tiến trình). Postgres thuộc v2.0.

## Chưa làm (cố ý)

P×I reference score từng được nhắc trong bản nháp tài liệu nhưng **không có trong code v1.0**; được chuyển sang thiết kế v2.0 (xem roadmap) để tài liệu khớp với code.
