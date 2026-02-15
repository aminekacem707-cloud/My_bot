import requests
from bs4 import BeautifulSoup
import telebot

# إعدادات البوت الخاصة بك
TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
MY_CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_last_result(url):
    try:
        response = requests.get(url, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        result_div = soup.find('div', class_='stats-number')
        return result_div.text.strip() if result_div else None
    except:
        return None

def main():
    # روابط الألعاب الأربعة
    games = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }

    for game_name, url in games.items():
        res = get_last_result(url)
        if res:
            # إرسال البيانات بالصيغة التي يفهمها البوت التفاعلي
            bot.send_message(MY_CHAT_ID, f"{game_name}:{res}")
            print(f"Sent: {game_name}:{res}")

if __name__ == "__main__":
    main()
