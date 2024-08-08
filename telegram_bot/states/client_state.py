from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class ClientState(StatesGroup):
    EXAM_CHOISING = State()
    CATEGORY_CHOISING = State()
    SECTION_CHOISING = State()
    QUESTION_CHOISING = State()