from aiogram.fsm.state import State, StatesGroup


class AddItemState(StatesGroup):
    title = State()
    desc = State()
    cost = State()
    preview = State()
