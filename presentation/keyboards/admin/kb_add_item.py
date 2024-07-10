import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class CategoryChoice(CallbackData, prefix="Category*Choice"):
    name: str
    page: int


class CategoryNavication(CallbackData, prefix="Category*Navication"):
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
            callback_data=CategoryNavication(page=current_page - 1).pack()
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
            callback_data=CategoryNavication(page=current_page + 1).pack()
        ))
    else:
        nav.append(InlineKeyboardButton(
            text='>',
            callback_data="None"
        ))

    inline_kb.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=inline_kb, resize_keyboard=True)


class PreviewItemPublish(CallbackData, prefix="Preview*Item*Publish"):
    state: str


kb_preview_add_item = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.PUBLISH_ITEM(), callback_data=PreviewItemPublish(state="publish").pack())],
    [InlineKeyboardButton(text=L.ADMIN.RESTART_PUBLISH(), callback_data=PreviewItemPublish(state="restart").pack())],
])

kb_publish_onemore = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ADD_ITEM(), callback_data=PreviewItemPublish(state="restart").pack())],
])
