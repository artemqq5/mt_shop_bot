from aiogram.fsm.state import State, StatesGroup


class ProfileState(StatesGroup):
    ProfileView = State()
    Orders = State()
