import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageIsTooLong

from data.constants.base_constants import WRONG_FORRMAT_DATE, SKIP, MESSAGE_IS_TOO_LONG
from data.constants.design_constants import *
from handlers.buy.creo.creo_base_handler import check_size_message_creo
from handlers.buy.creo.creo_use_case.format_task_view import check_view_order
from handlers.buy.creo.creo_use_case.send_order_creo import send_order_creo
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from keyboard.creo.design_keyboard import check_task_view_keyboard, design_format_keyboard
from states.creo.creo_default_state import CreoDefaultState
from states.creo.order_creative_state import OrderCreativeState


def register_creo_default_handlers(dispatcher):
    dispatcher.register_message_handler(callback=set_geo_default_creative, state=CreoDefaultState.geo)
    dispatcher.register_message_handler(callback=set_language_default_creative, state=CreoDefaultState.language)
    dispatcher.register_message_handler(callback=set_currency_default_creative, state=CreoDefaultState.currency)
    dispatcher.register_message_handler(callback=set_format_default_creative, state=CreoDefaultState.format)
    dispatcher.register_message_handler(callback=set_offer_default_creative, state=CreoDefaultState.offer)
    dispatcher.register_message_handler(callback=set_voice_default_creative, state=CreoDefaultState.voice)
    dispatcher.register_message_handler(callback=set_source_default_creative, state=CreoDefaultState.source)
    dispatcher.register_message_handler(callback=set_description_default_creative, state=CreoDefaultState.description)
    dispatcher.register_message_handler(callback=set_count_default_creative, state=[CreoDefaultState.count, CreoDefaultState.sub_description])
    dispatcher.register_message_handler(callback=set_deadline_default_creative, state=CreoDefaultState.deadline)


# set geo -> request language
async def set_geo_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(geo=message.text)
        await message.answer(LANGUAGE_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(geo=message.text)
        await message.answer(LANGUAGE_MESSAGE, reply_markup=cancel_keyboard())


# set language -> request currency
async def set_language_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(language=message.text)
        await message.answer(CURRENCY_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(language=message.text)
        await message.answer(CURRENCY_MESSAGE, reply_markup=cancel_keyboard())


# set currency -> request format
async def set_currency_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(currency=message.text)
        await message.answer(FORMAT_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(currency=message.text)
        await message.answer(FORMAT_MESSAGE, reply_markup=cancel_keyboard())


# set format -> request offer
async def set_format_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(format=message.text)
        await message.answer(OFFER_MESSAGE, reply_markup=cancel_keyboard())


# set offer -> request voice
async def set_offer_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(offer=message.text)
        await message.answer(VOICE_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(offer=message.text)
        await message.answer(VOICE_MESSAGE, reply_markup=cancel_keyboard())


# set voice -> request source
async def set_voice_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(voice=message.text)
        await message.answer(SOURCE_MESSAGE, reply_markup=skip_keyboard())
    else:
        await state.update_data(voice=message.text)
        await message.answer(SOURCE_MESSAGE, reply_markup=cancel_keyboard())


# set source -> request description
async def set_source_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.next()
    type_creo = await state.get_data()
    if type_creo['general']['type'] == ADAPTIVE_CREATIVE:
        if message.text != SKIP:
            await state.update_data(source=message.text)
    else:
        await state.update_data(source=message.text)

    await message.answer(DESCRIPTION_MESSAGE, reply_markup=cancel_keyboard())


# set description -> request count\sub_desc
async def set_description_default_creative(message: types.Message, state: FSMContext):
    await CreoDefaultState.count.set()
    await state.update_data(description=message.text)
    await message.answer(COUNT_OF_CREO, reply_markup=skip_keyboard())


async def set_count_default_creative(message: types.Message, state: FSMContext):
    state_type = await state.get_state()
    if state_type == CreoDefaultState.count.state:
        if message.text == SKIP:
            await state.update_data(count=1)
            await CreoDefaultState.check.set()
            task_data = await state.get_data()
            await check_size_message_creo(message, task_data, state)
        else:
            try:
                count = int(message.text)
                await state.update_data(count=count)
                if count > 1:
                    await CreoDefaultState.sub_description.set()
                    await message.answer(SUB_DESC_FOR_OTHER_CREO, reply_markup=cancel_keyboard())
                elif count == 1:
                    await CreoDefaultState.check.set()
                    task_data = await state.get_data()
                    await check_size_message_creo(message, task_data, state)
                else:
                    await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
            except Exception as e:
                print(f"set_count_default_creative: {e}")
                await message.answer(WRONG_FORMAT_INPUT_CREO, reply_markup=skip_keyboard())
    else:
        await state.update_data(sub_description=message.text)
        await CreoDefaultState.check.set()
        task_data = await state.get_data()
        await check_size_message_creo(message, task_data, state)


# set deadline ->
async def set_deadline_default_creative(message: types.Message, state: FSMContext):
    if message.text != SKIP:
        try:
            date_time = datetime.datetime.strptime(message.text + " +0400", '%Y-%m-%d %H:%M %z')

            await state.update_data(deadline=str(date_time))
            data = await state.get_data()
            await state.finish()
        except Exception as e:
            print(f"set_deadline_default_creative - {e}")
            data = None
            await message.answer(WRONG_FORRMAT_DATE, reply_markup=skip_keyboard())

        await send_order_creo(data, message)

    else:
        await state.update_data(deadline=None)
        data = await state.get_data()
        await state.finish()

        await send_order_creo(data, message)
