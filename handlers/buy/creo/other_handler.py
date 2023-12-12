import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.constants.base_constants import WRONG_FORRMAT_DATE, SKIP
from data.constants.design_constants import *
from handlers.buy.creo.creo_use_case.format_task_view import check_view_order
from handlers.buy.creo.creo_use_case.send_order_creo import send_order_creo
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from keyboard.creo.design_keyboard import check_task_view_keyboard
from states.creo.creo_other_state import CreoOtherState


def register_creo_other_handlers(dispatcher):
    dispatcher.register_message_handler(callback=set_format_other_creative, state=CreoOtherState.format)
    dispatcher.register_message_handler(callback=set_offer_other_creative, state=CreoOtherState.offer)
    dispatcher.register_message_handler(callback=set_source_other_creative, state=CreoOtherState.source)
    dispatcher.register_message_handler(callback=set_description_other_creative, state=CreoOtherState.description)
    dispatcher.register_message_handler(callback=set_deadline_other_creative, state=CreoOtherState.deadline)


# set format -> request offer
async def set_format_other_creative(message: types.Message, state: FSMContext):
    await CreoOtherState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=cancel_keyboard())


# set offer -> request source
async def set_offer_other_creative(message: types.Message, state: FSMContext):
    await CreoOtherState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(offer=message.text)
    else:
        await state.update_data(offer=message.text)

    await message.answer(SOURCE_MESSAGE, reply_markup=cancel_keyboard())


# set source -> request description
async def set_source_other_creative(message: types.Message, state: FSMContext):
    await CreoOtherState.next()
    await state.update_data(source=message.text)
    await message.answer(DESCRIPTION_MESSAGE, reply_markup=cancel_keyboard())


# set description -> request deadline
async def set_description_other_creative(message: types.Message, state: FSMContext):
    await CreoOtherState.next()
    await state.update_data(description=message.text)
    task_data = await state.get_data()
    await message.answer(check_view_order(task_data), reply_markup=check_task_view_keyboard())


# set deadline ->
async def set_deadline_other_creative(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        try:
            date_time = datetime.datetime.strptime(message.text + " +0400", '%Y-%m-%d %H:%M %z')
            # await message.answer(str(date_time)) todo output time for test

            await state.update_data(deadline=str(date_time))
            data = await state.get_data()
            await state.finish()
        except Exception as e:
            print(f"set_deadline_other_creative - {e}")
            data = None
            await message.answer(WRONG_FORRMAT_DATE, reply_markup=skip_keyboard())

        await send_order_creo(data, message)

    else:
        await state.update_data(deadline=None)
        data = await state.get_data()
        await state.finish()

        await send_order_creo(data, message)
