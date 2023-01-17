from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
API_TOKEN = '5899616155:AAGlbH_ChBiVkaaWsIwU9Xbb60X_umGsuRY'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)