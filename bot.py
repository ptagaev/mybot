from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="6109625058:AAFxvgmKeauJBlCRRbm38qlclRHN8gZnfhU")
dp = Dispatcher(bot, storage=storage)