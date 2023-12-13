from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import *
from data.constants.admin_constants import *
from data.constants.base_constants import *
from data.repository.users import UsersRepository
from handlers.admin.db_use_case.add_account import add_item_case
from keyboard.admin.admin_items_keyboard import choice_type_account_keyboard, choice_type_item_keyboard
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.add_account_state import AddAccountState
from states.admin.add_item_state import AddItemState


def register_add_item_handlers(dispatcher):
    dispatcher.register_message_handler(type_of_add_item, lambda message: message.text == ADD_ITEMS)
    dispatcher.register_message_handler(add_items_handler, lambda message: message.text in LIST_OF_ITEMS_TYPE,
                                        state=AddItemState.add_item)
    dispatcher.register_message_handler(choice_type_account, lambda message: message.text in LIST_OF_ACCOUNTS_TYPE,
                                        state=AddAccountState.type)
    dispatcher.register_message_handler(choice_geo_account, state=AddAccountState.geo)
    dispatcher.register_message_handler(choice_name_account, state=AddAccountState.name)
    dispatcher.register_message_handler(choice_desc_account, state=AddAccountState.desc)
    dispatcher.register_message_handler(choice_price_account, state=AddAccountState.price)
    dispatcher.register_message_handler(choice_count_account, state=AddAccountState.count)


async def type_of_add_item(message: types.Message):
    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ====================
            await AddItemState.add_item.set()  # set state to add item
            await message.answer(CHOICE_TYPE_OF_ADD, reply_markup=choice_type_item_keyboard())
            # ==========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def add_items_handler(message: types.Message, state: FSMContext):
    await state.finish()  # cancel state add item
    if message.text == ACCOUNT_ITEM:
        await AddAccountState.type.set()
        await message.answer(CHOICE_TYPE_OF_ACCOUNT, reply_markup=choice_type_account_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)


async def choice_type_account(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_GEO_OF_ACCOUNT, reply_markup=cancel_keyboard())


async def choice_geo_account(message: types.Message, state: FSMContext):
    await state.update_data(geo=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_NAME_OF_ACCOUNT, reply_markup=cancel_keyboard())


async def choice_name_account(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_DESC_OF_ACCOUNT, reply_markup=cancel_keyboard())


async def choice_desc_account(message: types.Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_PRICE_OF_ACCOUNT, reply_markup=cancel_keyboard())


async def choice_price_account(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await AddAccountState.next()
    await message.answer(INPUT_COUNT_OF_ACCOUNT, reply_markup=cancel_keyboard())


async def choice_count_account(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        current_user = UsersRepository().get_user(message.chat.id)
        if current_user is not None:
            if current_user['position'] == ADMIN:
                # main ====================
                # add item to db
                await state.update_data(count=count)
                data = await state.get_data()
                await state.finish()

                await add_item_case(data, message)
                # ===========================
            else:
                await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
        else:
            await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        print(f"choice_count_account: {e}")
        await message.answer(INPUT_INEGER, reply_markup=cancel_keyboard())
