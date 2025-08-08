
import time

login_fail_counter = {}

def login_pixnet(email, password):
    # 模擬登入（實際應替換為真實邏輯）
    if "fail" in email:
        return False
    return True

def auto_post_articles():
    results = []
    with open("自動發文主帳號.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        email, password = line.strip().split(":")
        account = f"{email}:{password}"

        try:
            success = login_pixnet(email, password)
            if not success:
                raise Exception("Login failed")

            if account in login_fail_counter:
                del login_fail_counter[account]

            results.append(f"[成功] {email} 發文成功")
        
        except Exception as e:
            login_fail_counter[account] = login_fail_counter.get(account, 0) + 1

            if login_fail_counter[account] >= 3:
                with open("自動發文主帳號.txt", "w", encoding="utf-8") as wf:
                    for l in lines:
                        if l.strip() != account:
                            wf.write(l)
                results.append(f"[刪除] {account} 登入失敗 3 次，已刪除")
                del login_fail_counter[account]
            else:
                results.append(f"[失敗] {account}：{login_fail_counter[account]} 次失敗")

    return {"result": results}
