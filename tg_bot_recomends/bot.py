import logging
import os
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import register_all_handlers
from dotenv import load_dotenv
from utils.constants import API_BASE_URL, API_KEY

# Завантаження змінних середовища з .env файлу
load_dotenv()

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Токен бота 
API_TOKEN = os.getenv("BOT_TOKEN")
if not API_TOKEN:
    logging.error("Токен бота не знайдено! Перевірте наявність файлу .env з BOT_TOKEN=your_token")
    exit(1)

# Ініціалізація бота і диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def check_api_connection():
    """Перевірка підключення до API"""
    try:
        url = f"{API_BASE_URL}/configuration"
        params = {
            "api_key": API_KEY,
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    logging.info("Підключення до API успішне")
                    return True
                else:
                    logging.error(f"Помилка підключення до API. Статус: {response.status}")
                    return False
    except Exception as e:
        logging.error(f"Помилка перевірки API: {e}")
        return False

async def on_startup():
    """Дії при запуску бота"""
    logging.info("Бот запущено")
    
    # Перевірка підключення до API
    api_connected = await check_api_connection()
    if not api_connected:
        logging.warning("Бот запущено з проблемами підключення до API")

async def start_bot():
    # Реєстрація всіх обробників
    register_all_handlers(dp)
    
    # Встановлюємо обробник запуску
    dp.startup.register(on_startup)
    
    # Запускаємо бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
