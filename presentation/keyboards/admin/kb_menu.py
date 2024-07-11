from aiogram_i18n import L
from aiogram_i18n.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=L.ADMIN.ORDERS()), KeyboardButton(text=L.ADMIN.MANAGEMENT())],
    [KeyboardButton(text=L.ADMIN.MESSAGING()), KeyboardButton(text=L.ADMIN.BAN_USER())],
], resize_keyboard=True)
