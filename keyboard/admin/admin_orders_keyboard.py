from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.admin_constants import *
from data.constants.base_constants import MENU


def admin_orders_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in ORDER_TYPES_LIST:
        keyboard.add(KeyboardButton(text=i))

    keyboard.add(KeyboardButton(text=MENU))

    return keyboard


def inline_orders_keyboard(list_of_orders) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in list_of_orders:
        name = f"#{i['id']} | {i['type']} | {i['date']}"
        keyboard.add(InlineKeyboardButton(text=name, callback_data=i['id_order']))

    return keyboard


def managment_order_keyboard(order) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in ORDER_STATUS_LIST:
        keyboard.add(InlineKeyboardButton(text=i, callback_data=f"{ORDER_STATUS_LIST[i]}_{order['id_order']}"))

    if order['status'] == REVIEW and order['type'] == CREO_TYPE:
        keyboard.add(InlineKeyboardButton(text=SEND_TASK_TO_TRELLO, callback_data=f"{TRELLO_}_{order['id_order']}"))

    return keyboard
