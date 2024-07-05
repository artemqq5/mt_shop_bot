from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderAccountState(StatesGroup):
    source = State()
    desc = State()
    count = State()


class OrderCardState(StatesGroup):
    order = State()
    desc = State()
    count = State()


class OrderCabinetState(StatesGroup):
    order = State()
    desc = State()
    count = State()


class OrderVerificationState(StatesGroup):
    order = State()
    desc = State()
    count = State()
