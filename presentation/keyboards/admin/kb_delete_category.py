from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_managment import ManagementBack


class CategoryAproveDelete(CallbackData, prefix="Category*Aprove*Delete"):
    pass


def kb_category_delete(category):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.DELETE(), callback_data=CategoryAproveDelete().pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementBack(category=category).pack())]
    ])
