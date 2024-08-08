from aiogram import Dispatcher, Bot, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from telegram_bot.handlers.user.exams import exam_choose, category_choose, section_choose, question_choose
from telegram_bot.keyboards import get_main_keyboard
from telegram_bot.states.client_state import ClientState

from typing import Any

async def __start(message: Message, state: FSMContext) -> None:
    bot: Bot = message.bot
    user_id = message.from_user.id
    await bot.send_message(user_id, f"{message.from_user.first_name}, че, сам ничего не можешь? Выбери экзамен, помогу, чем смогу.\n", reply_markup=get_main_keyboard())
    await state.set_state(ClientState.EXAM_CHOISING)

async def __help(message: Message) -> None:
    bot: Bot = message.bot
    user_id = message.from_user.id
    await bot.send_message(user_id, f"Мне бы кто помог...\n")

def register_users_handlers(rt: Router) -> None:
    rt.message.register(__start, Command('start'))
    rt.callback_query.register(__start, lambda c: c.data == 'back_exams')
    rt.message.register(__help, Command('help'))
    rt.message.register(exam_choose, ClientState.EXAM_CHOISING)
    rt.message.register(category_choose, ClientState.CATEGORY_CHOISING)
    rt.message.register(section_choose, ClientState.SECTION_CHOISING)
    rt.message.register(question_choose, ClientState.QUESTION_CHOISING)
    
