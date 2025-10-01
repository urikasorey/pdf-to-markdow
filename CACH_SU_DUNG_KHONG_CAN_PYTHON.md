# 🚀 Cách sử dụng KHÔNG CẦN cài Python

## ✅ CÁCH 1: Sử dụng file .EXE (Đơn giản nhất)

### Bước 1: Build file .exe (chỉ làm 1 lần)

Nếu bạn có máy có Python, chạy các lệnh sau 1 lần:

```powershell
pip install pyinstaller
python build_exe.py
```

### Bước 2: Chia sẻ file .exe

File `.exe` sẽ được tạo trong thư mục `dist/DocToMarkdown.exe`

**Chia sẻ file này cho bất kỳ ai** - họ chỉ cần:
1. Double-click vào file `DocToMarkdown.exe`
2. Trình duyệt tự động mở
3. Sử dụng ngay!

**✨ Không cần cài Python, không cần cài gì cả!**

---

## ✅ CÁCH 2: Deploy lên Web (Miễn phí)

Deploy lên Streamlit Cloud - sử dụng qua trình duyệt:

### Bước 1: Tạo file cấu hình

Đã có sẵn file `.streamlit/config.toml` và `requirements.txt`

### Bước 2: Push code lên GitHub

```powershell
git init
git add .
git commit -m "Doc to Markdown converter"
git branch -M main
git remote add origin <URL-GitHub-repo-của-bạn>
git push -u origin main
```

### Bước 3: Deploy trên Streamlit Cloud

1. Truy cập: https://share.streamlit.io/
2. Đăng nhập bằng GitHub
3. Chọn repository của bạn
4. Chọn file `app.py`
5. Click "Deploy"!

**Kết quả**: Bạn có link web công khai (VD: `https://your-app.streamlit.app`)

**✨ Ai cũng có thể truy cập qua trình duyệt - không cần cài gì!**

---

## ✅ CÁCH 3: Sử dụng Docker

Nếu bạn biết Docker, có thể chạy:

```powershell
docker build -t doc-to-markdown .
docker run -p 8501:8501 doc-to-markdown
```

Truy cập: `http://localhost:8501`

---

## 🎯 So sánh các cách

| Cách | Ưu điểm | Nhược điểm |
|------|---------|------------|
| **File .EXE** | ⭐ Đơn giản nhất, chạy offline, không cần cài gì | File hơi nặng (~200MB) |
| **Web Deploy** | Dùng mọi nơi qua link, nhẹ, tự động update | Cần internet, giới hạn tài nguyên |
| **Docker** | Portable, dễ scale | Cần biết Docker |

---

## 💡 Khuyến nghị

- **Dùng cá nhân/offline**: Dùng file .EXE
- **Chia sẻ công khai**: Deploy lên web
- **Dùng trong công ty**: Docker hoặc .EXE

---

## ❓ Câu hỏi thường gặp

**Q: File .exe có virus không?**  
A: Không, nhưng Windows Defender có thể cảnh báo vì file không có chữ ký số. Bạn có thể bỏ qua cảnh báo này.

**Q: File .exe chạy trên máy nào?**  
A: Chỉ Windows. Nếu muốn chạy trên Mac/Linux, dùng cách 2 (Web Deploy).

**Q: Tôi không có Python để build .exe?**  
A: Dùng cách 2 (Web Deploy) hoặc nhờ bạn bè có Python build giúp 1 lần.
