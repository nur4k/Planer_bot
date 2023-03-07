from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import disp, bot
from data_base.sqlite_db import sql_add_command
from keyboard import admin_kb

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def command_start(message: types.Message):
    await FSMAdmin.photo.set()
    await bot.send_message(message.from_user.id, '/Загрузить', reply_markup=admin_kb.button_case_admin)

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введите название')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите описание')

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите цену')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    
    await sql_add_command(state=state)

    await state.finish()


async def cancel_handler(message: types.Message, state: FSMContext):
    cancel_option = await state.get_state()
    if cancel_option is None:
        return
    await state.finish()
    await message.reply('OK')


def register_handlers_admin(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['Загрузить'], state=None)
    disp.register_message_handler(load_photo, state=FSMAdmin.photo)
    disp.register_message_handler(load_name, state=FSMAdmin.name)
    disp.register_message_handler(load_description, state=FSMAdmin.description)
    disp.register_message_handler(load_price, state=FSMAdmin.price)
    disp.register_message_handler(cancel_handler, state="*", commands='отмена')
    disp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")



