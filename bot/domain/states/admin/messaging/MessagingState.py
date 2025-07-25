from aiogram.fsm.state import State, StatesGroup


class MessagingState(StatesGroup):
    MessagingType = State()
    TelegramID = State()
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    RepeatButton = State()
    Preview = State()
