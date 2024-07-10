from aiogram import types

from dev.constants.base_constants import NOT_IMPLEMENTED
from keyboard.info.about_us_keyboard import *


def register_about_us_handlers(dispatcher):
    dispatcher.register_message_handler(flow_about_us_handler, lambda message: message.text in ABOUT_US_LIST)


async def flow_about_us_handler(message: types.Message):
    if message.text == MT_MEDIA:
        with open("source/mt_media.png", 'rb') as photo_file:
            await message.answer_photo(photo_file)
        await message.answer(MT_MEDIA_DESC, reply_markup=mt_media_keyboard())
    elif message.text == MASONS_TRAFFIC:
        with open("source/mt.png", 'rb') as photo_file:
            await message.answer_photo(photo_file)
        await message.answer(MASONS_TRAFFIC_DESC, reply_markup=masons_traffic_keyboard())

    elif message.text == MASONS_PARTNERS:
        with open("source/mt_partners.png", 'rb') as photo_file:
            await message.answer_photo(photo_file)
        await message.answer(MASONS_PARTNERS_DESC, reply_markup=masons_partners_keyboard())

    elif message.text == MASONS_APPS:
        with open("source/mt_apps.png", 'rb') as photo_file:
            await message.answer_photo(photo_file)
        await message.answer(MASONS_APPS_DESC, reply_markup=masons_apps_keyboard())

    elif message.text == MT_SHOP:
        with open("source/mt_shop.png", 'rb') as photo_file:
            await message.answer_photo(photo_file)
        await message.answer(MT_SHOP_DESC, reply_markup=mt_shop_keyboard())

    else:
        await message.answer(NOT_IMPLEMENTED)
