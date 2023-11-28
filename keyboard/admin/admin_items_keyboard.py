from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.admin_constants import *
from data.constants.accounts_constants import *
from data.constants.base_constants import CANCEL
from data.repository import MyRepository


def choice_type_item_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in LIST_OF_ITEMS_TYPE:
        keyboard.add(KeyboardButton(i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def choice_type_account_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in LIST_OF_ACCOUNTS_TYPE:
        keyboard.add(KeyboardButton(i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def show_item_accounts_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in MyRepository().get_accounts():
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=i['id']))

    return keyboard


def manag_item_keyboard(id_account) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    account = MyRepository().get_account(id_account)

    keyboard.add(InlineKeyboardButton(text=HIDE_ITEM, callback_data=f"{HIDE_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=OPEN_ITEM, callback_data=f"{OPEN_STATE}_{account['id']}"))

    return keyboard

