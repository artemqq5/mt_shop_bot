from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.constants.accounts_constants import *
from data.constants.base_constants import INPUT_INEGER, SKIP, CLIENT, ERROR_REGISTER_MESSAGE
from data.repository.users import UsersRepository
from handlers.buy.farm_use_case.output_farm import formatted_output_verification
from handlers.buy.farm_use_case.send_order_farm import send_order_verification
from is_banned import is_banned
from keyboard.accounts.accounts_keyboard import *
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard

from keyboard.accounts.accounts_keyboard import buy_item_keyboard
from states.farm.order_farm_state import OrderVerificationState


def register_order_verifications_handlers(dispatcher):
    dispatcher.register_message_handler(choice_verification, lambda message: message.text == VERIFICATIONS_FARM)
    dispatcher.register_callback_query_handler(
        details_verification_handler,
        lambda call: call.data in list_of_callback_verifications(),
        state=OrderVerificationState.order
    )
    dispatcher.register_message_handler(desc_verification_order, state=OrderVerificationState.desc)
    dispatcher.register_message_handler(count_verification_order, state=OrderVerificationState.count)


async def choice_verification(message: types.Message):
    if await is_banned(message):
        return

    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == CLIENT:

            await OrderVerificationState.order.set()

            verifications = AccountsRepository().get_verifications()
            open_verifications = []
            for i in verifications:
                if i['visibility'] == OPEN_STATE:
                    open_verifications.append(i)

            if len(open_verifications) > 0:
                await message.answer(CARDS_FARM, reply_markup=available_verifications_keyboard(open_verifications))
            else:
                await message.answer(ITEMS_IS_EMPTY)
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def details_verification_handler(callback: types.CallbackQuery, state: FSMContext):

    verification_type = AccountsRepository().get_verification(callback.data.split("_")[1])

    if verification_type is not None:
        if callback.data.split("_")[0] == "verification":
            await callback.message.answer(
                text=formatted_output_verification(verification_type),
                reply_markup=buy_item_keyboard(verification_type['id'])
            )
        else:
            await state.update_data(account=verification_type)
            await OrderVerificationState.desc.set()
            await callback.message.answer(PARAM_DESC, reply_markup=skip_keyboard())


async def desc_verification_order(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        await state.update_data(desc=message.text)
    await OrderVerificationState.count.set()
    await message.answer(PARAM_COUNT, reply_markup=cancel_keyboard())


async def count_verification_order(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        if count <= 0:
            await message.answer(COUNT_IS_BIGGER_ZERO, reply_markup=cancel_keyboard())
        else:
            await state.update_data(count=count)
            data = await state.get_data()
            await state.finish()

            await send_order_verification(data, message)

    except Exception as e:
        print(f"count_verification_order: {e}")
        await message.answer(INPUT_INEGER, reply_markup=cancel_keyboard())

