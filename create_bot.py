import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


from dotenv import load_dotenv


load_dotenv()

token = os.getenv('API_KEY_BOT')

bot = Bot(token=token)
disp = Dispatcher(bot) 
