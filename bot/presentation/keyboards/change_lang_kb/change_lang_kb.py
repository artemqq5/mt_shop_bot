from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup


class ChangeLang(CallbackData, prefix="ChangeLang"):
    lang: str


kb_change_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=L.GENERAL.CHANGE_LANG.UK(), callback_data=ChangeLang(lang="uk").pack())],
        [InlineKeyboardButton(text=L.GENERAL.CHANGE_LANG.EN(), callback_data=ChangeLang(lang="en").pack())],
        [InlineKeyboardButton(text=L.GENERAL.CHANGE_LANG.RU(), callback_data=ChangeLang(lang="ru").pack())],
    ]
)
