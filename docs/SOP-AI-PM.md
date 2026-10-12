**SOP CÁ NHÂN**

**ỨNG DỤNG & TÍCH HỢP AI VÀO QUY TRÌNH QUẢN LÝ DỰ ÁN**

*Tài liệu vận hành cá nhân — dựa trên PMBOK® Guide, Eighth Edition (7 Performance Domain, 5 Focus Area, Appendix X3 – Artificial Intelligence)*

| Phiên bản | Ngày | Người sở hữu | Nội dung thay đổi |
| :---- | :---- | :---- | :---- |
| 1.0 | 15/07/2026 | Trần Khánh Chi | Khởi tạo SOP cá nhân hóa: thay toàn bộ bảng mẫu ở Giai đoạn 1–3 bằng 24 pain point thật (sau đó bổ sung thêm 3 pain point PP-25–PP-27), phân theo 4 cấp độ Cơ bản → Chuyên sâu/Chiến lược, gắn khung Automation/Assistance/Augmentation (PMBOK X3.1.1). |
| 1.1 | 16/07/2026 | Trần Khánh Chi | Bổ sung ví dụ AI Agent (khác AI Assistant) vào các pain point phù hợp; thêm 3 pain point mới sau khi đối chiếu với tài liệu tham khảo: PP-25 Soạn agenda trước họp, PP-26 Dựng Gantt & Critical Path nháp, PP-27 Phân tích nguyên nhân gốc & so sánh phương án xử lý (Problem Solving). |
| 1.2 | 16/07/2026 | Trần Khánh Chi | Bổ sung PP-28 Compliance và PP-29 Quality sau khi đối chiếu với khung 9 agent chuyên biệt (Planning/Risk/Finance/Compliance/Procurement/Scheduling/Reporting/Documentation/Quality Agent); thêm mục "Lộ trình dài hạn — từ Pain Point riêng lẻ đến hệ Agent chuyên biệt" làm bản đồ định hướng, không thay đổi cấu trúc vận hành hiện tại. |
| 1.3 | 16/07/2026 | Trần Khánh Chi | Viết lại hoàn toàn Giai đoạn 9: thay thư viện prompt tĩnh (copy–paste thủ công) bằng khung Skill Card (Trigger/Input/Rule bất biến/Output/Checkpoint/Vai trò AI) — đóng gói 1 lần, dùng lại nhiều lần, không phụ thuộc 1 công cụ AI cụ thể. Bổ sung 11 Skill Card đại diện 4 cấp độ + bảng tổng hợp khả năng đóng gói Skill cho toàn bộ 29 pain point. |
| 1.4 | 05/09/2026 | Trần Khánh Chi | Sau review kỹ thuật (Agentic Engineering): thêm trường "Harness cần thiết" vào Skill Card (12 card, bổ sung PP-13); viết lại 5 Rule bất biến định lượng (PP-06, PP-13, PP-18, PP-28, PP-21) sang định dạng Given–When–Then (Gherkin); thêm cột "Nguồn dữ liệu tham chiếu" ở Giai đoạn 3.1; thêm cảnh báo chống "Context Rot" ở mục 9.6; mở rộng Data Fabrication Test (5.1) để kiểm tra cả nguồn dữ liệu chứ không chỉ output; thêm bước tự kiểm tra định kỳ ở Giai đoạn 10 (rút gọn từ mô hình Red Team, làm thủ công quy mô cá nhân). |

# Mục lục

