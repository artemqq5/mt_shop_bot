from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.management.kb_managment import ManagementBack


class PreviewItemPublish(CallbackData, prefix="Preview*Item*Publish"):
    state: str


def kb_preview_add_item(category):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.PUBLISH_ITEM(), callback_data=PreviewItemPublish(state="publish").pack())],
        [InlineKeyboardButton(text=L.ADMIN.RESTART_PUBLISH(),
                              callback_data=PreviewItemPublish(state="restart").pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())]
    ])


def kb_publish_onemore(category):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.ADD_ITEM(), callback_data=PreviewItemPublish(state="restart").pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())]
    ])
