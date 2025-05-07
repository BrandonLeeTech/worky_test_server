# 使用官方 Python 3.11 輕量版作為基礎鏡像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製整個後端程式碼到容器中
COPY . .

# 設定環境變數（可選）
ENV PYTHONUNBUFFERED=1

# 複製啟動腳本並設置執行權限
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# 使用 entrypoint.sh 作為入口點
CMD ["./entrypoint.sh"]