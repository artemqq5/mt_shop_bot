from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.info_constants import MT_SHOP_ACCOUNTS_SUPPORT_LABEL, MT_SHOP_ACCOUNTS_SUPPORT, \
    MT_SHOP_CREO_SUPPORT_LEBAL, MT_SHOP_CREO_SUPPORT


def support_contacts_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MT_SHOP_ACCOUNTS_SUPPORT_LABEL, url=MT_SHOP_ACCOUNTS_SUPPORT))
    keyboard.add(InlineKeyboardButton(text=MT_SHOP_CREO_SUPPORT_LEBAL, url=MT_SHOP_CREO_SUPPORT))

    return keyboard
