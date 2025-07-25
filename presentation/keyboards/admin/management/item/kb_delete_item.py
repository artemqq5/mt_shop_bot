from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.management.item.kb_management_item import ManagementItemBack


class ItemApproveDelete(CallbackData, prefix="Item*Approve*Delete"):
    id: int


def kb_item_delete(item):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.DELETE(), callback_data=ItemApproveDelete(id=item['id']).pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=ManagementItemBack(id=item['id']).pack())]
    ])
