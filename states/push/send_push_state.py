from aiogram.dispatcher.filters.state import StatesGroup, State


class SendPushState(StatesGroup):
    type = State()
    id = State()
    message = State()
