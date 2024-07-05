from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.base_constants import *


def cancel_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(CANCEL)]], resize_keyboard=True)


def skip_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=SKIP))
    keyboard.add(KeyboardButton(text=CANCEL))

    return keyboard
