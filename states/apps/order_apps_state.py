from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderAppsState(StatesGroup):
    choice_type_app = State()
