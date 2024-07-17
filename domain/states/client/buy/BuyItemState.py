from aiogram.fsm.state import StatesGroup, State


class BuyItemState(StatesGroup):
    Category = State()
    