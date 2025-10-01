"""
Script để build ứng dụng thành file .exe
Chạy: python build_exe.py
"""
import PyInstaller.__main__
import os

# Cấu hình PyInstaller
PyInstaller.__main__.run([
    'app.py',
    '--name=DocToMarkdown',
    '--onefile',
    '--windowed',
    '--icon=NONE',
    '--clean',
    '--noconfirm',
    '--add-data=README.md;.',
])

print("\n✅ Build hoàn tất!")
print("📁 File .exe nằm trong thư mục: dist/DocToMarkdown.exe")
