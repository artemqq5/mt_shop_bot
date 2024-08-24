from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from private_cfg import SUPPORT_CONTACT


class BalanceReplenish(CallbackData, prefix="BalanceReplenish"):
    pass


kb_balance_replenish = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.CLIENT.BALANCE_REPLENISH(), callback_data=BalanceReplenish().pack())],
    [InlineKeyboardButton(text=L.CLIENT.SUPPORT_CONTACT(), url=SUPPORT_CONTACT)]
])


def kb_pay_invoice(url_invoice):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=L.CLIENT.BALANCE_PAY_INVOICE(), url=url_invoice)]
    ])
