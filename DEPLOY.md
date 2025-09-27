# Hướng dẫn Deploy ứng dụng lên Heroku

## 🚀 Các bước deploy

### 1. Chuẩn bị repository
```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push origin main
```

### 2. Tạo ứng dụng trên Heroku
1. Truy cập [Heroku Dashboard](https://dashboard.heroku.com/)
2. Click "New" → "Create new app"
3. Đặt tên app (ví dụ: `naa-dnri-lab`)
4. Chọn region: United States
5. Click "Create app"

### 3. Kết nối với GitHub
1. Trong Heroku Dashboard, chọn app vừa tạo
2. Vào tab "Deploy"
3. Chọn "GitHub" làm deployment method
4. Kết nối với GitHub repository
5. Chọn branch `main`
6. Click "Deploy Branch"

### 4. Cấu hình biến môi trường (nếu cần)
1. Vào tab "Settings"
2. Click "Reveal Config Vars"
3. Thêm các biến cần thiết:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key-here`

### 5. Kiểm tra logs
```bash
heroku logs --tail --app your-app-name
```

## 📁 Các file đã được tạo/sửa

- ✅ `Procfile` - Hướng dẫn Heroku chạy app
- ✅ `runtime.txt` - Chỉ định Python version
- ✅ `requirements.txt` - Đã thêm gunicorn
- ✅ `wsgi.py` - Đã cập nhật để tương thích Heroku

## 🔧 Troubleshooting

### Lỗi thường gặp:
1. **Build failed**: Kiểm tra `requirements.txt` có đúng không
2. **App crashed**: Kiểm tra logs với `heroku logs --tail`
3. **Port binding**: Đã cập nhật `wsgi.py` để sử dụng PORT từ Heroku

### Lệnh hữu ích:
```bash
# Xem logs
heroku logs --tail --app your-app-name

# Restart app
heroku restart --app your-app-name

# Mở app trong browser
heroku open --app your-app-name
```

## 🌐 Sau khi deploy thành công

App sẽ có URL dạng: `https://your-app-name.herokuapp.com`

**Lưu ý**: Heroku miễn phí có giới hạn:
- App sẽ sleep sau 30 phút không hoạt động
- Có giới hạn về memory và CPU
- Có thể cần upgrade để sử dụng production tốt hơn
