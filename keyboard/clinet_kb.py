from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Таски_на_сегодня')
b3 = KeyboardButton('/Расположение')
b4 = KeyboardButton('/Поделится своим nickname', request_user=True) 
b5 = KeyboardButton('/Поделится местоположением', request_location=True) 


kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.add(b1).add(b2).insert(b3).row(b4, b5)
