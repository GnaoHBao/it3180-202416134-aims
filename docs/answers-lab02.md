# Báo cáo thảo luận Lab 02

### 1. Phân biệt 3 chiến lược Merge Pull Request:
- **Merge commit (`--no-ff`):**
  - Giữ lại toàn bộ cây lịch sử và các commit con của nhánh tính năng, đồng thời tạo ra một merge commit kết nối.
  - Phù hợp khi muốn bảo toàn chi tiết từng bước phát triển của tính năng phức tạp.
- **Squash and merge:**
  - Gộp tất cả commit từ nhánh con thành duy nhất một commit đưa vào nhánh chính.
  - Phù hợp để giữ nhánh chính (`master`) tuyến tính, sạch sẽ, dễ theo dõi.
- **Rebase and merge:**
  - Nối tiếp các commit của nhánh con vào đỉnh của nhánh chính mà không tạo merge commit.
  - Tạo lịch sử dạng một đường thẳng, nhưng làm thay đổi mã băm (commit hash) của các commit con.

### 2. Ý nghĩa của từ khóa đóng Issue tự động (Fixes / Closes):
- Khi viết `Fixes #<số_issue>` hoặc `Closes #<số_issue>` vào commit message hoặc mô tả Pull Request, GitHub sẽ tự động đóng Issue liên quan ngay khi PR được merge vào nhánh mặc định (`master`). Giúp tự động hóa liên kết giữa yêu cầu thay đổi và mã nguồn thực thi.
