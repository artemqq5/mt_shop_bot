from aiogram_i18n import L
from aiogram_i18n.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from bot.config import CHANNEL_URL, SUPPORT_CONTACT
from bot.data.default_constants import CHANNEL_NAME

kb_subsribe = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=CHANNEL_NAME, url=CHANNEL_URL)]])

kb_menu_client = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=L.CLIENT.BUY()), KeyboardButton(text=L.CLIENT.AVAILABILITY())],
        [KeyboardButton(text=L.CLIENT.PROFILE()), KeyboardButton(text=L.GENERAL.CHANGE_LANG())],
        [KeyboardButton(text=L.CLIENT.SUPPORT())],
    ],
    resize_keyboard=True,
)

kb_support = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=L.CLIENT.SUPPORT_CONTACT(), url=SUPPORT_CONTACT)]]
)
