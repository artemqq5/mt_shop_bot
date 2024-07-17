import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class BuyItemChoice(CallbackData, prefix="BuyItemChoice"):
    item_id: int
    page: int


class BuyItemNavigation(CallbackData, prefix="BuyItemNavigation"):
    page: int


class BuyChoiceCategoryBack(CallbackData, prefix="BuyChoiceCategoryBack"):
    pass


def kb_buy_item_choice(items, current_page=1):
    inline_kb = []

    total_pages = math.ceil(len(items) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(items))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=L.CLIENT.BUY_ITEM_LIST_TEMPLATE(title=items[i]['title'], cost=items[i]['cost']),
                callback_data=BuyItemChoice(item_id=items[i]['id'], page=current_page).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=BuyItemNavigation(page=current_page - 1).pack()
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
            callback_data=BuyItemNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)
    inline_kb.append([
        InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceCategoryBack().pack())
    ])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class BuyChoiceItemBack(CallbackData, prefix="BuyChoiceItemBack"):
    pass


def kb_item_buy(item_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.CLIENT.BUY(), callback_data="None")],
        [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())],
    ])
