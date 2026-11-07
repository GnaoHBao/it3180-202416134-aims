# Báo cáo thảo luận Lab 05

### 1. Vì sao release/* không merge ngược lại vào master? So sánh với GitFlow:
- Trong mô hình Release Flow của môn học, nhánh `release/*` là nhánh đóng băng để duy trì các phiên bản bảo trì cố định. Nếu merge toàn bộ `release/*` vào `master`, các cấu hình đặc thù phiên bản cũ (như hạ version 1.0.1) sẽ làm bẩn lịch sử của nhánh chính.
- Khác với GitFlow (nơi hotfix bắt buộc merge vào cả `master` và `develop`), Release Flow sử dụng `cherry-pick` để bốc tách duy nhất commit sửa logic đưa về `master` mà không làm xáo trộn các tính năng đang phát triển.

### 2. Ưu và nhược điểm của Upstream First (Microsoft) so với Release First:
- **Upstream First (Sửa trên master trước rồi cherry-pick về release):**
  - *Ưu điểm:* Đảm bảo không bao giờ sót lỗi trên nhánh chính, tránh tình trạng phiên bản sau tái diễn lỗi cũ (regression bug).
  - *Nhược điểm:* Commit sửa lỗi trên master có thể bị phụ thuộc vào các module tính năng mới viết, gây khó khăn khi cherry-pick về nhánh cũ.
- **Release First (Sửa trên release trước rồi cherry-pick lên master - mô hình học phần):**
  - *Ưu điểm:* Phát hành bản vá khẩn cấp nhanh nhất có thể cho khách hàng dùng bản cũ mà không phụ thuộc tiến độ của master.
  - *Nhược điểm:* Đòi hỏi quy trình kiểm toán chặt chẽ để tránh quên đồng bộ bản vá lên nhánh chính.
