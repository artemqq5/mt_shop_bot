from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.about_us_constants import *


def mt_media_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MT_MEDIA_GROUP_LABEL, url=MT_MEDIA_GROUP))
    keyboard.add(InlineKeyboardButton(text=MT_MEDIA_CHAT_LABEL, url=MT_MEDIA_CHAT))

    return keyboard
