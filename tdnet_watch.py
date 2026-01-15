import requests
from bs4 import BeautifulSoup
import os
import time

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

URL = "https://www.release.tdnet.info/inbs/I_list_001_202401.html"

def send_discord(msg):
    requests.post(WEBHOOK_URL, json={"content": msg})

def main():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    rows = soup.select("table tr")[1:]
    if not rows:
        return

    latest = rows[0].get_text(" ", strip=True)
    send_discord(f"📢 TDnet 新着情報\n{latest}")

if __name__ == "__main__":
    main()
print("=== TEST: sending message to Discord ===")

import os
import requests

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

requests.post(
    webhook_url,
    json={"content": "✅ GitHub Actions からのテスト通知です"}
)

print("=== TEST: done ===")
