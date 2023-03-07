import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage 

from dotenv import load_dotenv


load_dotenv()

token = os.getenv('API_KEY_BOT')

storage = MemoryStorage()

bot = Bot(token=token)
disp = Dispatcher(bot=bot, storage=storage) 
