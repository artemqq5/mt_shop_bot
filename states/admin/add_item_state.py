from aiogram.dispatcher.filters.state import StatesGroup, State


class AddItemState(StatesGroup):
    add_item = State()


class AddAccountState(StatesGroup):
    type = State()
    geo = State()
    name = State()
    desc = State()
    price = State()


class AddCardState(StatesGroup):
    name = State()
    desc = State()
    price = State()


class AddCabinetState(StatesGroup):
    name = State()
    desc = State()
    price = State()


class AddVerificationState(StatesGroup):
    name = State()
    geo = State()
    desc = State()
    price = State()

