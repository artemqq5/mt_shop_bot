from aiogram import types

from data.constants.about_us_constants import *
from data.constants.base_constants import NOT_IMPLEMENTED
from keyboard.about.about_us_keyboard import mt_media_keyboard


def register_about_us_handlers(dispatcher):
    dispatcher.register_message_handler(flow_about_us_handler, lambda message: message.text in ABOUT_US_LIST)


async def flow_about_us_handler(message: types.Message):
    if message.text == MT_MEDIA:
        await message.answer(MT_MEDIA_DESC, reply_markup=mt_media_keyboard())
    elif message.text == MASONS_TRAFFIC:
        await message.answer(NOT_IMPLEMENTED)
    elif message.text == MASONS_PARTNERS:
        await message.answer(NOT_IMPLEMENTED)
    elif message.text == MASONS_APPS:
        await message.answer(NOT_IMPLEMENTED)
    elif message.text == MT_SHOP:
        await message.answer(NOT_IMPLEMENTED)
    else:
        await message.answer(NOT_IMPLEMENTED)
