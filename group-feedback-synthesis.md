# 4. Bảng Tổng Hợp Phản Hồi Toàn Đội (Group Feedback Synthesis)

Sau khi cả 3 thành viên hoàn thành feedback note riêng, nhóm đối chiếu hành vi và lựa chọn của từng tester như sau:

| Nội dung đối chiếu | Feedback 1 (Tester của TV 1) | Feedback 2 (Tester của TV 2) | Feedback 3 (Tester của TV 3) | Quy luật lặp lại (Pattern) hoặc Điểm đối lập |
| --- | --- | --- | --- | --- |
| **First Action**<br>Điểm chạm đầu tiên | Tìm định nghĩa để highlight. | Chuyển slide đầu tiên. | Cố highlight đoạn cần note. | Cả ba bắt đầu bằng việc tìm hoặc thao tác trên nội dung bài học; hai tester chủ động hướng tới đoạn muốn lưu/hiểu. Tester 2 bắt đầu bằng điều hướng slide. |
| **Major Breakdown**<br>Điểm tắc nghẽn lớn nhất | Không ghi nhận do dự. | Hiểu nhầm như ở version A: nghĩ rằng phải bấm nút mới mở được note. | Không ghi nhận do dự. | Chỉ có một breakdown được ghi nhận: cách mở note chưa đủ rõ với Tester 2. Hai phiếu còn lại không ghi nhận lúng túng; chưa thể kết luận đây là vấn đề phổ biến. |
| **Control Taken**<br>Cách lấy lại quyền kiểm soát | Dùng nút tắt phía trên câu trả lời của AI Agent. | Tạo chat mới. | Dùng nút tắt trên AI. | Cả ba đều chủ động dùng điều khiển trong giao diện để thoát hoặc làm lại; Tester 1 và 3 dùng nút tắt, Tester 2 chọn tạo chat mới. |
| **Selected Option**<br>Phương án được chọn | Option B. | Option C; thích giải thích ngay khi highlight ở C và khả năng tổng hợp của B. | Option A. | Không có phương án chiếm đa số: A, B, C mỗi phương án được chọn một lần. Tester 2 nêu rõ giá trị của cả C lẫn B, cho thấy có thể cần kiểm thử một luồng kết hợp thay vì tuyên bố phương án thắng cuộc. |
| **Key Trade-off**<br>Sự đánh đổi then chốt | Chấp nhận tốn thêm thời gian take note để nhận giải thích cô đọng hơn; lựa chọn này trái với kỳ vọng ban đầu rằng tester sẽ ưu tiên phương án tối giản. | A cần chủ động mở nên có thể bất tiện; B hỗ trợ take note; thích giải thích tức thì của C và tổng hợp của B. | Chấp nhận ít chi tiết hơn để đổi lấy sự tiện lợi; ưu tiên này đối lập với Tester 1. | Hai ưu tiên đối lập xuất hiện trực tiếp: tiện lợi (Tester 3) so với độ cô đọng/chi tiết và tổng hợp (Tester 1, Tester 2). Tester 2 muốn lợi ích của B và C. |

## Quyết định hành động tiếp theo của cả nhóm

- **Đúng MỘT Next Change cho vòng tiếp theo:** Kiểm thử một luồng ghi chú kết hợp: người học chủ động gọi giải thích ngữ cảnh ngay tại highlight; các giải thích được gom để xem trong một bản tổng hợp cuối phiên, không tự bật lời nhắc giữa giờ. Đây là giả thuyết cần kiểm thử, chưa phải quyết định triển khai.
- **Dữ kiện thực tế dẫn đến quyết định:** Có một phiếu chọn B, một chọn A và một chọn C. Tester 2 thích giải thích tức thì của C cùng khả năng tổng hợp của B; Tester 1 đánh đổi thời gian để lấy giải thích cô đọng hơn, trong khi Tester 3 ưu tiên tiện lợi. Hai tester dùng nút tắt trên AI và một tester tạo chat mới để lấy lại quyền kiểm soát. Chỉ Tester 2 ghi nhận hiểu nhầm về cách mở note.
- **Điều vẫn CHƯA THỂ CHỨNG MINH sau 3 phiên test:** Luồng kết hợp có thực sự dễ dùng và ít gián đoạn hơn không; người học có kiểm tra nguồn và hiểu đúng nội dung giải thích không; việc tổng hợp cuối phiên có giúp nhớ lại bài tốt hơn hay tiết kiệm thời gian không. Mẫu chỉ có ba tester và mỗi phương án được chọn một lần, nên chưa đủ cơ sở khẳng định phương án nào được đa số ưa thích.
