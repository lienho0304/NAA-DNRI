# Lab Sample Management System

Hệ thống quản lý mẫu phòng thí nghiệm với giao diện hiện đại và tính năng đầy đủ.

## ✨ Tính năng chính

- 🔐 **Xác thực người dùng** với phân quyền
- 👥 **Quản lý người dùng** và khách hàng
- 📦 **Nhận mẫu** với import/export Excel
- 🔬 **Đóng mẫu** (thường, foil, standard) với nhiều box
- ☢️ **Chiếu mẫu** (sắp triển khai)
- 📊 **Báo cáo** và xuất dữ liệu Excel

## 🚀 Cài đặt và chạy

### Local Development
```bash
# Tạo virtual environment
python -m venv .venv

# Kích hoạt (Windows)
.venv\Scripts\activate

# Kích hoạt (Linux/Mac)
source .venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python -m app
```

Truy cập: `http://127.0.0.1:5000`

### Deploy lên Heroku
Xem file [DEPLOY.md](DEPLOY.md) để biết hướng dẫn chi tiết.

## 🔑 Thông tin đăng nhập

- **Username**: Admin
- **Password**: admin

## 📁 Cấu trúc dự án

```
app/
├── __init__.py          # Flask app factory
├── routes.py            # Routes chính
├── auth.py             # Xác thực và phân quyền
├── users_store.py      # Quản lý người dùng
├── customers_store.py  # Quản lý khách hàng
├── samples_store.py    # Quản lý mẫu
├── closed_samples_store.py # Quản lý mẫu đóng
├── templates/          # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── home.html
│   ├── users/
│   ├── customers/
│   ├── samples/
│   └── closing/
└── static/            # CSS, JS, images
    └── styles.css

data/                  # JSON data files
├── users.json
├── customers.json
├── samples.json
└── closed_samples.json

# Deploy files
Procfile              # Heroku deployment
runtime.txt           # Python version
requirements.txt      # Dependencies
wsgi.py              # WSGI entry point
```

## 🛠️ Công nghệ sử dụng

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: JSON files (có thể nâng cấp lên SQLite/PostgreSQL)
- **Deploy**: Heroku (miễn phí)

## 📋 Tính năng chi tiết

### Đóng mẫu thường
- ✅ Nhập thông tin mẫu cơ bản
- ✅ Quản lý nhiều box cho một mẫu
- ✅ Tính toán tự động khối lượng hiệu chỉnh
- ✅ Giao diện thân thiện với người dùng

### Quản lý mẫu
- ✅ Import/Export Excel
- ✅ Tìm kiếm và lọc
- ✅ Phân trang
- ✅ Chỉnh sửa thông tin

### Báo cáo
- ✅ Xuất dữ liệu ra Excel
- ✅ Thống kê theo thời gian
- ✅ Báo cáo chi tiết

## 🔄 Cập nhật gần đây

- **v2.0**: Cải tiến giao diện đóng mẫu thường
- **v1.5**: Thêm tính năng import/export Excel
- **v1.0**: Phiên bản đầu tiên với xác thực cơ bản

## 📞 Hỗ trợ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub repository.
