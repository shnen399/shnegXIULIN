
# PIXNET 自動發文系統（進階排程 + 通知）

## 功能包含：

- FastAPI 啟動 Web API `/post_article`
- 自動從 `自動發文主帳號.txt` 每 180 秒輪流發文
- 成功後記錄至 `發文紀錄.txt`
- 成功發文自動 LINE Notify 通知

## 啟動服務：

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

打開 Swagger 測試介面：

```
http://localhost:10000/docs
```

### 環境變數（.env）

請設定：

```
LINE_NOTIFY_TOKEN=你的 LINE Notify 權杖
```

### 帳密檔案格式

`自動發文主帳號.txt`：

```
帳號1:密碼1
帳號2:密碼2
```
