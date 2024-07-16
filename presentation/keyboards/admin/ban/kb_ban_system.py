from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class BanUserCallback(CallbackData, prefix="BanUserCallback"):
    pass


class UnBanUserCallback(CallbackData, prefix="UnBanUserCallback"):
    pass


class ListBannedUsersCallback(CallbackData, prefix="ListBannedUsersCallback"):
    pass


kb_ban_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.BAN_USER(), callback_data=BanUserCallback().pack())],
    [InlineKeyboardButton(text=L.ADMIN.UNBAN_USER(), callback_data=UnBanUserCallback().pack())],
    [InlineKeyboardButton(text=L.ADMIN.BAN_LIST(), callback_data=ListBannedUsersCallback().pack())],
])


class BanSystemBack(CallbackData, prefix="BanSystemBack"):
    pass


kb_ban_system_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BanSystemBack().pack())]
])

