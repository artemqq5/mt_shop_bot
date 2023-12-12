from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.accounts_constants import ACCOUNTS
from data.constants.agency_accounts_constants import AGENCY_ACCOUNTS
from data.constants.apps_constants import APPS
from data.constants.base_constants import *
from data.repository import MyRepository
from keyboard.admin.admin_keyboard import admin_panel_keyboard


def main_keyboard(message) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    if MyRepository().get_user(message.chat.id)['position'] is not None:  # check if user admin set admin command
        is_admin = MyRepository().get_user(message.chat.id)['position'] == ADMIN
    else:
        is_admin = False

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
    keyboard.add(KeyboardButton(APPS))
    keyboard.add(KeyboardButton(AGENCY_ACCOUNTS))
    keyboard.add(KeyboardButton(MENU))

    return keyboard


def about_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(MENU))

    for i in ABOUT_US_LIST:
        keyboard.add(KeyboardButton(i))

    return keyboard


