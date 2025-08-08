from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content={"message": "PIXNET 自動發文系統已啟動"})

@app.post("/post_article")
def post_article():
    return JSONResponse(content={"message": "文章已成功發佈！"})
