from aiogram.fsm.state import StatesGroup, State


class ManagementCategoryState(StatesGroup):
    SetCategory = State()
    CreateCategory = State()
    DeleteCategory = State()

