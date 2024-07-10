from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from dev.constants.accounts_constants import *
from dev.constants.base_constants import INPUT_INEGER, SKIP, CLIENT, ERROR_REGISTER_MESSAGE
from data.repository.users import UsersRepository
from handlers.buy.farm_use_case.output_farm import formatted_output_cabinet
from handlers.buy.farm_use_case.send_order_farm import send_order_cabinet
from dev.is_banned import is_banned
from keyboard.accounts.accounts_keyboard import *
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard

from keyboard.accounts.accounts_keyboard import buy_item_keyboard
from states.farm.order_farm_state import OrderCabinetState


def register_order_cabinets_handlers(dispatcher):
    dispatcher.register_message_handler(choice_cabinet, lambda message: message.text == CABINETS_FARM)
    dispatcher.register_callback_query_handler(
        details_cabinet_handler,
        lambda call: call.data in list_of_callback_cabinets(),
        state=OrderCabinetState.order
    )
    dispatcher.register_message_handler(desc_cabinet_order, state=OrderCabinetState.desc)
    dispatcher.register_message_handler(count_cabinet_order, state=OrderCabinetState.count)


async def choice_cabinet(message: types.Message):
    if await is_banned(message):
        return

    current_user = UsersRepository().get_user(message.chat.id)
    if current_user is not None:
        if current_user['position'] == CLIENT:

            await OrderCabinetState.order.set()

            cabinets = AccountsRepository().get_cabinets()
            open_cabinets = []
            for i in cabinets:
                if i['visibility'] == OPEN_STATE:
                    open_cabinets.append(i)

            if len(open_cabinets) > 0:
                await message.answer(CARDS_FARM, reply_markup=available_cabinets_keyboard(open_cabinets))
            else:
                await message.answer(ITEMS_IS_EMPTY)
    else:
        await message.answer(ERROR_REGISTER_MESSAGE, reply_markup=ReplyKeyboardRemove())


async def details_cabinet_handler(callback: types.CallbackQuery, state: FSMContext):

    cabinet_type = AccountsRepository().get_cabinet(callback.data.split("_")[1])

    if cabinet_type is not None:
        if callback.data.split("_")[0] == "cabinet":
            await callback.message.answer(
                text=formatted_output_cabinet(cabinet_type),
                reply_markup=buy_item_keyboard(cabinet_type['id'])
            )
        else:
            await state.update_data(account=cabinet_type)
            await OrderCabinetState.desc.set()
            await callback.message.answer(PARAM_DESC, reply_markup=skip_keyboard())


async def desc_cabinet_order(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        await state.update_data(desc=message.text)
    await OrderCabinetState.count.set()
    await message.answer(PARAM_COUNT, reply_markup=cancel_keyboard())


async def count_cabinet_order(message: types.Message, state: FSMContext):
    try:
        count = int(message.text)
        if count <= 0:
            await message.answer(COUNT_IS_BIGGER_ZERO, reply_markup=cancel_keyboard())
        else:
            await state.update_data(count=count)
            data = await state.get_data()
            await state.finish()

            await send_order_cabinet(data, message)

    except Exception as e:
        print(f"count_cabinet_order: {e}")
        await message.answer(INPUT_INEGER, reply_markup=cancel_keyboard())