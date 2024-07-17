from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from data.default_constants import CHANNEL_NAME
from private_cfg import CHANNEL_URL

kb_subsribe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=CHANNEL_NAME, url=CHANNEL_URL)]
])

kb_menu_client = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.CLIENT.BUY()), KeyboardButton(text=L.CLIENT.AVAILABILITY())],
    [KeyboardButton(text=L.CLIENT.PROFILE())],
    [KeyboardButton(text=L.CLIENT.SUPPORT())]
], resize_keyboard=True)
