# Changelog

## 1.0.0 — repo hoàn chỉnh đầu tiên
Trước đó repo chỉ có cấu trúc thiết kế rỗng. Bản này triển khai v1.0 thật (client giả, 67 test) và chỉnh tài liệu theo review kiến trúc.

### Quyết định từ review kiến trúc
| Nhận xét | Quyết định |
|---|---|
| RAG "calibrate" P×I mơ hồ | Nhận. RAG = ngữ cảnh tham khảo; bỏ chữ "recommendation" (mâu thuẫn schema không có field khuyến nghị) |
| Tách SOP / lịch sử sprint | Nhận. `knowledge_type = POLICY / HISTORICAL_CASE` |
| Semantic matching cần confidence gate | Nhận, siết thêm: kết quả semantic không tính là nguồn xác nhận |
| Jira sau approval + idempotency | Gate đã có; thêm idempotency (key `sprint_id:ticket_id`, không phải `run_id`) — **đã triển khai ở v1.0** |
| Lifecycle/retention cho state | Nhận (thiết kế v2.0) |
| Metric chất lượng quyết định | Nhận, gắn nhãn "planned, not yet measured" |
| CRM thừa | Nhận, bỏ khỏi v2.0 và khỏi sơ đồ |
| Gate v1→v2 thành 4 nhóm | Nhận |
| Lỗi hình thức tree | Nhận, sửa |
| Không khoe thứ chưa làm | Nhận, README có bảng trạng thái |

### Sửa lỗi phát hiện khi đối chiếu
- `compile()` thiếu checkpointer (`interrupt()` sẽ lỗi) → mặc định `MemorySaver`.
- Vòng reject không có giới hạn → `max_revisions=3`; thêm circuit breaker (SOP 3.3 Bước 2).
- Mức CRITICAL chưa bao giờ được gán → có rule và test.
- Evidence rỗng được chấp nhận trong schema → `evidence_refs` bắt buộc ≥1.
- Regex SĐT `+84` không khớp, regex thẻ báo nhầm timestamp, thiếu "mật khẩu:" → sửa (Luhn cho thẻ).
- P×I có trong tài liệu nhưng không có trong code → chuyển sang thiết kế v2.0.
- Tên file SVG roadmap không khớp tree; sơ đồ v1 có node P×I không tồn tại trong code → vẽ lại v1; sơ đồ v2 bỏ CRM.
- Thay đổi hành vi: `reject` kết thúc lượt chạy (trước đó quay lại soạn thảo); `edit` mới quay lại.
