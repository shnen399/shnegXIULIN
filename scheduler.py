
from apscheduler.schedulers.background import BackgroundScheduler
from panel_article import generate_article_and_keywords, post_to_pixnet
import time

def post_from_account_file():
    try:
        with open("自動發文主帳號.txt", "r", encoding="utf-8") as f:
            accounts = [line.strip() for line in f if line.strip()]
        for account_line in accounts:
            account, password = account_line.split(":")
            title, content = generate_article_and_keywords()
            post_to_pixnet(account, password, title, content)
            time.sleep(5)  # 每個帳號間隔幾秒，避免過快
    except Exception as e:
        print("排程發文失敗:", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_from_account_file, "interval", seconds=180)
    scheduler.start()
