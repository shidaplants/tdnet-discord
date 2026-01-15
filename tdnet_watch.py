import requests
import os
from bs4 import BeautifulSoup

TDNET_URL = "https://www.release.tdnet.info/inbs/I_main_00.html"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord(title, description, color):
    payload = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

def main():
    res = requests.get(TDNET_URL, timeout=10)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    rows = soup.select("tr")
    for row in rows[:10]:
        text = row.get_text(strip=True)

        # 決算
        if any(k in text for k in ["決算", "決算短信"]):
            send_discord("🔵 決算速報", text, 3447003)  # 青
            break

        # 業績修正
        if any(k in text for k in ["業績予想の修正", "上方修正", "下方修正"]):
            send_discord("🟢 業績予想修正", text, 3066993)  # 緑
            break

        # 自己株式取得
        if any(k in text for k in ["自己株式取得", "自己株式の取得"]):
            send_discord("🟡 自己株式取得", text, 15844367)  # 黄
            break

if __name__ == "__main__":
    main()
