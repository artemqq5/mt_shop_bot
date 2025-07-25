from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.ban.kb_ban_system import BanSystemBack


class BanOneMoreCallback(CallbackData, prefix="BanOneMoreCallback"):
    pass


kb_ban_user_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.BAN_ONE_MORE(), callback_data=BanOneMoreCallback().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BanSystemBack().pack())]
])
