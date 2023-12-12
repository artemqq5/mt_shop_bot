from aiogram import types
from aiogram.dispatcher import FSMContext

from data.repository import MyRepository
from keyboard.base_keyboard import cancel_keyboard, skip_keyboard
from keyboard.menu.menu_keyboard import main_keyboard
from keyboard.creo.design_keyboard import *
from states.creo.creo_app_state import CreoAppState
from states.creo.creo_default_state import CreoDefaultState
from states.creo.creo_other_state import CreoOtherState
from states.creo.order_creative_state import OrderCreativeState


def register_handlers_creo(dispatcher):
    dispatcher.register_message_handler(
        design_format,
        lambda message: message.text == DESIGN
    )
    dispatcher.register_message_handler(
        design_type,
        lambda message: message.text in FORMAT_CREO_LIST,
        state=OrderCreativeState.format
    )
    dispatcher.register_message_handler(
        design_category,
        lambda message: message.text in TYPE_CREO_LIST,
        state=OrderCreativeState.type
    )
    dispatcher.register_callback_query_handler(
        type_creative_handler,
        lambda call: call.data in (
                CATEGORY_CREO_LIST_VIDEO + CATEGORY_CREO_LIST_STATIC
                + CATEGORY_CREO_LIST_GIF_ANIM + FINANCE_CATEGORY_LIST
        ),
        state=OrderCreativeState.category
    )


# format ("Видео", "Статика", "GIF-анимация")
async def design_format(message: types.Message):
    await OrderCreativeState.format.set()
    await message.answer(DESIGN_FORMAT, reply_markup=design_format_keyboard())


# type (NEW, ADAPTIVE)
async def design_type(message: types.Message, state: FSMContext):
    await OrderCreativeState.next()
    await state.update_data(format=message.text)
    await message.answer(DESIGN_TYPE, reply_markup=design_type_keyboard())


# category (NUTRA, BETTING, I_GAMING, DATING, DEEP_FAKE, FINANCE, E_COMMERCE, SWEEPSTAKES, ESSAY, GAMING, OTHER, APP_DESIGN)
async def design_category(message: types.Message, state: FSMContext):
    await OrderCreativeState.next()
    await state.update_data(type=message.text)
    data_format = await state.get_data()

    if data_format['format'] == VIDEO_FORMAT:
        keyboard_type = CATEGORY_CREO_LIST_VIDEO
    elif data_format['format'] == STATIC_FORMAT:
        keyboard_type = CATEGORY_CREO_LIST_STATIC
    else:
        keyboard_type = CATEGORY_CREO_LIST_GIF_ANIM

    await message.answer(DESIGN_CATEGORY, reply_markup=design_category_keyboard(keyboard_type))


async def type_creative_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == FINANCE:  # send new keyboard to choice sub category
        await callback.message.answer(text=FINANCE, reply_markup=design_category_finance_keyboard())
    else:
        await state.update_data(category=callback.data)
        start_data_order = await state.get_data()
        await state.finish()

        format_creo = start_data_order['format']
        type_creo = start_data_order['type']
        category_creo = start_data_order['category']

        # ======== TEST ================================= todo remove this in prodaction version
        # await callback.message.answer(
        #     text=f"Формат: {format_creo}\nТип: {type_creo}\nКатегория: {category_creo}",
        #     reply_markup=main_keyboard(callback.message)
        # )
        # ================================================

        # APP Creo
        if category_creo == APP_DESIGN:
            await CreoAppState.general.set()
            await state.update_data(general=start_data_order)
            await CreoAppState.next()

            await callback.message.answer(PLATFORM_MESSAGE, reply_markup=design_app_platform_keyboard())

        # Custom Creo (Other)
        elif category_creo == OTHER:
            await CreoOtherState.general.set()
            await state.update_data(general=start_data_order)
            await CreoOtherState.next()

            if type_creo == NEW_CREATIVE:
                await callback.message.answer(FORMAT_MESSAGE, reply_markup=cancel_keyboard())
            else:
                await callback.message.answer(FORMAT_MESSAGE, reply_markup=skip_keyboard())

        # all default categories of Creo
        else:
            await CreoDefaultState.general.set()
            await state.update_data(general=start_data_order)
            await CreoDefaultState.next()

            if type_creo == NEW_CREATIVE:
                await callback.message.answer(GEO_MESSAGE, reply_markup=cancel_keyboard())
            else:
                await callback.message.answer(GEO_MESSAGE, reply_markup=skip_keyboard())
