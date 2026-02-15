import requests
from bs4 import BeautifulSoup
import telebot

TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_live_val(url):
    try:
        # إضافة هوية متصفح حقيقية لتجاوز الحماية
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=30)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # البحث عن الرقم في عدة أماكن محتملة بالموقع
        selectors = ['div.stats-number', 'div.last-results-list span', 'div.number-box']
        for selector in selectors:
            res = soup.select_one(selector)
            if res and res.text.strip():
                return res.text.strip()
        return "جاري التحديث..."
    except:
        return "خطأ اتصال"

def main():
    targets = {
        "Roulette": "https://tracksino.com/lightning-roulette",
        "Dice": "https://tracksino.com/sicbo",
        "Monopoly": "https://tracksino.com/monopoly",
        "CrazyTime": "https://tracksino.com/crazytime"
    }
    for name, url in targets.items():
        val = get_live_val(url)
        # إرسال النتيجة بصيغة يفهمها العقل
        bot.send_message(CHAT_ID, f"{name}:{val}")

if __name__ == "__main__":
    main()
