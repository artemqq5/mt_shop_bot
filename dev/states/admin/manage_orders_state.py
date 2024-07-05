from aiogram.dispatcher.filters.state import StatesGroup, State


class ManageOrderState(StatesGroup):
    type = State()
    managment = State()
    dropbox = State()
    refinement = State()

