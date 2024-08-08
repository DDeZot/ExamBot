from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from telegram_bot.utils import CPP_EXAM, MATH_EXAM
from telegram_bot.states.client_state import ClientState
from telegram_bot.keyboards.markups import setMarkup, BACK_TO_SECTIONS, BACK_TO_EXAMS, BACK_TO_CATEGORY

async def exam_choose(msg: Message, state: FSMContext) -> None:
    bot: Bot = msg.bot
    user_id = msg.from_user.id

    await bot.send_message(user_id, text='Вернуться назад:', reply_markup=BACK_TO_EXAMS)

    if(msg.text == 'C++'): 
        await bot.send_message(user_id, text='Список разделов: ', reply_markup=setMarkup(items=CPP_EXAM))
        await state.update_data(EXAM_CHOSEN=CPP_EXAM)
        await state.set_state(ClientState.CATEGORY_CHOISING)    

    if(msg.text == 'Мат. Анализ'): 
        await bot.send_message(user_id, text='Список разделов: ', reply_markup=setMarkup(items=MATH_EXAM))
        await state.update_data(EXAM_CHOSEN=MATH_EXAM)
        await state.set_state(ClientState.SECTION_CHOISING) 

    #if(msg.text == 'Python'): 
    #    await bot.send_message(user_id, text='Список разделов: ', reply_markup=setMarkup(items=PYTHON_EXAM))
    #    await state.update_data(EXAM_CHOSEN=PYTHON_EXAM)
    #    await state.set_state(ClientState.EXAM_CHOSEN) 
    
async def category_choose(msg: Message, state: FSMContext) -> None:
    dict = await state.get_data()
    bot: Bot = msg.bot
    user_id = msg.from_user.id

    await bot.send_message(user_id, text='Вернуться назад:', reply_markup=BACK_TO_CATEGORY)
    await bot.send_message(user_id, text='Список категорий: ', reply_markup=setMarkup(items=dict['EXAM_CHOSEN'][msg.text]))

    await state.update_data(EXAM_CHOSEN=dict['EXAM_CHOSEN'], 
                            CATEGORY_CHOSEN = dict['EXAM_CHOSEN'][msg.text])
    await state.set_state(ClientState.SECTION_CHOISING)
    
async def section_choose(msg: Message, state: FSMContext) -> None:
    dict = await state.get_data()
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await bot.send_message(user_id, text='Вернуться назад:', reply_markup=BACK_TO_EXAMS)
    await bot.send_message(user_id, text='Список вопросов/билетов: ', reply_markup=setMarkup(items=dict['EXAM_CHOSEN'][msg.text]))

    await state.update_data(EXAM_CHOSEN=dict['EXAM_CHOSEN'], 
                            CATEGORY_CHOSEN = dict['CATEGORY_CHOSEN'], 
                            SECTION_CHOSEN=dict['CATEGORY_CHOSEN'][msg.text])
    
    await state.set_state(ClientState.QUESTION_CHOISING)

async def question_choose(msg: Message, state: FSMContext) -> None:
    dict = await state.get_data()
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await bot.send_message(user_id, text='Вернуться назад:', reply_markup=BACK_TO_EXAMS)
    if(dict['SECTION_CHOSEN'][msg.text]['text']): await bot.send_message(user_id, text=dict['SECTION_CHOSEN'][msg.text]['text'])
    if(dict['SECTION_CHOSEN'][msg.text]['photo']): await bot.send_photo(user_id, photo=FSInputFile(path=dict['SECTION_CHOSEN'][msg.text]['photo']))
    
async def back_to_category(state: FSMContext):  
    data = state.get_data()

    message: str

    if(data['EXAM_CHOSEN'] == CPP_EXAM):
        message = 'C++'
    if(data['EXAM_CHOSEN'] == MATH_EXAM):
        message = 'Мат. Анализ'
    
    state.set_state(ClientState.EXAM_CHOISING)
    state.set_data(None)
    exam_choose(msg= message, state= ClientState.EXAM_CHOISING)
    