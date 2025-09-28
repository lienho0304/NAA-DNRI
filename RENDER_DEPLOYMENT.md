# Hướng dẫn triển khai ứng dụng Flask trên Render

## Các file cần thiết đã được tạo/cập nhật:

### 1. `render.yaml` - File cấu hình triển khai
- Định nghĩa cấu hình dịch vụ web
- Chỉ định build command và start command
- Cấu hình environment variables

### 2. `runtime.txt` - Phiên bản Python
- Chỉ định phiên bản Python 3.11.0

### 3. `requirements.txt` - Dependencies (đã cập nhật)
- Thêm gunicorn và Werkzeug với phiên bản cụ thể
- Đảm bảo tương thích với Render

### 4. `wsgi.py` - WSGI entry point (đã cập nhật)
- Cấu hình để đọc PORT từ environment
- Tắt debug mode cho production

### 5. `env.example` - Template cho environment variables
- Hướng dẫn các biến môi trường cần thiết

## Các bước triển khai trên Render:

### Bước 1: Chuẩn bị repository
1. Đảm bảo tất cả code đã được commit và push lên GitHub
2. Kiểm tra các file cấu hình đã được tạo

### Bước 2: Tạo tài khoản Render
1. Truy cập https://render.com
2. Đăng ký/đăng nhập tài khoản
3. Kết nối với GitHub account

### Bước 3: Tạo Web Service
1. Chọn "New" → "Web Service"
2. Kết nối với repository GitHub của bạn
3. Chọn branch (thường là main/master)

### Bước 4: Cấu hình triển khai
1. **Name**: Đặt tên cho service (ví dụ: naa-dnri-app)
2. **Environment**: Python 3
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi_production:app`
5. **Plan**: Chọn Free plan (hoặc paid plan nếu cần)

### Bước 5: Cấu hình Environment Variables
Trong phần Environment Variables, thêm:
- `SECRET_KEY`: Tạo một secret key mạnh
- `FLASK_ENV`: production
- Các biến khác nếu cần (database URL, API keys, etc.)

### Bước 6: Triển khai
1. Click "Create Web Service"
2. Render sẽ tự động build và deploy ứng dụng
3. Theo dõi logs để đảm bảo không có lỗi

## Lưu ý quan trọng:

1. **Dữ liệu**: Render free plan không lưu trữ dữ liệu persistent. Nếu cần lưu trữ dữ liệu, hãy sử dụng database service.

2. **File uploads**: Render free plan có giới hạn về file storage. Cân nhắc sử dụng cloud storage (AWS S3, Cloudinary, etc.)

3. **Environment Variables**: Không commit file `.env` vào repository. Chỉ sử dụng `env.example` làm template.

4. **Logs**: Kiểm tra logs trong Render dashboard để debug nếu có lỗi.

5. **Custom Domain**: Có thể cấu hình custom domain trong settings của service.

## Troubleshooting:

- **Build fails**: Kiểm tra requirements.txt và runtime.txt
- **App không start**: Kiểm tra start command và wsgi.py
- **Environment variables**: Đảm bảo tất cả biến cần thiết đã được set
- **Port issues**: Render tự động set PORT, không cần hardcode

## Liên kết hữu ích:
- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/latest/deploying/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/configure.html)
