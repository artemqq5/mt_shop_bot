from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.base_constants import *


def design_format_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in FORMAT_CREO_LIST:
        keyboard.add(KeyboardButton(text=i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def design_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in TYPE_CREO_LIST:
        keyboard.add(KeyboardButton(text=i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def design_category_keyboard(category_creo_list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in category_creo_list:
        keyboard.add(InlineKeyboardButton(text=i, callback_data=i))

    return keyboard


def design_category_finance_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in FINANCE_CATEGORY_LIST:
        keyboard.add(InlineKeyboardButton(text=i, callback_data=i))

    return keyboard


def design_app_platform_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(APP_STORE_TYPE))
    keyboard.add(KeyboardButton(GOOGLE_PLEY_TYPE))
    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard
