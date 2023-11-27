from aiogram import types
from aiogram.dispatcher import FSMContext

from data.constants.accounts_constants import *
from data.constants.base_constants import NOT_IMPLEMENTED, INPUT_INEGER, SKIP
from handlers.accounts.account_use_case.output_account import formatted_output_account
from handlers.accounts.account_use_case.send_order_account import send_order_account
from keyboard.accounts.accounts_keyboard import *
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from states.account.order_account_state import OrderAccountState


def register_accounts_handlers(dispatcher):
    dispatcher.register_message_handler(choice_account, lambda message: message.text == ACCOUNTS)
    dispatcher.register_message_handler(desc_account_order, state=OrderAccountState.desc)
    dispatcher.register_message_handler(count_account_order, state=OrderAccountState.count)
    dispatcher.register_callback_query_handler(details_account_handler,
                                               lambda call: call.data in list_of_callback_accounts())


async def choice_account(message: types.Message):
    accounts = MyRepository().get_accounts()

    if len(accounts) > 0:
        await message.answer(ACCOUNTS, reply_markup=available_accounts_keyboard(accounts))
    else:
        await message.answer(ITEMS_IS_EMPTY)


async def details_account_handler(callback: types.CallbackQuery, state: FSMContext):

    account_type = MyRepository().get_account(callback.data.split("_")[1])

    if account_type is not None:
        if callback.data.split("_")[0] == "account":
            await callback.message.answer(
                text=formatted_output_account(account_type),
                reply_markup=buy_account_keyboard(account_type['id'])
            )
        else:
            await OrderAccountState().account.set()
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
        await state.update_data(count=count)
        data = await state.get_data()
        await state.finish()

        await send_order_account(data, message)

    except Exception as e:
        print(f"count_account_order: {e}")
        await message.answer(INPUT_INEGER, reply_markup=cancel_keyboard())


