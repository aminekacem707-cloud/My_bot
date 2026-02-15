import requests
import telebot

# إعدادات البوت الخاصة بك
TOKEN = "8380499471:AAEjcV3pOVaIuQOOxdL-wCDgOjvFpivzI1s"
CHAT_ID = "8034521813"
bot = telebot.TeleBot(TOKEN)

def get_live_api_data(game_slug):
    try:
        # الاتصال المباشر ببيانات Tracksino الخام
        url = f"https://api.tracksino.com/v1/games/{game_slug}/results"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        # استخراج آخر نتيجة ظهرت في المصفوفة
        if data and 'results' in data and len(data['results']) > 0:
            return data['results'][0]['result']
        return "جاري التحديث"
    except Exception as e:
        return "خطأ اتصال"

def main():
    # الألعاب المتاحة في استراتيجية Black Diamond
    games = {
        "Roulette": "lightning-roulette",
        "Dice": "sicbo",
        "Monopoly": "monopoly",
        "CrazyTime": "crazytime"
    }
    
    for name, slug in games.items():
        result = get_live_api_data(slug)
        # إرسال النتيجة بالصيغة التي يفهمها المحرك
        bot.send_message(CHAT_ID, f"{name}:{result}")

if __name__ == "__main__":
    main()
