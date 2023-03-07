from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button_load = KeyboardButton('/Загрузить базу')
button_delete = KeyboardButton('/Удалить базу')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
                    .add(button_delete)
