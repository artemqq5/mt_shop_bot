from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.constants.base_constants import *


def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(ABOUT))
    keyboard.add(KeyboardButton(BUY))
    keyboard.add(KeyboardButton(RULES))
    keyboard.add(KeyboardButton(SUPPORT))

    return keyboard


def buy_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(DESIGN))

    return keyboard


def cancel_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(CANCEL)]], resize_keyboard=True)
