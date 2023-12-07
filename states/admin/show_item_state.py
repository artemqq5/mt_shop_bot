from aiogram.dispatcher.filters.state import StatesGroup, State


class ShowItemState(StatesGroup):
    type = State()


class ShowAccountState(StatesGroup):
    source = State()
