from aiogram.utils import executor
from handlers import client
from create_bot import dp
import pymysql
#from database.config_db import host, db_name, user, password
from pymysql import cursors
from database import mysql_db

async def on_startup(_):
    print('Бот в онлайне')


client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)