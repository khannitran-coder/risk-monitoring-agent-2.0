# Case Study: Sprint Risk Monitoring Agent

> Trạng thái: **khung case study — chưa có kết quả đo**. Điền sau khi chạy pilot trên sprint thật.

## Vấn đề
Mỗi tuần PM tự rà 3 nơi (Jira, GitHub, Slack) để phát hiện ticket tắc nghẽn. Thủ công thì chậm và dễ sót; AI tích hợp sẵn trong từng tool chỉ thấy dữ liệu của chính nó.

## Cách tiếp cận
Tương quan 3 nguồn bằng rule (≥2/3 nguồn mới gán mức), định tuyến theo mức rủi ro, checkpoint con người 2 tầng, guardrail code hóa từ các bài test thủ công của SOP (Severity Distortion, Data Fabrication, Confidentiality).

## Đã làm (có bằng chứng trong repo)
- Luồng LangGraph + 67 test chạy với client giả; kiểm chứng interrupt/resume, vòng edit có giới hạn, reject không gửi gì, idempotency, circuit breaker.
- Redact tại nguồn và grounding check chạy tự động trong luồng.

## Chưa làm
- Nối MCP Jira/GitHub/Slack thật; kiểm thử drafter LLM với API thật; pilot ≥1 sprint đầy đủ.

## Kết quả
*Chưa đo.* Đo theo SOP Giai đoạn 8: thời gian tiết kiệm so với baseline, tỉ lệ báo động giả, % bản nháp bị sửa/từ chối, số cảnh báo grounding.

## Bài học
*(điền sau pilot)*
