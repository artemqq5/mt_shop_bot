from aiogram.fsm.state import StatesGroup, State


class ManageItemState(StatesGroup):
    SetItem = State()
