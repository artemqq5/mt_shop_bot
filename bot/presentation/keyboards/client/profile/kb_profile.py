import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.data.repository.items import ItemRepository
from bot.presentation.keyboards.client.profile.kb_balance import BalanceReplenish


class MyOrdersProfile(CallbackData, prefix="MyOrdersProfile"):
    pass


kb_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=L.CLIENT.PROFILE.ORDERS(), callback_data=MyOrdersProfile().pack())],
        [InlineKeyboardButton(text=L.CLIENT.BALANCE_REPLENISH(), callback_data=BalanceReplenish().pack())],
    ]
)


class ProfileOrderDetail(CallbackData, prefix="ProfileOrderDetail"):
    order_id: int


class ProfileOrdersNav(CallbackData, prefix="ProfileOrdersNav"):
    page: int


class ProfileBack(CallbackData, prefix="ProfileBack"):
    pass


def kb_profile_orders(orders, current_page=1):
    inline_kb = []

    total_pages = math.ceil(len(orders) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(orders))

    # load from db
    for i in range(start_index, end_index):
        item = ItemRepository().item(orders[i]["item_id"])
        inline_kb.append(
            [
                InlineKeyboardButton(
                    text=L.CLIENT.PROFILE.ORDER_LIST_TEMPLATE(
                        title=item["title"], count=orders[i]["count"], price=orders[i]["total_cost"]
                    ),
                    callback_data=ProfileOrderDetail(order_id=orders[i]["id"]).pack(),
                )
            ]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(text="<", callback_data=ProfileOrdersNav(page=current_page - 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text="<", callback_data="None"))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(text=">", callback_data=ProfileOrdersNav(page=current_page + 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text=">", callback_data="None"))

    inline_kb.append(nav)
    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=ProfileBack().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class ProfileOrdersBack(CallbackData, prefix="ProfileOrdersBack"):
    pass


kb_profile_orders_back = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=L.BACK(), callback_data=ProfileOrdersBack().pack())]]
)
