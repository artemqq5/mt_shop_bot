import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.data.repository.items import ItemRepository


class BuyCategoryChoice(CallbackData, prefix="BuyCategoryChoice"):
    name: str


class BuyCategoryNavigation(CallbackData, prefix="BuyCategoryNavigation"):
    page: int


def kb_buy_category_choice(categories, current_page=1):
    inline_kb = []

    total_pages = math.ceil(len(categories) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(categories))

    # load from db
    for i in range(start_index, end_index):
        items = ItemRepository().items_by_category(categories[i]["name"])
        count = f" | {len(items)}" if len(items) else ""
        inline_kb.append(
            [
                InlineKeyboardButton(
                    text=f"{categories[i]['name']}{count}",
                    callback_data=BuyCategoryChoice(name=categories[i]["name"]).pack(),
                )
            ]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(text="<", callback_data=BuyCategoryNavigation(page=current_page - 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text="<", callback_data="None"))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(text=">", callback_data=BuyCategoryNavigation(page=current_page + 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text=">", callback_data="None"))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
