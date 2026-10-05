# AI Support Log

## Tổng quan

- **Công cụ/model AI:** Cursor, dùng để dựng prototype và điền báo cáo. Model trả lời trong prototype là GPT-4o mini (`OPENAI_MODEL` trong `.env.example`).
- **Thời gian sử dụng:** 05/10/2026, trong repo Track1 Day 19.
- **Mục đích sử dụng:** Dựng Smart AI Note, chỉnh format design sheet, điền các file báo cáo từ dữ liệu đã có.

## Nhật ký hỗ trợ

| # | AI được dùng để làm gì | AI đã đề xuất/tạo ra | Tôi đã sử dụng phần nào | Tôi đã tự sửa/ra quyết định gì |
|---|---|---|---|---|
| 1 | Dựng prototype Option C | Màn chia đôi, lưu đoạn bằng màu, API ngữ cảnh, chat chỉ đọc note đã lưu, deploy Vercel | Giữ split-screen, Sửa/Đóng AI Context, và câu từ chối khi hỏi ngoài note | Giữ GPT-4o mini chỉ giải thích 2–3 câu từ đoạn được cung cấp. Không cho AI bịa số liệu hay trả lời cả bài. |
| 2 | Điền mô tả Option C | Bản mô tả ngắn cho design sheet trước khi có bảng so sánh | Cách hoạt động và flow chọn đoạn → AI Context → chat | Thay bằng bảng A/B/C do người nộp đưa: A truy xuất theo yêu cầu, B checkpoint 5 mục, C ngữ cảnh ngay lúc lưu. |
| 3 | Điền file báo cáo | Có nguy cơ viết observation và quote tester cho đủ form | Phần mô tả option, link A và C, giả định cần test, và nhật ký AI | Không điền feedback giả. Các mục observation để trạng thái “chưa có phiên”. |

## AI làm tốt ở đâu?

AI dựng được prototype chạy được: chọn đoạn, gọi `/api/context`, và chat `/api/ask` bám note đã lưu. AI cũng tách bảng bốn cột thành các mục A/B/C dễ đọc mà không đổi nội dung so sánh.

## AI sai hoặc hời hợt ở đâu?

AI không có nguyên văn hypothesis Day 18, tên nhóm, link Option B, hay một phiên test nào. Nếu viết quote tester hoặc kết luận “user đã xác nhận option”, phần đó sẽ là bịa. Bản hypothesis trong README chỉ là câu làm việc rút từ design sheet, không phải lời Day 18.

## Tôi đã tự sửa và kiểm chứng như thế nào?

Đối chiếu README và các file feedback với design sheet, `prototype-link.md`, và code trong `demo_option_c/` cùng `lib/openai.js`. Chỗ nào không có trong các nguồn đó thì ghi “chưa có”, không suy diễn thêm.

## Human–AI decision log

Người nộp giữ quyết định: chat Option C phải từ chối câu ngoài note, và user phải sửa hoặc đóng được AI Context. AI không được viết observation, feedback, hay chốt hypothesis thay nhóm.
