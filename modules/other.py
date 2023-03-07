from aiogram import types, Dispatcher
from create_bot import disp


# @disp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(f"Salam {message.from_user.first_name}") # Просто ответ сообщению
    # await message.reply(f"{message.from_user.first_name}") # Ответ конкретному пользователю
    # await bot.send_message(message.from_user.id, message.text) # Отвечает в чат пользователю написавшему в чат
    return echo_send


def register_handler_other(disp: Dispatcher):
    disp.register_message_handler(echo_send )