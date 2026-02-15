import requests
from bs4 import BeautifulSoup
import telebot

# إعدادات البوت الخاصة بك
TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
MY_CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_last_number(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # جلب آخر رقم ظهر من موقع Tracksino
        numbers = soup.find_all('div', class_='stats-number')
        if numbers:
            return numbers[0].text.strip()
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
    return None

def main():
    # 1. جلب رقم الروليت
    roulette_url = "https://tracksino.com/lightning-roulette"
    r_num = get_last_number(roulette_url)
    if r_num:
        bot.send_message(MY_CHAT_ID, f"Roulette:{r_num}")
        print(f"Sent Roulette: {r_num}")

    # 2. جلب رقم النرد (Sic Bo)
    sicbo_url = "https://tracksino.com/sicbo"
    d_num = get_last_number(sicbo_url)
    if d_num:
        bot.send_message(MY_CHAT_ID, f"Dice:{d_num}")
        print(f"Sent Dice: {d_num}")

if __name__ == "__main__":
    main()
