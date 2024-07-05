from aiogram.dispatcher.filters.state import StatesGroup, State


class UserOrdersState(StatesGroup):
    view = State()
    status = State()
    message = State()
