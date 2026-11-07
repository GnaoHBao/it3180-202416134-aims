# Báo cáo thảo luận Lab 03

### 1. Nguyên nhân gây ra xung đột (Merge Conflict)?
- Xung đột xảy ra khi hai nhánh khác nhau cùng chỉnh sửa vào cùng một dòng (hoặc một khối dòng liền kề) trong cùng một tệp tin, hoặc một nhánh xóa tệp trong khi nhánh kia vẫn chỉnh sửa. Git không thể tự quyết định lấy thay đổi của ai mà yêu cầu lập trình viên phải chủ động can thiệp giải quyết.

### 2. So sánh git revert và git reset:
- **`git reset`:** Di chuyển con trỏ HEAD về quá khứ, loại bỏ hoặc viết lại lịch sử commit. Rất nguy hiểm nếu đã push lên repo từ xa vì sẽ phá vỡ lịch sử của cả nhóm.
- **`git revert`:** Tạo ra một commit mới với nội dung đảo ngược hoàn toàn thay đổi của một commit trước đó. Lịch sử được bảo toàn nguyên vẹn và an toàn tuyệt đối khi làm việc nhóm.
