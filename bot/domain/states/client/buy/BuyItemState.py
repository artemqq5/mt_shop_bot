from aiogram.fsm.state import State, StatesGroup


class BuyItemState(StatesGroup):
    Category = State()
    Item = State()
    BuySetCount = State()
    BuySetDesc = State()
    BuyItemPreview = State()
