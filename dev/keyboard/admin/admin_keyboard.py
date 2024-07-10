from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from dev.constants.admin_constants import *
from dev.constants.base_constants import CANCEL


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=ALL_ORDERS))
    keyboard.add(KeyboardButton(text=ADD_ITEMS))
    keyboard.add(KeyboardButton(text=SHOW_ITEMS))
    keyboard.add(KeyboardButton(text=PUSH_NOTIFICATION))
    keyboard.add(KeyboardButton(text=SYSTEM_OF_BAN))

    return keyboard


def admin_ban_system_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=BAN_USER_CATEGORY))
    keyboard.add(KeyboardButton(text=SHOW_BANNED_USERS))
    keyboard.add(KeyboardButton(text=CANCEL))

    return keyboard


def ban_user_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=BAN_USER))
    keyboard.add(KeyboardButton(text=CANCEL))

    return keyboard
