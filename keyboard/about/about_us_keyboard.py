from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.constants.about_us_constants import *


def mt_media_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MT_MEDIA_GROUP_LABEL, url=MT_MEDIA_GROUP))
    keyboard.add(InlineKeyboardButton(text=MT_MEDIA_CHAT_LABEL, url=MT_MEDIA_CHAT))

    return keyboard


def masons_traffic_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MASONS_TRAFFIC_LINK_LABEL, url=MASONS_TRAFFIC_LINK))
    keyboard.add(InlineKeyboardButton(text=SUPPORT_MANAGER, url=CHAT_SUPPORT_MASONS))

    return keyboard


def masons_partners_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MASONS_PARTNERS_LINK_LABEL, url=MASONS_PARTNERS_LINK))
    keyboard.add(InlineKeyboardButton(text=SUPPORT_MANAGER, url=CHAT_SUPPORT_PARTNERS_1))
    keyboard.add(InlineKeyboardButton(text=SUPPORT_MANAGER, url=CHAT_SUPPORT_PARTNERS_2))

    return keyboard


def masons_apps_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MASONS_APPS_LABEL, url=MASONS_APPS_LINK))

    return keyboard


def mt_shop_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(text=MT_SHOP_LINK_LABEL, url=MT_SHOP_LINK))
    keyboard.add(InlineKeyboardButton(text=SUPPORT_MANAGER, url=CHAT_SUPPORT_MT_SHOP))

    return keyboard
