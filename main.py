
from fastapi import FastAPI
from panel_article import auto_post_articles

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PIXNET 自動發文系統已啟動"}

@app.post("/post_article")
def manual_post():
    return auto_post_articles()
