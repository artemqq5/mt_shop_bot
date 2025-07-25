from aiogram.fsm.state import State, StatesGroup


class BanSystemState(StatesGroup):
    ChoiceOperation = State()
    BanUserID = State()
    UnBanUserID = State()
    BanListUser = State()
