from aiogram import types

from data.constants.apps_constants import *
from data.constants.base_constants import NOT_IMPLEMENTED
from is_banned import is_banned
from keyboard.apps.apps_keeyboard import *
from keyboard.menu.menu_keyboard import main_keyboard
from states.apps.order_apps_state import OrderAppsState


def register_hundler_apps(dispatcher):
    dispatcher.register_message_handler(order_apps, lambda message: message.text == APPS)
    dispatcher.register_message_handler(choice_app_type, lambda message: message.text in (GAMBLING_APPS, WHITE_APPS),
                                        state=OrderAppsState.choice_type_app)


async def order_apps(message: types.Message):
    if await is_banned(message):
        return

    await OrderAppsState.choice_type_app.set()
    await message.answer(APPS_TYPE, reply_markup=apps_type_keyboard())


async def choice_app_type(message: types.Message):
    if message.text == GAMBLING_APPS:
        await message.answer(GAMBLING_APPS_DESC, reply_markup=apps_contact_order())
    elif message.text == WHITE_APPS:
        await message.answer(WHITE_APPS_DESC, reply_markup=apps_contact_order())
    else:
        await message.answer(NOT_IMPLEMENTED, reply_markup=main_keyboard(message))
