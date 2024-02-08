from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.admin_constants import *
from data.constants.accounts_constants import *
from data.constants.base_constants import CANCEL
from data.repository.accounts import AccountsRepository


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


def show_item_accounts_keyboard(source) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in AccountsRepository().get_accounts(source):
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=str(i['id'])))

    return keyboard


def show_item_cards_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in AccountsRepository().get_cards():
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=str(i['id'])))

    return keyboard


def show_item_cabinets_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in AccountsRepository().get_cabinets():
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=str(i['id'])))

    return keyboard


def show_item_verifications_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in AccountsRepository().get_verifications():
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=str(i['id'])))

    return keyboard


def list_of_callback_menagment_accounts() -> list[str]:
    list_callbacks = []

    for i in AccountsRepository().get_accounts():
        list_callbacks.append(str(i['id']))
        list_callbacks.append(f"{HIDE_STATE}_{i['id']}")
        list_callbacks.append(f"{OPEN_STATE}_{i['id']}")
        list_callbacks.append(f"{DELETE_STATE}_{i['id']}")

    return list_callbacks


def list_of_callback_menagment_cards() -> list[str]:
    list_callbacks = []

    for i in AccountsRepository().get_cards():
        list_callbacks.append(str(i['id']))
        list_callbacks.append(f"{HIDE_STATE}_{i['id']}")
        list_callbacks.append(f"{OPEN_STATE}_{i['id']}")
        list_callbacks.append(f"{DELETE_STATE}_{i['id']}")

    return list_callbacks


def list_of_callback_menagment_cabinets() -> list[str]:
    list_callbacks = []

    for i in AccountsRepository().get_cabinets():
        list_callbacks.append(str(i['id']))
        list_callbacks.append(f"{HIDE_STATE}_{i['id']}")
        list_callbacks.append(f"{OPEN_STATE}_{i['id']}")
        list_callbacks.append(f"{DELETE_STATE}_{i['id']}")

    return list_callbacks


def list_of_callback_menagment_verifications() -> list[str]:
    list_callbacks = []

    for i in AccountsRepository().get_verifications():
        list_callbacks.append(str(i['id']))
        list_callbacks.append(f"{HIDE_STATE}_{i['id']}")
        list_callbacks.append(f"{OPEN_STATE}_{i['id']}")
        list_callbacks.append(f"{DELETE_STATE}_{i['id']}")

    return list_callbacks


def manag_account_keyboard(id_) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    account = AccountsRepository().get_account(id_)

    keyboard.add(InlineKeyboardButton(text=HIDE_ITEM, callback_data=f"{HIDE_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=OPEN_ITEM, callback_data=f"{OPEN_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=DELETE_ITEM, callback_data=f"{DELETE_STATE}_{account['id']}"))

    return keyboard


def manag_card_keyboard(id_) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    account = AccountsRepository().get_card(id_)

    keyboard.add(InlineKeyboardButton(text=HIDE_ITEM, callback_data=f"{HIDE_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=OPEN_ITEM, callback_data=f"{OPEN_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=DELETE_ITEM, callback_data=f"{DELETE_STATE}_{account['id']}"))

    return keyboard


def manag_cabinet_keyboard(id_) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    account = AccountsRepository().get_cabinet(id_)

    keyboard.add(InlineKeyboardButton(text=HIDE_ITEM, callback_data=f"{HIDE_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=OPEN_ITEM, callback_data=f"{OPEN_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=DELETE_ITEM, callback_data=f"{DELETE_STATE}_{account['id']}"))

    return keyboard


def manag_verification_keyboard(id_) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    account = AccountsRepository().get_verification(id_)

    keyboard.add(InlineKeyboardButton(text=HIDE_ITEM, callback_data=f"{HIDE_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=OPEN_ITEM, callback_data=f"{OPEN_STATE}_{account['id']}"))
    keyboard.add(InlineKeyboardButton(text=DELETE_ITEM, callback_data=f"{DELETE_STATE}_{account['id']}"))

    return keyboard

