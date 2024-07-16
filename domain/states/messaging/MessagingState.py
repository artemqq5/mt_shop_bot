from aiogram.fsm.state import StatesGroup, State


class MessagingState(StatesGroup):
    MessagingType = State()
    TelegramID = State()
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    RepeatButton = State()
    Preview = State()
