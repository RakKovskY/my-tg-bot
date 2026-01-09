import os
from dotenv import load_dotenv

#загружаем данные из .env (bot_token)

load_dotenv()

#получаем токен из .env
BOT_TOKEN=os.getenv('BOT_TOKEN')

#проверяем что токен загрузился
if BOT_TOKEN is None:
    print("❌ ОШИБКА: Токен не найден в .env файле!")
    print("✅ Убедитесь, что в .env есть строка: BOT_TOKEN=ваш_токен")