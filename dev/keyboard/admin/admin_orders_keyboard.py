from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from dev.constants.admin_constants import *
from dev.constants.base_constants import CANCEL
from dev.constants.creos import CreosRepository
from dev.constants.orders import OrdersRepository


def type_of_orders_admin() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in TYPE_OF_ORDERS:
        keyboard.add(i)

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def admin_orders_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in ORDER_TYPES_LIST:
        keyboard.add(KeyboardButton(text=i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def inline_orders_keyboard(list_of_orders, type_oder) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for i in list_of_orders:
        if CREO_TYPE in type_oder:
            task = CreosRepository().get_creo(i['id_order'])
            name = f"#{task['id']} | {task['format']} | {task['category']} | {task['type']}"
        else:
            task = OrdersRepository().get_account_order(i['id_order'])
            name = f"#{task['id']} | {task['name']} | кол-во: {task['count']}"

        keyboard.add(InlineKeyboardButton(text=name, callback_data=i['id_order']))

    return keyboard


def managment_order_keyboard(order) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    if order['status'] == ON_APPROVE:
        keyboard.add(InlineKeyboardButton(text=COMMENT_AND_REFINEMENT, callback_data=f"{REFINEMENT_}_{order['id_order']}"))
        keyboard.add(InlineKeyboardButton(text=SET_COMAPLETED_STATUS, callback_data=f"{COMPLETED}_{order['id_order']}"))
    else:
        for i in ORDER_STATUS_LIST:
            keyboard.add(InlineKeyboardButton(text=i, callback_data=f"{ORDER_STATUS_LIST[i]}_{order['id_order']}"))

        if order['status'] == REVIEW and order['type'] == CREO_TYPE:
            keyboard.add(InlineKeyboardButton(text=SEND_TASK_TO_TRELLO, callback_data=f"{TRELLO_}_{order['id_order']}"))

    return keyboard


def send_refainement_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(SEND_COMMENT_TO_TRELLO)

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard
