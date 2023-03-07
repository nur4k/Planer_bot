from aiogram.utils import executor
from create_bot import bot, disp

from modules import client, other, admin
from data_base import sqlite_db


async def on_startup(_):
    print(bot, 'Бот запустился')
    sqlite_db.sql_start()

admin.register_handlers_admin(disp=disp)
client.register_handler_client(disp=disp)
other.register_handler_other(disp=disp) 


executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
