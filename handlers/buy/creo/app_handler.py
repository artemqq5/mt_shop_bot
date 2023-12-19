import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.constants.base_constants import WRONG_FORRMAT_DATE, SKIP
from data.constants.design_constants import *
from handlers.buy.creo.creo_use_case.format_task_view import check_view_order
from handlers.buy.creo.creo_use_case.send_order_creo import send_order_creo
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from keyboard.creo.design_keyboard import check_task_view_keyboard
from states.creo.creo_app_state import CreoAppState


def register_creo_app_handlers(dispatcher):
    dispatcher.register_message_handler(callback=set_plarform_app_creative, state=CreoAppState.platform)
    dispatcher.register_message_handler(callback=set_format_app_creative, state=CreoAppState.format)
    dispatcher.register_message_handler(callback=set_offer_app_creative, state=CreoAppState.offer)
    dispatcher.register_message_handler(callback=set_source_app_creative, state=CreoAppState.source)
    dispatcher.register_message_handler(callback=set_description_app_creative, state=CreoAppState.description)
    dispatcher.register_message_handler(callback=set_count_app_creative, state=[CreoAppState.count, CreoAppState.sub_description])
    dispatcher.register_message_handler(callback=set_deadline_app_creative, state=CreoAppState.deadline)


# set platform -> request format
async def set_plarform_app_creative(message: types.Message, state: FSMContext):
    await CreoAppState.next()
    await state.update_data(plarform=message.text)
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        await message.answer(FORMAT_MESSAGE, reply_markup=skip_keyboard())
    else:
        await message.answer(FORMAT_MESSAGE, reply_markup=cancel_keyboard())


# set format -> request offer
async def set_format_app_creative(message: types.Message, state: FSMContext):
    await CreoAppState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=cancel_keyboard())


# set offer -> request source
async def set_offer_app_creative(message: types.Message, state: FSMContext):
    await CreoAppState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(offer=message.text)
    else:
        await state.update_data(offer=message.text)

    await message.answer(SOURCE_MESSAGE, reply_markup=cancel_keyboard())


# set source -> request description
async def set_source_app_creative(message: types.Message, state: FSMContext):
    await CreoAppState.next()
    await state.update_data(source=message.text)
    await message.answer(DESCRIPTION_MESSAGE, reply_markup=cancel_keyboard())


# set description -> request count\sub_desc
async def set_description_app_creative(message: types.Message, state: FSMContext):
    await CreoAppState.count.set()
    await state.update_data(description=message.text)
    await message.answer(COUNT_OF_CREO, reply_markup=skip_keyboard())


async def set_count_app_creative(message: types.Message, state: FSMContext):
    state_type = await state.get_state()
    if state_type == CreoAppState.count.state:
        if message.text == SKIP:
            await state.update_data(count=1)
            await CreoAppState.check.set()
            task_data = await state.get_data()
            await message.answer(check_view_order(task_data), reply_markup=check_task_view_keyboard())
        else:
            try:
                count = int(message.text)
                await state.update_data(count=count)
                if count > 1:
                    await CreoAppState.sub_description.set()
                    await message.answer(SUB_DESC_FOR_OTHER_CREO, reply_markup=cancel_keyboard())
                elif count == 1:
                    await CreoAppState.check.set()
                    task_data = await state.get_data()
                    await message.answer(check_view_order(task_data), reply_markup=check_task_view_keyboard())
                else:
                    await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
            except Exception as e:
                print(f"set_count_app_creative: {e}")
                await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
    else:
        await state.update_data(sub_description=message.text)
        await CreoAppState.check.set()
        task_data = await state.get_data()
        await message.answer(check_view_order(task_data), reply_markup=check_task_view_keyboard())


# set deadline ->
async def set_deadline_app_creative(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        try:
            date_time = datetime.datetime.strptime(message.text + " +0400", '%Y-%m-%d %H:%M %z')
            # await message.answer(str(date_time)) todo output time for test

            await state.update_data(deadline=str(date_time))
            data = await state.get_data()
            await state.finish()
        except Exception as e:
            print(f"set_deadline_app_creative - {e}")
            data = None
            await message.answer(WRONG_FORRMAT_DATE, reply_markup=skip_keyboard())

        await send_order_creo(data, message)

    else:
        await state.update_data(deadline=None)
        data = await state.get_data()
        await state.finish()

        await send_order_creo(data, message)
