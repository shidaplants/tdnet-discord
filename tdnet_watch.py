import requests
import os
from bs4 import BeautifulSoup

TDNET_URL = "https://www.release.tdnet.info/inbs/I_main_00.html"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord(message):
    requests.post(WEBHOOK_URL, json={"content": message})

def main():
    res = requests.get(TDNET_URL, timeout=10)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    rows = soup.select("tr")
    for row in rows[:5]:  # 最新5件だけ
        text = row.get_text(strip=True)
        if "決算" in text:
            send_discord(f"📢 TDnet決算速報\n{text}")
            break

if __name__ == "__main__":
    main()
