import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class ChoiceOrderItem(CallbackData, prefix="ChoiceOrderItem"):
    order_id: int
    page: int


class OrderItemNavigation(CallbackData, prefix="OrderItemNavigation"):
    page: int


def kb_orders_choice(orders, current_page=1):
    inline_kb = []

    total_pages = math.ceil(len(orders) / 7)
    start_index = (current_page - 1) * 7
    end_index = min(start_index + 7, len(orders))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=L.ADMIN.ORDER_LIST_TEMPLATE(
                    id=orders[i]['id'],
                    category=orders[i]['category'],
                    count=orders[i]['count'],
                    price=orders[i]['total_cost']
                ),
                callback_data=ChoiceOrderItem(order_id=orders[i]['id'], page=current_page).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=OrderItemNavigation(page=current_page - 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data="None"
        ))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data=OrderItemNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class OrderItemBack(CallbackData, prefix="OrderItemBack"):
    page: int


def kb_order_back(page):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.BACK(), callback_data=OrderItemBack(page=page).pack())]
    ])
