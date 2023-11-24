from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.base_constants import *


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    KeyboardButton(CANCEL)

    return keyboard
