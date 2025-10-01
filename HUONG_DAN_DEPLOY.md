# 🚀 Hướng dẫn Deploy lên Streamlit Cloud

## ✅ Bước 1: Chuẩn bị GitHub

### 1.1. Tạo repository mới trên GitHub

1. Truy cập: https://github.com/new
2. Đặt tên repository: `doc-to-markdown` (hoặc tên bạn thích)
3. Chọn **Public** (bắt buộc để deploy miễn phí)
4. ❌ KHÔNG tích "Add a README file"
5. Click **Create repository**

### 1.2. Push code lên GitHub

Mở PowerShell tại thư mục `doc-to-markdown` và chạy:

```powershell
# Khởi tạo Git (nếu chưa có)
git init

# Thêm tất cả file
git add .

# Commit
git commit -m "Initial commit: Doc to Markdown converter"

# Đổi tên branch thành main
git branch -M main

# Thêm remote (thay YOUR_USERNAME và YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push lên GitHub
git push -u origin main
```

**💡 Lưu ý**: Thay `YOUR_USERNAME` và `YOUR_REPO` bằng tên GitHub và tên repository của bạn.

---

## ✅ Bước 2: Deploy trên Streamlit Cloud

### 2.1. Đăng nhập Streamlit Cloud

1. Truy cập: https://share.streamlit.io/
2. Click **Sign in with GitHub**
3. Cho phép Streamlit truy cập GitHub

### 2.2. Deploy ứng dụng

1. Click nút **"New app"** (hoặc "Create app")
2. Điền thông tin:
   - **Repository**: Chọn `your-username/doc-to-markdown`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Click **"Deploy!"**

### 2.3. Đợi deploy hoàn tất

- Quá trình mất khoảng 2-3 phút
- Bạn sẽ thấy logs đang cài đặt dependencies
- Khi xong, ứng dụng tự động mở!

---

## 🎉 Hoàn tất!

Bạn sẽ nhận được link dạng:
```
https://your-username-doc-to-markdown-xxxxxx.streamlit.app
```

**Chia sẻ link này cho bất kỳ ai** - họ có thể dùng ngay qua trình duyệt!

---

## 🔄 Cập nhật khi sửa bug

Sau này khi sửa code, chỉ cần:

```powershell
# Thêm file đã sửa
git add .

# Commit với message mô tả
git commit -m "Fix: Sửa lỗi chuyển đổi hình ảnh"

# Push lên GitHub
git push
```

**✨ Streamlit Cloud tự động cập nhật** sau vài giây!

---

## 📊 Quản lý ứng dụng

Tại https://share.streamlit.io/ bạn có thể:
- ✅ Xem logs
- ✅ Xem số người dùng
- ✅ Tắt/bật ứng dụng
- ✅ Xóa ứng dụng
- ✅ Xem tài nguyên sử dụng

---

## 🔧 Troubleshooting

### Lỗi: "Requirements file not found"
- Kiểm tra file `requirements.txt` có trong repository không
- File phải nằm ở thư mục gốc

### Lỗi: "Module not found"
- Thêm module vào `requirements.txt`
- Push lại lên GitHub

### Ứng dụng chạy chậm
- Streamlit Cloud miễn phí có giới hạn tài nguyên
- Tối ưu code hoặc nâng cấp plan

### Lỗi Git khi push
```powershell
# Nếu bị lỗi authentication, dùng Personal Access Token
# Tạo token tại: https://github.com/settings/tokens
# Khi git hỏi password, nhập token thay vì password
```

---

## 💡 Tips

1. **Custom domain**: Có thể thêm domain riêng trong settings
2. **Secrets**: Lưu API keys trong Settings > Secrets (không push lên GitHub)
3. **Analytics**: Thêm Google Analytics để theo dõi người dùng
4. **Share**: Nhúng ứng dụng vào website với iframe

---

## 📝 Checklist trước khi deploy

- [x] File `requirements.txt` đầy đủ
- [x] File `.gitignore` để không push file thừa
- [x] File `app.py` chạy được locally
- [x] Repository là Public
- [x] Đã test upload file PDF/Word
- [x] README.md có hướng dẫn

---

## 🆘 Cần giúp đỡ?

- **Streamlit Docs**: https://docs.streamlit.io/
- **Community Forum**: https://discuss.streamlit.io/
- **GitHub Issues**: Tạo issue trong repo của bạn

---

**Chúc bạn deploy thành công! 🎉**
