from aiogram.fsm.state import State, StatesGroup


class ManagementItemState(StatesGroup):
    SetItem = State()
    DeleteItem = State()
