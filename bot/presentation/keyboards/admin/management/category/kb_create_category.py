from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.presentation.keyboards.admin.management.category.kb_managment import (
    ChoiceCategoryBack,
    CreateNewCategory,
)

kb_create_category_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.CREATE_NEW_CATEGORY(), callback_data=CreateNewCategory().pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=ChoiceCategoryBack().pack())],
    ]
)
