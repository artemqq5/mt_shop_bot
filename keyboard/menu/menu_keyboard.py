from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.base_constants import *
from keyboard.admin.admin_keyboard import admin_panel_keyboard


def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    if is_admin:
        return admin_panel_keyboard()

    keyboard.add(KeyboardButton(ABOUT))
    keyboard.add(KeyboardButton(BUY))
    keyboard.add(KeyboardButton(RULES))
    keyboard.add(KeyboardButton(SUPPORT))

    return keyboard


def buy_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(DESIGN))
    keyboard.add(KeyboardButton(MENU))

    return keyboard

