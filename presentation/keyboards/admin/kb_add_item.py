from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class CategoryChoice(CallbackData, prefix="Category*Choice"):
    name: str


class CreateNewCategory(CallbackData, prefix="Create*New*Category"):
    key: str = "CreateNewCategory"


def kb_choice_category(categories):
    # create new category
    inline_kb = [[InlineKeyboardButton(
        text=L.ADMIN.ADD_ITEM.CREATE_NEW_CATEGORY(),
        callback_data=CreateNewCategory().pack()
    )]]

    # load from db
    for category in categories:
        inline_kb.append(
            [InlineKeyboardButton(
                text=category['name'],
                callback_data=CategoryChoice(name=category['name']).pack()
            )]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_kb, resize_keyboard=True)
