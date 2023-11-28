from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.admin_constants import *
from data.constants.base_constants import *
from data.repository import MyRepository
from handlers.accounts.account_use_case.output_account import formatted_output_account
from keyboard.admin.admin_items_keyboard import choice_type_item_keyboard, show_item_accounts_keyboard, \
    manag_item_keyboard
from keyboard.base_keyboard import cancel_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.show_item_state import ShowItemState


def register_show_item_handlers(dispatcher):
    dispatcher.register_message_handler(type_of_show_item, lambda message: message.text == SHOW_ITEMS)
    dispatcher.register_message_handler(show_items_handler, state=ShowItemState.show_item)
    dispatcher.register_callback_query_handler(account_detail_handler, state=ShowItemState.account_details)


async def type_of_show_item(message: types.Message, state: FSMContext):
    current_user = MyRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ====================
            await ShowItemState.show_item.set()  # set state to show item
            await message.answer(CHOICE_TYPE_OF_SHOW, reply_markup=choice_type_item_keyboard())
            # ==========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def show_items_handler(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == ACCOUNT_ITEM:
        await ShowItemState.account_details.set()
        await message.answer(ACCOUNT_ITEM, reply_markup=show_item_accounts_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)


async def account_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = MyRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ======================
            if HIDE_STATE in callback.data:
                result = MyRepository().exchange_visibility_account(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data:
                result = MyRepository().exchange_visibility_account(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            else:
                account_info = MyRepository().get_account(callback.data)
                await callback.message.answer(formatted_output_account(account_info), reply_markup=manag_item_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
