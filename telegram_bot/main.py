from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from telegram_bot.handlers import register_all_handlers
from env import TOKEN

async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)

async def start_telegram_bot() -> None:
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    register_all_handlers(dp)
    await dp.start_polling(bot, skip_updates=True, on_startup=__on_start_up)