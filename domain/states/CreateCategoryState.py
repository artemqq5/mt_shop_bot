from aiogram.fsm.state import StatesGroup, State


class CreateCategoryState(StatesGroup):
    name = State()

