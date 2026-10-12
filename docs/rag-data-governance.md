# RAG Data Governance — THIẾT KẾ, CHƯA TRIỂN KHAI

Điều kiện tiên quyết cho nhóm "Security readiness" của gate v1→v2 (xem roadmap-v2.md). Không có Vector DB nào tồn tại ở v1.0.

## Hai loại tri thức, hai mức thẩm quyền

| `knowledge_type` | Nội dung | Vai trò | Thẩm quyền |
|---|---|---|---|
| `POLICY` | SOP, Skill Card | "Nên làm gì" — dùng để giải thích | Cao hơn; nhưng ngưỡng/rule vẫn code cứng, không đọc từ Vector DB |
| `HISTORICAL_CASE` | Sprint cũ, retro, lessons learned | "Trước đây đã xảy ra gì" — tiền lệ | Chỉ tham khảo; không biến thành quy tắc quyết định |

## Quy tắc nạp dữ liệu (đề xuất)
1. Chỉ nạp nguồn nằm trong danh sách được duyệt; mỗi nguồn có người chịu trách nhiệm.
2. Ẩn danh/redact (dùng cùng `redact_sensitive`) trước khi embed — không embed dữ liệu gốc.
3. Không nạp đánh giá cá nhân, số liệu ngân sách nhạy cảm, thông tin khách hàng.
4. Mỗi chunk lưu `knowledge_type`, nguồn, ngày, người duyệt; có chính sách xóa/hết hạn.
5. Mọi nội dung RAG trả về đi qua grounding check và luôn hiển thị kèm nguồn cho PM.
