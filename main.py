from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from panel_article import generate_article_and_keywords, post_to_pixnet

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content={"message": "PIXNET 自動發文系統已啟動"})

@app.post("/post_article")
async def post_article(request: Request):
    try:
        data = await request.json()
        account = data.get("account")
        password = data.get("password")
        title, content = generate_article_and_keywords()
        url = post_to_pixnet(account, password, title, content)
        return {"status": "success", "title": title, "url": url}
    except Exception as e:
        return {"status": "error", "message": str(e)}
