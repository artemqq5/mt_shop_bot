from aiogram.dispatcher.filters.state import StatesGroup, State


class BanSystemState(StatesGroup):
    todo = State()
    ban = State()
    message = State()
    finish = State()

