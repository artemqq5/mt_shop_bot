from aiogram.fsm.state import StatesGroup, State


class ProfileState(StatesGroup):
    ProfileView = State()
    Orders = State()
