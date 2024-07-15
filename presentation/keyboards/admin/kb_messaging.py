from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


class AllClientsMessaging(CallbackData, prefix="AllClientsMessaging"):
    pass


class IndividualMessaging(CallbackData, prefix="IndividualMessaging"):
    pass


kb_messaging_categories = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.MESSAGE_ALL_CLIENTS(), callback_data=AllClientsMessaging().pack())],
    [InlineKeyboardButton(text=L.ADMIN.MESSAGE_INDIVIDUAL(), callback_data=IndividualMessaging().pack())],
])


class BackMessaging(CallbackData, prefix="BackMessaging"):
    pass


kb_back_messaging = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])

# kb_skip_messaging =

