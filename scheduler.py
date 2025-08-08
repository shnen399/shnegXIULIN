
from apscheduler.schedulers.background import BackgroundScheduler
from pixnet_api import post_to_pixnet
from article_generator import generate_article
import time

def run_auto_post():
    try:
        with open("pixnet_accounts.txt", "r", encoding="utf-8") as f:
            accounts = [line.strip() for line in f if line.strip()]
        for account_line in accounts:
            account, password = account_line.split(":")
            title, content = generate_article()
            post_to_pixnet(account, password, title, content)
            time.sleep(5)
    except Exception as e:
        print("自動發文錯誤：", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_auto_post, "interval", seconds=180)
    scheduler.start()
