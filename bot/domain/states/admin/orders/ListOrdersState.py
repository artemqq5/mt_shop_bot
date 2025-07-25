from aiogram.fsm.state import State, StatesGroup


class ListOrdersState(StatesGroup):
    ListOrders = State()
    OrderView = State()
