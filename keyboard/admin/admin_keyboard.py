from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.admin_constants import *
from data.constants.base_constants import MENU


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=ALL_ORDERS))
    keyboard.add(KeyboardButton(text=ADD_ITEMS))
    keyboard.add(KeyboardButton(text=SHOW_ITEMS))

    return keyboard



