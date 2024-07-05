from aiogram.dispatcher.filters.state import StatesGroup, State


class AgencyTypeState(StatesGroup):
    type = State()
