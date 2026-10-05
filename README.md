# Day 19 — Three Solution Options & Prototype Feedback

## 1. Thông tin cá nhân và nhóm

- **MHV:** 2A202602639
- **Họ và tên:** Tô Anh Đức
- **Các thành viên:**
  - Tô Anh Đức — 2A202602639 — Option C
  - Dương Hải Minh — 2A202602680 — Option A
  - Đỗ Trương Thành Ân — 2A202602899 — Option B
- **Case/Challenge:** AI Notes. Ba option cùng xử lý việc người học mất ngữ cảnh của đoạn đã highlight.

## 2. Hypothesis Problem

Hypothesis làm việc, rút từ phần chung của ba option trong [three-option-design-sheet.md](three-option-design-sheet.md):

> Khi đang học hoặc ôn lại, người học gặp khó trong việc khôi phục ngữ cảnh của đoạn đã highlight hoặc đã ghi, vì đoạn đó bị tách khỏi bài xung quanh, nên họ quên vì sao mình đánh dấu và khó học tiếp.

**Đối tượng chính:** Người học đang đọc bài giảng, slide hoặc PDF và có highlight hoặc take-note.  
**Nhu cầu/vấn đề:** Lấy lại ngữ cảnh của ý đã đánh dấu mà không phải đọc lại cả bài.  
**Bối cảnh:** Trong buổi học hoặc lúc ôn. Ba option khác nhau ở thời điểm AI lên tiếng: lúc ôn theo lệnh (A), khi đủ 5 mục (B), hoặc ngay lúc lưu note (C).

## 3. Three Solution Options

| Option | Mô tả ngắn | Prototype |
|---|---|---|
| **A** | Lúc ôn, user bấm highlight và gọi "Explain Context". AI đọc đoạn trước/sau rồi tóm tắt 1–2 câu. | [Margin](https://minhdh329.github.io/Track1_Day19_2A202602680_DuongHaiMinh/) |
| **B** | AI đếm highlight và bullet take-note. Đủ 5 mục thì hỏi tổng hợp ngay hay hoãn đến cuối buổi, kèm vị trí nguồn. | [Checkpoint](https://track1day192a202602899dotruongthanhan-production.up.railway.app/) |
| **C** | Đang đọc, user gắn màu để lưu thì AI viết 2–3 câu ngữ cảnh. Chat chỉ trả lời từ note đã lưu và ngữ cảnh đó. | [Smart AI Note](https://ainote-itt9q3xqj-anhduc0712s-projects.vercel.app/) |

Chi tiết cơ chế, trigger và trade-off: [three-option-design-sheet.md](three-option-design-sheet.md)  
Danh sách link: [prototype-link.md](prototype-link.md)

## 4. Đóng góp của tôi trong nhóm

- **Option/area phụ trách:** Option C — Smart AI Note (màn chia đôi, lưu đoạn bằng màu, AI Context, chat chỉ trong note đã lưu).
- **Shared context/content đã đóng góp:** Prototype `demo_option_c/`, API `/api/context` và `/api/ask`, bản deploy Vercel, và phần Option C trong design sheet.
- **Human–AI decisions:** AI dựng khung prototype. Tôi giữ cơ chế AI chỉ giải thích đoạn vừa lưu, chat từ chối câu ngoài note, và user được Sửa hoặc Đóng AI Context. Phiếu test và bảng tổng hợp lấy từ ghi chép của nhóm, không do AI viết quote.
- **Facilitation:** Tôi điều phối phiên 05/10/2026 với tester Trần Đình Hinh (2A202602399).
- **Observation:** Tester cố highlight đoạn cần note, không có điểm lúng túng được ghi, có kiểm tra nguồn, và dùng nút tắt trên AI khi kết quả chưa ưng. Tester chọn Option A.
- **Tổng hợp feedback:** Phiếu của tôi là phiếu 3 trong [prototype-feedback-note.md](prototype-feedback-note.md). Đối chiếu cả ba phiếu nằm ở [group-feedback-synthesis.md](group-feedback-synthesis.md).

## 5. Prototype Feedback

### Observation từ phiên tôi facilitate

Phiên 05/10/2026, tester Trần Đình Hinh, trên cả ba option:

- Hành động đầu: cố highlight đoạn cần note.
- Không ghi nhận chỗ lúng túng.
- Có kiểm tra lại nguồn.
- Khi chưa ưng câu trả lời, dùng nút tắt trên AI.
- Chọn Option A. Lý do ghi trong phiếu: sẵn sàng bớt độ chi tiết để đổi lấy sự tiện lợi.
- Điểm ngược kỳ vọng: tester này ưu tiên tiện lợi, trong khi tester của phiếu 1 chọn phương án chi tiết hơn.

### Three-feedback synthesis

1. **Không có option chiếm đa số.** Mỗi option được chọn một lần: phiếu 1 chọn B, phiếu 2 chọn C (và nói thêm thích phần tổng hợp của B), phiếu 3 chọn A.
2. **Hai ưu tiên đối lập.** Phiếu 1 chấp nhận tốn thời gian take-note để lấy giải thích cô đọng. Phiếu 3 chấp nhận ít chi tiết hơn để lấy sự tiện lợi. Phiếu 2 muốn cả giải thích ngay của C và tổng hợp của B.
3. **Chỉ một breakdown được ghi.** Phiếu 2 hiểu nhầm giống version A: tưởng phải bấm nút mới mở được note. Hai phiếu kia không ghi do dự. Cả ba đều tự lấy lại quyền kiểm soát: hai người dùng nút tắt trên AI, một người tạo chat mới.

Bản ghi từng phiên: [prototype-feedback-note.md](prototype-feedback-note.md)  
Bản đối chiếu của nhóm: [group-feedback-synthesis.md](group-feedback-synthesis.md)

### Next Change

Kiểm thử một luồng ghi chú kết hợp: người học chủ động gọi giải thích ngữ cảnh ngay tại highlight; các giải thích được gom để xem trong một bản tổng hợp cuối phiên, không tự bật lời nhắc giữa giờ. Đây là giả thuyết cần kiểm thử, chưa phải quyết định triển khai.

### Still Unproven

Chưa biết luồng kết hợp có dễ dùng và ít gián đoạn hơn không, người học có kiểm tra nguồn và hiểu đúng nội dung giải thích không, và bản tổng hợp cuối phiên có giúp nhớ lại bài hoặc tiết kiệm thời gian không. Mẫu chỉ có ba tester và mỗi phương án được chọn một lần.

## 6. AI Support Log

AI đã hỗ trợ những phần nào, điểm nào còn hời hợt và tôi đã tự sửa ra sao được ghi tại [ai-support-log.md](ai-support-log.md).

## Tài liệu nhóm

- [Three-option design sheet](three-option-design-sheet.md)
- [Prototype links](prototype-link.md)
- [Prototype feedback note](prototype-feedback-note.md)
- [Group feedback synthesis](group-feedback-synthesis.md)
- [AI support log](ai-support-log.md)
