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


class PreviewItemPublish(CallbackData, prefix="Preview*Item*Publish"):
    state: str


kb_preview_add_item = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.PUBLISH_ITEM(), callback_data=PreviewItemPublish(state="publish").pack())],
    [InlineKeyboardButton(text=L.ADMIN.RESTART_PUBLISH(), callback_data=PreviewItemPublish(state="restart").pack())],
])

kb_publish_onemore = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.ADD_ITEM(), callback_data=PreviewItemPublish(state="restart").pack())],
])
