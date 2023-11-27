from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderAccountState(StatesGroup):
    account = State()
    desc = State()
    count = State()
