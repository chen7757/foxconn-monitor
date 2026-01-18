
import os, requests, json

def send_msg(content):
# 從 GitHub Secrets 讀取你的 Discord 網址
url = os.environ.get('DISCORDWEBHOOK')
data = {"content": content, "username": "鴻海 2317 監控官"}
requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if __name__ == "__main__":
# 這是測試戰報內容
report = "🚀 **iPhone 17 監控連線成功！**\n\n狀態：雲端系統已準備就緒。\n目標：鴻海 (2317) 監控任務啟動中。"
send_msg(report)