- [Ghi chú sử dụng tài liệu](#ghi-chú-sử-dụng-tài-liệu)
- [GIAI ĐOẠN 1 — NGHIÊN CỨU SÂU & XÁC ĐỊNH PAIN POINT](#giai-đoạn-1--nghiên-cứu-sâu--xác-định-pain-point)
  - [1.1 Vì sao phải nghiên cứu sâu trước khi nghĩ đến tool](#11-vì-sao-phải-nghiên-cứu-sâu-trước-khi-nghĩ-đến-tool)
  - [1.2 Kỹ thuật thu thập Pain Point (áp dụng lên chính công việc mình)](#12-kỹ-thuật-thu-thập-pain-point-áp-dụng-lên-chính-công-việc-mình)
  - [1.3 Bộ câu hỏi Self-Interview theo từng Focus Area — mở rộng đến cấp Master](#13-bộ-câu-hỏi-self-interview-theo-từng-focus-area--mở-rộng-đến-cấp-master)
  - [1.4 Pain Point Inventory — Dữ liệu thật, dùng lâu dài](#14-pain-point-inventory--dữ-liệu-thật-dùng-lâu-dài)
- [GIAI ĐOẠN 2 — PHÂN TÍCH & ƯU TIÊN HÓA PAIN POINT](#giai-đoạn-2--phân-tích--ưu-tiên-hóa-pain-point)
  - [2.1 Ma trận Impact–Effort (chọn pain point nào làm trước)](#21-ma-trận-impacteffort-chọn-pain-point-nào-làm-trước)
- [GIAI ĐOẠN 3 — NGHIÊN CỨU & ĐỀ XUẤT CÔNG CỤ AI THEO TỪNG PAIN POINT](#giai-đoạn-3--nghiên-cứu--đề-xuất-công-cụ-ai-theo-từng-pain-point)
  - [3.1 Bản đồ Pain Point → Loại công cụ AI](#31-bản-đồ-pain-point--loại-công-cụ-ai)
  - [3.2 Scoring Rubric chọn công cụ AI (áp dụng cho công cụ PM)](#32-scoring-rubric-chọn-công-cụ-ai-áp-dụng-cho-công-cụ-pm)
  - [3.3 Recommendation Memo mẫu — PP-06 (Status Report Assistant)](#33-recommendation-memo-mẫu--pp-06-status-report-assistant)
- [GIAI ĐOẠN 4 — THIẾT KẾ THỬ NGHIỆM (PILOT) CHO TỪNG USE CASE](#giai-đoạn-4--thiết-kế-thử-nghiệm-pilot-cho-từng-use-case)
- [GIAI ĐOẠN 5 — TEST & KIỂM SOÁT CHẤT LƯỢNG](#giai-đoạn-5--test--kiểm-soát-chất-lượng)
  - [5.1 Bộ Test Case riêng cho AI hỗ trợ công việc PM](#51-bộ-test-case-riêng-cho-ai-hỗ-trợ-công-việc-pm)
  - [5.2 Nguyên tắc "Human-in-the-loop bắt buộc" theo cấp độ](#52-nguyên-tắc-human-in-the-loop-bắt-buộc-theo-cấp-độ)
- [GIAI ĐOẠN 6 — TÍCH HỢP VÀO QUY TRÌNH QUẢN LÝ DỰ ÁN THẬT](#giai-đoạn-6--tích-hợp-vào-quy-trình-quản-lý-dự-án-thật)
  - [6.1 Bảng "AI-Augmented PM Workflow" — quy trình cũ vs quy trình mới](#61-bảng-ai-augmented-pm-workflow--quy-trình-cũ-vs-quy-trình-mới)
  - [6.2 Nhịp độ tích hợp vào lịch làm việc tuần của PM](#62-nhịp-độ-tích-hợp-vào-lịch-làm-việc-tuần-của-pm)
- [GIAI ĐOẠN 7 — ĐÓNG GÓI THÀNH SOP VẬN HÀNH CHÍNH THỨC](#giai-đoạn-7--đóng-gói-thành-sop-vận-hành-chính-thức)
  - [7.1 Cấu trúc SOP cá nhân hóa (dùng lâu dài, cập nhật định kỳ)](#71-cấu-trúc-sop-cá-nhân-hóa-dùng-lâu-dài-cập-nhật-định-kỳ)
  - [7.2 Nguyên tắc đóng gói cuối cùng](#72-nguyên-tắc-đóng-gói-cuối-cùng)
- [GIAI ĐOẠN 8 — ĐO LƯỜNG HIỆU QUẢ SAU TRIỂN KHAI](#giai-đoạn-8--đo-lường-hiệu-quả-sau-triển-khai)
- [GIAI ĐOẠN 9 — PHỤ LỤC: SKILL CARD THEO USE CASE](#giai-đoạn-9--phụ-lục-skill-card-theo-use-case)
  - [9.1 Vì sao không dùng "Thư viện Prompt" tĩnh nữa](#91-vì-sao-không-dùng-thư-viện-prompt-tĩnh-nữa)
  - [9.2 Cấu trúc chuẩn của 1 Skill Card](#92-cấu-trúc-chuẩn-của-1-skill-card)
  - [9.3 Thư viện Skill Card — 12 use case đại diện cho 4 cấp độ](#93-thư-viện-skill-card--12-use-case-đại-diện-cho-4-cấp-độ)
  - [9.4 Bảng tổng hợp — 29 pain point, đóng gói Skill được không, mức tự chủ cho phép](#94-bảng-tổng-hợp--29-pain-point-đóng-gói-skill-được-không-mức-tự-chủ-cho-phép)
  - [9.5 Cách lưu Skill Card để dùng lại — không phụ thuộc 1 công cụ AI cụ thể](#95-cách-lưu-skill-card-để-dùng-lại--không-phụ-thuộc-1-công-cụ-ai-cụ-thể)
  - [9.6 Cảnh báo "Context Rot" — không nạp dồn nhiều Skill Card cùng lúc](#96-cảnh-báo-context-rot--không-nạp-dồn-nhiều-skill-card-cùng-lúc)
- [GIAI ĐOẠN 10 — QUẢN TRỊ RỦI RO & ĐẠO ĐỨC KHI PM DÙNG AI](#giai-đoạn-10--quản-trị-rủi-ro--đạo-đức-khi-pm-dùng-ai)
- [LỘ TRÌNH DÀI HẠN — TỪ PAIN POINT RIÊNG LẺ ĐẾN HỆ AGENT CHUYÊN BIỆT](#lộ-trình-dài-hạn--từ-pain-point-riêng-lẻ-đến-hệ-agent-chuyên-biệt)
- [TÓM TẮT QUY TRÌNH END-TO-END](#tóm-tắt-quy-trình-end-to-end)

# **Ghi chú sử dụng tài liệu**

Tài liệu này là bản SOP cá nhân — được chuyển từ khung Playbook tổng quát sang dữ liệu thật của chính công việc quản lý dự án. Giai đoạn 1–3 đã được thay hoàn toàn bằng 29 pain point thật (không còn bảng "mẫu điền"), trải đều từ cấp Cơ bản đến Chuyên sâu/Chiến lược.

Nguyên tắc xuyên suốt: cấp độ pain point càng cao thì vai trò AI càng chuyển từ "làm thay" (Automation) sang "hỗ trợ ra quyết định" (Augmentation) — không bao giờ để AI tự quyết định thay tại các điểm chiến lược (xem Giai đoạn 2 và Giai đoạn 10). Khi vận hành ở dạng AI Agent (tự động thu thập dữ liệu), mức tự chủ ra quyết định KHÔNG tự tăng lên — Checkpoint con người luôn giữ nguyên vị trí.

# **GIAI ĐOẠN 1 — NGHIÊN CỨU SÂU & XÁC ĐỊNH PAIN POINT**

## **1.1 Vì sao phải nghiên cứu sâu trước khi nghĩ đến tool**

Sai lầm phổ biến nhất: thấy tool AI hot rồi mới đi tìm chỗ để nhét vào. Thứ tự đúng phải là: hiểu quy trình đang chảy như thế nào → tìm điểm nghẽn/tốn thời gian/dễ sai sót → mới xét đến AI có giải quyết được không.

## **1.2 Kỹ thuật thu thập Pain Point (áp dụng lên chính công việc mình)**

| Kỹ thuật | Cách làm | Output |
| :---- | :---- | :---- |
| Time Audit | Ghi lại tất cả đầu việc trong 2 tuần làm việc thật, kèm thời gian tốn cho mỗi việc | Bảng thời gian theo hoạt động |
| Process Mapping | Vẽ lại toàn bộ quy trình PM đang làm theo 5 Focus Area (PMBOK) | Sơ đồ quy trình hiện tại |
| Self-Interview có cấu trúc | Tự trả lời bộ câu hỏi cố định (mục 1.3) cho từng Focus Area, từ việc cơ bản đến việc chiến lược | Danh sách pain point thô, đã phân cấp độ |
| Rà soát Artifact hiện có | Xem lại báo cáo, template, email đã gửi 3 tháng gần nhất — chỗ nào lặp cấu trúc giống nhau | Danh sách việc có thể chuẩn hóa/tự động hóa |
| So sánh Effort thực tế vs nên có | Với mỗi đầu việc, tự hỏi "việc này cần tư duy con người hay chỉ là tổng hợp/định dạng lại thông tin?" | Phân loại: Cần người vs Có thể máy hỗ trợ |

## **1.3 Bộ câu hỏi Self-Interview theo từng Focus Area — mở rộng đến cấp Master**

Bộ câu hỏi gốc chỉ dừng ở việc hành chính. Bản cập nhật thêm lớp câu hỏi cấp Nâng cao/Chiến lược để không bỏ sót pain point ở tầng ra quyết định — nơi giá trị tiết kiệm được là lớn nhất nhưng cũng rủi ro nhất nếu giao nhầm cho AI.

### **Initiating (Khởi tạo dự án)**

* Cơ bản: Soạn Charter/Business case mất bao lâu? Có phần nào lặp lại cấu trúc từ dự án trước không? (→ PP-01)

* Cơ bản: Xác định stakeholder ban đầu — có đang làm thủ công (hỏi từng người) không? (→ PP-02)

* Trung cấp: Với stakeholder phức tạp, có đang phân tích quyền lực/lợi ích một cách bài bản không, hay chỉ dựa cảm tính? (→ PP-08)

### **Planning (Lập kế hoạch)**

* Cơ bản: WBS cấp 1–2 có đang soạn lại từ đầu mỗi lần dù cấu trúc tương tự? (→ PP-03)

* Trung cấp: Risk Register ban đầu và RACI matrix — có đang tốn nhiều thời gian soạn từ số 0? (→ PP-09, PP-10)

* Nâng cao: Ước lượng thời gian/ngân sách — có dựa trên dữ liệu dự án cũ một cách hệ thống không, hay chủ yếu là kinh nghiệm cá nhân? (→ PP-15)

* Nâng cao: Khi nguồn lực bị giới hạn, việc tối ưu lịch trình (crashing/fast-tracking) có đang làm thủ công, mất nhiều vòng thử-sai? (→ PP-16)

### **Executing (Thực thi)**

* Cơ bản: Soạn email/thông báo cho stakeholder — có đang viết lại từ đầu mỗi lần dù nội dung tương tự? (→ PP-05)

* Cơ bản: Tổng hợp biên bản họp — có đang gõ tay trong lúc họp, dễ bỏ sót? (→ PP-04)

* Trung cấp: Với stakeholder khó tính/bất đồng, có đang mất nhiều thời gian soạn thông điệp thuyết phục? (→ PP-11)

* Nâng cao: Hồ sơ đấu thầu/đàm phán vendor — có đang tốn nhiều công sức nghiên cứu thị trường thủ công? (→ PP-17)

### **Monitoring & Controlling (Giám sát & Kiểm soát)**

* Cơ bản: Tổng hợp status update từ nhiều nguồn thành 1 báo cáo — mất bao lâu/tuần? (→ PP-06)

* Trung cấp: Phát hiện rủi ro — đang chủ động rà soát hay chỉ phản ứng khi vấn đề đã xảy ra? Change Request có đang được đánh giá tác động một cách nhất quán? (→ PP-12, PP-13)

* Nâng cao: Phân tích EVM (CPI/SPI/EAC) — có đang làm đều đặn hay chỉ làm khi bị hỏi? Phân tích định lượng rủi ro có đang bị bỏ qua vì quá phức tạp để làm tay? (→ PP-18, PP-20)

* Nâng cao: Xung đột giữa các phòng ban tranh giành nguồn lực — có công cụ/khung nào hỗ trợ chuẩn bị trước khi vào cuộc họp căng thẳng không? (→ PP-19)

### **Closing (Kết thúc)**

* Cơ bản/Trung cấp: Viết Lessons Learned, báo cáo tổng kết — có đang làm qua loa vì hết thời gian dự án không? (→ PP-07, PP-14)

### **Governance & Portfolio (cấp Chuyên sâu / Chiến lược — vượt ngoài 1 dự án đơn lẻ)**

* Tại các phase gate, quyết định go/no-go có đang dựa trên dữ liệu đầy đủ, được tổng hợp khách quan từ nhiều nguồn hay chỉ dựa trên báo cáo miệng? (→ PP-21)

* Khi phải ưu tiên nhiều dự án cùng lúc trong danh mục (portfolio), việc so sánh ROI/rủi ro giữa các dự án có đang làm bài bản hay chỉ theo cảm tính/áp lực chính trị nội bộ? (→ PP-22)

* Khi dự án tạo ra thay đổi lớn trong tổ chức, có đang có chiến lược quản trị thay đổi (change management) bài bản, hay chỉ thông báo và hy vọng mọi người thích nghi? (→ PP-23)

* Khi phải tái phân bổ ngân sách/nguồn lực giữa nhiều dự án hoặc chương trình, quyết định có đang dựa trên mô hình tài chính rõ ràng không? (→ PP-24)

## **1.4 Pain Point Inventory — Dữ liệu thật, dùng lâu dài**

### **1.4 Pain Point Inventory — dữ liệu thật, 4 cấp độ (Cơ bản → Chuyên sâu/Chiến lược)**

Đây là danh sách pain point thật của công việc quản lý dự án, được xây dựng theo đúng 5 Focus Area (PMBOK® Guide, Eighth Edition) và 7 Performance Domain (Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk). Mỗi pain point được gắn 1 trong 4 cấp độ năng lực để việc AI-hóa đi đúng lộ trình từ dễ đến khó, thay vì nhảy thẳng vào việc phức tạp/rủi ro cao.

* Cơ bản — việc hành chính, lặp lại, PM mới cũng làm được; AI có thể tự động hóa gần như hoàn toàn.

* Trung cấp — cần phán đoán nghiệp vụ nhẹ; AI đóng vai trò hỗ trợ (Assistance), PM vẫn kiểm tra kỹ.

* Nâng cao — nhiều biến số, ảnh hưởng cam kết với stakeholder; AI chỉ tăng cường năng lực phân tích (Augmentation), không thay quyết định.

* Chuyên sâu / Chiến lược — cấp Governance/Portfolio, tác động toàn tổ chức; AI tuyệt đối không được giao quyền quyết định, chỉ tổng hợp/mô phỏng dữ liệu đầu vào.

*Khung 3 cấp độ vai trò AI (Automation / Assistance / Augmentation) tham chiếu trực tiếp PMBOK® Guide — Eighth Edition, Appendix X3, mục X3.1.1 "Strategies for AI Adoption" (tr. 343).*

| Mã | Cấp độ | Domain / Focus Area | Pain point | Tần suất | Thời gian/lần | Khó chịu(1–5) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| PP-01 | Cơ bản | Initiating (Governance) | Soạn Project Charter / business case sơ bộ theo template có sẵn, tham chiếu dự án tương tự đã làm trước đó | Mỗi dự án mới | 2 giờ | 3 |
| PP-02 | Cơ bản | Initiating (Stakeholders) | Lập danh sách & thông tin liên hệ stakeholder ban đầu (tên, vai trò, phòng ban, kênh liên lạc) | Mỗi dự án mới | 1 giờ | 2 |
| PP-03 | Cơ bản | Planning (Scope) | Soạn WBS cấp 1–2 từ phạm vi (scope) đã thống nhất với khách hàng/sponsor | Mỗi dự án mới | 1,5 giờ | 2 |
| PP-04 | Cơ bản | Executing | Ghi biên bản họp trong lúc họp + soạn action item kèm người phụ trách/deadline | 3 lần/tuần | 30 phút/lần | 3 |
| PP-25 | Cơ bản | Executing | Soạn agenda trước mỗi cuộc họp quan trọng (mục tiêu, chủ đề, thời lượng từng phần) để họp đúng trọng tâm, tránh lan man | 3 lần/tuần | 10 phút/lần | 2 |
| PP-05 | Cơ bản | Executing (Stakeholders) | Soạn email cập nhật định kỳ (routine) cho stakeholder theo mẫu lặp lại | 2 lần/tuần | 20 phút/lần | 2 |
| PP-06 | Cơ bản | M&C (Governance) | Tổng hợp 5 status update rời rạc từ các Trưởng phòng thành 1 báo cáo tuần | Hàng tuần | 2 giờ | 4 |
| PP-07 | Cơ bản | Closing | Soạn checklist đóng dự án, thu hồi tài liệu/bàn giao vận hành | Cuối mỗi dự án | 1 giờ | 2 |
| PP-08 | Trung cấp | Initiating (Stakeholders) | Phân tích quyền lực/lợi ích (Power–Interest Grid) và mức độ ủng hộ cho stakeholder phức tạp | Mỗi dự án mới | 1,5 giờ | 3 |
| PP-09 | Trung cấp | Planning (Risk) | Soạn Risk Register ban đầu (định tính) cho dự án mới, dựa trên danh mục rủi ro chuẩn | Mỗi dự án mới | 3 giờ | 3 |
| PP-10 | Trung cấp | Planning | Xây dựng RACI matrix cho dự án có nhiều phòng ban tham gia | Mỗi dự án mới | 1 giờ | 2 |
| PP-26 | Trung cấp | Planning (Schedule) | Dựng khung Gantt chart nháp + xác định critical path ban đầu từ WBS/task list và thời lượng ước tính, trước khi tinh chỉnh trong công cụ lập lịch chuyên dụng | Mỗi dự án mới | 2 giờ | 3 |
| PP-11 | Trung cấp | Executing (Stakeholders) | Soạn email/thông điệp thuyết phục stakeholder khó tính, xử lý bất đồng nhẹ | 2 lần/tuần | 25 phút/lần | 4 |
| PP-12 | Trung cấp | M&C (Risk) | Chủ động rà soát & phát hiện rủi ro mới thay vì chỉ phản ứng khi vấn đề đã xảy ra | Hàng tuần | 1 giờ | 4 |
| PP-13 | Trung cấp | M&C (Governance) | Theo dõi Change Request, đánh giá sơ bộ tác động Scope/Schedule/Cost trước khi trình CCB | 1–2 lần/tuần | 45 phút/lần | 3 |
| PP-27 | Trung cấp | M&C | Khi có vấn đề phát sinh: phân tích nguyên nhân gốc (root cause, ví dụ khung fishbone/Ishikawa: People/Process/Tools/Environment) và so sánh các phương án xử lý theo Impact/Effort/Cost/Risk trước khi quyết định | Khi có vấn đề phát sinh | 1–2 giờ/lần | 3 |
| PP-28 | Trung cấp | Compliance / Governance | Rà soát tuân thủ (compliance) dự án theo quy định nội bộ/hợp đồng/pháp lý liên quan (VD: chính sách bảo mật dữ liệu, điều khoản hợp đồng, quy định ngành) trước các mốc quan trọng | Trước mỗi mốc quan trọng / theo quý | 2 giờ | 3 |
| PP-29 | Trung cấp | Quality | Soạn/rà soát Definition of Done (DoD) và tiêu chí nghiệm thu (acceptance criteria) cho từng deliverable, theo dõi defect/rework để giảm Cost of Quality | Mỗi deliverable/sprint | 1 giờ/lần | 3 |
| PP-14 | Trung cấp | Closing | Viết Lessons Learned + báo cáo tổng kết dự án từ nhiều nguồn tài liệu | Cuối mỗi dự án | 2 giờ | 2 |
| PP-15 | Nâng cao | Planning (Finance/Schedule) | Ước lượng effort/ngân sách dựa trên dữ liệu lịch sử nhiều dự án (analogous/parametric estimating) | Mỗi dự án mới | 4 giờ | 5 |
| PP-16 | Nâng cao | Planning (Schedule/Resources) | Tối ưu lịch trình khi nguồn lực bị giới hạn (resource leveling, crashing, fast-tracking, phân tích đánh đổi) | Khi có xung đột nguồn lực | 3 giờ | 5 |
| PP-17 | Nâng cao | Executing (Procurement) | Chuẩn bị hồ sơ đấu thầu/đàm phán vendor (RFP/RFQ, tiêu chí chọn nhà cung cấp) | Theo nhu cầu dự án | 4 giờ | 4 |
| PP-18 | Nâng cao | M&C (Finance) | Phân tích Earned Value Management: CPI, SPI, dự báo EAC/ETC/TCPI | Hàng tháng | 2 giờ | 4 |
| PP-19 | Nâng cao | Stakeholders | Xử lý xung đột đa bên khi nhiều phòng ban tranh giành nguồn lực chung | Không cố định | 2–3 giờ/lần | 5 |
| PP-20 | Nâng cao | Risk | Phân tích định lượng rủi ro (sensitivity analysis, tornado diagram, decision tree, mô phỏng) | Dự án rủi ro cao | 4 giờ | 5 |
| PP-21 | Chuyên sâu / Chiến lược | Governance | Ra quyết định go/no-go tại phase gate dựa trên nhiều nguồn dữ liệu mâu thuẫn nhau | Mỗi phase gate | 3 giờ chuẩn bị | 5 |
| PP-22 | Chuyên sâu / Chiến lược | Governance (Portfolio) | Ưu tiên hóa danh mục dự án (portfolio prioritization) khi tổ chức giới hạn nguồn lực | Theo quý | 1 ngày | 5 |
| PP-23 | Chuyên sâu / Chiến lược | Stakeholders (Change Mgmt) | Xây dựng chiến lược quản trị thay đổi tổ chức khi dự án tạo disruption lớn | Dự án chuyển đổi lớn | Nhiều ngày | 5 |
| PP-24 | Chuyên sâu / Chiến lược | Finance (Portfolio) | Phân tích đánh đổi ngân sách/nguồn lực đa dự án, đề xuất tái phân bổ giữa các chương trình | Theo quý hoặc khi khủng hoảng | 1 ngày | 5 |

### **Chú giải màu theo cấp độ**

| Màu | Cấp độ | Ý nghĩa |
| :---- | :---- | :---- |
| Xanh lá nhạt | Cơ bản | Automation — AI làm gần như toàn bộ, PM chỉ duyệt nhanh |
| Vàng nhạt | Trung cấp | Assistance — AI làm nháp, PM kiểm tra & bổ sung nghiệp vụ |
| Cam nhạt | Nâng cao | Augmentation — AI phân tích/mô phỏng, PM tự ra quyết định |
| Đỏ nhạt | Chuyên sâu / Chiến lược | Augmentation nghiêm ngặt — AI tuyệt đối không quyết định thay |

# **GIAI ĐOẠN 2 — PHÂN TÍCH & ƯU TIÊN HÓA PAIN POINT**

## **2.1 Ma trận Impact–Effort (chọn pain point nào làm trước)**

* Impact cao, Effort thấp, AI hỗ trợ dễ → LÀM TRƯỚC (Quick Win)

* Impact cao, Effort cao → LÀM SAU, cần chuẩn bị kỹ (dữ liệu lịch sử, prompt phức tạp, cơ chế duyệt)

* Impact thấp, Effort thấp → Làm khi rảnh, không ưu tiên

* Impact rất cao nhưng Effort rất cao VÀ rủi ro quyết định sai lớn (cấp Chuyên sâu/Chiến lược) → AI chỉ đóng vai Augmentation, KHÔNG BAO GIỜ để AI tự động hoàn toàn hay tự quyết định

| Mã | Pain point | Impact | Effort AI-hóa | Nhóm ưu tiên | Vai trò AI |
| :---- | :---- | :---- | :---- | :---- | :---- |
| PP-01 | Soạn Charter/business case theo template | Cao | Trung bình | Nhóm 2 — làm sau Quick Win | Assistance (Hỗ trợ) |
| PP-02 | Lập danh sách stakeholder ban đầu | Trung bình | Thấp | Quick Win | Automation (Tự động hóa) |
| PP-03 | Soạn WBS cấp 1–2 từ scope đã có | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-04 | Ghi biên bản họp + action item | Cao | Thấp | Quick Win | Automation |
| PP-25 | Soạn agenda trước họp | Trung bình | Thấp | Quick Win | Automation |
| PP-05 | Soạn email cập nhật định kỳ | Trung bình | Thấp | Quick Win | Automation |
| PP-06 | Tổng hợp status report tuần | Cao | Thấp | Quick Win — ưu tiên số 1 | Assistance |
| PP-07 | Checklist đóng dự án | Thấp | Thấp | Làm khi rảnh | Automation |
| PP-08 | Phân tích Power–Interest Grid | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-09 | Soạn Risk Register ban đầu | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-10 | Xây dựng RACI matrix | Trung bình | Thấp | Quick Win | Automation |
| PP-26 | Dựng Gantt & Critical Path nháp | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-11 | Email thuyết phục stakeholder khó tính | Trung bình–Cao | Thấp | Quick Win | Assistance |
| PP-12 | Chủ động phát hiện rủi ro mới | Cao | Trung bình | Nhóm 2 | Assistance |
| PP-13 | Theo dõi & đánh giá sơ bộ Change Request | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-27 | Phân tích nguyên nhân gốc & so sánh phương án xử lý | Trung bình–Cao | Trung bình | Nhóm 2 | Assistance |
| PP-28 | Rà soát tuân thủ (compliance) dự án | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-29 | Soạn DoD/tiêu chí nghiệm thu & theo dõi defect | Trung bình | Trung bình | Nhóm 2 | Assistance |
| PP-14 | Viết Lessons Learned & báo cáo tổng kết | Thấp–Trung bình | Thấp | Làm khi rảnh | Assistance |
| PP-15 | Ước lượng effort/ngân sách theo dữ liệu lịch sử | Cao nhưng ít xảy ra | Cao | Làm sau cùng — thận trọng nhất | Augmentation (KHÔNG giao quyết định) |
| PP-16 | Tối ưu lịch trình khi nguồn lực giới hạn | Cao | Cao | Làm sau, cần chuẩn bị kỹ | Augmentation |
| PP-17 | Chuẩn bị hồ sơ đấu thầu/đàm phán vendor | Trung bình | Cao | Làm sau | Assistance |
| PP-18 | Phân tích EVM (CPI/SPI/EAC/ETC) | Cao | Trung bình–Cao | Làm sau | Assistance |
| PP-19 | Xử lý xung đột đa bên tranh giành nguồn lực | Cao | Cao | Bỏ qua tự động hóa — chỉ dùng AI làm sparring partner | Augmentation (con người quyết định 100%) |
| PP-20 | Phân tích định lượng rủi ro | Cao | Cao | Làm sau, thận trọng | Augmentation |
| PP-21 | Ra quyết định go/no-go tại phase gate | Rất cao | Rất cao | KHÔNG giao AI quyết định — chỉ tổng hợp dữ liệu đầu vào | Augmentation (AI KHÔNG được quyết định) |
| PP-22 | Ưu tiên hóa danh mục dự án | Rất cao | Rất cao | AI chỉ hỗ trợ phân tích đa tiêu chí, con người quyết | Augmentation |
| PP-23 | Chiến lược quản trị thay đổi tổ chức | Rất cao | Rất cao | AI hỗ trợ research/soạn thảo, con người thiết kế chiến lược | Augmentation |
| PP-24 | Tái phân bổ ngân sách đa dự án/chương trình | Rất cao | Rất cao | AI mô phỏng kịch bản, con người quyết định cuối | Augmentation |

### **Nhận định — quy luật giữa cấp độ pain point và vai trò AI**

29 pain point trên cho thấy 1 quy luật rõ ràng: khi đi từ Cơ bản → Chuyên sâu/Chiến lược, vai trò của AI dịch chuyển từ Automation (tự động hóa gần như toàn bộ) sang Assistance (hỗ trợ soạn thảo/phân tích, PM luôn duyệt lại) rồi đến Augmentation (chỉ tăng cường năng lực phân tích và mô phỏng kịch bản, con người luôn là người quyết định cuối cùng). Đây chính là 3 cấp độ chiến lược áp dụng AI được PMBOK® Guide — Eighth Edition mô tả tại Appendix X3, mục X3.1.1 "Strategies for AI Adoption" (tr. 343\) và minh họa cụ thể theo mức độ phức tạp/nhu cầu giám sát con người tại mục X3.2 "Common Use Cases" (tr. 344).

*Nguyên tắc chọn thứ tự làm: Bắt đầu từ Quick Win (PP-02, PP-04, PP-05, PP-06, PP-10, PP-11, PP-25) để tạo momentum và niềm tin vào AI, trước khi động vào việc rủi ro cao như ước lượng effort (PP-15) hay quyết định go/no-go (PP-21) — vì sai ở tầng này ảnh hưởng trực tiếp đến cam kết với stakeholder hoặc tổ chức.*

# **GIAI ĐOẠN 3 — NGHIÊN CỨU & ĐỀ XUẤT CÔNG CỤ AI THEO TỪNG PAIN POINT**

## **3.1 Bản đồ Pain Point → Loại công cụ AI**

Cột "Ví dụ công cụ" bên dưới phân biệt 2 dạng công cụ, vì mức độ Human-in-the-loop cần thiết là khác nhau giữa hai dạng này:

* AI Assistant (trợ lý hỏi–đáp): PM tự tay paste dữ liệu vào, AI trả lời/soạn thảo trong 1 phiên hội thoại. Phù hợp giai đoạn mới bắt đầu pilot vì dễ kiểm soát, dễ dừng lại kiểm tra từng bước.

* AI Agent (tác nhân tự động): AI tự thực hiện nhiều bước và tự gọi các công cụ khác (đọc email, Drive, Jira/Atlassian, hệ thống tài chính...) để thu thập & xử lý dữ liệu mà không cần PM paste tay từng lần. Phù hợp khi pain point đã pilot ổn định ở dạng Assistant và PM đã tin tưởng vào chất lượng output.

*Nguyên tắc: mức tự động của AI Agent (được phép tự lấy dữ liệu tới đâu, có được tự gửi output đi hay không) phải đi cùng đúng cấp Automation/Assistance/Augmentation của từng pain point ở Giai đoạn 2 — lên Agent không đồng nghĩa với việc bỏ qua bước duyệt của con người, đặc biệt với nhóm Nâng cao/Chuyên sâu (PP-15 → PP-24).*

*Cột "Nguồn dữ liệu tham chiếu" (thêm ở v1.4) ghi rõ Agent/Assistant cần lấy dữ liệu từ đâu để trả lời — tách bạch rõ 2 việc khác nhau: Skill Card (Giai đoạn 9\) định nghĩa "làm như thế nào", còn nguồn dữ liệu định nghĩa "dùng dữ liệu gì". Không gộp chung 2 việc này vào 1 chỗ để tránh Skill Card phình to và khó bảo trì.*

| Mã | Loại công cụ cần tìm | Nguồn dữ liệu tham chiếu | Ví dụ công cụ (tham khảo) | Vai trò AI |
| :---- | :---- | :---- | :---- | :---- |
| PP-01 | AI assistant giữ context dự án dài hạn + kho template Charter cũ | Kho Charter/Business case dự án cũ (Drive) | Claude Projects/Cowork (upload Charter mẫu + business case cũ) | Assistance (Hỗ trợ) |
| PP-02 | AI trích xuất & chuẩn hóa thông tin liên hệ; AI Agent có thể tự lấy trực tiếp từ hộp thư/Drive thay vì phải paste tay | Email/tài liệu liên hệ dự án trước (Drive/Email) | Claude/ChatGPT (paste dữ liệu thô); nâng cấp: AI Agent qua MCP (Google Drive) tự quét tài liệu dự án cũ để dựng danh sách | Automation (Tự động hóa) |
| PP-03 | AI gợi ý decomposition theo cấu trúc WBS chuẩn | Scope Statement dự án hiện tại | Claude/ChatGPT + Project Scope Statement làm input | Assistance |
| PP-04 | AI ghi âm + tóm tắt cuộc họp; AI Agent có thể tự tạo issue/task trực tiếp trên hệ thống quản lý công việc, không chỉ dừng ở bản tóm tắt | Bản ghi âm/transcript cuộc họp | Otter.ai, Fireflies, Zoom/Meet AI note; nâng cấp: AI Agent (Claude + MCP Jira/Atlassian) tự tạo Jira issue từ action item sau khi PM duyệt | Automation |
| PP-25 | AI soạn agenda từ mục tiêu cuộc họp, có thể tham chiếu biên bản họp trước (PP-04) để tránh lặp chủ đề | Biên bản họp trước (nếu có) — tránh lặp chủ đề | Claude/ChatGPT (paste mục tiêu họp → agenda có timebox từng mục) | Automation |
| PP-05 | AI soạn thảo văn bản theo template/tone cố định | Không cần nguồn ngoài — nội dung PM tự cung cấp | Claude/ChatGPT với style guide đã lưu | Automation |
| PP-06 | Giai đoạn đầu: AI assistant giữ context (Charter, RAID log, báo cáo cũ), PM tự paste update. Giai đoạn trưởng thành: AI Agent tự vào Slack/Email/Jira lấy update, chỉ dừng lại hỏi PM khi thiếu dữ liệu | Charter + RAID Log + báo cáo tuần cũ (Claude Project); bản nâng cấp: Slack/Email/Jira | Claude Projects (paste tay) — xem Recommendation Memo ở mục 3.3; nâng cấp: AI Agent (Claude Cowork + MCP Slack/Email/Atlassian) tự thu thập update, PM chỉ duyệt bản nháp cuối | Assistance |
| PP-07 | AI tạo checklist từ template chuẩn + scope dự án | Template checklist chuẩn + Scope dự án | Claude/ChatGPT | Automation |
| PP-08 | AI hỗ trợ phân loại dựa trên dữ liệu tương tác đã ghi nhận | Ghi chú tương tác stakeholder đã có | Claude/ChatGPT + ghi chú tương tác stakeholder | Assistance |
| PP-09 | AI gợi ý theo Risk Breakdown Structure (RBS): Technical, Management, Commercial, External; AI Agent có thể tự quét tài liệu dự án (Charter, Scope, email) để đề xuất rủi ro thay vì PM tự mô tả lại | Risk Breakdown Structure (RBS) chuẩn + tài liệu dự án | Claude/ChatGPT + checklist RBS PMBOK; nâng cấp: AI Agent (MCP Google Drive) đọc trực tiếp bộ tài liệu dự án để đề xuất Risk Register nháp | Assistance |
| PP-10 | AI dựng bảng RACI từ danh sách hoạt động + vai trò | Danh sách hoạt động + sơ đồ tổ chức dự án | Claude/ChatGPT (skill xlsx nếu cần file Excel) | Automation |
| PP-26 | AI dựng bảng Gantt nháp (task, duration, dependency) + gợi ý critical path từ dữ liệu WBS, PM tự kiểm tra logic phụ thuộc trước khi đưa vào công cụ chính thức | WBS + ước tính thời lượng từng task | Claude/ChatGPT (dựng bảng nháp) + MS Project/Excel để tinh chỉnh & xác nhận chính thức | Assistance |
| PP-11 | AI soạn thảo theo phong cách giao tiếp (DISC) của từng stakeholder | Hồ sơ giao tiếp (DISC) từng stakeholder đã lưu | Claude/ChatGPT | Assistance |
| PP-12 | Use case điển hình cho AI Agent: cần tự động quét nhiều nguồn (status update, email, Jira) liên tục theo thời gian, không phải hỏi-đáp 1 lượt | Status update + email + Jira liên tục (qua MCP) | AI Agent (Claude Cowork/Claude Code + MCP Email/Atlassian) chạy định kỳ, gắn cờ dấu hiệu rủi ro sớm (leading indicators) cho PM rà soát; bản đơn giản hơn: Claude Projects (dùng chung context với PP-06) | Assistance |
| PP-13 | AI phân tích tác động dựa trên baseline hiện có; AI Agent có thể tự đọc issue mới trên hệ thống ticket và soạn nháp đánh giá tác động ngay khi Change Request được tạo | Scope/Schedule/Cost baseline hiện tại + Jira | Claude/ChatGPT + Scope/Schedule/Cost baseline; nâng cấp: AI Agent (MCP Atlassian Rovo) tự theo dõi Jira, soạn nháp đánh giá tác động cho từng CR mới | Assistance |
| PP-27 | AI hỗ trợ liệt kê nguyên nhân gốc theo khung fishbone + dựng bảng so sánh phương án có điểm số (Impact/Effort/Cost/Risk), PM tự quyết định phương án cuối | Mô tả vấn đề + dữ liệu liên quan (nếu có) | Claude/ChatGPT (paste mô tả vấn đề → gợi ý nguyên nhân gốc + bảng so sánh phương án) | Assistance |
| PP-28 | AI đối chiếu tài liệu dự án với checklist compliance chuẩn (nội bộ/hợp đồng), gắn cờ điểm thiếu sót; PM/bộ phận pháp lý luôn là người xác nhận cuối vì hậu quả pháp lý | Checklist compliance/hợp đồng do pháp lý cung cấp | Claude/ChatGPT + checklist compliance nội bộ; nâng cấp: AI Agent (MCP Drive/Atlassian) tự quét tài liệu dự án đối chiếu checklist | Assistance |
| PP-29 | AI soạn nháp DoD/tiêu chí nghiệm thu theo khung Quality Performance Domain + tổng hợp log defect/rework để tính xu hướng Cost of Quality; PM luôn quyết định deliverable đạt/không đạt | Template DoD/tiêu chí nghiệm thu + log defect (Jira) | Claude/ChatGPT + skill quality-delivery-control (DoD templates, CoQ framework); nâng cấp: AI Agent theo dõi defect log tự động từ Jira | Assistance |
| PP-14 | AI tổng hợp từ toàn bộ tài liệu dự án làm input; AI Agent có thể tự thu thập tài liệu rải rác trên Drive/email trước khi tổng hợp | Toàn bộ tài liệu dự án (Drive) | Claude/ChatGPT (PM tự tập hợp tài liệu); nâng cấp: AI Agent (MCP Google Drive) tự gom tài liệu dự án rồi soạn nháp Lessons Learned | Assistance |
| PP-15 | AI phân tích xu hướng từ dữ liệu lịch sử sạch, không giao toàn quyền quyết định | Dữ liệu lịch sử effort/ngân sách các dự án trước (Excel/Sheet) | Excel/Sheet dữ liệu lịch sử + AI phân tích xu hướng | Augmentation (KHÔNG giao quyết định) |
| PP-16 | AI mô phỏng kịch bản đánh đổi Scope/Schedule/Cost, con người chọn phương án | Lịch trình hiện tại + ràng buộc nguồn lực (MS Project/Excel) | Claude/ChatGPT phân tích what-if + công cụ lập lịch (MS Project/Excel) | Augmentation |
| PP-17 | AI soạn nháp RFP/RFQ + checklist tiêu chí đánh giá, PM tự thẩm định pháp lý; phù hợp AI Agent vì cần tự chạy nhiều bước research + tổng hợp trước khi ra bản nháp | Nghiên cứu thị trường + tiêu chí đánh giá vendor nội bộ | AI Agent (Claude Cowork, chế độ agentic research) tự tìm & so sánh nhà cung cấp trên web, soạn nháp RFP/RFQ; PM luôn tự thẩm định pháp lý trước khi phát hành | Assistance |
| PP-18 | AI tính công thức EVM chuẩn + diễn giải kết quả dễ hiểu cho sponsor; AI Agent có thể tự kéo số liệu actual cost/tiến độ từ hệ thống tài chính/Jira thay vì PM nhập tay mỗi tháng | Số liệu PV/EV/AC đã tính từ hệ thống tài chính/Excel | Excel có công thức EVM + Claude diễn giải; nâng cấp: AI Agent (MCP kết nối hệ thống tài chính/Atlassian) tự lấy số liệu, PM chỉ đối chiếu & duyệt trước khi gửi | Assistance |
| PP-19 | AI mô phỏng kịch bản đàm phán/phản biện trước khi PM vào cuộc họp thật | Ghi chú lịch sử tương tác giữa các phòng ban liên quan | Claude đóng vai các bên liên quan để PM luyện tập trước | Augmentation (con người quyết định 100%) |
| PP-20 | AI hỗ trợ dựng mô hình/diễn giải kết quả thống kê, PM kiểm tra giả định đầu vào | Dữ liệu rủi ro lịch sử + giả định đầu vào PM cung cấp | Excel/Python mô phỏng + Claude diễn giải | Augmentation |
| PP-21 | AI Agent tổng hợp đa nguồn dữ liệu mâu thuẫn (tài chính, tiến độ, rủi ro) thành bức tranh khách quan; AI KHÔNG được đưa ra khuyến nghị go/no-go, chỉ trình bày dữ kiện | Báo cáo tài chính + tiến độ + rủi ro từ nhiều nguồn (đa hệ thống) | AI Agent (Claude Cowork + MCP Drive/Atlassian/tài chính) tự kéo & đối chiếu dữ liệu từ nhiều hệ thống thành 1 bản tổng hợp cho PM/Sponsor quyết | Augmentation (AI KHÔNG được quyết định) |
| PP-22 | AI multicriteria decision analysis hỗ trợ so sánh ROI/rủi ro/chiến lược giữa các dự án | Danh sách dự án trong danh mục + tiêu chí ưu tiên tổ chức | Excel ma trận đa tiêu chí + Claude phân tích | Augmentation |
| PP-23 | AI research mô hình change management (Kotter, ADKAR) + soạn nháp kế hoạch truyền thông | Tài liệu văn hóa tổ chức + mô hình change management tham khảo | Claude Cowork research + soạn thảo kế hoạch | Augmentation |
| PP-24 | AI mô phỏng kịch bản tái phân bổ + tính tác động tài chính từng phương án | Mô hình tài chính đa dự án/chương trình | Excel mô hình tài chính + Claude phân tích kịch bản | Augmentation |

## **3.2 Scoring Rubric chọn công cụ AI (áp dụng cho công cụ PM)**

| Tiêu chí | Trọng số | Lưu ý riêng cho công cụ PM |
| :---- | :---- | :---- |
| Giải quyết đúng pain point | 30% | Ưu tiên tool giữ được context dài hạn của dự án, không phải chat rời rạc từng lần |
| Chi phí/ROI | 20% | So chi phí với giá trị giờ làm việc của chính PM bị tiết kiệm |
| Dễ dùng | 15% | PM tự dùng nên có thể chấp nhận learning curve cao hơn nhân viên khác 1 chút |
| Bảo mật/DPA | 20% | Quan trọng nhất với PM — dữ liệu dự án thường có thông tin nhạy cảm về ngân sách, đánh giá con người, thông tin khách hàng. Càng lên cấp Nâng cao/Chuyên sâu, mức độ nhạy cảm càng cao (PP-18, PP-21, PP-24) |
| Tích hợp | 10% | Có tích hợp được với công cụ đang dùng (Excel, Slack, email) không |
| Support | 5% | Ít quan trọng hơn vì PM tự vận hành, không cần support cho end-user khác |

## **3.3 Recommendation Memo mẫu — PP-06 (Status Report Assistant)**

1\. Vấn đề: Mất 2 giờ/tuần tổng hợp 5 status update thành báo cáo, dễ bỏ sót thông tin khi làm gấp cuối ngày.

2\. Lựa chọn: So sánh Claude Projects vs ChatGPT Projects vs làm thủ công tiếp tục — Claude Projects điểm cao nhất nhờ context window dài, giữ được toàn bộ tài liệu dự án (Charter, RAID log, báo cáo cũ) làm nền tham chiếu liên tục.

3\. Đề xuất: Dùng Claude Projects, tạo 1 project riêng cho mỗi dự án đang quản lý, upload sẵn Charter + RAID Log + mẫu báo cáo chuẩn.

4\. Chi phí: Gói cá nhân, quy đổi ROI: tiết kiệm khoảng 1 giờ/tuần ngay từ tuần đầu.

5\. Rủi ro: AI có thể làm dịu mức độ nghiêm trọng của rủi ro khi viết lại — cần bước duyệt thủ công phần Risk trước khi gửi (xem Human-in-the-loop, Giai đoạn 5.2).

6\. Bước tiếp theo: Pilot 2 tuần trước khi thay hoàn toàn cách làm cũ (xem Giai đoạn 4).

# **GIAI ĐOẠN 4 — THIẾT KẾ THỬ NGHIỆM (PILOT) CHO TỪNG USE CASE**

Áp dụng khung Plan → Test → Pilot → Feedback → Iterate → Gate cho từng Quick Win đã chọn ở Giai đoạn 2\. Bảng dưới tổng hợp SMART goal theo đúng mã pain point đã cập nhật, kèm 1 ví dụ cấp Nâng cao để thấy lộ trình phát triển sau khi Quick Win đã ổn định.

| Mã | Use case | SMART Goal | Thời gian pilot | Cách đo |
| :---- | :---- | :---- | :---- | :---- |
| PP-06 | Status report | Giảm 50% thời gian tổng hợp (2h → 1h) trong 2 tuần | 2 tuần | Bấm giờ thực tế trước/sau |
| PP-04 | Biên bản họp | Giảm 80% thời gian ghi chép tay, action item không sót | 2 tuần | So sánh biên bản AI vs check lại bằng trí nhớ |
| PP-11 | Email stakeholder khó tính | Giảm 50% thời gian soạn, giữ nguyên tỷ lệ phản hồi tích cực từ stakeholder | 3 tuần | Thời gian soạn + theo dõi phản hồi stakeholder có bất thường không |
| PP-18 | Phân tích EVM (Nâng cao) | AI tính đúng 100% công thức CPI/SPI/EAC so với tính tay, PM luôn tự duyệt trước khi báo cáo sponsor | 1 chu kỳ báo cáo tháng | Đối chiếu số liệu AI vs tính tay + log số lần phải sửa |

# **GIAI ĐOẠN 5 — TEST & KIỂM SOÁT CHẤT LƯỢNG**

## **5.1 Bộ Test Case riêng cho AI hỗ trợ công việc PM**

| Loại test | Vì sao quan trọng với PM | Ví dụ |
| :---- | :---- | :---- |
| Severity Distortion Test | AI có xu hướng viết "mềm" hơn thực tế để nghe xuôi tai | So sánh câu AI viết về 1 rủi ro Critical (PP-06, PP-09) — có còn giữ đúng mức độ nghiêm trọng không |
| Data Fabrication Test (mở rộng ở v1.4) | AI có thể bịa số liệu tiến độ nếu input không đủ — HOẶC tệ hơn: lấy đúng số nhưng từ nguồn sai. Kiểm tra output đúng chưa đủ, còn phải kiểm tra AI có thực sự dựa trên đúng nguồn đã cung cấp không | Cố tình đưa input thiếu 1 phần dữ liệu (PP-06, PP-18), xem AI có tự "đoán" điền vào không hay báo thiếu; định kỳ tự đối chiếu ngược 1–2 con số trong output với đúng nguồn gốc, không chỉ tin vì output nhìn hợp lý |
| Confidentiality Test | Dữ liệu dự án có thể có thông tin đánh giá con người, ngân sách nhạy cảm | Kiểm tra tool có lưu/dùng data để train lại model không (đọc kỹ điều khoản DPA, không đoán) |
| Consistency Test | Cùng 1 input, chạy 2 lần, kết quả có lệch nhau nhiều không | Chạy lại prompt PP-06 hoặc PP-18 hai lần, so sánh độ nhất quán số liệu |
| Tone/Audience Test | Báo cáo cho Sponsor/Ban điều hành khác giọng văn báo cáo nội bộ team | Test cùng nội dung PP-06 với 2 prompt khác nhau (dành cho cấp trên vs dành cho team) |

## **5.2 Nguyên tắc "Human-in-the-loop bắt buộc" theo cấp độ**

Khác với công cụ dành cho end-user khác, với vai trò PM, mức độ bắt buộc con người xác nhận tăng dần đúng theo 4 cấp độ pain point:

* Cơ bản (PP-01 → PP-07, PP-25): PM duyệt nhanh (spot-check), không cần kiểm tra từng chi tiết.

* Trung cấp (PP-08 → PP-14, PP-26 → PP-29): PM đọc kỹ toàn bộ trước khi gửi, đặc biệt phần đánh giá tác động/rủi ro.

* Nâng cao (PP-15 → PP-20): PM tự kiểm tra chéo mọi con số với nguồn gốc dữ liệu; AI chỉ được dùng để mô phỏng kịch bản, không đưa ra khuyến nghị cuối cùng mà không có review.

* Chuyên sâu/Chiến lược (PP-21 → PP-24): AI tuyệt đối không được tự động hoàn toàn ở các bước — quyết định mức độ rủi ro Critical/High, số liệu ngân sách/tiến độ gửi cấp trên, ưu tiên hóa danh mục dự án, và mọi nội dung liên quan đến đánh giá hiệu suất cá nhân trong team đều cần PM/Sponsor/CCB xác nhận cuối cùng.

# **GIAI ĐOẠN 6 — TÍCH HỢP VÀO QUY TRÌNH QUẢN LÝ DỰ ÁN THẬT**

## **6.1 Bảng "AI-Augmented PM Workflow" — quy trình cũ vs quy trình mới**

| Mã | Bước quy trình cũ | Bước có AI hỗ trợ | Tool | Checkpoint con người |
| :---- | :---- | :---- | :---- | :---- |
| PP-06 | Nhận status update rời rạc qua chat/email | AI Agent tự gom update từ Slack/Email/Jira vào 1 nơi (không cần PM paste tay từng phòng ban) → AI Project tổng hợp thành báo cáo nháp | Claude Cowork/Agent (MCP Slack/Email/Atlassian) + Claude Projects | PM đối chiếu nhanh xem Agent có gom thiếu phòng ban nào không, rồi mới duyệt & gửi báo cáo |
| PP-04 | Gõ tay biên bản họp trong lúc họp | Ghi âm → AI tóm tắt + trích action item | Otter.ai/Fireflies | PM xác nhận action item đúng người, đúng deadline |
| PP-09 | Viết Risk Register từ đầu | AI gợi ý theo Risk Breakdown Structure (RBS) chuẩn PMBOK → PM chọn lọc, bổ sung theo bối cảnh thật | Claude/ChatGPT + checklist RBS | PM luôn là người quyết định mức Impact/Probability cuối cùng |
| PP-11 | Soạn email thuyết phục stakeholder khó tính | AI soạn draft theo DISC profile của stakeholder đó | Claude/ChatGPT | PM chỉnh sửa câu chữ nhạy cảm trước khi gửi |
| PP-18 | Tính tay CPI/SPI/EAC mỗi tháng, dễ nhầm công thức | AI tính EVM tự động từ số liệu thô + diễn giải bằng ngôn ngữ cho sponsor | Excel công thức + Claude diễn giải | PM đối chiếu số liệu gốc trước khi đưa vào báo cáo chính thức |

## **6.2 Nhịp độ tích hợp vào lịch làm việc tuần của PM**

| Thứ / Chu kỳ | Hoạt động có AI hỗ trợ |
| :---- | :---- |
| Thứ 2 | AI Agent gom status update tuần trước từ Slack/Email/Jira → AI dựng khung báo cáo tuần, PM đối chiếu & duyệt (PP-06) |
| Thứ 3–5 | Mỗi cuộc họp quan trọng → bật ghi âm AI, cuối ngày duyệt lại biên bản (PP-04) |
| Thứ 6 | AI hỗ trợ soạn email tuần tới cho stakeholder cần theo dõi sát (PP-11) |
| Cuối tháng | AI hỗ trợ tính EVM + tổng hợp Monthly Report từ 4 báo cáo tuần đã có (PP-18) |
| Cuối quý (lộ trình tương lai, sau khi Quick Win đã thành thục) | Bắt đầu dùng AI hỗ trợ (không quyết định thay) cho rà soát portfolio và tái phân bổ ngân sách (PP-22, PP-24) — chỉ triển khai khi đã quen với nguyên tắc Human-in-the-loop ở mục 5.2 |

# **GIAI ĐOẠN 7 — ĐÓNG GÓI THÀNH SOP VẬN HÀNH CHÍNH THỨC**

## **7.1 Cấu trúc SOP cá nhân hóa (dùng lâu dài, cập nhật định kỳ)**

* Mục đích & Phạm vi: AI hỗ trợ những đầu việc nào trong quy trình PM của tôi (29 pain point ở Giai đoạn 1.4, phân theo 4 cấp độ)

* Công cụ chính thức đang dùng: Tên tool, gói đang trả phí, tài khoản

* Thư viện Skill Card chuẩn: xem Giai đoạn 9 — không soạn lại rule/prompt từ đầu mỗi lần

* Quy tắc Human-in-the-loop: theo đúng 4 cấp độ ở Giai đoạn 5.2, không được nới lỏng khi lên cấp Nâng cao/Chuyên sâu

* Quy trình xử lý khi AI sai: Log lại lỗi vào 1 file riêng để cải thiện Skill Card theo thời gian

* Lịch rà soát SOP: Mỗi quý xem lại — có pain point mới không, có tool tốt hơn xuất hiện không, có pain point nào đã "tốt nghiệp" lên cấp độ cao hơn không

## **7.2 Nguyên tắc đóng gói cuối cùng**

Một quy trình AI-augmented chỉ coi là "vận hành chính thức" khi: (1) không còn phải nhớ rule/prompt trong đầu — đã đóng gói thành Skill Card; (2) có quy tắc rõ ràng khi nào không dùng AI, đặc biệt tại các pain point cấp Nâng cao/Chuyên sâu; (3) đã đo được số liệu tiết kiệm thời gian thực tế qua ít nhất 1 chu kỳ đầy đủ (ví dụ: trọn 1 dự án hoặc 1 quý).

# **GIAI ĐOẠN 8 — ĐO LƯỜNG HIỆU QUẢ SAU TRIỂN KHAI**

| Chỉ số | Cách đo | Mục tiêu tham khảo |
| :---- | :---- | :---- |
| Thời gian tiết kiệm/tuần | Time audit lại sau 1 tháng, so với baseline ở Giai đoạn 1 | ≥30% thời gian các đầu việc Cơ bản/Trung cấp |
| Chất lượng báo cáo | Tự đánh giá hoặc hỏi Sponsor/cấp trên có thấy báo cáo rõ ràng hơn không | Không giảm chất lượng so với trước |
| Số lần AI sai phải sửa | Đếm qua log lỗi (SOP mục 7.1) | Xu hướng giảm dần theo thời gian, không tăng |
| Mức độ tự tin gửi báo cáo không cần double-check (cấp Cơ bản/Trung cấp) | Tự đánh giá chủ quan 1–5 | Tăng dần qua các tháng |
| Số pain point đã "tốt nghiệp" từ Assistance lên tự động hóa an toàn | So sánh danh sách Giai đoạn 1.4 mỗi quý | Tăng dần, nhưng KHÔNG áp dụng cho nhóm Chuyên sâu/Chiến lược (PP-21→24) |

# **GIAI ĐOẠN 9 — PHỤ LỤC: SKILL CARD THEO USE CASE**

## **9.1 Vì sao không dùng "Thư viện Prompt" tĩnh nữa**

Một đoạn prompt soạn sẵn để copy–paste có 3 điểm yếu: (1) phải nhớ paste đúng nguyên tắc mỗi lần — dễ quên hoặc rút gọn dần theo thời gian; (2) không có chỗ cố định để lưu context lặp lại (Charter, RAID log, phong cách giao tiếp từng stakeholder...), nên vẫn phải gõ tay từng phần mỗi lần dùng; (3) không portable — đổi công cụ AI là phải soạn lại từ đầu.

Skill Card giải quyết cả 3 điểm này: đóng gói 1 lần thành một gói cố định gồm Trigger (câu lệnh kích hoạt tự nhiên), Input cần thiết, Rule bất biến (nguyên tắc không được vi phạm dù input là gì), Output chuẩn, Checkpoint con người, và Harness cần thiết (kết nối dữ liệu nếu có). Sau khi đóng gói, chỉ cần gõ đúng Trigger — không soạn lại rule, không lệch chuẩn giữa các lần dùng.

*Rule bất biến có thể viết ở 2 dạng: ngôn ngữ tự nhiên (cho nguyên tắc định tính/phong cách, VD "giữ giọng theo DISC") hoặc Given–When–Then / Gherkin (cho nguyên tắc định lượng, có ngưỡng rõ ràng, VD "nếu chi phí vượt X% thì..."). Không ép cả 2 dạng vào cùng 1 khuôn — ép rule định tính sang Gherkin sẽ gượng và khó đọc hơn ngôn ngữ tự nhiên.*

## **9.2 Cấu trúc chuẩn của 1 Skill Card**

| Trường | Ý nghĩa |
| :---- | :---- |
| Trigger | Câu lệnh ngắn, tự nhiên để kích hoạt — không cần giải thích lại bối cảnh mỗi lần |
| Input cần thiết | Dữ liệu PM phải cung cấp khi gọi Skill (một số input là cố định, lưu sẵn — không phải nhập lại mỗi lần) |
| Rule bất biến | Nguyên tắc AI KHÔNG được vi phạm dù input thế nào — phần quan trọng nhất; viết bằng ngôn ngữ tự nhiên (định tính) hoặc Given–When–Then (định lượng, có ngưỡng) |
| Output chuẩn | Định dạng đầu ra cố định, để không phải mô tả lại cấu trúc mong muốn mỗi lần dùng |
| Checkpoint con người | Bước bắt buộc PM phải tự duyệt trước khi output được dùng chính thức — mức độ khắt khe tăng dần theo cấp độ pain point |
| Vai trò AI | Automation / Assistance / Augmentation — quyết định Skill được phép tự chủ tới đâu (xem Giai đoạn 2\) |
| Harness cần thiết | Kênh kết nối dữ liệu (MCP/API) nếu Skill vận hành ở dạng Agent, và có cần hỗ trợ kỹ thuật (developer) để thiết lập hay không — ghi rõ để không ngộ nhận tự dựng được một mình |

## **9.3 Thư viện Skill Card — 12 use case đại diện cho 4 cấp độ**

Không liệt kê hết 29 pain point ở dạng chi tiết (xem bảng tổng hợp ở mục 9.4) — 12 Skill Card dưới đây đại diện cho các dạng khác nhau: soạn thảo lặp lại (Cơ bản), tổng hợp có phán đoán và có ngưỡng định lượng (Trung cấp), phân tích cần dữ liệu chuẩn hóa (Nâng cao), và tổng hợp dữ liệu không khuyến nghị (Chuyên sâu).

### **Skill Card — PP-25: Soạn Agenda trước họp**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Soạn agenda cho họp \[tên họp\] ngày \[ngày\], thời lượng \[x\] phút" |
| Input cần thiết | Mục tiêu họp, danh sách người tham gia, các mục cần bàn (nếu có) |
| Rule bất biến | Mỗi mục phải có timebox cụ thể; tổng thời lượng agenda khớp đúng thời lượng họp; nếu chưa rõ mục tiêu họp, PHẢI hỏi lại trước khi soạn — không tự bịa mục tiêu |
| Output chuẩn | Bảng: Mục | Nội dung | Thời lượng | Người trình bày |
| Checkpoint con người | PM duyệt nhanh trước khi gửi người tham gia (spot-check) |
| Vai trò AI | Automation |
| Harness cần thiết | Không cần kết nối ngoài — chạy trong 1 phiên chat thông thường |

### **Skill Card — PP-04: Tóm tắt biên bản họp + Action Item**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Tóm tắt biên bản họp từ bản ghi sau" |
| Input cần thiết | Bản ghi âm/transcript cuộc họp |
| Rule bất biến | KHÔNG tự gán người phụ trách nếu transcript không nói rõ — ghi "chưa xác định"; không bỏ sót quyết định đã chốt; giữ nguyên số liệu/deadline được nhắc, không làm tròn hay suy đoán |
| Output chuẩn | 3 mục cố định: Quyết định đã chốt / Action item (người phụ trách, deadline) / Vấn đề còn bỏ ngỏ |
| Checkpoint con người | PM xác nhận đúng người, đúng deadline trước khi phân công chính thức |
| Vai trò AI | Automation |
| Harness cần thiết | Cần công cụ ghi âm (Otter.ai/Fireflies); bản nâng cấp tự tạo issue trên Jira cần MCP Atlassian — nên có hỗ trợ kỹ thuật để thiết lập kết nối 1 lần |

### **Skill Card — PP-05: Email cập nhật định kỳ**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Soạn email cập nhật tuần cho \[stakeholder\]" |
| Input cần thiết | Nội dung cần cập nhật, hồ sơ giao tiếp của người nhận (lưu sẵn, cập nhật khi cần) |
| Rule bất biến | Dưới 150 từ; không dùng thuật ngữ PM khó hiểu nếu người nhận ngoài ngành; giữ đúng tone đã lưu cho từng người nhận |
| Output chuẩn | Email hoàn chỉnh, có subject line |
| Checkpoint con người | PM đọc lướt trước khi gửi (rủi ro thấp, không cần kiểm tra sâu) |
| Vai trò AI | Automation |
| Harness cần thiết | Không cần kết nối ngoài |

### **Skill Card — PP-06: Tổng hợp Status Report tuần**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Tổng hợp status report tuần từ các update sau" |
| Input cần thiết | Context dự án cố định (Charter/RAID log — lưu 1 lần, không soạn lại mỗi tuần) + update thô từng phòng ban tuần này |
| Rule bất biến | Given thiếu update từ 1 phòng ban nào đó, When tổng hợp báo cáo tuần, Then ghi rõ "chưa có update" cho phòng ban đó — KHÔNG suy đoán số liệu thay thế. Given có rủi ro được nêu trong update gốc, When viết lại thành báo cáo, Then giữ nguyên mức độ nghiêm trọng, KHÔNG được làm dịu ngôn từ. |
| Output chuẩn | \[Phòng ban\]: \[Trạng thái Green/Yellow/Red\], \[Tóm tắt 1 câu\], \[Action cần làm\] |
| Checkpoint con người | PM đọc duyệt toàn bộ phần Risk/Issue trước khi gửi — bắt buộc, không được bỏ qua |
| Vai trò AI | Assistance |
| Harness cần thiết | Bản cơ bản: không cần kết nối ngoài (PM tự paste). Bản nâng cấp (Agent tự gom qua Slack/Email/Jira): cần MCP kết nối các nguồn này — nên có hỗ trợ kỹ thuật thiết lập |

### **Skill Card — PP-10: Dựng RACI Matrix**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Dựng RACI cho các hoạt động sau" |
| Input cần thiết | Danh sách hoạt động, danh sách vai trò/phòng ban liên quan |
| Rule bất biến | Mỗi hoạt động phải có đúng 1 người Accountable — không để trống, không gán nhiều hơn 1; nếu thiếu thông tin vai trò, hỏi lại thay vì tự gán |
| Output chuẩn | Bảng RACI chuẩn (Hoạt động × Vai trò) |
| Checkpoint con người | PM xác nhận vai trò Accountable đúng thực tế tổ chức |
| Vai trò AI | Automation |
| Harness cần thiết | Không cần kết nối ngoài |

### **Skill Card — PP-09: Gợi ý Risk Register ban đầu**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Gợi ý Risk Register cho dự án: \[mô tả\]" |
| Input cần thiết | Mô tả dự án, ngành, quy mô |
| Rule bất biến | Chỉ dựa trên 4 nhóm rủi ro chuẩn (Technical/Management/Commercial/External); LUÔN ghi rõ đây là gợi ý tham khảo; KHÔNG tự gán điểm Impact/Probability |
| Output chuẩn | Danh sách rủi ro theo 4 nhóm, mỗi rủi ro kèm mô tả ngắn |
| Checkpoint con người | PM luôn là người gán Impact/Probability — không giao cho AI |
| Vai trò AI | Assistance |
| Harness cần thiết | Không cần kết nối ngoài; bản nâng cấp dùng MCP Drive để tự đọc tài liệu dự án cần hỗ trợ kỹ thuật thiết lập 1 lần |

### **Skill Card — PP-11: Email thuyết phục stakeholder khó tính**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Soạn email gửi \[stakeholder\], phong cách DISC: \[D/I/S/C\]" |
| Input cần thiết | Hồ sơ giao tiếp stakeholder (lưu sẵn), nội dung cần truyền đạt |
| Rule bất biến | Dưới 150 từ; giữ đúng tone theo DISC; KHÔNG dùng câu có thể hiểu là cam kết chắc chắn (deadline, ngân sách...) nếu PM chưa xác nhận rõ |
| Output chuẩn | Email hoàn chỉnh |
| Checkpoint con người | PM luôn chỉnh câu chữ nhạy cảm trước khi gửi |
| Vai trò AI | Assistance |
| Harness cần thiết | Không cần kết nối ngoài |

### **Skill Card — PP-13: Đánh giá tác động Change Request**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Đánh giá tác động của Change Request sau lên Scope/Schedule/Cost" |
| Input cần thiết | Change Request mới, Scope/Schedule/Cost baseline hiện tại |
| Rule bất biến | Given Change Request tác động Cost \> 5% ngân sách còn lại HOẶC Schedule \> 3 ngày so với baseline, When đánh giá xong, Then gắn nhãn "Cần trình CCB" và liệt kê rõ mức tác động ước tính. Given tác động dưới ngưỡng trên, When đánh giá xong, Then vẫn ghi rõ số liệu tác động nhưng gắn nhãn "PM tự quyết theo thẩm quyền". Trong mọi trường hợp: KHÔNG tự phê duyệt hay từ chối Change Request — chỉ đánh giá & gắn nhãn. |
| Output chuẩn | Bảng: Change Request | Tác động Cost | Tác động Schedule | Nhãn (Cần CCB / PM tự quyết) |
| Checkpoint con người | PM xác nhận số liệu tác động đúng trước khi đưa vào cuộc họp CCB hoặc tự quyết |
| Vai trò AI | Assistance |
| Harness cần thiết | Không cần kết nối ngoài ở bản cơ bản; bản nâng cấp dùng MCP Atlassian Rovo để tự đọc Jira cần hỗ trợ kỹ thuật thiết lập |

### **Skill Card — PP-27: Root Cause & So sánh phương án**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Phân tích nguyên nhân gốc & so sánh phương án cho vấn đề: \[mô tả\]" |
| Input cần thiết | Mô tả vấn đề, các phương án đã nghĩ tới (nếu có) |
| Rule bất biến | Dùng khung fishbone (People/Process/Tools/Environment); mỗi điểm số trong bảng so sánh phải kèm giải thích giả định — không cho điểm mà không giải thích |
| Output chuẩn | Danh sách nguyên nhân gốc theo khung fishbone + bảng so sánh phương án (Impact/Effort/Cost/Risk/Score) |
| Checkpoint con người | PM tự chọn phương án cuối — AI chỉ trình bày so sánh, KHÔNG đề xuất "phương án tốt nhất" |
| Vai trò AI | Assistance |
| Harness cần thiết | Không cần kết nối ngoài |

### **Skill Card — PP-28: Rà soát Compliance**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Đối chiếu tài liệu dự án sau với checklist compliance: \[checklist\]" |
| Input cần thiết | Checklist compliance/hợp đồng do PM/bộ phận pháp lý cung cấp — AI KHÔNG tự tạo checklist |
| Rule bất biến | Given 1 điều khoản trong checklist compliance, When đối chiếu với tài liệu dự án, Then chỉ trả về 1 trong 3 trạng thái: "Đạt" / "Chưa rõ — cần bổ sung" / "Có dấu hiệu thiếu sót" — KHÔNG bao giờ trả về "Vi phạm" hay "Tuân thủ" (đây là kết luận pháp lý, chỉ bộ phận pháp lý được đưa ra). Given checklist không đề cập rõ 1 quy định, When rà soát, Then KHÔNG tự suy diễn quy định ngoài checklist đã cung cấp. |
| Output chuẩn | Bảng: Điều khoản | Trạng thái | Ghi chú |
| Checkpoint con người | Bộ phận pháp lý/PM luôn là người kết luận cuối cùng |
| Vai trò AI | Assistance |
| Harness cần thiết | Không cần kết nối ngoài; bản nâng cấp dùng MCP Drive/Atlassian để tự quét tài liệu cần hỗ trợ kỹ thuật |

### **Skill Card — PP-18: Diễn giải kết quả EVM (Nâng cao — dùng thận trọng)**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Diễn giải số liệu EVM tháng này: \[paste bảng\]" |
| Input cần thiết | Số liệu EVM đã tính sẵn bằng công thức chuẩn (PV, EV, AC, CPI, SPI, EAC, TCPI) — AI không tự tính |
| Rule bất biến | Given số liệu EVM (PV, EV, AC, CPI, SPI, EAC, TCPI) đã được PM cung cấp sẵn, When diễn giải, Then chỉ dùng đúng số liệu đó — KHÔNG tự tính lại hoặc suy đoán. Given CPI hoặc SPI \< 0.9, When diễn giải cho sponsor, Then phải nêu rõ đây là mức lệch đáng kể, KHÔNG được giảm nhẹ mức độ. Given thiếu bất kỳ số liệu nào trong 7 chỉ số trên, When được yêu cầu diễn giải, Then báo thiếu dữ liệu — KHÔNG tự điền giá trị giả định. |
| Output chuẩn | Diễn giải bằng ngôn ngữ phi kỹ thuật cho sponsor (nhanh/chậm bao nhiêu %, dự báo hoàn thành) |
| Checkpoint con người | PM đối chiếu số liệu gốc trước khi đưa vào báo cáo chính thức — bắt buộc |
| Vai trò AI | Augmentation |
| Harness cần thiết | Không cần kết nối ngoài ở bản diễn giải; bản tự động kéo số liệu tài chính cần MCP + hỗ trợ kỹ thuật — và nên cách ly việc TÍNH TOÁN trong Excel/công thức đã kiểm chứng, không giao AI tự tính |

### **Skill Card — PP-21: Tổng hợp dữ liệu cho quyết định go/no-go (Chuyên sâu — Data Synthesis)**

| Trường | Nội dung |
| :---- | :---- |
| Trigger | "Tổng hợp dữ liệu tài chính + tiến độ + rủi ro sau thành 1 bảng để tôi ra quyết định" |
| Input cần thiết | Báo cáo tài chính, tiến độ, rủi ro từ nhiều nguồn — kể cả khi các nguồn mâu thuẫn nhau |
| Rule bất biến | Given 2 nguồn dữ liệu trở lên có con số khác nhau cho cùng 1 chỉ tiêu (VD: tiến độ báo cáo bởi Trưởng phòng khác với số liệu trên Jira), When tổng hợp, Then liệt kê CẢ HAI số liệu kèm nguồn — KHÔNG tự chọn số nào đáng tin hơn để trình bày. Given đã tổng hợp xong toàn bộ dữ liệu, When trình bày kết quả, Then KHÔNG đưa ra khuyến nghị go/no-go hay bất kỳ hình thức gợi ý quyết định nào — chỉ trình bày dữ kiện khách quan. |
| Output chuẩn | Bảng tổng hợp khách quan theo từng tiêu chí, có mục riêng "Điểm dữ liệu mâu thuẫn cần làm rõ" |
| Checkpoint con người | PM/Sponsor là người duy nhất ra quyết định cuối — Skill này KHÔNG được thiết kế lại thành "trợ lý tư vấn quyết định" |
| Vai trò AI | Augmentation (không quyết định) |
| Harness cần thiết | Cần MCP kết nối nhiều nguồn (tài chính/tiến độ/rủi ro) — bắt buộc có hỗ trợ kỹ thuật; do dữ liệu nhạy cảm cấp chiến lược, ưu tiên kiểm tra chính sách bảo mật dữ liệu của nhà cung cấp MCP trước khi kết nối |

## **9.4 Bảng tổng hợp — 29 pain point, đóng gói Skill được không, mức tự chủ cho phép**

| Mã | Pain point | Đóng gói Skill được không & mức tự chủ |
| :---- | :---- | :---- |
| PP-01 | Soạn Charter/business case theo template | Có — tự chủ cao (Automation) |
| PP-02 | Lập danh sách stakeholder ban đầu | Có — tự chủ cao (Automation) |
| PP-03 | Soạn WBS cấp 1–2 từ scope đã có | Có — tự chủ cao (Automation) |
| PP-04 | Ghi biên bản họp + action item | Có — tự chủ cao (Automation) |
| PP-25 | Soạn agenda trước họp | Có — tự chủ cao (Automation) |
| PP-05 | Soạn email cập nhật định kỳ | Có — tự chủ cao (Automation) |
| PP-06 | Tổng hợp status report tuần | Có — tự chủ cao (Automation) |
| PP-07 | Checklist đóng dự án | Có — tự chủ cao (Automation) |
| PP-08 | Phân tích Power–Interest Grid | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-09 | Soạn Risk Register ban đầu | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-10 | Xây dựng RACI matrix | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-26 | Dựng Gantt & Critical Path nháp | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-11 | Email thuyết phục stakeholder khó tính | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-12 | Chủ động phát hiện rủi ro mới | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-13 | Theo dõi & đánh giá sơ bộ Change Request | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-27 | Phân tích nguyên nhân gốc & so sánh phương án xử lý | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-28 | Rà soát tuân thủ (compliance) dự án | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-29 | Soạn DoD/tiêu chí nghiệm thu & theo dõi defect | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-14 | Viết Lessons Learned & báo cáo tổng kết | Có — tự chủ trung bình (Assistance), luôn có checkpoint |
| PP-15 | Ước lượng effort/ngân sách theo dữ liệu lịch sử | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-16 | Tối ưu lịch trình khi nguồn lực giới hạn | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-17 | Chuẩn bị hồ sơ đấu thầu/đàm phán vendor | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-18 | Phân tích EVM (CPI/SPI/EAC/ETC) | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-19 | Xử lý xung đột đa bên tranh giành nguồn lực | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-20 | Phân tích định lượng rủi ro | Có, giới hạn (Augmentation) — không tự động hoàn toàn, cần input đã chuẩn hóa |
| PP-21 | Ra quyết định go/no-go tại phase gate | Có, nhưng CHỈ dạng Data Synthesis — không bao giờ đưa khuyến nghị/kết luận |
| PP-22 | Ưu tiên hóa danh mục dự án | Có, nhưng CHỈ dạng Data Synthesis — không bao giờ đưa khuyến nghị/kết luận |
| PP-23 | Chiến lược quản trị thay đổi tổ chức | Có, nhưng CHỈ dạng Data Synthesis — không bao giờ đưa khuyến nghị/kết luận |
| PP-24 | Tái phân bổ ngân sách đa dự án/chương trình | Có, nhưng CHỈ dạng Data Synthesis — không bao giờ đưa khuyến nghị/kết luận |

## **9.5 Cách lưu Skill Card để dùng lại — không phụ thuộc 1 công cụ AI cụ thể**

* Nếu công cụ AI đang dùng có tính năng lưu ngữ cảnh/hướng dẫn cố định cho 1 không gian làm việc riêng (project, custom instruction, system prompt...): lưu nguyên văn cột "Rule bất biến" + "Output chuẩn" vào đó — từ lần sau chỉ cần gõ đúng Trigger.

* Nếu công cụ chưa hỗ trợ tính năng này: lưu toàn bộ Skill Card (mục 9.3) thành 1 file tham chiếu cố định, mở kèm khi bắt đầu phiên làm việc — vẫn nhanh hơn nhiều so với soạn lại rule từ trí nhớ.

* Rà soát lại Skill Card cùng lịch rà soát SOP mỗi quý (Giai đoạn 7.1): Rule nào hay bị AI vi phạm → viết rõ hơn (cân nhắc chuyển sang Given–When–Then nếu là rule định lượng); Skill nào đã đủ tin cậy → cân nhắc nới Checkpoint theo đúng nguyên tắc ở Giai đoạn 5.2.

## **9.6 Cảnh báo "Context Rot" — không nạp dồn nhiều Skill Card cùng lúc**

Mỗi Skill Card được thiết kế để dùng RIÊNG theo đúng Trigger của nó, không phải để nạp cả 29 card cùng lúc vào 1 project/system prompt. Nạp dồn nhiều bộ Rule khác nhau vào cùng 1 ngữ cảnh dễ khiến AI nhầm lẫn quy tắc giữa các use case (VD: áp nhầm rule của PP-11 khi đang làm PP-06), hoặc bỏ sót chỉ dẫn quan trọng do bị loãng giữa quá nhiều nội dung.

* Nguyên tắc: 1 Skill Card = 1 context riêng (1 project/1 phiên chat), chỉ nạp đúng Skill Card cần dùng cho việc đang làm.

* Nếu dùng chung 1 project cho nhiều Skill Card liên quan (VD: PP-06 và PP-12 đều dùng chung context dự án), nên ghi rõ ranh giới giữa các Rule bất biến của từng Skill trong cùng project đó, tránh để AI trộn lẫn.

* Nếu số lượng Skill Card cần dùng thường xuyên tăng lên nhiều, cân nhắc giữ 1 danh sách "Skill đang hoạt động" ngắn gọn (tên + Trigger, không kèm Rule chi tiết) để dễ chọn đúng Skill trước khi mở đầy đủ nội dung — đây là bản rút gọn, làm thủ công, của ý tưởng "chỉ nạp thông tin cần thiết khi cần".

# **GIAI ĐOẠN 10 — QUẢN TRỊ RỦI RO & ĐẠO ĐỨC KHI PM DÙNG AI**

| Rủi ro | Nguyên tắc phòng ngừa |
| :---- | :---- |
| Rò rỉ dữ liệu nhạy cảm (ngân sách, đánh giá con người) qua AI | Không paste thông tin định danh cá nhân trực tiếp nếu tool không có DPA rõ ràng; ẩn danh khi có thể |
| Phụ thuộc quá mức, mất kỹ năng tự phân tích | Định kỳ (ví dụ: mỗi quý) tự làm 1 báo cáo hoàn toàn thủ công để giữ phản xạ nghề nghiệp, đặc biệt với các pain point Nâng cao (PP-15 → PP-20) |
| Báo cáo lên cấp trên bị sai lệch do AI làm dịu vấn đề | Luôn tự đọc lại phần Risk/Issue trước khi gửi, không bao giờ gửi thẳng 100% nội dung AI-generated cho thông tin nhạy cảm |
| Stakeholder phát hiện email/báo cáo "có mùi AI", giảm tin tưởng | Luôn chỉnh sửa lại bằng giọng văn cá nhân, AI chỉ là bản nháp, không phải bản gửi cuối |
| Giao AI quyết định thay tại các điểm chiến lược (go/no-go, portfolio, tái phân bổ ngân sách, đánh giá con người) | Nguyên tắc bất di bất dịch cho nhóm PP-21 → PP-24: AI chỉ tổng hợp/mô phỏng, KHÔNG BAO GIỜ là người quyết định cuối cùng. Mọi quyết định chiến lược luôn có bước escalation lên PM/Sponsor/CCB với xác nhận con người rõ ràng, có thể truy vết |
| Chưa từng tự kiểm tra xem Rule bất biến có bị "lách" bởi input bất thường không (v1.4) | Mỗi quý, PM tự đóng vai "kẻ phá hoại": thử đưa input mơ hồ/mâu thuẫn/thiếu vào 1 Skill Card đang dùng thường xuyên để xem AI có tuân thủ đúng Rule không hay bị lách; nếu bị lách, viết lại Rule rõ hơn (rút gọn từ mô hình Red Team, làm thủ công ở quy mô cá nhân, không cần hạ tầng riêng) |

# **LỘ TRÌNH DÀI HẠN — TỪ PAIN POINT RIÊNG LẺ ĐẾN HỆ AGENT CHUYÊN BIỆT**

Xu hướng ngành đang hướng tới môi trường doanh nghiệp có nhiều AI agent chuyên biệt phối hợp với nhau: Planning Agent, Risk Agent, Finance Agent, Compliance Agent, Procurement Agent, Scheduling Agent, Reporting Agent, Documentation Agent, Quality Agent. Đây là tầm nhìn cấp tổ chức, không phải thứ SOP cá nhân này cần dựng ngay — nhưng nên có bản đồ định hướng để biết cụm pain point nào sẽ gộp lại thành agent nào khi năng lực và hạ tầng đã sẵn sàng.

| Agent tương lai | Pain point sẽ gộp vào | Điều kiện tiên quyết trước khi lên cấp Agent chuyên biệt |
| :---- | :---- | :---- |
| Planning Agent | PP-01, 03, 08, 09, 10, 15, 16, 26 | Đã pilot ổn định từng pain point riêng lẻ ở mức Assistance; có kho dữ liệu lịch sử dự án đủ sạch cho PP-15 |
| Scheduling Agent | PP-03, 16, 26 | Có công cụ lập lịch tích hợp (MS Project/Jira) để agent đọc/ghi trực tiếp, không chỉ dựng bảng nháp |
| Risk Agent | PP-09, 12, 20 | Có nguồn dữ liệu liên tục (status update, email, Jira) để agent quét theo thời gian thực; đã qua Severity Distortion Test nhiều lần (Giai đoạn 5.1) |
| Finance Agent | PP-15, 18, 24 | Có hệ thống tài chính có API hoặc dữ liệu chuẩn hóa; công thức EVM/mô hình tài chính đã được PM kiểm chứng đủ tin cậy |
| Compliance Agent | PP-28 | Có checklist compliance/hợp đồng được số hóa, cập nhật thường xuyên bởi bộ phận pháp lý |
| Procurement Agent | PP-17 | Có quy trình đấu thầu chuẩn hóa, tiêu chí đánh giá vendor rõ ràng, không thay đổi tùy hứng theo từng lần |
| Reporting Agent | PP-06, 14 | Đã đạt mức tự tin cao ở Giai đoạn 8 với báo cáo do AI hỗ trợ; tổ chức chấp nhận báo cáo bán tự động |
| Documentation Agent | PP-01, 07, 14 | Có kho template/tài liệu dự án được chuẩn hóa, cấu trúc nhất quán giữa các dự án |
| Quality Agent | PP-29 | Có DoD/tiêu chí nghiệm thu số hóa theo từng loại deliverable, log defect được ghi nhận có hệ thống |

*Nguyên tắc bất biến dù có bao nhiêu agent: mọi quyết định go/no-go, mức độ rủi ro Critical/High, số liệu gửi cấp trên (PP-21 → PP-24) vẫn luôn cần con người xác nhận — đúng nguyên tắc Human-in-the-loop ở Giai đoạn 5.2 và Giai đoạn 10\. Multi-agent chỉ thay đổi CÁCH thu thập/tổng hợp dữ liệu, không thay đổi những gì AI được phép tự quyết định.*

*Không nên triển khai một nền tảng multi-agent orchestration thật (kiểu Agent Manager của các IDE agentic hiện nay), cũng như hạ tầng cấp production (sandbox cách ly, tracing OpenTelemetry, LM Judge riêng, Red/Blue/Green Team, Vector DB/Graph RAG) trước khi từng pain point riêng lẻ đã ổn định ở mức Assistance/Automation qua pilot thật và có hỗ trợ kỹ thuật (developer) đi kèm. Đây là hạ tầng cấp tổ chức, vượt quy mô 1 PM vận hành solo — nhảy thẳng vào sẽ nhân rủi ro sai sót lên nhiều lần thay vì giảm, đi ngược nguyên tắc Quick Win trước, việc rủi ro cao làm sau của Giai đoạn 2\.*

# **TÓM TẮT QUY TRÌNH END-TO-END**

* 1\. Nghiên cứu sâu (Time Audit + Process Mapping + Self-Interview theo 4 cấp độ)

* 2\. Ưu tiên hóa (Ma trận Impact–Effort → chọn Quick Win trước, gắn vai trò AI Automation/Assistance/Augmentation)

* 3\. Đề xuất tool (Scoring Rubric riêng cho PM + Recommendation Memo + Nguồn dữ liệu tham chiếu)

* 4\. Pilot từng use case (Plan–Test–Pilot–Feedback–Iterate–Gate)

* 5\. Test chuyên sâu (Severity Distortion, Fabrication, Confidentiality...) + Human-in-the-loop theo cấp độ

* 6\. Tích hợp vào lịch làm việc thật (bảng Workflow cũ vs mới + nhịp độ tuần/quý)

* 7\. Đóng gói SOP cá nhân (Skill Card library + Human-in-the-loop rules)

* 8\. Đo lường & rà soát định kỳ (mỗi quý)

*Ghi chú sử dụng tài liệu: Đây là SOP thật — 29 pain point ở Giai đoạn 1–3 phản ánh đúng phổ công việc quản lý dự án từ Cơ bản đến Chuyên sâu/Chiến lược theo PMBOK® Guide, Eighth Edition. Cập nhật lại bảng ở Giai đoạn 1.4 mỗi quý khi có pain point mới hoặc khi 1 pain point đã "tốt nghiệp" sang mức độ tự động hóa cao hơn.*
