from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import INPUT_DESC_OF_ITEM, INPUT_PRICE_OF_ITEM, ACCOUNTS, INPUT_GEO_OF_ITEM
from data.constants.base_constants import ADMIN, NO_ACCESS, ERROR_REGISTER_MESSAGE
from data.repository.users import UsersRepository
from handlers.admin.db_use_case.add_farm import add_verification_case
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.add_item_state import AddVerificationState


def register_add_verification_handlers(dispatcher):
    dispatcher.register_message_handler(choice_name_verification, state=AddVerificationState.name)
    dispatcher.register_message_handler(choice_geo_verification, state=AddVerificationState.geo)
    dispatcher.register_message_handler(choice_desc_verification, state=AddVerificationState.desc)
    dispatcher.register_message_handler(choice_price_verification, state=AddVerificationState.price)


async def choice_name_verification(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await AddVerificationState.geo.set()
    await message.answer(INPUT_GEO_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_geo_verification(message: types.Message, state: FSMContext):
    await state.update_data(geo=message.text)
    await AddVerificationState.desc.set()
    await message.answer(INPUT_DESC_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_desc_verification(message: types.Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await AddVerificationState.price.set()
    await message.answer(INPUT_PRICE_OF_ITEM, reply_markup=cancel_keyboard())


async def choice_price_verification(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)

    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if (current_user['position'] == ADMIN and
                (current_user['sub_position'] is None or current_user['sub_position'] == ACCOUNTS)):
            # main ====================
            data = await state.get_data()
            await state.finish()

            await add_verification_case(data, message)
            # ===========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
