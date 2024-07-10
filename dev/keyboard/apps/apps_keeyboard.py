from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from dev.constants.apps_constants import GAMBLING_APPS, WHITE_APPS, ORDER_APPS
from dev.constants.base_constants import CANCEL
from dev.constants.info_constants import MASONS_APPS_LINK


def apps_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=GAMBLING_APPS))
    keyboard.add(KeyboardButton(text=WHITE_APPS))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def apps_contact_order() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=ORDER_APPS, url=MASONS_APPS_LINK))
    return keyboard


