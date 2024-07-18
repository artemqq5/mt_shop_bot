from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.client.buy.kb_buy_item import BuyChoiceItemBack
from private_cfg import SUPPORT_CONTACT

kb_buy_item_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
])


class BuyOrderDescSkip(CallbackData, prefix="BuyOrderDescSkip"):
    pass


kb_buy_item_skip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.SKIP(), callback_data=BuyOrderDescSkip().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
])


class BuyOrderItemSend(CallbackData, prefix="BuyOrderItemSend"):
    pass


class BuyOrderItemRestart(CallbackData, prefix="BuyOrderItemRestart"):
    item_id: int


def kb_buy_preview_item(item_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.CLIENT.BUY.SEND(), callback_data=BuyOrderItemSend().pack())],
        [InlineKeyboardButton(text=L.CLIENT.BUY.RESTART(), callback_data=BuyOrderItemRestart(item_id=item_id).pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
    ])


def kb_buy_send_error(item_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.CLIENT.SUPPORT_CONTACT(), url=SUPPORT_CONTACT)],
        [InlineKeyboardButton(text=L.CLIENT.BUY.RESTART(), callback_data=BuyOrderItemRestart(item_id=item_id).pack())],
        [InlineKeyboardButton(text=L.BACK(), callback_data=BuyChoiceItemBack().pack())]
    ])
