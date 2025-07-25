from aiogram.fsm.state import State, StatesGroup


class ManagementCategoryState(StatesGroup):
    SetCategory = State()
    CreateCategory = State()
    DeleteCategory = State()
