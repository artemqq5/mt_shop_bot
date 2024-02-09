from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import *
from data.constants.admin_constants import *
from data.constants.base_constants import *
from data.repository.users import UsersRepository
from handlers.admin.add_items.add_account import register_add_account_handlers
from handlers.admin.add_items.add_cabinet import register_add_cabinet_handlers
from handlers.admin.add_items.add_card import register_add_card_handlers
from handlers.admin.add_items.add_verification import register_add_verification_handlers
from keyboard.admin.admin_items_keyboard import choice_type_account_keyboard, choice_type_item_keyboard
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.add_item_state import AddItemState, AddAccountState, AddCardState, AddCabinetState, \
    AddVerificationState


def register_add_item_handlers(dispatcher):
    dispatcher.register_message_handler(type_of_add_item, lambda message: message.text == ADD_ITEMS)
    dispatcher.register_message_handler(add_items_handler, lambda message: message.text in LIST_OF_ITEMS_TYPE,
                                        state=AddItemState.add_item)

    # register add farm, card, cabinet, verification
    register_add_account_handlers(dispatcher)
    register_add_card_handlers(dispatcher)
    register_add_cabinet_handlers(dispatcher)
    register_add_verification_handlers(dispatcher)


async def type_of_add_item(message: types.Message):
    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if (current_user['position'] == ADMIN and
                (current_user['sub_position'] is None or current_user['sub_position'] == SUB_POSITION_ACCOUNT)):
            # main ====================
            await AddItemState.add_item.set()  # set state to add item
            await message.answer(CHOICE_TYPE_OF_ADD, reply_markup=choice_type_item_keyboard())
            # ==========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def add_items_handler(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == ACCOUNT_ITEM:
        await AddAccountState.type.set()
        await message.answer(CHOICE_TYPE_OF_ACCOUNT, reply_markup=choice_type_account_keyboard())
    elif message.text == CARDS_FARM:
        await AddCardState.name.set()
        await message.answer(INPUT_NAME_OF_ITEM, reply_markup=cancel_keyboard())
    elif message.text == CABINETS_FARM:
        await AddCabinetState.name.set()
        await message.answer(INPUT_NAME_OF_ITEM, reply_markup=cancel_keyboard())
    elif message.text == VERIFICATIONS_FARM:
        await AddVerificationState.name.set()
        await message.answer(INPUT_NAME_OF_ITEM, reply_markup=cancel_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)

