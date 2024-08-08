from typing import Final
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def setMarkup(items: dict) -> ReplyKeyboardMarkup:
    buttons_list = list()

    for k in items.keys():
        new_button = KeyboardButton(text=k)
        new_button_place = list()
        new_button_place.append(new_button)
        buttons_list.append(new_button_place)

    markup = ReplyKeyboardMarkup(keyboard=buttons_list, resize_keyboard=True)
    return markup
        