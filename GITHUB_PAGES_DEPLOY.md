# Hướng dẫn Deploy lên GitHub Pages

## 🚀 Các bước deploy static version lên GitHub Pages

### 1. Chuẩn bị repository
```bash
# Commit tất cả files
git add .
git commit -m "Add static version for GitHub Pages"
git push origin main
```

### 2. Cấu hình GitHub Pages
1. Truy cập repository trên GitHub
2. Vào **Settings** → **Pages**
3. Trong phần **Source**, chọn **Deploy from a branch**
4. Chọn branch **main** và folder **/ (root)**
5. Click **Save**

### 3. Kiểm tra deployment
- GitHub sẽ tự động build và deploy
- URL sẽ có dạng: `https://your-username.github.io/naa-dnri`
- Quá trình deploy thường mất 1-2 phút

## 📁 Cấu trúc files cho GitHub Pages

```
/
├── index.html              # Trang chủ (GitHub Pages sẽ mở file này)
├── closing.html            # Trang đóng mẫu thường
├── samples.html            # Trang quản lý mẫu
├── customers.html          # Trang quản lý khách hàng
├── static/
│   ├── styles.css          # CSS chính
│   └── app.js             # JavaScript chính
├── README.md               # Documentation
└── GITHUB_PAGES_DEPLOY.md  # Hướng dẫn này
```

## ✨ Tính năng static version

### ✅ Đã triển khai:
- **Trang chủ** với giao diện hiện đại
- **Đóng mẫu thường** với nhiều box
- **Quản lý mẫu** cơ bản
- **Quản lý khách hàng**
- **Tính toán tự động** khối lượng hiệu chỉnh
- **Lưu trữ local** với localStorage
- **Export CSV** cho báo cáo
- **Responsive design**

### 🔧 Công nghệ sử dụng:
- **HTML5** - Cấu trúc trang
- **CSS3** - Styling và responsive
- **JavaScript** - Tương tác và logic
- **Bootstrap 5** - UI framework
- **Bootstrap Icons** - Icon set
- **localStorage** - Lưu trữ dữ liệu

## 🎯 So sánh với Flask version

| Tính năng | Flask Version | Static Version |
|-----------|---------------|----------------|
| Backend | ✅ Python/Flask | ❌ Không có |
| Database | ✅ JSON files | ✅ localStorage |
| Authentication | ✅ Có | ❌ Không |
| Multi-user | ✅ Có | ❌ Không |
| Server | ✅ Cần | ❌ Không cần |
| Deploy | ✅ Heroku | ✅ GitHub Pages |
| Cost | ✅ Miễn phí (giới hạn) | ✅ Hoàn toàn miễn phí |

## 🔄 Cập nhật và bảo trì

### Cập nhật code:
```bash
# Sau khi sửa code
git add .
git commit -m "Update static version"
git push origin main
# GitHub Pages sẽ tự động deploy
```

### Xem logs:
- Vào **Actions** tab trong GitHub repository
- Xem quá trình build và deploy

## 🚨 Lưu ý quan trọng

### Hạn chế của static version:
1. **Không có backend** - Không thể xử lý server-side
2. **Không có authentication** - Ai cũng có thể truy cập
3. **Dữ liệu local** - Chỉ lưu trên browser của user
4. **Không có database** - Không thể chia sẻ dữ liệu giữa users

### Khi nào nên dùng:
- ✅ **Demo/Prototype** - Để demo tính năng
- ✅ **Single user** - Chỉ một người sử dụng
- ✅ **Local use** - Sử dụng trên máy cá nhân
- ✅ **Free hosting** - Không muốn trả phí hosting

### Khi nào cần Flask version:
- ✅ **Multi-user** - Nhiều người sử dụng
- ✅ **Shared data** - Chia sẻ dữ liệu
- ✅ **Authentication** - Cần đăng nhập
- ✅ **Production** - Sử dụng thực tế

## 📞 Hỗ trợ

Nếu gặp vấn đề với deployment:
1. Kiểm tra **Actions** tab để xem lỗi build
2. Đảm bảo file `index.html` có trong root directory
3. Kiểm tra đường dẫn CSS/JS có đúng không
4. Clear cache browser và thử lại

**URL sau khi deploy thành công:**
`https://your-username.github.io/naa-dnri`
