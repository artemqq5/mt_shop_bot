from aiogram.dispatcher.filters.state import StatesGroup, State


class ShowItemState(StatesGroup):
    show_item = State()
    account_details = State()
