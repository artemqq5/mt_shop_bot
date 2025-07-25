import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.presentation.keyboards.admin.management.category.kb_managment import (
    ManagementBack,
)


class ItemChoice(CallbackData, prefix="Item*Choice"):
    id: int


class ItemNavigation(CallbackData, prefix="Item*Navigation"):
    page: int


def kb_choice_item(items, category, current_page: int = 1):
    inline_kb = []

    total_pages = math.ceil(len(items) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(items))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(text=items[i]["title"], callback_data=ItemChoice(id=items[i]["id"]).pack())]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(text="<", callback_data=ItemNavigation(page=current_page - 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text="<", callback_data="None"))

    nav.append(InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data="None"))

    if current_page < total_pages:
        nav.append(InlineKeyboardButton(text=">", callback_data=ItemNavigation(page=current_page + 1).pack()))
    else:
        nav.append(InlineKeyboardButton(text=">", callback_data="None"))

    inline_kb.append(nav)
    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class ItemManagementVisibility(CallbackData, prefix="Item*Management*Visibility"):
    id: int
    visibility: bool


class ItemManagementDelete(CallbackData, prefix="Item*Management*Delete"):
    id: int


class ChoiceItemBack(CallbackData, prefix="Choice*Item*Back"):
    pass


class ManagementItemBack(CallbackData, prefix="Management*Item*Back"):
    id: int


def kb_item_management(item):
    inline_kb = []

    if item["visibility"] == 1:
        inline_kb.append(
            [
                InlineKeyboardButton(
                    text=L.ADMIN.HIDE(), callback_data=ItemManagementVisibility(visibility=False, id=item["id"]).pack()
                )
            ]
        )
    else:
        inline_kb.append(
            [
                InlineKeyboardButton(
                    text=L.ADMIN.OPEN(), callback_data=ItemManagementVisibility(visibility=True, id=item["id"]).pack()
                )
            ]
        )

    inline_kb.append(
        [InlineKeyboardButton(text=L.ADMIN.DELETE(), callback_data=ItemManagementDelete(id=item["id"]).pack())]
    )

    inline_kb.append([InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceItemBack().pack())])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


kb_back_item_choice = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceItemBack().pack())]]
)
