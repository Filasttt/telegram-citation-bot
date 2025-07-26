from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import random

# Встав сюди свій токен і chat_id
BOT_TOKEN = "7589285720:AAHslXE_TgaeWweabraD5d4LAzufW7Da3Ww"
CHAT_ID = "470247691"  # Ми отримаємо його нижче

quotes = [
    "Куди б ти не йшов — іди з усім серцем.",
    "Твій розум — інструмент, не хазяїн.",
    "Зміни починаються всередині тебе.",
    "Справжній шлях — це шлях постійного вдосконалення.",
    "Рух — це життя. Застій — смерть.",
    "Проблеми — це можливості перевтілені.",
    "Кожна дія — це вибір між страхом і любов’ю.",
    "Бути — важливіше, ніж досягати.",
    "Жити зараз — ось справжнє мистецтво.",
    "Спокій — це сила, а не слабкість."
]

bot = Bot(token=TOKEN)

def send_quote():
    quote = random.choice(quotes)
    bot.send_message(chat_id=CHAT_ID, text=quote)

scheduler = BlockingScheduler()
scheduler.add_job(send_quote, 'cron', hour=5, minute=1)  # щодня о 5:01
scheduler.start()
