FROM python:3.11-slim

WORKDIR /app

# Cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8501

# Chạy ứng dụng
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
