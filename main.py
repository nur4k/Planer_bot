from aiogram.utils import executor
from create_bot import bot, disp

from modules import client, other


async def on_startup(_):
    print(bot, 'Бот запустился')

client.register_handler_client(disp=disp)
other.register_handler_other(disp=disp) 


executor.start_polling(disp, skip_updates=True, on_startup=on_startup)
