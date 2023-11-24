from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderCreativeState(StatesGroup):
    format = State()
    type = State()
    category = State()
