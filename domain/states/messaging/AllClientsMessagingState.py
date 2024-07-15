from aiogram.fsm.state import StatesGroup, State


class AllClientsMessagingState(StatesGroup):
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    Preview = State()

