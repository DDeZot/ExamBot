from aiogram.types import ReplyKeyboardMarkup
from telegram_bot.keyboards.start import KB_CPP, KB_MATH, KB_PYTHON

def get_main_keyboard() -> ReplyKeyboardMarkup:
    km = ReplyKeyboardMarkup(keyboard=[
        [KB_CPP],
        [KB_MATH],
        [KB_PYTHON]
    ])
    return km