from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.base_constants import *
from data.repository.users import UsersRepository
from handlers.buy.accounts.account_use_case.output_account import formatted_output_account
from keyboard.accounts.accounts_keyboard import source_account_keyboard
from keyboard.admin.admin_items_keyboard import *
from keyboard.menu.menu_keyboard import main_keyboard
from states.admin.show_item_state import ShowItemState, ShowAccountState


def register_show_item_handlers(dispatcher):
    dispatcher.register_message_handler(type_of_show_item, lambda message: message.text == SHOW_ITEMS)
    dispatcher.register_message_handler(choice_account_type, lambda message: message.text in LIST_OF_ITEMS_TYPE,
                                        state=ShowItemState.type)
    dispatcher.register_message_handler(source_account_item, lambda message: message.text in LIST_OF_ACCOUNTS_TYPE,
                                        state=ShowAccountState.source)
    dispatcher.register_callback_query_handler(account_detail_handler,
                                               lambda call: call.data in list_of_callback_show_item(),
                                               state=ShowAccountState.source)


async def type_of_show_item(message: types.Message, state: FSMContext):
    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ====================
            await ShowItemState.type.set()  # set state to show item
            await message.answer(CHOICE_TYPE_OF_SHOW, reply_markup=choice_type_item_keyboard())
            # ==========================
        else:
            await message.answer(NO_ACCESS, reply_markup=main_keyboard(message))
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def choice_account_type(message: types.Message, state: FSMContext):
    await state.finish()

    if message.text == ACCOUNT_ITEM:
        await ShowAccountState.source.set()
        await message.answer(CHOICE_TYPE_OF_ACCOUNT, reply_markup=source_account_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)


async def source_account_item(message: types.Message):
    await message.answer(ACCOUNT_ITEM, reply_markup=show_item_accounts_keyboard(message.text))


async def account_detail_handler(callback: types.CallbackQuery, state: FSMContext):
    current_user = UsersRepository().get_user(callback.message.chat.id)
    if current_user is not None:
        if current_user['position'] == ADMIN:
            # main ======================
            if HIDE_STATE in callback.data:
                result = AccountsRepository().exchange_visibility_account(HIDE_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            elif OPEN_STATE in callback.data:
                result = AccountsRepository().exchange_visibility_account(OPEN_STATE, callback.data.split("_")[1])
                if result is not None:
                    await callback.message.answer(SUCCESULL_UPDATE_VISIBILITY)
                else:
                    await callback.message.answer(FAIL_UPDATE_VISIBILITY)
            else:
                account_info = AccountsRepository().get_account(callback.data)
                await callback.message.answer(formatted_output_account(account_info),
                                              reply_markup=manag_item_keyboard(callback.data))
            # ============================
        else:
            await callback.message.answer(NO_ACCESS, reply_markup=main_keyboard(callback.message))
    else:
        await callback.message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())
