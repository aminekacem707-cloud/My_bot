import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_data(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0'}
        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        # استهداف الحاوية المباشرة للأرقام في Tracksino
        res = soup.find('div', class_='stats-number')
        return res.text.strip() if res else "N/A"
    except:
        return "Error"

def main():
    games = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }
    for name, url in games.items():
        val = get_data(url)
        # إرسال فوري ومباشر
        bot.send_message(CHAT_ID, f"{name}:{val}")

if __name__ == "__main__":
    main()
