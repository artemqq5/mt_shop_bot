from aiogram.dispatcher.filters.state import StatesGroup, State


class CreoAppState(StatesGroup):
    general = State()
    platform = State()
    format = State()
    offer = State()
    source = State()
    description = State()
    deadline = State()
