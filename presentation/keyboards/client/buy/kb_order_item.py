from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.client.buy.kb_buy_item import BuyChoiceItemBack

kb_buy_item_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
])

kb_buy_preview_item = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.BUY.SEND(), callback_data="None")],
    [InlineKeyboardButton(text=L.CLIENT.BUY.RESTART(), callback_data="None")],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
])
