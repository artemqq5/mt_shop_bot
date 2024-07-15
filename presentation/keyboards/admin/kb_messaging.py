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


class MediaMessagingSkip(CallbackData, prefix="MediaMessagingSkip"):
    pass


kb_skip_messaging_media = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SKIP(), callback_data=MediaMessagingSkip().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])


class ButtonMessagingSkip(CallbackData, prefix="ButtonMessagingSkip"):
    pass


kb_skip_messaging_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SKIP(), callback_data=ButtonMessagingSkip().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])


class RepeatButtonChoice(CallbackData, prefix="RepeatButtonChoice"):
    repeat: bool


kb_repeat_button_messaging = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.YES(), callback_data=RepeatButtonChoice(repeat=True).pack())],
    [InlineKeyboardButton(text=L.NO(), callback_data=RepeatButtonChoice(repeat=False).pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])


class SendMessageAllClients(CallbackData, prefix="SendMessageAllClients"):
    pass


class RestartMessage(CallbackData, prefix="RestartMessage"):
    pass


kb_send_message_all_clients = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.SEND(), callback_data=SendMessageAllClients().pack())],
    [InlineKeyboardButton(text=L.ADMIN.RESTART(), callback_data=RestartMessage().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])
