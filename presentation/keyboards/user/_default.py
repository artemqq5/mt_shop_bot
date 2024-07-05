from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from private_cfg import CHANNEL_URL

keyboard_subsribe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="MT | SHOP", url=CHANNEL_URL)]
])
