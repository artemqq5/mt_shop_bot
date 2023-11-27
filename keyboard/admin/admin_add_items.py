from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.admin_constants import *
from data.constants.accounts_constants import *
from data.constants.base_constants import CANCEL


def choice_type_account_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in LIST_OF_ACCOUNTS_TYPE:
        keyboard.add(KeyboardButton(i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


