from aiogram import types

from data.constants.base_constants import NOT_IMPLEMENTED
from is_banned import is_banned
from keyboard.agency.agency_keyboard import *
from keyboard.menu.menu_keyboard import main_keyboard
from states.agency.agency_type_state import AgencyTypeState


def register_agency_handlers(dispatcher):
    dispatcher.register_message_handler(order_agency, lambda message: message.text == AGENCY_ACCOUNTS)
    dispatcher.register_message_handler(choice_source_agency,
                                        lambda message: message.text in (FB_SOURCE, GOOGLE_SOURCE),
                                        state=AgencyTypeState.type)


async def order_agency(message: types.Message):
    if await is_banned(message):
        return

    await AgencyTypeState.type.set()
    await message.answer(AGENCY_TYPE, reply_markup=agency_type_keyboard())


async def choice_source_agency(message: types.Message):
    if message.text == FB_SOURCE:
        await message.answer(FB_AGENCY_DESC, reply_markup=contact_support())
    elif message.text == GOOGLE_SOURCE:
        await message.answer(GOOGLE_AGENCY_DESC, reply_markup=contact_support())
    else:
        await message.answer(NOT_IMPLEMENTED, reply_markup=main_keyboard(message))
