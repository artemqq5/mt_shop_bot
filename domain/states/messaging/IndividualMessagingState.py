from aiogram.fsm.state import StatesGroup, State


class IndividualMessagingState(StatesGroup):
    UserID = State()
    Message = State()
    Media = State()
    ButtonText = State()
    ButtonUrl = State()
    Preview = State()
