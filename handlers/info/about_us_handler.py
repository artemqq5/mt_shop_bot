from aiogram import types

from data.constants.base_constants import NOT_IMPLEMENTED
from keyboard.about.about_us_keyboard import *


def register_about_us_handlers(dispatcher):
    dispatcher.register_message_handler(flow_about_us_handler, lambda message: message.text in ABOUT_US_LIST)


async def flow_about_us_handler(message: types.Message):
    if message.text == MT_MEDIA:
        await message.answer(MT_MEDIA_DESC, reply_markup=mt_media_keyboard())
    elif message.text == MASONS_TRAFFIC:
        await message.answer(MASONS_TRAFFIC_DESC, reply_markup=masons_traffic_keyboard())
    elif message.text == MASONS_PARTNERS:
        await message.answer(MASONS_PARTNERS_DESC, reply_markup=masons_partners_keyboard())
    elif message.text == MASONS_APPS:
        await message.answer(MASONS_APPS_DESC, reply_markup=masons_apps_keyboard())
    elif message.text == MT_SHOP:
        await message.answer(MT_SHOP_DESC, reply_markup=mt_shop_keyboard())
    else:
        await message.answer(NOT_IMPLEMENTED)
