from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dev.constants.agency_accounts_constants import SUPPORT_AGENCY_CONTACT, SUPPORT_AGENCY_LABEL
from dev.constants.info_constants import MT_SHOP_ACCOUNTS_SUPPORT_LABEL, MT_SHOP_ACCOUNTS_SUPPORT, \
    MT_SHOP_CREO_SUPPORT_LEBAL, MT_SHOP_CREO_SUPPORT, MASONS_APPS_LABEL, MASONS_APPS_LINK


def support_contacts_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MT_SHOP_ACCOUNTS_SUPPORT_LABEL, url=MT_SHOP_ACCOUNTS_SUPPORT))
    keyboard.add(InlineKeyboardButton(text=MT_SHOP_CREO_SUPPORT_LEBAL, url=MT_SHOP_CREO_SUPPORT))
    keyboard.add(InlineKeyboardButton(text=MASONS_APPS_LABEL, url=MASONS_APPS_LINK))
    keyboard.add(InlineKeyboardButton(text=SUPPORT_AGENCY_LABEL, url=SUPPORT_AGENCY_CONTACT))

    return keyboard
