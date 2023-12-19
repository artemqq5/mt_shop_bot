from aiogram.dispatcher.filters.state import StatesGroup, State


class CreoOtherState(StatesGroup):
    general = State()
    format = State()
    offer = State()
    source = State()
    description = State()

    count = State()
    sub_description = State()

    check = State()
    deadline = State()
