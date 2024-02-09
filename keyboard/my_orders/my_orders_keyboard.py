from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.admin_constants import COMPLETED, ACTIVE, ACTIVE_ORDERS, COMPLETED_ORDERS, CREO_TYPE, CANCELED, \
    ACCOUNT_TYPE_FB, ACCOUNT_TYPE_GOOGLE
from data.constants.base_constants import CANCEL, LIST_OF_USER_VIEW, CALL_ADMIN_ABOUT_ORDER, MESSAGE_
from data.repository.creos import CreosRepository
from data.repository.orders import OrdersRepository


def user_view_choice_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    for i in LIST_OF_USER_VIEW:
        keyboard.add(KeyboardButton(text=i))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def user_view_type_orders_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    keyboard.add(KeyboardButton(text=ACTIVE_ORDERS))
    keyboard.add(KeyboardButton(text=COMPLETED_ORDERS))

    keyboard.add(KeyboardButton(CANCEL))  # cancel button

    return keyboard


def user_task_keyboard(orders) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for order in orders:
        if order['status'] in (COMPLETED, CANCELED):
            status = COMPLETED
        else:
            status = ACTIVE

        if order['type'] == CREO_TYPE:
            my_order = CreosRepository().get_creo(order['id_order'])
            if my_order is not None:
                name = f"#{my_order['id']} | {my_order['format']} | {my_order['category']}"
                keyboard.add(InlineKeyboardButton(text=name, callback_data=f"{status}_{CREO_TYPE}_{my_order['id_order']}"))
        else:
            my_order = OrdersRepository().get_account_order(order['id_order'])
            if my_order is not None:
                name = f"#{my_order['id']} | {my_order['name']} | кол-во: {my_order['count']}"
                keyboard.add(InlineKeyboardButton(text=name, callback_data=f"{status}_{order['type']}_{my_order['id_order']}"))
                print(order['type'])

    return keyboard


def call_about_task_keyboard(task_id) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=CALL_ADMIN_ABOUT_ORDER, callback_data=f"{MESSAGE_}_{task_id}"))

    return keyboard


