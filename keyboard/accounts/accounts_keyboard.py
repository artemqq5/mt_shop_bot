from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from data.constants.accounts_constants import LIST_OF_ACCOUNTS_TYPE
from data.constants.admin_constants import OPEN_STATE
from data.constants.base_constants import BUY, CANCEL
from data.repository.accounts import AccountsRepository


def source_account_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in LIST_OF_ACCOUNTS_TYPE:
        keyboard.add(KeyboardButton(i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def available_accounts_keyboard(list_accounts) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in list_accounts:
        if i['visibility'] == OPEN_STATE:
            keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=f"account_{i['id']}"))

    return keyboard


def list_of_callback_accounts() -> list[str]:
    list_callbacks = []

    for i in AccountsRepository().get_accounts():
        if i['visibility'] == OPEN_STATE:
            list_callbacks.append(f"account_{i['id']}")

    for i in AccountsRepository().get_accounts():
        if i['visibility'] == OPEN_STATE:
            list_callbacks.append(f"buy_{i['id']}")

    return list_callbacks


def buy_account_keyboard(id_account) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=BUY, callback_data=f"buy_{id_account}"))

    return keyboard
