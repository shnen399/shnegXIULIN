
from longtail_keywords import generate_keywords
from news_fetcher import fetch_hot_news

def generate_article():
    keywords = generate_keywords()
    news_title, news_summary = fetch_hot_news()
    title = f"理債一日便：{news_title}"
    content = f"""{news_summary}

本篇由理債一日便自動產生，協助您快速整合負債，免保人、免抵押、低利方案馬上了解！
👉 馬上申請：https://lihi.cc/japMO

延伸關鍵字：{", ".join(keywords)}
"""
    return title, content
