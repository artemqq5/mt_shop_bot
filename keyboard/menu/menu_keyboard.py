from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.accounts_constants import ACCOUNTS
from data.constants.base_constants import *
from data.repository import MyRepository
from keyboard.admin.admin_keyboard import admin_panel_keyboard


def main_keyboard(message) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    is_admin = MyRepository().get_user(message.chat.id)['position'] == ADMIN  # check if user admin set admin command

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
    keyboard.add(KeyboardButton(ACCOUNTS))
    keyboard.add(KeyboardButton(MENU))

    return keyboard


def about_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(MENU))

    for i in ABOUT_US_LIST:
        keyboard.add(KeyboardButton(i))

    return keyboard


