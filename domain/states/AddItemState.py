from aiogram.fsm.state import StatesGroup, State


class AddItemState(StatesGroup):
    category = State()
    title = State()
    desc = State()
    cost = State()
    preview = State()

