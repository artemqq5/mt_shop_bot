from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.default_constants import ALL_CLIENT_MESSAGING, INDIVIDUAL_MESSAGING


class ChoiceTypeMessaging(CallbackData, prefix="ChoiceTypeMessaging"):
    type: str


kb_messaging_categories = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.MESSAGE_ALL_CLIENTS(),
                          callback_data=ChoiceTypeMessaging(type=ALL_CLIENT_MESSAGING).pack())],
    [InlineKeyboardButton(text=L.ADMIN.MESSAGE_INDIVIDUAL(),
                          callback_data=ChoiceTypeMessaging(type=INDIVIDUAL_MESSAGING).pack())],
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
    button: bool


kb_skip_messaging_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.YES(), callback_data=ButtonMessagingSkip(button=True).pack())],
    [InlineKeyboardButton(text=L.SKIP(), callback_data=ButtonMessagingSkip(button=False).pack())],
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


kb_send_message_all_clients = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.ADMIN.SEND(), callback_data=SendMessageAllClients().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackMessaging().pack())]
])
