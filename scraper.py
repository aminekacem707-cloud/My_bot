import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def fetch_number(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(r.text, 'html.parser')
        # البحث عن الرقم الأخير في الموقع
        res = soup.find('div', class_='stats-number')
        return res.text.strip() if res else None
    except:
        return None

def main():
    targets = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }
    for name, url in targets.items():
        val = fetch_number(url)
        if val:
            bot.send_message(CHAT_ID, f"{name}:{val}")

if __name__ == "__main__":
    main()
