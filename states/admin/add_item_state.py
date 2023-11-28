from aiogram.dispatcher.filters.state import StatesGroup, State


class AddItemState(StatesGroup):
    add_item = State()
