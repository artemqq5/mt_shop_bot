from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.agency_accounts_constants import *
from data.constants.base_constants import CANCEL


def agency_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=FB_SOURCE))
    keyboard.add(KeyboardButton(text=GOOGLE_SOURCE))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def contact_support() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=SUPPORT_AGENCY, url=SUPPORT_AGENCY_CONTACT))
    return keyboard
