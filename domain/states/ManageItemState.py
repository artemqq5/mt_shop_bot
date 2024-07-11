from aiogram.fsm.state import StatesGroup, State


class ManagementItemState(StatesGroup):
    category = State()

