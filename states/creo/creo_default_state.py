from aiogram.dispatcher.filters.state import StatesGroup, State


class CreoDefaultState(StatesGroup):
    general = State()
    geo = State()
    language = State()
    currency = State()
    format = State()
    offer = State()
    voice = State()
    source = State()
    description = State()
    deadline = State()
    send = State()


