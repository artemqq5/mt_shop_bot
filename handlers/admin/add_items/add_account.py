from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import INPUT_GEO_OF_ITEM, INPUT_NAME_OF_ITEM, INPUT_COUNT_OF_ITEM, \
    INPUT_DESC_OF_ITEM, INPUT_PRICE_OF_ITEM, LIST_OF_ACCOUNTS_TYPE, ACCOUNTS, FB_TYPE, GOOGLE_TYPE
from data.constants.admin_constants import ACCOUNT_TYPE_GOOGLE, ACCOUNT_TYPE_FB
from data.constants.base_constants import ADMIN, NO_ACCESS, ERROR_REGISTER_MESSAGE, INPUT_INEGER, SUB_POSITION_ACCOUNT
from data.repository.users import UsersRepository
from handlers.admin.db_use_case.add_farm import add_account_case
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.add_item_state import AddAccountState


def register_add_account_handlers(dispatcher):
    dispatcher.register_message_handler(choice_type_account, lambda message: message.text in LIST_OF_ACCOUNTS_TYPE,
                                        state=AddAccountState.type)
    dispatcher.register_message_handler(choice_geo_account, state=AddAccountState.geo)
    dispatcher.register_message_handler(choice_name_account, state=AddAccountState.name)
    dispatcher.register_message_handler(choice_desc_account, state=AddAccountState.desc)
    dispatcher.register_message_handler(choice_price_account, state=AddAccountState.price)


async def choice_type_account(message: types.Message, state: FSMContext):
    if message.text == FB_TYPE:
        await state.update_data(type=ACCOUNT_TYPE_FB)
    elif message.text == GOOGLE_TYPE:
        await state.update_data(type=ACCOUNT_TYPE_GOOGLE)

    await AddAccountState.next()
    await message.answer(INPUT_GEO_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_geo_account(message: types.Message, state: FSMContext):
    await state.update_data(geo=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_NAME_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_name_account(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_DESC_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_desc_account(message: types.Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_PRICE_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_price_account(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)

    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if (current_user['position'] == ADMIN and
                (current_user['sub_position'] is None or current_user['sub_position'] == SUB_POSITION_ACCOUNT)):
            # main ====================
            data = await state.get_data()
            await state.finish()

            await add_account_case(data, message)
            # ===========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())

