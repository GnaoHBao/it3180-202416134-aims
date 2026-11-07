# Báo cáo thảo luận Lab 01

### 1. Ý nghĩa của Working Directory, Staging Area và Git Repository?
- **Working Directory:** Thư mục làm việc vật lý trên máy tính, nơi người dùng trực tiếp sửa đổi và thêm bớt tệp.
- **Staging Area (Index):** Khu vực chuẩn bị; lưu vết các thay đổi đã chọn qua `git add` trước khi đóng gói thành commit.
- **Git Repository:** Nơi lưu trữ vĩnh viễn toàn bộ lịch sử các commit và metadata quản lý phiên bản trong thư mục ẩn `.git`.

### 2. Vai trò của tệp .gitignore?
- Ngăn không cho các tệp sinh tự động (cache `__pycache__`, môi trường ảo `.venv/`, cài đặt cá nhân của IDE `.vscode/`) bị vô tình commit và đẩy lên repo chung, giữ repo sạch và tránh xung đột môi trường.
