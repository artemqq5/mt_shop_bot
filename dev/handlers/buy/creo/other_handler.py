import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from dev.constants.base_constants import WRONG_FORRMAT_DATE, SKIP
from dev.constants.design_constants import *
from dev.handlers.buy.creo.creo_base_handler import check_size_message_creo
from handlers.buy.creo.creo_use_case.send_order_creo import send_order_creo
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from states.creo.creo_other_state import CreoOtherState


def register_creo_other_handlers(dispatcher):
    dispatcher.register_message_handler(callback=set_format_other_creative, state=CreoOtherState.format)
    dispatcher.register_message_handler(callback=set_offer_other_creative, state=CreoOtherState.offer)
    dispatcher.register_message_handler(callback=set_source_other_creative, state=CreoOtherState.source)
    dispatcher.register_message_handler(callback=set_description_other_creative, state=CreoOtherState.description)
    dispatcher.register_message_handler(callback=set_count_other_creative, state=[CreoOtherState.count, CreoOtherState.sub_description])
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


# set description -> request count\sub_desc
async def set_description_other_creative(message: types.Message, state: FSMContext):
    await CreoOtherState.count.set()
    await state.update_data(description=message.text)
    await message.answer(COUNT_OF_CREO, reply_markup=skip_keyboard())


async def set_count_other_creative(message: types.Message, state: FSMContext):
    state_type = await state.get_state()
    if state_type == CreoOtherState.count.state:
        if message.text == SKIP:
            await state.update_data(count=1)
            await CreoOtherState.check.set()
            task_data = await state.get_data()
            await check_size_message_creo(message, task_data, state)
        else:
            try:
                count = int(message.text)
                await state.update_data(count=count)
                if count > 1:
                    await CreoOtherState.sub_description.set()
                    await message.answer(SUB_DESC_FOR_OTHER_CREO, reply_markup=cancel_keyboard())
                elif count == 1:
                    await CreoOtherState.check.set()
                    task_data = await state.get_data()
                    await check_size_message_creo(message, task_data, state)
                else:
                    await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
            except Exception as e:
                print(f"set_count_other_creative: {e}")
                await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
    else:
        await state.update_data(sub_description=message.text)
        await CreoOtherState.check.set()
        task_data = await state.get_data()
        await check_size_message_creo(message, task_data, state)


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
