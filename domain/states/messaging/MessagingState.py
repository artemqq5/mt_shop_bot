from aiogram.fsm.state import StatesGroup, State


class MessagingState(StatesGroup):
    MessagingType = State()
