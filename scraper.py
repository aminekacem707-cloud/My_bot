import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_live_data(url):
    try:
        r = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'html.parser')
        # البحث عن الرقم الأخير في الموقع
        res = soup.find('div', class_='stats-number')
        return res.text.strip() if res else "N/A"
    except: return "N/A"

def main():
    games = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }
    for name, url in games.items():
        val = get_live_data(url)
        # إرسال البيانات بصيغة (الاسم:الرقم)
        bot.send_message(CHAT_ID, f"{name}:{val}")

if __name__ == "__main__":
    main()
