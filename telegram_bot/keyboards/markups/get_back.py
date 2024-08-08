from typing import Final
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BACK_TO_EXAMS: Final = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<---Назад', callback_data='back_exams')]
])

BACK_TO_SECTIONS: Final = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<---Назад', callback_data='back_sections')]
])

BACK_TO_CATEGORY: Final = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<---Назад', callback_data='back_category')]
])

