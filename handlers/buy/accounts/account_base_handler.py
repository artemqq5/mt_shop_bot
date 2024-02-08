from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import *
from data.constants.base_constants import INPUT_INEGER, SKIP, CLIENT, ERROR_REGISTER_MESSAGE
from data.repository.users import UsersRepository
from handlers.buy.accounts.account_use_case.output_farm import formatted_output_account
from handlers.buy.accounts.account_use_case.send_order_account import send_order_account
from keyboard.accounts.accounts_keyboard import *
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard

from keyboard.accounts.accounts_keyboard import buy_account_keyboard
from states.account.order_account_state import OrderAccountState


def register_accounts_handlers(dispatcher):
    dispatcher.register_message_handler(source_account, lambda message: message.text == ACCOUNTS)
    dispatcher.register_message_handler(choice_account, lambda message: message.text in LIST_OF_ACCOUNTS_TYPE,
                                        state=OrderAccountState.source)
    dispatcher.register_callback_query_handler(details_account_handler,
                                               lambda call: call.data in list_of_callback_accounts(), state=OrderAccountState.source)
    dispatcher.register_message_handler(desc_account_order, state=OrderAccountState.desc)
    dispatcher.register_message_handler(count_account_order, state=OrderAccountState.count)


async def source_account(message: types.Message):
    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == CLIENT:
            # main ====================
            await OrderAccountState.source.set()
            await message.answer(CHOICE_TYPE_OF_ACCOUNT, reply_markup=source_account_keyboard())
            # =========================
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def choice_account(message: types.Message):
    accounts = AccountsRepository().get_accounts()
    open_accounts = []
    for i in accounts:
        if i['visibility'] == OPEN_STATE and i['type'] == message.text:
            open_accounts.append(i)

    if len(open_accounts) > 0:
        await message.answer(ACCOUNTS, reply_markup=available_accounts_keyboard(open_accounts))
    else:
        await message.answer(ITEMS_IS_EMPTY)


async def details_account_handler(callback: types.CallbackQuery, state: FSMContext):
    account_type = AccountsRepository().get_account(callback.data.split("_")[1])

    if account_type is not None:
        if callback.data.split("_")[0] == "account":
            await callback.message.answer(
                text=formatted_output_account(account_type),
                reply_markup=buy_account_keyboard(account_type['id'])
            )
        else:
            await OrderAccountState().next()
            await state.update_data(account=account_type)
            await OrderAccountState.next()
            await callback.message.answer(PARAM_DESC_ACCOUNT, reply_markup=skip_keyboard())


async def desc_account_order(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        await state.update_data(desc=message.text)
    await OrderAccountState.next()
    await message.answer(PARAM_COUNT_ACCOUNT, reply_markup=cancel_keyboard())


async def count_account_order(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        if count <= 0:
            await message.answer(COUNT_IS_BIGGER_ZERO, reply_markup=cancel_keyboard())
        else:
            await state.update_data(count=count)
            data = await state.get_data()
            await state.finish()

            await send_order_account(data, message)

    except Exception as e:
        print(f"count_account_order: {e}")
        await message.answer(INPUT_INEGER, reply_markup=cancel_keyboard())
