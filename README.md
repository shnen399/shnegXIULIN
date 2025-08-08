
# PIXNET 自動發文系統

✅ 功能包含：自動產文、自動關鍵字、自動抓新聞、自動發文、自動推播

## 🛠️ 使用方式

### 🔧 部署前準備

1. 填入 pixnet_accounts.txt 帳密（格式：帳號:密碼）
2. 複製 .env.example 為 .env，填入 LINE Notify 權杖
3. 使用 render.yaml 一鍵部署

### 🚀 發文 API 測試

前往 `/docs` 介面，使用 `/post_article` 測試發文

```json
{
  "account": "帳號",
  "password": "密碼"
}
```
