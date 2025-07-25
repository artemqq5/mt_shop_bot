from aiogram.fsm.state import StatesGroup, State


class BanSystemState(StatesGroup):
    ChoiceOperation = State()
    BanUserID = State()
    UnBanUserID = State()
    BanListUser = State()
