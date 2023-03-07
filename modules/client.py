from aiogram import types, Dispatcher
from create_bot import bot

from keyboard import kb


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Начинаем планировку!', reply_markup=kb)
    except:
        await message.reply('Общение с ботом через ЛС, добавьте бота: \nhttps://t.me/Planer_DevBot.')


async def command_work(message: types.Message):
    await message.reply('Работа с 10:00 до 17:00.')


async def command_task(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот твои таски на сегодня!')

async def command_location(message: types.Message):
    await message.reply('Байтик баатыра 126.')


def register_handler_client(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(command_work, commands=['Режим_работы'])
    disp.register_message_handler(command_task, commands=['Таски_на_сегодня'])
    disp.register_message_handler(command_location, commands=['Расположение'])