from aiogram.fsm.state import StatesGroup, State


class ListOrdersState(StatesGroup):
    ListOrders = State()
    OrderView = State()
