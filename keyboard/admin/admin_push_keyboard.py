from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.admin_constants import PUSH_TYPE_LIST
from data.constants.base_constants import CANCEL


def admin_push_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in PUSH_TYPE_LIST:
        keyboard.add(KeyboardButton(i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard
