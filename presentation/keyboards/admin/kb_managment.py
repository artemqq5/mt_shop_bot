import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class CategoryChoice(CallbackData, prefix="Category*Choice"):
    name: str
    page: int


class CategoryNavigation(CallbackData, prefix="Category*Navigation"):
    page: int


class CreateNewCategory(CallbackData, prefix="Create*New*Category"):
    key: str = "CreateNewCategory"


def kb_choice_category(categories, current_page: int = 1):
    # create new category
    inline_kb = [[InlineKeyboardButton(
        text=L.ADMIN.CREATE_NEW_CATEGORY(),
        callback_data=CreateNewCategory().pack()
    )]]

    total_pages = math.ceil(len(categories) / 5)
    start_index = (current_page - 1) * 5
    end_index = min(start_index + 5, len(categories))

    # load from db
    for i in range(start_index, end_index):
        inline_kb.append(
            [InlineKeyboardButton(
                text=categories[i]['name'],
                callback_data=CategoryChoice(name=categories[i]['name'], page=current_page).pack()
            )]
        )

    nav = []

    # Navigation buttons
    if current_page > 1:
        nav.append(InlineKeyboardButton(
            text='<',
            callback_data=CategoryNavigation(page=current_page - 1).pack()
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
            callback_data=CategoryNavigation(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


class CategoryManagementAddItem(CallbackData, prefix="Category*Management*AddItem"):
    pass


class CategoryManagementItemList(CallbackData, prefix="Category*Management*ItemList"):
    category: str
    page: int = 1


class CategoryManagementItemListNavigation(CallbackData, prefix="Category*Management*ItemList*Navigation"):
    page: int


class CategoryManagementVisibility(CallbackData, prefix="Category*Management*Visibility"):
    category: str
    visibility: bool


class CategoryManagementDelete(CallbackData, prefix="Category*Management*Delete"):
    pass


class ChoiceCategoryBack(CallbackData, prefix="Choice*Category*Back"):
    pass


class ManagementBack(CallbackData, prefix="Management*Back"):
    category: str


def kb_category_management(category):
    inline_kb = [
        [InlineKeyboardButton(
            text=L.ADMIN.ADD_ITEM(),
            callback_data=CategoryManagementAddItem().pack()
        )],
        [InlineKeyboardButton(
            text=L.ADMIN.SHOW_ITEMS(),
            callback_data=CategoryManagementItemList(category=category['name']).pack()
        )]
    ]

    if category['visibility'] == 1:
        inline_kb.append([InlineKeyboardButton(
            text=L.ADMIN.HIDE(),
            callback_data=CategoryManagementVisibility(category=category['name'], visibility=False).pack()
        )])
    else:
        inline_kb.append([InlineKeyboardButton(
            text=L.ADMIN.OPEN(),
            callback_data=CategoryManagementVisibility(category=category['name'], visibility=True).pack()
        )])

    inline_kb.append([
        InlineKeyboardButton(
            text=L.ADMIN.DELETE(),
            callback_data=CategoryManagementDelete().pack()
        )
    ])

    inline_kb.append([
        InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceCategoryBack().pack())
    ])

    return InlineKeyboardMarkup(inline_keyboard=inline_kb)


def kb_back_category_management(category):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())]
    ])


kb_back_category_choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceCategoryBack().pack())]
])
