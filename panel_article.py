
import requests, os

def send_line_notify(message):
    token = os.getenv("LINE_NOTIFY_TOKEN")
    if not token:
        return
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"message": message}
    try:
        requests.post(url, headers=headers, data=data)
    except:
        pass
