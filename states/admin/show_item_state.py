from aiogram.dispatcher.filters.state import StatesGroup, State


class ShowItemState(StatesGroup):
    type = State()


class ShowAccountState(StatesGroup):
    source = State()


class ShowCardsState(StatesGroup):
    source = State()


class ShowCabinetsState(StatesGroup):
    source = State()


class ShowVerificationsState(StatesGroup):
    source = State()
