# Báo cáo thảo luận Lab 04

### 1. Quy ước Semantic Versioning (SemVer: MAJOR.MINOR.PATCH):
- **MAJOR:** Tăng khi có những thay đổi phá vỡ tính tương thích ngược (breaking changes / API incompatibilities).
- **MINOR:** Tăng khi bổ sung chức năng mới nhưng vẫn duy trì tương thích hoàn toàn với các phiên bản trước.
- **PATCH:** Tăng khi phát hành các bản sửa lỗi khẩn cấp, vá bảo mật mà không làm thay đổi hay bổ sung API công khai.

### 2. Sự khác biệt giữa Tag và Nhánh release:
- **Tag:** Là một con trỏ cố định (immutable pointer) gắn chặt vào một commit băm duy nhất, không bao giờ di chuyển, dùng để định danh chính xác phiên bản phát hành tại một thời điểm.
- **Nhánh release:** Là dòng phát triển bảo trì (maintenance line), con trỏ nhánh có thể di chuyển tiếp khi nhận thêm các bản vá lỗi (hotfix/patch commit) cho nhánh phát hành đó.
