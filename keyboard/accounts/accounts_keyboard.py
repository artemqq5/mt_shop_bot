from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.base_constants import BUY
from data.repository import MyRepository


def available_accounts_keyboard(list_accounts) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in list_accounts:
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=f"account_{i['id']}"))

    return keyboard


def list_of_callback_accounts() -> list[str]:
    list_callbacks = []

    for i in MyRepository().get_accounts():
        list_callbacks.append(f"account_{i['id']}")

    for i in MyRepository().get_accounts():
        list_callbacks.append(f"buy_{i['id']}")

    return list_callbacks


def buy_account_keyboard(id_account) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=BUY, callback_data=f"buy_{id_account}"))

    return keyboard
