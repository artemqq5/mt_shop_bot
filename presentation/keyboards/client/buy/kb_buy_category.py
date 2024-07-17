import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class BuyCategoryChoice(CallbackData, prefix="BuyCategoryChoice"):
    name: str


class BuyCategoryNavigation(CallbackData, prefix="BuyCategoryNavigation"):
    page: int


def kb_buy_category_choice(categories, current_page=1):
    # create new category
    inline_kb = []

    total_pages = math.ceil(len(categories) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(categories))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=categories[i]['name'],
                callback_data=BuyCategoryChoice(name=categories[i]['name']).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=BuyCategoryNavigation(page=current_page - 1).pack()
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
            callback_data=BuyCategoryNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)

#
# class CategoryManagementAddItem(CallbackData, prefix="Category*Management*AddItem"):
#     pass
#
#
# class CategoryManagementItemList(CallbackData, prefix="Category*Management*ItemList"):
#     pass
#
#
# class CategoryManagementVisibility(CallbackData, prefix="Category*Management*Visibility"):
#     visibility: bool
#
#
# class CategoryManagementDelete(CallbackData, prefix="Category*Management*Delete"):
#     pass
#
#
# class ChoiceCategoryBack(CallbackData, prefix="Choice*Category*Back"):
#     pass
#
#
# class ManagementBack(CallbackData, prefix="Management*Back"):
#     category: str
#
#
# def kb_category_management(category):
#     inline_kb = [
#         [InlineKeyboardButton(
#             text=L.ADMIN.ADD_ITEM(),
#             callback_data=CategoryManagementAddItem().pack()
#         )],
#         [InlineKeyboardButton(
#             text=L.ADMIN.SHOW_ITEMS(),
#             callback_data=CategoryManagementItemList().pack()
#         )]
#     ]
#
#     if category['visibility'] == 1:
#         inline_kb.append([InlineKeyboardButton(
#             text=L.ADMIN.HIDE(),
#             callback_data=CategoryManagementVisibility(visibility=False).pack()
#         )])
#     else:
#         inline_kb.append([InlineKeyboardButton(
#             text=L.ADMIN.OPEN(),
#             callback_data=CategoryManagementVisibility(visibility=True).pack()
#         )])
#
#     inline_kb.append([
#         InlineKeyboardButton(
#             text=L.ADMIN.DELETE(),
#             callback_data=CategoryManagementDelete().pack()
#         )
#     ])
#
#     inline_kb.append([
#         InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceCategoryBack().pack())
#     ])
#
#     return InlineKeyboardMarkup(inline_keyboard=inline_kb)
#
#
# def kb_back_category_management(category):
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())]
#     ])
#
#
# kb_back_category_choice = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceCategoryBack().pack())]
# ])
