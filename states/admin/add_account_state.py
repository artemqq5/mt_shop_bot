from aiogram.dispatcher.filters.state import StatesGroup, State


class AddAccountState(StatesGroup):
    type = State()
    geo = State()
    name = State()
    desc = State()
    price = State()
    count = State()
