#!/bin/bash

# 啟動 Uvicorn 伺服器（背景運行）
uvicorn main:app --host 0.0.0.0 --port 8000 &

# 啟動 Socket.IO 伺服器（背景運行）
python start_server.py &

# 確保容器不會退出，等待所有背景進程
wait