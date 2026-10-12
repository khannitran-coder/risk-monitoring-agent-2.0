# Roadmap v2.0 — controlled agent với persistent state, governed retrieval và approved external actions

> **Trạng thái: THIẾT KẾ, CHƯA TRIỂN KHAI.** Không phải code đang chạy. Code đã triển khai và có test là v1.0 (`src/sprint_risk_agent/`). Chưa có benchmark, chưa triển khai production.

## v1.0 vs v2.0

- **v1.0 (đã triển khai, test với client giả):** fetch 3 nguồn → correlate rule-based (≥2/3) → digest/action plan → checkpoint người → gửi. Không RAG, `MemorySaver`, MCP chưa nối.
- **v2.0 (thiết kế):** thêm persistent state (Postgres), retrieval có quản trị (Vector DB), hành động ngoài được duyệt (Slack approval, Jira), quan sát (tracing + dashboard).

Sơ đồ: [flow v2](./diagrams/agent-flow-v2.svg) · [harness v2](./diagrams/harness-v2.svg)

## Các quyết định thiết kế (sau review kiến trúc)

1. **RAG là ngữ cảnh tham khảo, không phải thẩm quyền quyết định.** Node `retrieve_history` trả `historical_context` kèm nguồn, chỉ hiển thị cho PM. Nó **không** đi vào `risk_level` và không "calibrate" điểm số. Nội dung là so sánh case hiện tại với case cũ, không có khuyến nghị (giữ nguyên ranh giới Augmentation của SOP).
2. **P×I reference score (nếu làm):** tính bằng rule tất định, hiển thị song song để PM tham khảo; `pxi_divergence_warnings` cảnh báo khi lệch với `risk_level`. Không ghi đè routing.
3. **Hai loại tri thức:** metadata `knowledge_type = POLICY | HISTORICAL_CASE` (xem [rag-data-governance](./rag-data-governance.md)). POLICY dùng để giải thích; ngưỡng vẫn code cứng (SOP 3.3 Câu 1).
4. **Semantic matching cho Slack cần confidence gate:** exact match → dùng; không khớp → lấy top-k ứng viên; vượt ngưỡng và không mơ hồ → gắn nhãn *candidate*; nhiều ứng viên sát nhau → PM xác nhận; thấp → UNKNOWN. **Ticket khớp ngữ nghĩa không được tính là "nguồn xác nhận"** trong rule ≥2/3. Text Slack phải qua `redact_sensitive` trước khi embed.
5. **Jira chỉ tạo sau approval + idempotent** (đã có ở v1.0 qua key `sprint_id:ticket_id`). Tạo issue là hành động hoàn tác được; gửi Ban giám đốc thì không.
6. **Vòng đời state:** `RUNNING → WAITING_APPROVAL → APPROVED/REJECTED → COMPLETED → ARCHIVED`, kèm chính sách retention để Postgres không thành nơi chứa state vô thời hạn.
7. **Quan sát chất lượng quyết định, không chỉ kỹ thuật:** false-positive rate, % bản nháp bị edit/reject, thời gian chờ duyệt, ticket Jira trùng, thời gian tiết kiệm so với baseline, tuổi của rủi ro chưa xử lý. *Planned, not yet measured.*
8. **Không đưa CRM vào v2.0** vì chưa có business requirement. Audit trail ghi vào Postgres; CRM để Future Enhancement.

## Gate chuyển v1.0 → v2.0 (4 nhóm, cần đạt cả 4)

| Nhóm | Điều kiện |
|---|---|
| Operational | v1.0 nối MCP thật và chạy ổn định ≥1 sprint đầy đủ ở mức Assistance |
| Quality | `grounding_warnings` / `pxi_divergence_warnings` trong ngưỡng chấp nhận, không kích hoạt circuit breaker liên tục |
| Business need | Có use case thật (agent cần tham chiếu sprint cũ, hoặc Slack liên tục có mention mơ hồ regex không map được) — không "làm cho có RAG" |
| Security | Có data classification + chính sách nạp Vector DB (rag-data-governance) được duyệt |

Căn cứ: SOP mục *Lộ trình dài hạn* và Giai đoạn 2 (Quick Win trước, hạ tầng nặng sau khi pilot ổn định).

## Cấu trúc thư mục dự kiến (chưa tồn tại)

```text
src/sprint_risk_agent/
├── nodes/rag/            # retriever · embeddings · ingest_pipeline
├── nodes/checkpoints.py  # Slack Block Kit thật, resolve interrupt() qua webhook
└── mcp_clients/          # client MCP thật (Jira/GitHub/Slack)
infra/
├── checkpointer/migrations/   # schema Postgres
├── vector_db/schema.py        # collection theo knowledge_type
└── secrets/README.md          # lấy secret từ Vault/Secrets Manager
observability/
├── tracing.py                 # LangSmith/OpenTelemetry
└── dashboards/
docker-compose.yml             # Postgres + Qdrant/pgvector local
.github/workflows/deploy.yml   # deploy kèm migration
```
