import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class MyOrdersProfile(CallbackData, prefix="MyOrdersProfile"):
    pass


kb_profile_orders = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.PROFILE.ORDERS(), callback_data=MyOrdersProfile().pack())]
])

