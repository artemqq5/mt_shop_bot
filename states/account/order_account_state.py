from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderAccountState(StatesGroup):
    source = State()
    account = State()
    desc = State()
    count = State()
