from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.presentation.keyboards.admin.ban.kb_ban_system import BanSystemBack


class UnBanOneMoreCallback(CallbackData, prefix="BanOneMoreCallback"):
    pass


kb_unban_user_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=L.ADMIN.UNBAN_ONE_MORE(), callback_data=UnBanOneMoreCallback().pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=BanSystemBack().pack())],
    ]
)
