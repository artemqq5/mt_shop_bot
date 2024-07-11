from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_managment import CreateNewCategory


class CreateNewCategoryBack(CallbackData, prefix="Create*New*Category*Back"):
    key: str = "CreateNewCategoryBack"


kb_create_category_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=CreateNewCategoryBack().pack())]
])

kb_create_category_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.CREATE_NEW_CATEGORY(), callback_data=CreateNewCategory().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=CreateNewCategoryBack().pack())]
])
