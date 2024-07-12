from aiogram.fsm.state import StatesGroup, State


class ManagementItemState(StatesGroup):
    SetItem = State()
    DeleteItem = State()
