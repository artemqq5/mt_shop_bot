from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboard.base_keyboard import main_keyboard
from keyboard.design_keyboard import *
from states.design.creo_video import CreoVideoAdaptiveState, CreoVideoNewState
from states.design.order_creative_state import OrderCreativeState


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

        await callback.message.answer(
            text=f"Формат: {format_creo}\nТип: {type_creo}\nКатегория: {category_creo}",
            reply_markup=main_keyboard()
        )

        if format_creo == VIDEO_FORMAT:
            if type_creo == ADAPTIVE_CREATIVE:
                await CreoVideoAdaptiveState.general.set()
                await state.update_data(general=start_data_order)
                await CreoVideoAdaptiveState.next()
            elif type_creo == NEW_CREATIVE:
                await CreoVideoNewState.general.set()
                await state.update_data(general=start_data_order)
                await CreoVideoNewState.next()

        elif format_creo == STATIC_FORMAT:
            if type_creo == ADAPTIVE_CREATIVE:
                pass
            elif type_creo == NEW_CREATIVE:
                pass

        elif format_creo == GIF_ANIM_FORMAT:
            if type_creo == ADAPTIVE_CREATIVE:
                pass
            elif type_creo == NEW_CREATIVE:
                pass
