# 📝 Chuyển đổi PDF/Word sang Markdown

Ứng dụng web đơn giản để chuyển đổi file PDF hoặc Word (có chứa hình ảnh) sang định dạng Markdown.

## 🌐 Demo Online

**🚀 Sử dụng ngay tại**: [Link sẽ có sau khi deploy]

> Không cần cài đặt gì - chỉ cần trình duyệt!

## ✨ Tính năng

- ✅ Chuyển đổi PDF sang Markdown
- ✅ Chuyển đổi Word (.docx) sang Markdown
- ✅ Trích xuất và lưu hình ảnh từ tài liệu
- ✅ Giữ nguyên định dạng cơ bản (tiêu đề, in đậm, in nghiêng)
- ✅ Hỗ trợ bảng (từ Word)
- ✅ Preview Markdown trực tiếp
- ✅ Tải xuống file Markdown và hình ảnh

## 🚀 Cài đặt

### 1. Cài đặt Python

Đảm bảo bạn đã cài Python 3.8 trở lên. Kiểm tra bằng lệnh:

```powershell
python --version
```

### 2. Cài đặt thư viện

Mở PowerShell tại thư mục `doc-to-markdown` và chạy:

```powershell
pip install -r requirements.txt
```

## 📖 Sử dụng

### Chạy ứng dụng

```powershell
streamlit run app.py
```

Ứng dụng sẽ tự động mở trong trình duyệt tại địa chỉ: `http://localhost:8501`

### Các bước sử dụng

1. **Upload file**: Kéo thả hoặc chọn file PDF/Word cần chuyển đổi
2. **Nhấn nút "Chuyển đổi sang Markdown"**
3. **Xem kết quả**:
   - Nội dung Markdown (có thể copy)
   - Preview Markdown
   - Hình ảnh đã trích xuất
4. **Tải xuống**: Tải file Markdown và hình ảnh về máy

## 📁 Cấu trúc thư mục

```
doc-to-markdown/
│
├── app.py              # File chính của ứng dụng
├── requirements.txt    # Các thư viện cần thiết
├── README.md          # File hướng dẫn này
│
└── temp_output/       # Thư mục tạm (tự động tạo khi chạy)
    └── images/        # Hình ảnh được trích xuất
```

## 🛠️ Thư viện sử dụng

- **Streamlit**: Tạo giao diện web
- **PyMuPDF (fitz)**: Xử lý file PDF
- **python-docx**: Xử lý file Word
- **Pillow**: Xử lý hình ảnh

## 📝 Ví dụ Markdown Output

```markdown
## Tiêu đề chính

Đây là đoạn văn bản thông thường.

**Văn bản in đậm** và *văn bản in nghiêng*.

![Image](images/image_1.png)

| Cột 1 | Cột 2 | Cột 3 |
| --- | --- | --- |
| Dữ liệu 1 | Dữ liệu 2 | Dữ liệu 3 |
```

## ⚠️ Lưu ý

- Hình ảnh sẽ được lưu trong thư mục `images/` với đường dẫn tương đối
- Định dạng phức tạp có thể cần chỉnh sửa thủ công
- File PDF có layout phức tạp có thể không giữ được định dạng hoàn toàn
- Với Word, giữ được định dạng tốt hơn (tiêu đề, bảng, in đậm, in nghiêng)

## 🐛 Báo lỗi

Nếu gặp lỗi, vui lòng kiểm tra:
1. Đã cài đủ thư viện chưa
2. File input có đúng định dạng không

## 🚀 Deploy lên Web (Khuyên dùng!)

Xem hướng dẫn chi tiết tại: [HUONG_DAN_DEPLOY.md](HUONG_DAN_DEPLOY.md)

**Lợi ích**:
- ✅ Không cần cài đặt Python
- ✅ Dùng mọi nơi qua trình duyệt
- ✅ Tự động cập nhật khi sửa code
- ✅ Chia sẻ dễ dàng qua link

## 📜 License

MIT License - Sử dụng tự do cho mục đích cá nhân và thương mại.

## 👨‍💻 Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy tạo Pull Request hoặc Issues.
3. Có quyền ghi file trong thư mục không

## 📄 Giấy phép

Mã nguồn mở - Tự do sử dụng và chỉnh sửa.
