import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_live_data(url):
    try:
        # استخدام هوية متصفح قوية لتجنب المنع
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0'}
        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # استهداف "الأرقام الحية" مباشرة من الكلاسات النشطة
        res = soup.find('div', class_='stats-number')
        if res: return res.text.strip()
        
        # محاولة ثانية في حال تغير الموقع
        res2 = soup.select_one('.last-results-list .number')
        return res2.text.strip() if res2 else "قيد الانتظار"
    except:
        return "خطأ اتصال"

def main():
    games = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }
    for name, url in games.items():
        val = get_live_data(url)
        # إرسال البيانات بصيغة البرمجة (الاسم:القيمة)
        bot.send_message(CHAT_ID, f"{name}:{val}")

if __name__ == "__main__":
    main()
