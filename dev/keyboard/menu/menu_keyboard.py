from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from dev.constants.base_constants import *
from data.repository.users import UsersRepository
from dev.keyboard.admin.admin_keyboard import admin_panel_keyboard


def main_keyboard(message) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    if UsersRepository().get_user(message.chat.id)['position'] is not None:  # check if client admin set admin command
        is_admin = UsersRepository().get_user(message.chat.id)['position'] == ADMIN
    else:
        is_admin = False

    if is_admin:
        return admin_panel_keyboard()

    keyboard.add(KeyboardButton(ABOUT))
    keyboard.add(KeyboardButton(BUY))
    keyboard.add(KeyboardButton(MY_ORDERS))
    keyboard.add(KeyboardButton(RULES))
    keyboard.add(KeyboardButton(SUPPORT))

    return keyboard


def buy_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(ACCOUNTS))
    keyboard.add(KeyboardButton(DESIGN))
    keyboard.add(KeyboardButton(CARDS_FARM))
    keyboard.add(KeyboardButton(CABINETS_FARM))
    keyboard.add(KeyboardButton(VERIFICATIONS_FARM))
    keyboard.add(KeyboardButton(APPS))
    keyboard.add(KeyboardButton(AGENCY_ACCOUNTS))
    keyboard.add(KeyboardButton(CANCEL))

    return keyboard


def about_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(MENU))

    for i in ABOUT_US_LIST:
        keyboard.add(KeyboardButton(i))

    return keyboard


