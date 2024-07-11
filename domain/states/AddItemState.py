from aiogram.fsm.state import StatesGroup, State


class AddItemState(StatesGroup):
    title = State()
    desc = State()
    cost = State()
    preview = State()

