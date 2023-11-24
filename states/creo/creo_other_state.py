from aiogram.dispatcher.filters.state import StatesGroup, State


class CreoOtherState(StatesGroup):
    general = State()
    format = State()
    offer = State()
    source = State()
    description = State()
    deadline = State()
    send = State()
