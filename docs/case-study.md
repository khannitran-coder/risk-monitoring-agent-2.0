# Case Study: Sprint Risk Monitoring Agent

> Đây là case study về **quá trình xây dựng** (v1.0, chạy với dữ liệu giả). Chưa có pilot trên sprint thật nên chưa có số liệu hiệu quả; phần đó được ghi rõ ở cuối.

## Vấn đề

Mỗi tuần PM tự rà ba nơi (Jira, GitHub, Slack) để phát hiện ticket tắc nghẽn. Làm thủ công thì chậm và dễ sót. AI tích hợp sẵn trong từng công cụ chỉ thấy dữ liệu của chính nó, nên không nhận ra một ticket vừa quá hạn trên Jira, vừa có PR treo trên GitHub, vừa được nhắc "bị chặn" trên Slack.

## Cách tiếp cận

Bắt đầu từ SOP cá nhân ([SOP-AI-PM](./SOP-AI-PM.md)) thay vì bắt đầu từ công cụ: dùng khung quyết định ở mục 3.3 để xác định pain point nào thật sự cần agent (có rule định lượng, có nhánh rẽ, có bước dừng chờ người), rồi chuyển các bài test thủ công của SOP (Severity Distortion, Data Fabrication, Confidentiality) thành guardrail chạy tự động trong code.

- Tương quan 3 nguồn bằng rule: ≥2/3 nguồn mới gán mức rủi ro, mức do rule quyết định chứ không do LLM.
- Định tuyến theo mức: LOW/MEDIUM đi đường nhẹ, HIGH/CRITICAL phải qua duyệt đầy đủ.
- Hai tầng checkpoint với con người; `reject` kết thúc lượt chạy, không gửi gì.
- Bản nháp có ≥2 phương án xử lý khác chiến lược nhưng không có field "khuyến nghị": PM là người chọn.

Chi tiết lý do chọn xem [design-notes](./design-notes.md).

## Lỗi phát hiện và sửa khi đối chiếu code với tài liệu

| Phát hiện | Cách xử lý |
|---|---|
| Biên dịch graph không có checkpointer nên `interrupt()` sẽ lỗi | Mặc định dùng `MemorySaver` |
| Vòng reject/edit không giới hạn | Giới hạn 3 lần soạn lại; thêm circuit breaker dựa trên audit log |
| Mức CRITICAL chưa bao giờ được gán | Thêm rule và test |
| Schema chấp nhận evidence rỗng | `evidence_refs` bắt buộc ≥1 |
| Regex SĐT `+84` không khớp, regex thẻ báo nhầm timestamp, thiếu "mật khẩu:" | Sửa; dùng Luhn cho thẻ |
| P×I score có trong tài liệu nhưng không có trong code | Chuyển sang thiết kế v2.0 để tài liệu khớp với code |
| Sơ đồ v1 có node không tồn tại trong code | Vẽ lại sơ đồ theo code |

## Bài học

- **Tài liệu và code phải khớp nhau.** Nhiều lỗi ở trên không phải lỗi logic mà là tài liệu hứa nhiều hơn code làm được. Cách xử lý nhất quán: rút tài liệu về đúng trạng thái thật và ghi rõ phần "chỉ là thiết kế".
- **Tách "ai quyết định" khỏi "ai soạn".** Chính vì mức rủi ro do rule quyết định, drafter (template hay LLM) có thể thay thế mà không đổi hành vi an toàn của hệ thống.
- **Phân loại hành động theo khả năng hoàn tác.** Tạo Jira issue hoàn tác được và idempotent; gửi Slack cho Ban giám đốc thì không, nên chỉ chạy sau duyệt đầy đủ.

## Chưa làm

- Nối MCP Jira/GitHub/Slack thật.
- Kiểm thử drafter LLM với API thật.
- Pilot ít nhất 1 sprint đầy đủ.

## Kết quả

*Chưa đo.* Khi có pilot sẽ đo theo SOP Giai đoạn 8: thời gian tiết kiệm so với baseline, tỉ lệ báo động giả, % bản nháp bị sửa/từ chối, số cảnh báo grounding.
